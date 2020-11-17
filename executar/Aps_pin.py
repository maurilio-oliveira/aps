from Encript_pinheiros import*

i = ""
plan_txt ="maurilio"
passw= "m"

while i !="exit()":
 plan_txt = input("Digite um texo: ")
 passw=input("digite uma chave de um digito: ")
 binari = ConvToBin(plan_txt)
 passW = ConvToBin(passw)
 k = xor(binari,passW)
 s =ConvToString(k)

 d = xor(k,passW)
 c = ConvToString(d)
 print(c,"\n","\n",s)
 i = input("para sair digite: 'exit()' ")
 

