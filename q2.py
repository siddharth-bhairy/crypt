
import tkinter as tk
from tkinter import simpledialog

def decrypt():
    cipher=text1.get("1.0",tk.END).strip()

    if cipher=="":
        msg.config(text="Please enter cipher text")
        return

    key=simpledialog.askstring("Key","Enter key:")

    if key is None or key=="":
        msg.config(text="Please enter key")
        return

    if not key.isdigit():
        msg.config(text="Key must be a number")
        return

    key=int(key)
    plain=""

    for i in cipher:
        if i.isalpha():
            if i.isupper():
                res=chr((ord(i)-65-key)%26+65)
            else:
                res=chr((ord(i)-97-key)%26+97)
        else:
            res=i

        plain+=res

    text2.delete("1.0",tk.END)
    text2.insert(tk.END,plain)
    msg.config(text="")

root=tk.Tk()
root.title("Modified Caesar Cipher")
root.geometry("750x450")

box=tk.Frame(root,bd=2,relief="solid")
box.pack(padx=30,pady=30,fill="both",expand=True)

tk.Label(box,text="MODIFIED CAESAR CIPHER",
         font=("Arial",18)).pack(pady=20)

main=tk.Frame(box)
main.pack()

left=tk.Frame(main)
left.pack(side="left",padx=20)

tk.Label(left,text="Cipher Text").pack()
text1=tk.Text(left,width=30,height=10)
text1.pack(pady=10)

tk.Label(main,text="→",font=("Arial",30)).pack(side="left",padx=10)

right=tk.Frame(main)
right.pack(side="left",padx=20)

tk.Label(right,text="Plain Text").pack()
text2=tk.Text(right,width=30,height=10)
text2.pack(pady=10)

tk.Button(box,text="DECRYPT",command=decrypt).pack(pady=15)

msg=tk.Label(box,text="",fg="red")
msg.pack()

root.mainloop()
