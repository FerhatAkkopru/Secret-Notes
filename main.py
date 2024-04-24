import tkinter
from tkinter import messagebox
from cryptography.fernet import Fernet

# window
ui_window = tkinter.Tk()
ui_window.title("secret notes")
ui_window.config(pady=10)
ui_window.minsize(width=400, height=600)

# Font
FONT = ("Comic Sans MS", 12, "normal")

# encrypted code file, created first time because after that it can be a problem
# Secret_file = open("secret_code.txt", "x")

# encrypt and decrypt messages
enc_message = ""
dec_message = ""

# key
key = Fernet.generate_key()
fernet = Fernet(key)
master = ""


# encryption method
def encrypt():
    global master
    title = title_entry.get()
    message = enter_text.get(1.0, "end-1c")
    master = master_entry.get()
    if title == "" or message == "" or master == "":
        messagebox.showerror(title="Error!", message="Please enter all information.")
    else:
        global enc_message
        enc_message = fernet.encrypt(message.encode())
        print(enc_message)
        with open("secret_code.txt", mode="a") as appended_code:
            appended_code.write(f"Title: {title}\n")
            appended_code.write(f"Encrypted message: {str(enc_message)}\n")
        enter_text.delete(1.0, "end-1c")
        title_entry.delete(0, "end")
        master_entry.delete(0, "end")


# decryption method

def decrypt():
    master1 = master_entry.get()
    message = enter_text.get(1.0, "end-1c")
    if message == "" or master1 == "":
        messagebox.showerror(title="Error!", message="Please enter all information.")
    else:
        # controlling the master key
        if master1 == master:
            global dec_message
            dec_message = fernet.decrypt(enc_message).decode()
            enter_text.delete(1.0, "end-1c")
            enter_text.insert("1.0", dec_message)
            master_entry.delete(0, "end")
        else:
            messagebox.showinfo(title="Wrong master code", message="Master code is not correct")


# logo image
photo = tkinter.PhotoImage(file="img.png")
photo_label = tkinter.Label(image=photo)
# photo_label.config(width=100, height=100)
photo_label.pack()

# title label
title_label = tkinter.Label(text="Enter your title", font=FONT)
title_label.pack()

# title entry
title_entry = tkinter.Entry()
title_entry.config(width=30)
title_entry.pack(pady=10)

# enter label
enter_label = tkinter.Label(text="Enter your label", font=FONT)
enter_label.pack()

# enter text
enter_text = tkinter.Text()
enter_text.config(width=30, height=15)
enter_text.pack(pady=5)

# master key label
master_label = tkinter.Label(text="Enter your master key", font=FONT)
master_label.pack()

# master key entry
master_entry = tkinter.Entry()
master_entry.config(width=30)
master_entry.pack(pady=5)

# save and encrypt button
s_and_e = tkinter.Button(text="Save & Encrypt", command=encrypt, font=FONT)
s_and_e.pack(pady=5)

# decrypt button
decrypt_button = tkinter.Button(text="decrypt", command=decrypt, font=FONT)
decrypt_button.pack()

ui_window.mainloop()
