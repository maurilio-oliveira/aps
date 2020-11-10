#import {lista.py}
string = "Hello World"

# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
arr2 = bytes(string, 'ascii')

print(arr,'\n')

# actual bytes in the the string
for byte in arr:
    print(byte, end=' ')
print("\n")
for byte in arr2:
    print(byte, end=' ') 
