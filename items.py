from scrapy.item import Item, Field

class ByellowItem(Item):
    companyname=Field()
    category=Field()
    tel=Field()
    email=Field()
    address=Field()
    website=Field()
    description=Field()
