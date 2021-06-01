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
The configuration is simple json file, with default element of "pages". Each "page" needs to have "key", which defines each page. The file that will be created and searched in is named after this. If you want to override to whom you want to send email you include element "to_email", if element will be missing, emails from config will be used. If the link of each advert is combined with default url and page url, you have to enter element "default_url" otherwise you simply leave it empty or skip it. Element "page_url" is the page url that will be used for search. It has to contain all filters used for search. Element "mail_subject" is tag for defining subject you will recieve in mail, so if you run script for more pages you can identify upfront which one was changed. Element "bs4_block" is custom for each page, because some of webpages can use default blocks as "div" (most cases) some can use others - if you skip this element or leave it empty, it will use default "div". Element "href_parser" is used for finding links to advert - most pages have href defined in "a" tag, but there exists some of them that does not have it like that, so you can customize it - if you skip this element or leave it empty, it will use default "a". Element block "bs4_attrs" is used for searching adverts as full blocks. It has to have "class" tag so we can find the right block with advert, and it is recomended to use "itemtype" so it can be more specific. Element "bs4_attrs" can be skipt and script will use default configuration "{"class":"oglas_container", "itemtype": "http://schema.org/ListItem"}". Element block "info_attributes" is used to find some info of advert. it has 3 tags - "bs4_block" - block in the webpage where we find the info, "bs4_attrs" is same as before and can be empty and "bs4_class" with class name for more specific search. All data of element block "info_attributes" is optional and if empty it will use default settings. The same stuctire as element block "info_attributes" is for element block "summary_attributes".

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Resources:

https://www.nepremicnine.net/

https://realpython.com/python-concurrency/

https://realpython.com/intro-to-python-threading/

