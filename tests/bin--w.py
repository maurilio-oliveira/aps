def listar(a):
 b = a.encode("utf-8")
 d = []
 for c in b:
    f = c
    d.append(bin(f)[2:])
    print(d)
listar("maumau")

