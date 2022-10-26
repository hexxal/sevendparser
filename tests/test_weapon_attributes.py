def test_correct_weapon_count(parser):
    assert len(parser.weapons) == 49


def test_weapon_name(parser):
    first_five_weapons = parser.weapons[:5]
    assert first_five_weapons[0].name == "Bone Knife"
    assert first_five_weapons[1].name == "Hunting Knife"
    assert first_five_weapons[2].name == "Candy Cane Knife"
    assert first_five_weapons[3].name == "Machete"
    assert first_five_weapons[4].name == "Wooden Club"


def test_weapon_entity_damage(parser):
    first_five_weapons = parser.weapons[:5]
    assert first_five_weapons[0].entity_damage == "5.1"
    assert first_five_weapons[1].entity_damage == "6.1"
    assert first_five_weapons[2].entity_damage == "6.6"
    assert first_five_weapons[3].entity_damage == "19.8"
    assert first_five_weapons[4].entity_damage == "13.8"
