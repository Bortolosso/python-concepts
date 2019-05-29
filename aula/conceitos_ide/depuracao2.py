#coding: utf-8

a = 10
b = 1,2,3
x = [a,b]

def function1():
    print("TEXTO")
def function2():
    function1()
def function3():
    function2()
def function4():
    function3()
def function5():
    function4()

function5()

print(a)
print(b)
print(x)

