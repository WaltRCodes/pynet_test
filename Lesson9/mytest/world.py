from __future__ import print_function, unicode_literals
def func1():
    print("function1")
class MyClass(object):
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def threefunc(self):
        print("{} {} {}".format(self.var1, self.var2, self.var3))

    def remove_threefunc(self):
        print("Removing {} {} {}".format(self.var1, self.var2, self.var3))

class childclass(MyClass):
    def __init__(self, var1, var2, var3):
        print("Do something more in __init__()")
        MyClass.__init__(self, var1, var2, var3)
    def hello(self):
        print("Something else: {} {} {}".format(self.var1, self.var2, self.var3))



if __name__ == "__main__":
    print("function1 - world")
    my_obj = MyClass('NY', 'OH', 'TX')
    print(my_obj.var1, my_obj.var2, my_obj.var3)
    my_obj.threefunc()
    my_obj.remove_threefunc()
    new_obj = childclass('A', 'B', 'C')
    new_obj.threefunc()
    new_obj.remove_threefunc()
