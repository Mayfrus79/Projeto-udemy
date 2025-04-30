from collections import deque
from pathlib import Path
import json

parking = deque(maxlen=4)

parking.append({"Plate": "AAA111", "Model": "Corsa", "Color": "Gray"})
parking.append({"Plate": "BBB222", "Model": "Palio", "Color": "Red"})
parking.append({"Plate": "CCC333", "Model": "Gol", "Color": "Black"})
parking.appendleft({"Plate": "DDD444", "Model": "Fox", "Color": "White"})

FOLDER_PATH = Path.home() / "Desktop" / "Json_folder"
FOLDER_PATH.mkdir(exist_ok=True)
JSON_FILE = FOLDER_PATH / "Json_file.json"

if JSON_FILE.exists():
    print(f"The file '{JSON_FILE.name}' already exist in the folder '{FOLDER_PATH.name}'.")

else:
    with open(JSON_FILE, 'w', encoding='utf-8') as file:
        json.dump(list(parking), file, indent=3, ensure_ascii=False)
        print(f"File saved as: '{JSON_FILE.name}' in the folder: '{FOLDER_PATH.name}'")    