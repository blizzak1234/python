from math import sqrt

def solve(a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        print ("no solutions")
    elif d == 0:
        x = -b / (2*a)
        print ("one solution " + str(x))
    elif d > 0:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2*a)
        print ("two solutions " + str(x1) + " and " + str(x2))
    else:
        print("AAAAAAAAAAAAA!!!")


solve(1,1,1)
solve(1,2,1)
solve(1,5,6)



l = []

for i in range(-5, 6):
    l.append(Point(i, i*i))
print(l)

for el in l:
    el.y = -el.y
    print(el)

