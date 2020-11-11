
#import {lista.py}
palavra = input("texto plano: ")        #texto a ser criptografado

# string with encoding 'utf-8'
arr = bytes(palavra, 'utf-8')           #palavra -> bytes
arr2 = str(arr, 'utf-8')

print(arr,'\n')                         #imprimir resultado caso tenha dado certo


for byte in arr:                        #mostra os bytes
    print(byte, end='-')
print("\n")

for w in arr2:                       #mostra a frase 
    print(w, end=" - ")                


