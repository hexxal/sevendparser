from xml.etree import ElementTree


class SevendParser:
    def __init__(self, file_path, language="en-us"):
        self.language = language
        self.file_path = file_path
        self._items_tree = ElementTree.parse(file_path + "/items.xml")
        self._items_root = self._items_tree.getroot()

        self.weapons = self.get_weapons()

    def get_weapons(self):
        weapons = []
        for item_node in self._items_root:
            tags_node = item_node.find("*/[@name='Tags']")
            if tags_node is not None:
                tags = tags_node.attrib["value"].split(",")
                # TODO: Ignore admin/god tools for now
                if "weapon" in tags and "admin" not in item_node.attrib["name"].lower():
                    weapon = SevendWeapon(item_node=item_node, language=self.language)
                    weapons.append(weapon)
        return weapons


class SevendBase:
    LANGUAGE_INDEXES = {
        "en-us": 5,
        "de-de": 7,
        "es-mx": 8,
        "fr-fr": 9,
        "it-it": 10,
        "ja-jp": 11,
        "pl-pl": 13,
        "pt-br": 14,
        "ru-ru": 15,
        "tr-tr": 16,
        "zh-cn": 17,
        "zh-tw": 18,
    }

    def get_translated_string(self, string, language):
        if language not in self.LANGUAGE_INDEXES.keys():
            raise Exception("That is not a supported language")

        # TODO: Hard-coded path
        with open("config/Localization.txt", "r", newline="", encoding="utf-8") as csv_file:
            for line in csv_file:
                if line.startswith(string):
                    return line.split(",")[self.LANGUAGE_INDEXES[language]]


class SevendWeapon(SevendBase):
    def __init__(self, item_node, language):
        self.item_node = item_node
        self.language = language
        self.original_name = self.item_node.attrib["name"]
        self.name = self.get_translated_string(
            self.original_name, language=self.language
        )
        self.entity_damage = self.get_entity_damage(self.item_node)

    def get_entity_damage(self, item_node):
        effect_group = item_node.find(f"*/[@name='{self.original_name}']")
        try:
            # TODO: Fix this try-except, it's only there temporary.
            # Some weapons give funny entity damage values, debug here.
            return effect_group.find("*/[@name='EntityDamage']").attrib["value"]
        except:
            return None

    def _get_original_tags(self, item_node):
        tags_node = item_node.find("*/[@name='Tags']")
        tags = tags_node.attrib["value"].split(",")
        return tags

    def __repr__(self):
        return f"<SevendWeapon: {self.name}>"
