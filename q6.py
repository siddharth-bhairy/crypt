
p=int(input("Enter prime number: "))
g=int(input("Enter primitive root: "))

a=int(input("Enter private key of A: "))
b=int(input("Enter private key of B: "))

A=(g**a)%p
B=(g**b)%p

key1=(B**a)%p
key2=(A**b)%p

print("Public key of A:",A)
print("Public key of B:",B)

print("Secret key of A:",key1)
print("Secret key of B:",key2)

if key1==key2:
    print("Key exchange successful")
else:
    print("Key exchange failed")

