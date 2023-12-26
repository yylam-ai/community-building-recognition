class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, child):
        self.children.append(child)
        return self
    
    def test(self,array):
        queue = [self]
        print (queue.pop(0))


test = Node('a')
test.addChild('b')
test.addChild('c')
test2 = Node('d')
test2.addChild('e')
test.addChild(test)

array= [1,2,3]
test.test(array)