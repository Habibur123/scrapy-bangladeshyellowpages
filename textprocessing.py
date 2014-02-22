import re
class textparsing():
    def clearwhitespace(self,string):
        pattern = re.compile(r'\s+')
        return re.sub(pattern, ' ',string)
    def clearspace(self,string):
        return string.lstrip()
    def getTargetWord(self,fboundary,sboundary,string):
        if (sboundary==''):
            slen=len(string)
        else:
            slen=string.find(sboundary)
        return self.clearspace(string[len(fboundary)+string.find(fboundary):slen])
    def emailaddress(self,string):
        return re.findall(r'[\w\.-]+@[\w\.-]+', string)
    def website(self,string):
        sites=[]
        site=re.findall('https://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
        for s in site:
            sites.append(s)
        site=re.findall('http://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
        for s in site:
            sites.append(s)
        site=re.findall('http://www.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
        for s in site:
            sites.append(s)
        #site=re.findall('www.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
        #for s in site:
        #    sites.append(s)
        return sites
    def phonnumber(self,string):
        return re.findall('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', string)
