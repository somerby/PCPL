import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.index = 0
        if 'ignore_case' in kwargs:
            self.items = list({i.lower() if kwargs['ignore_case'] else i for i in items})
        else: self.items = list({i for i in items})

    def __next__(self):
        if self.index < len(self.items):
            out = self.items[self.index]
            self.index += 1
            return out
        else:
            self.index = 0
            raise StopIteration

    def __iter__(self):
        return self

def main():
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    _set1 = Unique(data)
    print(', '.join([str(i) for i in _set1]))
    data = gen_random.gen_random(10, 1, 3)
    _set2 = Unique(data)
    print(', '.join([str(i) for i in _set2]))
    data = ['a', 'A', 'b','B', 'a', 'A', 'b', 'B']
    _set3 = Unique(data)
    print(', '.join([str(i) for i in _set3]))
    data = ['a', 'A', 'b','B', 'a', 'A', 'b', 'B']
    _set4 = Unique(data, ignore_case=True)
    print(', '.join([str(i) for i in _set4]))

if __name__ == '__main__' :
    main()