
#concat {function} methold
#criar listar
def list_creator(txt):
   lista_primaria = list(txt)
   return lista_primaria

#e separa
def sp_list(word,):
 b=word
 fim = int(len(b))
 meio = int(len(b)/2)
 new_list = list(b)
 lado_a = slice(0,meio)
 lado_b = slice(meio,fim)
 saidA=new_list[lado_a]
 saidB=new_list[lado_b]
 print(saidB)
 print(saidA)
 return saidA,saidB
 


#lista{bytes}
def conv_bin(a):
            #texto a ser criptografado
 arr = bytes(a, 'utf-8')           #palavra -> bytes
 arr2 = str(arr, 'utf-8')
 print(arr,'\n') 
                       #imprimir resultado caso tenha dado certo

 for byte in arr:                        #mostra os bytes
    print(byte, end=' - ')
 print("\n")
 
 for w in arr2:                       #mostra a frase 
    print(w, end=" - ")    
 return arr

#lista {join}
def WordConcat(word):   
 word = "".join(word)
 print(word)
 return(word)
listA = ["o","p","p"]
listB = ["o","p","q"]
def ListConcat(listA,listB):   
 new_listA = "".join(listA)
 new_listB = "".join(listB)
 new_list = new_listA + new_listB
 return(new_list)

#list -> bin
def listBin(b,c,d):
 for c in b:
    f = c
    d.append(bin(f)[2:])




