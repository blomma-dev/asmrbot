
def parse_json_file(data):
    weekday_morning = data.get("weekday_morning", [])
    weekday_afternoon = data.get("weekday_afternoon", [])
    night = data.get("night", [])
    weekend = data.get("weekend", [])
    
    return weekday_morning, weekday_afternoon, night, weekend