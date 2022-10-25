import csv
import xml.etree.ElementTree as ET

class SevendParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self._items_tree = ET.parse(file_path + '/items.xml')
        self._items_root = self._items_tree.getroot()

        self.weapons = self.get_weapons()

    def get_weapons(self):
        weapons = []
        for item_node in self._items_root:
            tags_node = item_node.find("*/[@name='Tags']")
            if tags_node != None:
                tags = tags_node.attrib["value"].split(",")
                # TODO: Ignore admin/god tools for now
                if "weapon" in tags and not "admin" in item_node.attrib["name"].lower():
                    weapon = SevendWeapon(item_node=item_node)
                    weapons.append(weapon)
        return weapons


class SevendBase:

    def get_translated_string(self, string):
        # TODO: Language support. Currently defaults to english, which is index 5.
        with open('config/Localization.txt', 'r', newline='') as csv_file:
            for line in csv_file:
                if line.startswith(string):
                    return line.split(',')[5]


class SevendWeapon(SevendBase):
    def __init__(self, item_node):
        self.item_node = item_node
        self.original_name = self.item_node.attrib["name"]
        self.name = self.get_translated_string(self.item_node.attrib["name"])
        self.entity_damage = self.get_entity_damage(self.item_node)

    def get_entity_damage(self, item_node):
        effect_group = item_node.find(f"*/[@name='{self.original_name}']")
        try:
            # TODO: Fix this try-except, it's only there temporary.
            # Some weapons give funny entity damage values, debug here.
            return effect_group.find(f"*/[@name='EntityDamage']").attrib["value"]
        except:
            return None

    def _get_original_tags(self, item_node):
        tags_node = item_node.find("*/[@name='Tags']")
        tags = tags_node.attrib["value"].split(",")
        return tags

    def __repr__(self):
        return f"<SevendWeapon: {self.name}>"
