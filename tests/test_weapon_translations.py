import pytest
from sevendparser.src.main import SevendParser

def test_correct_weapon_count(parser):
    assert len(parser.weapons) == 49

def test_weapon_name_translations_de_de():
    parser = SevendParser(file_path="/home/hxl/projects/sevendparser/config", language="de-de")
    first_five_weapons = parser.weapons[:5]
    assert first_five_weapons[0].name == "Knochenmesser"  # Bone Knife
    assert first_five_weapons[1].name == "Jagdmesser"  # Hunting Knife
    assert first_five_weapons[2].name == "Zuckerstangenmesser"  # Candy Cane Knife
    assert first_five_weapons[3].name == "Machete"  # Machete
    assert first_five_weapons[4].name == "Holzknüppel"  # Wooden Club

def test_weapon_name_translations_es_mx():
    parser = SevendParser(file_path="/home/hxl/projects/sevendparser/config", language="es-mx")
    first_five_weapons = parser.weapons[:5]
    assert first_five_weapons[0].name == "Cuchillo de hueso"  # Bone Knife
    assert first_five_weapons[1].name == "Cuchillo de caza"  # Hunting Knife
    assert first_five_weapons[2].name == "Cuchillo de bastón de caramelo"  # Candy Cane Knife
    assert first_five_weapons[3].name == "Machete"  # Machete
    assert first_five_weapons[4].name == "Garrote de madera"  # Wooden Club

def test_weapon_name_translations_fr_fr():
    parser = SevendParser(file_path="/home/hxl/projects/sevendparser/config", language="fr-fr")
    first_five_weapons = parser.weapons[:5]
    assert first_five_weapons[0].name == "Couteau en os"  # Bone Knife
    assert first_five_weapons[1].name == "Couteau de chasse"  # Hunting Knife
    assert first_five_weapons[2].name == "Couteau sucre d'orge"  # Candy Cane Knife
    assert first_five_weapons[3].name == "Machette"  # Machete
    assert first_five_weapons[4].name == "Massue en bois"  # Wooden Club

def test_weapon_name_translations_it_it():
    parser = SevendParser(file_path="/home/hxl/projects/sevendparser/config", language="it-it")
    first_five_weapons = parser.weapons[:5]
    assert first_five_weapons[0].name == "Pugnale d'osso"  # Bone Knife
    assert first_five_weapons[1].name == "Pugnale da caccia"  # Hunting Knife
    assert first_five_weapons[2].name == "Pugnale di zucchero"  # Candy Cane Knife
    assert first_five_weapons[3].name == "Machete"  # Machete
    assert first_five_weapons[4].name == "Mazza di legno"  # Wooden Club

def test_weapon_name_translations_ja_jp():
    parser = SevendParser(file_path="/home/hxl/projects/sevendparser/config", language="ja-jp")
    first_five_weapons = parser.weapons[:5]
    assert first_five_weapons[0].name == "骨ナイフ"  # Bone Knife
    assert first_five_weapons[1].name == "狩猟ナイフ"  # Hunting Knife
    assert first_five_weapons[2].name == "キャンディーケーン型ナイフ"  # Candy Cane Knife
    assert first_five_weapons[3].name == "マチェーテ"  # Machete
    assert first_five_weapons[4].name == "木製棍棒"  # Wooden Club

def test_weapon_name_translations_pl_pl():
    parser = SevendParser(file_path="/home/hxl/projects/sevendparser/config", language="pl-pl")
    first_five_weapons = parser.weapons[:5]
    assert first_five_weapons[0].name == "Kościany nóż"  # Bone Knife
    assert first_five_weapons[1].name == "Nóż myśliwski"  # Hunting Knife
    assert first_five_weapons[2].name == "Zaostrzona laska cukrowa"  # Candy Cane Knife
    assert first_five_weapons[3].name == "Maczeta"  # Machete
    assert first_five_weapons[4].name == "Drewniana maczuga"  # Wooden Club

def test_weapon_name_translations_pt_br():
    parser = SevendParser(file_path="/home/hxl/projects/sevendparser/config", language="pt-br")
    first_five_weapons = parser.weapons[:5]
    assert first_five_weapons[0].name == "Faca de Osso"  # Bone Knife
    assert first_five_weapons[1].name == "Faca de Caça"  # Hunting Knife
    assert first_five_weapons[2].name == "Faca de Doce"  # Candy Cane Knife
    assert first_five_weapons[3].name == "Facão"  # Machete
    assert first_five_weapons[4].name == "Taco de Madeira"  # Wooden Club

def test_weapon_name_translations_ru_ru():
    parser = SevendParser(file_path="/home/hxl/projects/sevendparser/config", language="ru-ru")
    first_five_weapons = parser.weapons[:5]
    assert first_five_weapons[0].name == "Костяной нож"  # Bone Knife
    assert first_five_weapons[1].name == "Охотничий нож"  # Hunting Knife
    assert first_five_weapons[2].name == "Нож из карамельной трости"  # Candy Cane Knife
    assert first_five_weapons[3].name == "Мачете"  # Machete
    assert first_five_weapons[4].name == "Деревянная дубинка"  # Wooden Club

def test_weapon_name_translations_tr_tr():
    parser = SevendParser(file_path="/home/hxl/projects/sevendparser/config", language="tr-tr")
    first_five_weapons = parser.weapons[:5]
    assert first_five_weapons[0].name == "Kemik Bıçağı"  # Bone Knife
    assert first_five_weapons[1].name == "Av Bıçağı"  # Hunting Knife
    assert first_five_weapons[2].name == "Şeker Bıçak"  # Candy Cane Knife
    assert first_five_weapons[3].name == "Pala"  # Machete
    assert first_five_weapons[4].name == "Tahta Sopa"  # Wooden Club

def test_weapon_name_translations_zh_cn():
    parser = SevendParser(file_path="/home/hxl/projects/sevendparser/config", language="zh-cn")
    first_five_weapons = parser.weapons[:5]
    assert first_five_weapons[0].name == "骨刀"  # Bone Knife
    assert first_five_weapons[1].name == "猎刀"  # Hunting Knife
    assert first_five_weapons[2].name == "拐杖糖刀"  # Candy Cane Knife
    assert first_five_weapons[3].name == "砍刀"  # Machete
    assert first_five_weapons[4].name == "木棒"  # Wooden Club

def test_weapon_name_translations_zh_tw():
    parser = SevendParser(file_path="/home/hxl/projects/sevendparser/config", language="zh-tw")
    first_five_weapons = parser.weapons[:5]
    assert first_five_weapons[0].name == "骨刀"  # Bone Knife
    assert first_five_weapons[1].name == "獵刀"  # Hunting Knife
    assert first_five_weapons[2].name == "糖果拐杖刀"  # Candy Cane Knife
    assert first_five_weapons[3].name == "大砍刀"  # Machete
    assert first_five_weapons[4].name == "木棍"  # Wooden Club

def test_non_supported_language():
    with pytest.raises(Exception) as e:
        parser = SevendParser(file_path="/home/hxl/projects/sevendparser/config", language="foo")
    assert str(e.value) == "That is not a supported language"
