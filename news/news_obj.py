class News:
    """
    News object for instantiating title,site,link and date
    """
    
    def __init__(self,title,link,site,date=""):

        self._title = title
        self._link = link
        self._date = date
        self._site = site

    def title(self):
        """
        Returns title of news
        """
        return self._title

    def site(self):
        """
        Returns site of news
        """
        return self._site

    def link(self):
        """
        Returns link of news
        """
        return self._link

    def date(self):
        """
        Returns date of news
        """
        return self._date

    def set_date(self,date):
        """
        Set date of news
        """
        self._date = date
        
    def __eq__(self,other):
        """
        Returns if the news are same
        """
        return self._link == other.link()

    def __repr__(self):
        """
        Provides represntation of news
        """
        return '{}:{}:{}'.format(self._site[:5] , self._title ,self._date)


    
