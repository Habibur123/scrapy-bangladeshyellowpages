class ByellowPipeline(object):
    def process_item(self, item, spider):
        if len(item['tel'])<6:
            item['tel']=''
        item['address']=item['address'].replace('Dhaka',' Dhaka')
        item['email']=item['email'].replace(' ',' & ')
        item['website']=item['website'].replace('Web:','')
        return item
