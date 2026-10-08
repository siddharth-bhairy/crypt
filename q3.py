def ceasar_ciph(data):
    ct=""
    for i in data:
        if i.isalpha() and i.islower():
            ct+=chr((ord(i)+3-ord('a'))%26+ord('a'))
        elif i.isalpha() and i.isupper():
                ct+=chr((ord(i)+3-ord('A'))%26+ord('A'))
        elif i.isdigit():
                ct+=chr((ord(i)+3-ord('1'))%10+ord('1'))
        else:
            ct=ct+i
    return ct

ipf="xyz.txt"
opf="out.txt"
try:
    with open(ipf,'r') as in_file:
        data=in_file.read()
        ct=ceasar_ciph(data)
    with open(opf,'w') as out:
        out.write(ct)
except FileNotFoundError:
    with open(ipf,'w') as in_file:
         pt=input("enter text for encryption : ")
         in_file.write(pt)
    try:
        with open(opf,'x') as out:
            
            out.write(ceasar_ciph(pt))
    except FileNotFoundError:
         choice=input('press 0 for overwriting : ')
         