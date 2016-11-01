#Test

import urllib.request

def test_file(text_string):
    this_file = open('test.txt','a')
    this_file.write(text_string)
    this_file.close()


def get_data(url):
    fileobj = urllib.request.urlopen(url)
    fish_data=fileobj.read()
    return(fish_data)

def main():

    url = 'https://data.qld.gov.au/api/action/datastore_search?resource_id=32af9a35-d4db-41e9-b152-d52609ff6372'
    returned_data = get_data(url)

    print(returned_data)

main()

