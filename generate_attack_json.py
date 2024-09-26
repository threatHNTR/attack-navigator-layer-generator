import json
import logging

ATTACK_LOGO = '''

   ___ ________________    _______ __  _  _____ _   ______________ __________  ___    __________  _________  ___ __________  ___ 
  / _ /_  __/_  __/ __/___/ ___/ //_/ / |/ / _ | | / /  _/ ___/ _ /_  __/ __ \/ _ \  / ___/ __/ |/ / __/ _ \/ _ /_  __/ __ \/ _ \\
 / __ |/ /   / /  > _/_ _/ /__/ ,<   /    / __ | |/ // // (_ / __ |/ / / /_/ / , _/ / (_ / _//    / _// , _/ __ |/ / / /_/ / , _/
/_/ |_/_/   /_/  |_____/ \___/_/|_| /_/|_/_/ |_|___/___/\___/_/ |_/_/  \____/_/|_|  \___/___/_/|_/___/_/|_/_/ |_/_/  \____/_/|_| 


'''

def read_technique_ids_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            technique_ids = [line.strip() for line in file if line.strip()]
        return technique_ids
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []

def generate_attack_json(technique_ids, name, description="", sorting=0, show_id=False, output_file_name="cbc-heatmap-coverage.json"):
    logging.info("Generating ATT&CK Navigator layer...")

    navigator_json = {
        "name": name,
        "versions": {
            "attack": "15",
            "navigator": "5.0.1",
            "layer": "4.5"
        },
        "domain": "enterprise-attack",
        "description": description,
        "sorting": sorting,
        "layout": {
            "layout": "side",
            "showName": True,
            "showID": show_id,
            "showAggregateScores": True,
            "countUnscored": True,
            "aggregateFunction": "average"
        },
        "hideDisabled": False,
        "techniques": [],
        "gradient": {
            "colors": ["#8ec843", "#ffe766", "#ff6666"],
            "minValue": 0,
            "maxValue": 9
        },
    }

    for technique_id in technique_ids:
        existing_technique = next(
            (tech for tech in navigator_json["techniques"] if tech["techniqueID"] == technique_id), None)
        if existing_technique:
            existing_technique["score"] += 1
        else:
            technique_object = {
                "techniqueID": technique_id,
                "score": 1  
            }
            navigator_json["techniques"].append(technique_object)

    with open(output_file_name, 'w') as output_file:
        json.dump(navigator_json, output_file, indent=4)

    logging.info(f"ATT&CK Navigator layer JSON saved to {output_file_name} successfully!")

if __name__ == "__main__":

    print(ATTACK_LOGO + "by threatHNTR\n")

    input_file = input("Enter the path to the input file (techniques.txt): ")
    technique_ids = read_technique_ids_from_file(input_file)

    if not technique_ids:
        logging.error("No technique IDs found. Exiting program.")
        exit()

    name = input("Enter the layer name: ")
    description = input("Enter the layer description (optional): ")
    sorting_input = input("Enter the sorting option (0-3, default is 0): ")
    sorting = int(sorting_input) if sorting_input.isdigit() else 0
    show_id_input = input("Show ATT&CK IDs in the output? (yes/no, default is no): ")
    show_id = True if show_id_input.lower() == "yes" else False

    output_file_name = input("Enter the output file name (default is 'attack.json'): ")
    output_file_name = output_file_name if output_file_name.strip() else "attack.json"

    generate_attack_json(technique_ids, name, description, sorting, show_id, output_file_name)
