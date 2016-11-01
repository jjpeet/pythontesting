#Test
#import urllib.request
import requests

def test_file(text_string):
    this_file = open('test2.txt','a')
    this_file.write(text_string)
    this_file.close()


def get_data(url):
    data_request = requests.get(url)
    data_json = data_request.json()
    #print(data_json)
    fish_data = ''
    records = data_json['result']['records']
    count = 0
    for count in range(2):
        CommonName = data_json['result']['records'][count]['CommonName']
        MinSize = data_json['result']['records'][count]['MinSize']
        MaxSize = data_json['result']['records'][count]['MaxSize']
        FamilyName = data_json['result']['records'][count]['FamilyName1']
        Distribution = data_json['result']['records'][count]['Distribution']
        Image = data_json['result']['records'][count]['Image1']
        Description = data_json['result']['records'][count]['Description']
        
        fish_data = fish_data + 'Common Name\t' + CommonName + '\n'
        fish_data = fish_data + 'Family Name\t' + FamilyName + '\n'
        fish_data = fish_data + 'Max size\t' + MaxSize + '\n'
        fish_data = fish_data + 'Min size\t' + MinSize + '\n'
        fish_data = fish_data + 'Description\t' + Description + '\n'
        fish_data = fish_data + 'Image\t' + Image + '\n'
        fish_data = fish_data + '\n\n'

        count += count

    print(records)
    return(fish_data)

def main():

    url = 'https://data.qld.gov.au/api/action/datastore_search?limit=2&resource_id=32af9a35-d4db-41e9-b152-d52609ff6372'
    returned_data = get_data(url)

    test_file(returned_data)



main()

