class SearchResult:

    def __init__(self):
        self.title=""
        self.lastmod=""
        self.resourceType=""
        self.church=""
        self.resourceURL=""
        self.thumbnailURL=""
        self.tags=""
        self.isPinned=0

    def __repr__(self):
        lines = '---------------------------------------\r\n'
        returnMe = lines
        returnMe = returnMe + 'Church: ' + self.church + '\r\n'
        returnMe = returnMe + 'Title: ' + self.title + '\r\n'
        returnMe = returnMe + 'Resource URL: ' + self.resourceURL + '\r\n'
        returnMe = returnMe +'Church: ' +  self.church + '\r\n'
        returnMe = returnMe +'Last Mod: ' +  self.lastmod + '\r\n'
        returnMe = returnMe +'Thumb URL: ' +  self.thumbnailURL + '\r\n'

        returnMe = returnMe + lines
        return returnMe
    #
    # @property
    # def title(self):
    #     return self.title
    #
    # @title.setter
    # def title(self,new):
    #     self.title = new
    #
    # @property
    # def lastmod(self):
    #     return self.lastmod
    #
    # @lastmod.setter
    # def lastmod(self, new):
    #     self.lastmod = new
    #
    # @property
    # def resourceType(self):
    #     return self.resourceType
    #
    # @resourceType.setter
    # def resourceType(self, new):
    #     self.resourceType = new
    #
    # @property
    # def church(self):
    #     return self.church
    #
    # @church.setter
    # def church(self, new):
    #     self.church = new
    #
    # @property
    # def resourceURL(self):
    #     return self.resourceURL
    #
    # @resourceURL.setter
    # def resourceURL(self, new):
    #     self.resourceURL = new
    #
    # @property
    # def thumbnailURL(self):
    #     return self.thumbnailURL
    #
    # @thumbnailURL.setter
    # def thumbnailURL(self, new):
    #     self.thumbnailURL = new
    #
    # @property
    # def tags(self):
    #     return self.tags
    #
    # @tags.setter
    # def tags(self, new):
    #     self.tags = new
    #
    # @property
    # def isPinned(self):
    #     return self.isPinned
    #
    # @isPinned.setter
    # def isPinned(self, new):
    #     self.isPinned = new
