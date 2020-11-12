#quebra de list e relocaçao
#listar e separa
a = "uva"
def sp_list(a):
 b=a
 c = int(len(b))
 e = int(len(b)/2)
 d = list(b)
 lado_a = slice(0,e)
 lado_b = slice(e,c)
 print(d[lado_a])
 print(d[lado_b])

sp_list(a)