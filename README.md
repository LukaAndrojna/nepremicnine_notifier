# Nepremicnine Scraper and notifier

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Usage

Change the config.py file by entering in your email adresses and a gmail generated API key.
In configuration.json you can change and add pages you want to check. There exist a simple template what it should look like and also in next section there is description of json elements.

Run
Navigate to this directory.
```bash
bash setup.sh
python3 scraper.py
```
run the bash script on the first run only. I suggest you make a cron tab or nssm.exe for creating window service and add a while loop or with timeouts if you want to automate this.

## Configuration
The configuration is simple json file, the parameters you need to edit are:
- `key`: this will be used to seperate different queries to nepremicnine (and other sites in the future)
- `default_url`: root url of the page (for instance: "https://www.nepremicnine.net")
- `page_url`: link of the page you want to scrape, on nepremicnine.net thatis all filters used for search
- `from_email`: the Gmail address the email notification should be sent from
- `gmail_api_key`: generated API key or password for this email address
- `to_email`: list of all of recipient's email addresses 
- `mail_subject`: subject of the email

Advanced features defaults are set up for nepremicnine.net:

- `bs4_block` can differ between pages, change if needed. Defaults to `div`.
- `href_parser` used for finding links to advert, can differ between pages, change if needed. Defaults to `a`.
- `bs4_attrs` is used for searching adverts as full blocks:
  - `class` is used so we can find the right block within the advert.
  - `itemtype` so it can be more specific.
- `bs4_attrs`: is optional, defaults to "{"class":"oglas_container", "itemtype": "http://schema.org/ListItem"}".
- `info_attributes` is used to find some info of advert. it has 3 tags:
  - `bs4_block`: block in the webpage where we find the info.
  - `bs4_attrs`: is same as before and can be empty.
  - `bs4_class`: with class name for more specific search.

## Contributors
- [LukaAndrojna](https://github.com/LukaAndrojna)
- [KristjanDS](https://github.com/kristjands)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Resources:

https://www.nepremicnine.net/

https://realpython.com/python-concurrency/

https://realpython.com/intro-to-python-threading/

