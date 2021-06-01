import json

from helpers.page import Page

json_file = 'configuration.json'

from_email = 'example@gmail.com'
to_email = ['example2@gmail.com']
gmail_api_key = 'example_key'

configuration = []
with open(json_file) as json_file_path:
    for page in json.load(json_file_path)['pages']:
        page_conf = Page(page)
        page_conf.to_email = page_conf.to_email if page_conf.to_email != '' else to_email
        configuration.append(page_conf)

def get_serach_url(url :str, i :int):
    return f'{url}/{i}/'
