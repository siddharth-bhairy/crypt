
plain=input("Enter plain text: ")
key=input("Enter keyword: ")

key=key.upper().replace("J","I")
plain=plain.upper().replace("J","I")

matrix=""
for i in key+ "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if i.isalpha() and i not in matrix:
        matrix+=i

print("Keyword Matrix:")

for i in range(0,25,5):
    print(matrix[i],matrix[i+1],matrix[i+2],matrix[i+3],matrix[i+4])

text=""
i=0

while i<len(plain):
    a=plain[i]

    if i+1<len(plain):
        b=plain[i+1]
    else:
        b="X"

    if a==b:
        text+=a+"X"
        i+=1
    else:
        text+=a+b
        i+=2

cipher=""

for i in range(0,len(text),2):
    a=text[i]
    b=text[i+1]

    p1=matrix.index(a)
    p2=matrix.index(b)

    r1=p1//5
    c1=p1%5
    r2=p2//5
    c2=p2%5

    if r1==r2:
        cipher+=matrix[r1*5+(c1+1)%5]
        cipher+=matrix[r2*5+(c2+1)%5]

    elif c1==c2:
        cipher+=matrix[((r1+1)%5)*5+c1]
        cipher+=matrix[((r2+1)%5)*5+c2]

    else:
        cipher+=matrix[r1*5+c2]
        cipher+=matrix[r2*5+c1]

print("Cipher Text:",cipher)

