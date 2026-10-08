pt="hello world"
ct0=""
ct1=""
for i in pt:
    ct0=ct0+chr(ord(i)^0)
    ct1=ct1+chr(ord(i)^1)

print("xor with 0 : ",ct0)
print("xor with 1 : ",ct1)