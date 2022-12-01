import os

BASE = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE, "day1.txt")
file = open(path, "r")
c=[]
n=0
d=[]
part=input("Do you want the second part (N/y) ").upper()
for i in file.readlines():
    if i != "\n":
        n+=int(i)
    else:
        c.append(n)
        n=0

max_=max(c)
match part:
    case "Y":
        for i in range(3):
            max_=max(c)
            d.append(max_)
            c.remove(max_)
        print(sum(d))
    case default:
        print(max_)
