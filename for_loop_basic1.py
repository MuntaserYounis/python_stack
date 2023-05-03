for x in range(150): #basic
    print(x)

for y in range(5,1001,5): #multiples of five
    print(y)

for x in range(1,101,1): #counting the dojo way
    if x%10 == 0:
        print("Coding Dojo")
    elif x%5 == 0:
        print("Coding")
    else:
        print(x)

total = sum(range(1,500000,2)) # whoa that sucker's huge , other way to do it?
print(total)

for z in range(2018,0,-4):
    print(z)

lowNum = int(3)
highNum = int(9)
mult = int(3)

for c in range(lowNum-1,highNum+1):
    if c%mult == 0:
        print(c)
