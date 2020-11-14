
#concat {function} methold
#criar listar
def list_creator(txt):
   lista_primaria = list(txt)
   return lista_primaria

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

def ConvToString(binario): # word -> bin
    binario = str(binario)
    caractere = ''
    string = ''
    tamanho = len(binario)
    k = 1
    for j in binario:
        if j != ' ':
            caractere += j
            if k == tamanho:
                string += chr(int(caractere, 2))
        else:
            string += chr(int(caractere, 2))
            caractere = ''  
        k += 1
    return string

def WordConcat(word):   
 word = "".join(word)
 print(word)
 return(word)

def ListConcat(listA,listB):   #conatena lado a e lado b
 new_listA = "".join(listA)
 new_listB = "".join(listB)
 new_list = new_listA + new_listB
 return(new_list)

def listBin(b,c,d): #lista -> bin
 for c in b:
    f = c
    d.append(bin(f)[2:])

def ConvToBin(string): # bin ->word
    binar = ''
    for i in string:
        binar += bin(ord(i))[2::] + ' '
    return binar

def xor(a,b): #xor with binarios
 key=''
 lista_a =list(a)          
 lista_b = list(b)
 ta = len(lista_a) 
 tb = len(lista_b) - 1
 i = 0
 j = 0
 la = ""
 lb = ""
 n = int()
 m = int()
    
 while i < ta:
    if j >= tb:
        j = 0
        pass

    la  = lista_a[i]
    lb  = lista_b[j]
    i  += 1
    j  += 1

    if la !=  " ":
        if lb != " ":
            m = la
            n = lb
           
            d =  (~(int(m))^(int(n)))+2
           
            key += str(d)
            pass

        pass

    else:
        key+= " "
        pass
 return key   
