class Heap():
    def __init__(self, comp_fun):
        self.data = [0]
        self.comp_fun = comp_fun

    # Helper Methods #

    def parent(self, i):
        return i // 2

    def left(self, i):
        return i * 2

    def right(self, i):
        return (i * 2) + 1

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    # Public Methods #

    def size(self):
        return self.data[0]

    def compare(self, i1, i2):
        # return true if i1 should be above i2
        if i1 > self.size() or i2 > self.size():
            return True
        return self.comp_fun(self.data[i1], self.data[i2])

    def insert(self, val):
        self.data.append(val)
        self.data[0] = self.data[0] + 1

        i = self.size()
        j = self.parent(i)
        while j > 0 and self.compare(i, j):
            self.swap(i, j)
            i = j
            j = self.parent(j)
        print self.data
        return self

    def delete(self):
        removed = self.data[1]
        self.swap(1, -1)
        self.data = self.data[:-1]
        i = 1
        while self.compare(self.left(i), i) or self.compare(self.right(i), i):
            to_swap = self.left(i) if self.compare(self.left(i), self.right(i)) else self.right(i)
            self.swap(i, to_swap)
            i = to_swap
            if (self.left(i) >= self.size() or self.right(i) >= self.size()):
                break

        self.data[0] = self.size() - 1
        print( self.data )
        return removed


def f(a, b):
    return a > b

h = Heap(f)
h.insert(3)
h.insert(8)
h.insert(4)
h.insert(9)
h.insert(7)
h.insert(2)

h.delete()
h.delete()
h.delete()

# print(h.data)
