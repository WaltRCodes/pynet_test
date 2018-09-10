from __future__ import print_function, unicode_literals
from mytest import func1, func2, func3, MyClass


def main():
    func1()
    func2()
    func3()
    my_obj = MyClass('a', 'b', 'c')
    my_obj.threefunc()
    my_obj.remove_threefunc()


if __name__ == "__main__":
    main()
