class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

    def addInfo(self,data):
        self.info.append(data)
    
    def __repr__(self):
        return str(self.data)