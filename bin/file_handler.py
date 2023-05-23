import ijson
import json
import os

fp = 'C:\\xampp\\htdocs\\git\\get-rich-quick\\output.txt' #TODO: change this so it becomes dynamic

def process_auctionhouse_file(file_path, target_id):
    with open(file_path, 'rb') as f:
        # Create an iterator to parse the JSON data incrementally
        parser = ijson.parse(f)

        # Initialize variables
        row_iterator = 1
        current_id = 0
        quantity = 0

        # initialize the 
        auctionhouse_item = {
            'item_id': 37663,
            'item_auctionhouse_row': [
                {
                    'auctionhouse_row_id': 1,
                    'auctionhouse_price': 0,
                    'auctionhouse_quantity_per_price': 0
                }
            ]
        }

        # Iterate over the JSON stream
        for prefix, value in parser:
            # Check the 'id' field
            if prefix == 'auctions.item.item.id' and value == target_id:
                current_id = value

            if prefix == 'auctions.item.quantity' and current_id == target_id:
                quantity = value
            
            if prefix == 'auctions.item.unit_price' and current_id == target_id:
                price = value
                #print('ID: ' + str(current_id) + ', price: ' + str(value) + ', quantity: ' + str(quantity))

                #get highest id
                highest_id = max(auctionhouse_item['conf'], key=lambda x: x['id'])['id'] + 1

                # create new 
                new_conf = {
                    'auctionhouse_row_id': highest_id,
                    'auctionhouse_price': price,
                    'auctionhouse_quantity_per_price': quantity
                }

                auctionhouse_item['item_auctionhouse_row'].append(new_conf)

                # reset variables
                current_id = 0
                quantity = 0
                price = 0
        
        print(auctionhouse_item)



# Call the function with the path to your large JSON file
process_auctionhouse_file(fp, 37663)

