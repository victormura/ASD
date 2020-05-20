class Node:
    def __init__(self):
        self.val = []
        self.child = [None]
        self.length = 0
        self.parent = None

    def __add__(self, other):
        index = self.index(other)
        self.val = self.val[:index] + [other] + self.val[index:]
        self.child = self.child[:index] + [None] + self.child[index:]
        self.length += 1
        return self

    def index(self, val):
        index = 0
        while index < self.length and val > self.val[index]:
            index += 1
        return index

    def parent_child(self):
        for x in self.child:
            if x is not None:
                x.parent = self

    def split(self, aux, index):
        k = aux.length // 2

        self.child[index] = Node()
        self.child[index + 1] = Node()

        for x in aux.val[:k]:
            self.child[index] + x

        for x in aux.val[k + 1:]:
            self.child[index + 1] + x

        self.child[index].child = aux.child[:k + 1]
        self.child[index + 1].child = aux.child[k + 1:]

        self.parent_child()
        self.child[index].parent_child()
        self.child[index + 1].parent_child()

    def union(self,nod, index):
        self.child = self.child + nod.child
        self.val = self.val + [self.parent.val[index]] + nod.val
        self.length = len(self.val)

        self.parent.child.remove(nod)
        self.parent.val.remove(self.parent.val[index])
        self.parent.length -= 1
