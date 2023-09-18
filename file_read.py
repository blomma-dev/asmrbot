
import json
import random
import file_parse


file_type = "json"

def open_file(file_name):
    # Use 'r' mode to open the file for reading
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            if file_type == "json":
                # Read the content of the file
                content = json.load(file)
                weekday_morning, weekday_afternoon, night, weekend = file_parse.parse_json_file(content)
                # Print the lists
                #print("Week Names:", weekday_morning)
                #print("Week Status:", weekday_afternoon)
                #print("Weekend Names:", night)
                #print("Weekend Status:", weekend)
                return random.choice(weekday_morning)

            
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")