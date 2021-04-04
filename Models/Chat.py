class TestChat:
    usrerep = []
    sitarep = [["hi"]]
    type = None
    isrun=None
    rate=None

    def __init__(self):
        self.usrerep = []
        self.sitarep = ["hi"]
        self.mass = 0

    def get_isrun(self):
        return self.isrun

    def set_isrun(self,g_isrun):
        self.isrun=g_isrun

    def get_rate(self):
        return self.rate

    def set_rate(self,g_rate):
        self.rate=g_rate

    def get_usrerep(self):
        return self.usrerep

    def set_usrerep(self, usrerep):
        self.usrerep.append(usrerep)

    def get_sitarep(self):
        return self.sitarep

    def set_sitarep(self, sitarep):
        self.sitarep.append(sitarep)

    def get_lastuserreply(self):

        return self.usrerep[len(self.usrerep)-1]

    def get_lastsaitareply(self):
        return self.sitarep[len(self.sitarep)-1]

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type
