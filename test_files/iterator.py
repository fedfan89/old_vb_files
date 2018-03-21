class remote(object):
    def __init__(self):
        self.channels = ['hbo', 'cnn', 'espn']
        self.index = -1

    def __iter__(self):
		return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        else:
            return self.channels[self.index]
    
    def paul(self):
        return "Hi Paul"

r = remote()
print(r)
print(r.index)
r.__next__()
print(r.index)
r.__next__()
print(r.channels)
print(r.paul())
