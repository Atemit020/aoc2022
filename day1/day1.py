file = open("day1.txt", "r")
c=[]
n=0
for i in file.readlines():
    if i != "\n":
        n+=int(i)
    else:
        c.append(n)
        n=0

max_=max(c)
print(max_)
