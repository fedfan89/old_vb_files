class Test(object):
    def __init__(self):
        self.value = 5
    
    def function(self):
        print(self.value)

a = Test()
a.function()

class Test2(object):
    value = 5

    def function2(self):
        print(self.value)

b = Test2()
b.function2()

class Test3(object):
    i = 5

t = Test3()
t.p = 66
print(Test3.i, t.i, t.p, t.__dict__)
