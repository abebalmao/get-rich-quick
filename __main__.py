from blizzardapi import BlizzardApi
import json
import requests

#https://eu.api.blizzard.com/data/wow/search/connected-realm?namespace=dynamic-eu&realms.name.en_US=Draenor&access_token=USjxuNR6LQDBKhoPxtbOBrYh01jbHWfazI

# vars
client_id = 'f8ac93afe57f43189e6335cd67342ead'
client_secret = 'azjcGiGRXAb3VfKqaEgC4b7K8pvXBMhx'
access_token = 'USjxuNR6LQDBKhoPxtbOBrYh01jbHWfazI'

region = 'eu'
locale = 'en_US'


server_name = 'Draenor'
connected_realm_id = 1403
#connected_realm_id = ''
# cheat sheet:
#  - id

def auctions():
    api_client = BlizzardApi(client_id, client_secret)

    # get auctions    
    auctions = api_client.wow.game_data.get_auctions(region, locale, 1403)
    #auctions = api_client.wow.game_data.get_auctions_for_auction_house(region, locale, 1403, 3)

    #print(auctions.keys())

    for i in auctions['auctions']:
        item_id = i['item']['id']
        buyout_unstructured = i.get('buyout')
        
        # manip buyout
        buyout_string = str(buyout_unstructured)
        buyout_string = buyout_string[:-2]
        buyout_value = buyout_string[:-2] + '.' + buyout_string[-2:]
        if i.get('quantity') != 1:
            print(i)
        #    print('Item id: ' + str(item_id) + ' costs ' + buyout_value + 'g.')

def get_json():
    with open('items.json') as json_file:
        data = json.load(json_file)

        component_details_dict = {
            component['component_name']: {
                'component_id': int(component['component_id']),
                'component_price': int(component['component_price']),
                'component_amount': int(component['component_amount'])
            }
            for component in data['components']
        }


        print(component_details_dict)

def run():
    #get_json()
    auctions()



if __name__ == '__main__':
    run()

