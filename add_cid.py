import json
import os

# Path to the metadata directory
metadata_directory = 'metadata'

# CID for the IPFS
cid_ipfs = 'QmPr1FVzMTuRn42D3qPvThF1BNc1svgHRHKUeMTenQACqg'

def update_image_link(token_id, cid_ipfs):
    return f'{cid_ipfs}/tribal-{token_id}.png'

# Iterate over each file in the metadata directory
for filename in os.listdir(metadata_directory):
    if filename.endswith('.json'):
        file_path = os.path.join(metadata_directory, filename)
        
        # Read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Update the "image" field
        data['image'] = update_image_link(data['tokenId'], cid_ipfs)
        
        # Write the updated data back to the same JSON file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Updated {file_path}")
