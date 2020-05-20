from Node import Node

class BinaryTree:
    grad = 100
    def __init__(self):
        self.root = Node()

    def insert(self, val):
        current, index = self.traverse(val)
        current = current + val

        while current.length >= self.grad:
            if current.parent is None:
                current.parent = Node()
                self.root = current.parent

            new = current.parent
            median = current.val[current.length // 2]
            index = new.index(val)

            new = new + median
            new.split(current, index)
            current = new

    def traverse(self, val):
        current = self.root
        index = current.index(val)
        while self.grad > current.length and current.child[index] is not None:
            current = current.child[index]
            index = current.index(val)
        return current, index

    def print(self, current, nivel=0):
        if current.parent is not None:
            print(current.val, nivel, "length" ,len(current.parent.val))
        else:
            print(current.val, nivel)
        for index in current.child:
            if index is not None:
                self.print(index, nivel + 1)

    def sorted(self, current, left, right):
        result = []

        for index in current.child:
            if index is not None:
                self.sorted(index, left, right)
                aux = current.child.index(i)
                if aux < current.length:
                    if current.val[aux] > right:
                        return
                    if current.val[aux] >= left:
                        result.append(current.val[aux])
                        break
        else:
            for x in current.val:
                if x > right:
                    return
                if x >= left:
                    result.append(x)
        return result

    def find(self, current, val):
        if current is None:
            return None, 0

        current.parent_child()
        index = current.index(val)

        if index == current.length or current.val[index] > val:
            return self.find(current.child[index], val)
        elif current.val[index] == val:
            return current, index
        else:
            return self.find(current.child[index + 1], val)

    def delete(self, val):
        current, index = self.find(self.root, val)

        if current is None:
            return 0

        if all(current.child):
            next_val = self.successor(val)
            aux, aux_index = self.find(self.root, next_val)
            if aux.length > self.grad // 2:
                current.val[index], aux.val[aux_index] = aux.val[aux_index], current.val[index]
                current = aux
            else:
                next_val = self.pred(val)
                aux, aux_index = self.find(self.root, next_val)
                current.val[index], aux.val[aux_index] = aux.val[aux_index], current.val[index]
                current = aux
            index = aux_index

        current.val = current.val[:index] + current.val[index + 1:]
        current.length -= 1
        current.child = current.child[:index] + current.child[index + 1:]

        if current.length<self.grad//2 and current.parent is not None:
            return self.balance(current)

    def balance(self, current):
        if current.parent is not None:
            if current not in current.parent.child:
                self.print(self.root)
                return 1

            k = current.parent.child.index(current)

            if current.length < self.grad // 2:
                if k > 0 and current.parent.child[k - 1].length > self.grad // 2:
                    current.val.insert(0, current.parent.val[k - 1])
                    current.length += 1
                    current.parent.val[k - 1] = current.parent.child[k - 1].val[-1]
                    current.child.insert(0, current.parent.child[k - 1].child[-1])

                    del current.parent.child[k - 1].val[-1]
                    del current.parent.child[k - 1].child[-1]
                    current.parent.child[k - 1].length -= 1

                elif k < current.parent.length and current.parent.child[k + 1].length > self.grad // 2:
                    current.val.append(current.parent.val[k])
                    current.length += 1
                    current.parent.val[k] = current.parent.child[k + 1].val[0]
                    current.child.append(current.parent.child[k + 1].child[0])

                    del current.parent.child[k + 1].val[0]
                    del current.parent.child[k + 1].child[0]
                    current.parent.child[k + 1].length -= 1
                    
                else:
                    if k == current.parent.length:
                        current.parent.child[k - 1].union(current, k - 1)
                    else:
                        current.union(current.parent.child[k + 1], k)
                    if current.parent is not None and current.parent.length < self.grad // 2:
                        self.balance(current.parent)
                    if current.parent is None:
                        self.root = current
        else:
            if current.val == []:
                current.child[0].parent = None
                self.root = current.child[0]


    def successor(self,val):
        current = self.root
        while all(current.child):
            current = current.child[current.index(val)]

        while current.index(val) == current.length:
            current = current.parent
            if current is None:
                return
        else:
            return current.val[current.index(val)]
        return

    def predecessor(self,val):
        current = self.root
        if val in current.val:
            return val

        while all(current.child):
            current = current.child[current.index(val)]
            if val in current.val:
                return val

        while current.index(val) == 0:
            current = current.parent
            if current is None:
                return
        else:
            return current.val[current.index(val)-1]
        return
