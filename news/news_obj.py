class News:
    
    def __init__(self,title,link,site,date=""):
        self._title = title
        self._link = link
        self._date = date
        self._site = site

    def title(self):
        return self._title

    def site(self):
        return self._site

    def link(self):
        return self._link

    def date(self):
        return self._date

    def __eq__(self,other):
        return self._link == other.link()

    def __repr__(self):
        return '{}:{}:{}'.format(self._site[:5] , self._title ,self._date)


    
