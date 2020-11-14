from junçao import*

i = ""
plan_txt ="ma"
passw= "E"


def test(plan,passw):
   
 binari = ConvToBin(plan_txt)
 passW = ConvToBin(passw)
 k = xor(binari,passW)
 s =ConvToString(k)
 return s

def test2(k,p):
 passW = ConvToBin(p)
 k = ConvToBin(k)
 d = xor(k,passW)
 c = ConvToString(d)
 return c

while i != "exit()":
 plan_txt =input("escreva a senha: ")
 passw= input("escreva o texto a ser codificado: ")
 a =test(plan_txt,passw)
 print(a)
 k = a
 b = test2(a,passw)
 print(b)












    
