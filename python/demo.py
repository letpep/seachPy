#!/usr/bin/python3
#coding=utf-8
class Demo(object):
    message = "hello"
    def show(self):
        print (self.message)
    def __init__(self,name="test"):
        self.name = name

def main():
    demo = Demo(name="test2")
    demo.show()
    print(demo.message)
    Demo.message="world"
    Demo.name="test3"
    print(Demo.message)
    print(demo.name)
    print(Demo.name)


if __name__ == "__main__":
    main()