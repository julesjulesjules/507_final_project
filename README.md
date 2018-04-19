# 507_final_project

DATA SOURCES: 
UrbanOutfitters website - baseurl = https://www.urbanoutfitters.com/
Anthropologie website - baseurl = https://www.anthropologie.com/new-

OTHER: 
Plotly: https://plot.ly/python/getting-started/

CODE STRUCTURE: 
Program to run = main_program.py 
	This pulls in all necessary libraries/files/functions
Accessory programs (must be in the same folder to run)
	testfile.py -> UOpricescrape(gender)
	match_up_jsons.py -> read_in_UOfiles(), matchUOwomens(iw, pw), matchUOmens(im, pm), erase_tables(), make_db(), 
			     insert_gend(gender_list), insert_brand(brand_list), insert_cates(cate_list), insert_items(brand_dictionary)
	anthroscrape.py -> anthroScrape()
	anthro_json.py -> read_in_ANTfiles(), match_anthros(anthro)
	working_with_database.py -> find_a_pattern(), find_high_low_price(), compare_men_women()
	second_level.py -> rescrape_and_rebuild(), just_rebuild()
	working_clothes_functions.py -> UOwebscrape(gender)

USER GUIDE: 
<command line> python main_program.py

"rebuild" - completely re-scrapes Urban Outfitters and Anthropologie, and re-constructs database, then passes to next phase
"current" - re-constructs database from current files, then passes to next phase
"none" - passes onto the next phase of the program, uses whatever construct of the database exists

"help" - prints list of search command options, then allows user to search
"next" - goes on to search prompt

"pattern" - searches for pattern mentioned in item name
"price" - searches for most or least expensive items in specific categories
"compare" - shows a bar chart of the average or max prices of items in each category
"exit" - stops the program
