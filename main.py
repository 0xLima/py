import os
import json

# Path to the directory containing JSON files
directory_path = 'metadata'

for filename in os.listdir(directory_path):
    if filename.endswith('.json'):
        file_path = os.path.join(directory_path, filename)
        token_id = int(filename.split('.')[0])  # Extract the number from filename

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Insert "tokenId" at the beginning of the JSON object
        new_data = {"tokenId": token_id}
        new_data.update(data)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(new_data, file, ensure_ascii=False, indent=2)

print("Completed updating tokenId for all JSON files.")