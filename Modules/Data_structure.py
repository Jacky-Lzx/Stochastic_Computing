
class Priority_queue:
    def __init__(self):
        self.arr = list()

    def add(self, element):
        self.arr.append(element)
        list.sort(self.arr, key=lambda a: a.val())

    def remove_last(self):
        del(self.arr[-1])

    def length(self):
        return len(self.arr)

    def empty(self):
        return len(self.arr) == 0

    def print(self):
        print("---------Priority queue-------")
        for i in self.arr:
            print(i)
        print("--------------end-------------")