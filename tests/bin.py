a = input("test")
b = a.encode("utf-16")
d = []
for c in b:
    f = c
    d.append(bin(f)[2:])

print(a,"\n", b,"\n", c,"\n", d)