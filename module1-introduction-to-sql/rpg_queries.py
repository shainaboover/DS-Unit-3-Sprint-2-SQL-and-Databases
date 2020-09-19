
import sqlite3
import os

# construct path to database
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

query_1 = "SELECT count(distinct character_id) as unique_count FROM charactercreator_character"

result_1 = cursor.execute(query_1).fetchall()
print("RESULT_1", result_1)

query_2 = "SELECT COUNT(distinct cleric.character_ptr_id) as cleric_count, COUNT(distinct fighter.character_ptr_id) as fighter_count, COUNT(distinct mage.character_ptr_id) as mage_count, COUNT(distinct thief.character_ptr_id) as thief_count FROM charactercreator_character character LEFT JOIN charactercreator_cleric cleric ON cleric.character_ptr_id = character.character_id LEFT JOIN charactercreator_fighter fighter ON fighter.character_ptr_id = character.character_id LEFT JOIN charactercreator_mage mage ON mage.character_ptr_id = character.character_id LEFT JOIN charactercreator_thief thief ON thief.character_ptr_id = character.character_id"

result_2 = cursor.execute(query_2).fetchall()
print("RESULT_2", result_2)

query_3 = "SELECT COUNT(distinct item_id) as item_count FROM armory_item"

result_3 = cursor.execute(query_3).fetchall()
print("RESULT_3", result_3)

query_4 = "SELECT COUNT(distinct item_ptr_id) as weapon_count, COUNT(distinct item_id) as item_count, COUNT(distinct item_id) - count(distinct item_ptr_id) as non_weapon_count FROM armory_item item LEFT JOIN armory_weapon weapon ON item.item_id = weapon.item_ptr_id"

result_4 = cursor.execute(query_4).fetchall()
print("RESULT_4", result_4)

query_5 = "SELECT cci.character_id, COUNT(distinct item_id) as items_count FROM charactercreator_character_inventory cci GROUP BY character_id LIMIT 20"

result_5 = cursor.execute(query_5).fetchall()
print("RESULT_5", result_5)

query_6 = "SELECT cci.character_id, COUNT(distinct aw.item_ptr_id) as weapons_count FROM charactercreator_character_inventory cci LEFT JOIN armory_weapon aw ON cci.item_id = aw.item_ptr_id GROUP BY character_id LIMIT 20"

result_6 = cursor.execute(query_6).fetchall()
print("RESULT_6", result_6)

query_7 = "SELECT AVG(items_count) as avg_items_count FROM (SELECT cci.character_id, COUNT(distinct item_id) as items_count FROM charactercreator_character_inventory cci GROUP BY character_id)"

result_7 = cursor.execute(query_7).fetchall()
print("RESULT_7", result_7)

query_8 = "SELECT AVG(weapons_count) as avg_weapons_count FROM (SELECT cci.character_id, COUNT(distinct aw.item_ptr_id) as weapons_count FROM charactercreator_character_inventory cci LEFT JOIN armory_weapon aw ON cci.item_id = aw.item_ptr_id GROUP BY character_id)"

result_8 = cursor.execute(query_8).fetchall()
print("RESULT_8", result_8)