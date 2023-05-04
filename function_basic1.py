#1
def a():
    return 5
print(a()) 
#prints 5

#2
def a():
    return 5
print(a()+a())
# prints 10

#3
def a():
    return 5
    return 10
print(a())
#returns 5 because its the first return line shown

#4
def a():
    return 5
    print(10)
print(a())
# #returns 5 because its the value return from the function and saved outside the function

#5
def a():
    print(5)
x = a()
print(x)
#prints the first variable calling the function, then doesn't print anything since x wasn't saved anywhere

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
#prints 3 and 5 seperately, they are treated as strings so they don't get summed

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# treats the numbers as strings so it doesn't do mathematical sum, it just joins them, so its 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# error (explain)

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# prints 7 , 14,21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
#print 8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# prints 500,500,300,500 , print values don't get stored anywhere

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#500,500,300, 500(why not 300?)

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# 500,500, 300 , 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
#1,3,2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# explain the return values of 5,10






