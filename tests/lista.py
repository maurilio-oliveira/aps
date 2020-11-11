#quebra de list e relocaçao

a = "abcdefghijklmnopqrstuvwxyz"
aux = "bsalkb;vkdebvsakuvba;sbgkbg"
b="miguel" #input()
c = int(len(b))
e = int(len(b)/2)
d = list(b)

for i in b:
    if i in a:
      print("tem: ", i)
    else:
         pass
    

lado_a = slice(0,e)
lado_b = slice(e,c)
print(d[lado_a])
print(d[lado_b])

