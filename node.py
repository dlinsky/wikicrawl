

class Node:
    def __init__(self, data):
        self.children = []
        self.data = data

    def addChild(self, child):
        self.children.append(child)

    def printChild(self):
        for x in self.children:
            print(x.data)
    
