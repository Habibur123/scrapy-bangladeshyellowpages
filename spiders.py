from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from byellow.items import ByellowItem
from scrapy.http import Request
from bs4 import BeautifulSoup
from textprocessing import textparsing

class ByellowSpider(BaseSpider):
    name = 'byellow'
    allowed_domains = []
    start_urls = ['http://www.bangladeshyellowpages.com/search/alpha:a']
    def complateurl(self,url):
        return 'http://www.bangladeshyellowpages.com'+url
    def phonenumber(self,soup):
        tel=soup.find('h4')
        t=textparsing()
        number=t.getTargetWord('Tel :','',tel.text)
        return number.replace(',',' ')
    def address(self,soup):
        p=soup.find_all('p')
        for n in p:
            txt=n.text
            if txt.find('Address')!=-1:
                    t=textparsing()
                    address=t.getTargetWord('Address:','',txt)
                    return address.replace(',','')
            return ''
    def email(self,soup):
        p=soup.find_all('p')
        for n in p:
            txt=n.text
            if txt.find('Email')!=-1:
                t=textparsing()
                email=t.emailaddress(txt)
                return ' '.join(email)
        return ''
    def website(self,soup):
        p=soup.find_all('p')
        for n in p:
            txt=n.text
            if txt.find('Website:')!=-1:
                t=textparsing()
                site=t.getTargetWord('Website:','',txt)
                return site
        return ''
    def des(self,soup):
        desc=soup.find("p",{"class":"shortdes"})
        t=textparsing()
        ds=t.clearwhitespace(desc.text)
        return ds.replace(',','')
    def pagination(self,body):
        soup = BeautifulSoup(body)
        pagin=soup.find("div",{"class":"paginator"})
        span=pagin.find_all('span')
        urllist=[]
        if span is not None:
            for n in span:
                a=n.find('a')
                if a is not None:
                    classname=a.get('class')
                    if classname[0]=='page-numbers':
                        urllist.append(self.complateurl(a.get('href')))
        return  urllist


    def parse(self, response):

        soup=BeautifulSoup(response.body_as_unicode())
        cat=soup.find("div",{"class":"listing"})
        allcat=cat.find_all('li')
        for n in allcat:
            a=n.find('a');
            category=a.text
            link=self.complateurl(a.get('href'))
            yield   Request(link,meta={'category':category}, callback=self.parsepagin)

    def parsepagin(self,response):

        urllist=self.pagination(response.body_as_unicode())
        soup=BeautifulSoup(response.body_as_unicode())
        company=soup.find("dl",{"class":"result"})
        companylist=company.find_all('dd')
        for n in companylist:
            item=['','']
            a=n.find('a')
            item[1]=a.text
            item[0]=response.meta['category']
            link=self.complateurl(a.get('href'))
            yield   Request(link,meta={'info':item}, callback=self.parsedetails)
        for n in urllist:
            yield   Request(n,meta={'category':response.meta['category']}, callback=self.parsecategory)


    def parsecategory(self,response):
        soup=BeautifulSoup(response.body_as_unicode())
        company=soup.find("dl",{"class":"result"})
        companylist=company.find_all('dd')
        for n in companylist:
            item=['','']
            a=n.find('a')
            item[1]=a.text
            item[0]=response.meta['category']
            link=self.complateurl(a.get('href'))
            yield   Request(link,meta={'info':item}, callback=self.parsedetails)

    def parsedetails(self,response):
        soup=BeautifulSoup(response.body_as_unicode())
        details=soup.find("div",{"class":"infocon"})
        item=ByellowItem()
        item['companyname']=response.meta['info'][1]
        item['category']=response.meta['info'][0]
        item['tel']=self.phonenumber(details)
        item['email']=self.email(details)
        item['address']=self.address(details)
        item['website']=self.website(details)
        item['description']=self.des(soup)
        return item











