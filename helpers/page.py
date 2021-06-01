import helpers.config_defaults as defaults

class Page:
    def __init__(self, page):
        self.key = page["key"]
        self.to_email = page["to_email"] if "to_email" in page else ""
        self.default_url = page["default_url"] if "default_url" in page else ""
        self.page_url = page["page_url"]
        self.mail_subject = page["mail_subject"] if "mail_subject" in page else defaults.mail_subject
        self.bs4_block = page["bs4_block"] if "bs4_block" in page else defaults.bs4_block
        self.href_parser = page["href_parser"] if "href_parser" in page else defaults.href_parser
        self.bs4_attrs = page["bs4_attrs"] if "bs4_attrs" in page else defaults.bs4_attrs
        self.info_attributes_bs4_block = page["info_attributes"]["bs4_block"] if "info_attributes" in page and "bs4_block" in page["info_attributes"] else defaults.info_attributes_bs4_block
        self.info_attributes_bs4_attrs = page["info_attributes"]["bs4_attrs"] if "info_attributes" in page and "bs4_attrs" in page["info_attributes"] else defaults.info_attributes_bs4_attrs
        self.info_attributes_bs4_class = page["info_attributes"]["bs4_class"] if "info_attributes" in page and "bs4_class" in page["info_attributes"] else defaults.info_attributes_bs4_class

        self.summary_attributes_bs4_block = page["summary_attributes"]["bs4_block"] if "summary_attributes" in page and "bs4_block" in page["summary_attributes"] else defaults.summary_attributes_bs4_block
        self.summary_attributes_bs4_attrs = page["summary_attributes"]["bs4_attrs"] if "summary_attributes" in page and "bs4_attrs" in page["summary_attributes"] else defaults.summary_attributes_bs4_attrs
        self.summary_attributes_bs4_class = page["summary_attributes"]["bs4_class"] if "summary_attributes" in page and "bs4_class" in page["summary_attributes"] else defaults.summary_attributes_bs4_class
    