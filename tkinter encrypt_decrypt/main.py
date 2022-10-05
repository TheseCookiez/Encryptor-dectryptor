from tkinter import *
from cryptography.fernet import Fernet
from pathlib import Path
from tkinter import filedialog

# Defining the basic GUI
root = Tk()
root.title("The Tkinter Encrypter/Decrypter!")
root.geometry("1000x700")
root.configure(background="#1c1d29")
bg_img = PhotoImage(file="bebe.png")
bg = Label(root, image=bg_img)
bg.place(relx=.5, rely=.5, anchor="center")

# See if a key exists already, if not create a new key
try:
    with open("encryptionkey.key", "rb") as key:
        currentkey = key.read()
except FileNotFoundError:
    newkey = Fernet.generate_key()
    with open("encryptionkey.key", "wb") as key:
        key.write(newkey)
        print("No key was found, created a new one!")
        with open("encryptionkey.key", "rb") as createdkey:
            currentkey = createdkey.read()
        pass


def save_userenter_key():
    userkey = Enter_new_key.get()
    bytekey = userkey.encode()
    with open("encryptionkey.key", "wb") as keyfile:
        keyfile.write(bytekey)
        keyfile.close()
        getcurrentkey()
        Enter_new_key.delete(0, END)


# Display the current key
def getcurrentkey():
    with open("encryptionkey.key", "r") as thiskey:
        thecurrentkey = thiskey.read()
        thiskey.close()
        Displaykey = Label(root, text="The Current Key is:  " + thecurrentkey, fg="gray", bd="0", bg="#1c1d29",
                           width=70)
        Displaykey.place(relx=.5, rely=.5, anchor="center")
        print(thecurrentkey)


# Generate a new encryptionkey
def generatekey():
    genkey = Fernet.generate_key()
    with open("encryptionkey.key", "wb") as keyfile:
        keyfile.write(genkey)
        keyfile.close()
        getcurrentkey()


# Function to open a file to encrypt/decrypt
def openfile():
    selectfile = filedialog.askopenfilename(initialdir="\\", title="Select a file")
    with open(selectfile, "rb") as selectfile:
        selectedfile = selectfile.read()
        return selectedfile


# Encryption function on selected file
def encrypt():
    original = openfile()
    with open("encryptionkey.key", "rb") as key_for_encrypt:
        e_key = key_for_encrypt.read()
        fernet_e = Fernet(e_key)
        encrypted_file = fernet_e.encrypt(original)
        with open("Encrypted_File", "wb") as encrypted_message:
            encrypted_message.write(encrypted_file)
            encrypted_message.close()


# Decryption function on selected file
def decrypt():
    encrypted = openfile()
    with open("encryptionkey.key", "rb") as key_for_decrypt:
        d_key = key_for_decrypt.read()
        fernet_d = Fernet(d_key)
        decrypted = fernet_d.decrypt(encrypted)
        with open("Decrypted_File", "wb") as decrypted_file:
            decrypted_file.write(decrypted)
            decrypted_file.close()


# Display the current key when the program starts
getcurrentkey()

# Define the buttons
Generate_new_key = Button(root, text="Generate new Key", padx=30, pady=10, command=generatekey)
Encrypt_button = Button(root, text="Encrypt", padx=30, pady=10, command=encrypt)
Decrypt_button = Button(root, text="Decrypt", padx=30, pady=10, command=decrypt)
Enter_new_key = Entry(root, width=50)
Insert_new_key = Label(root, text="Enter a new key:", fg="gray", bd="0", bg="#1c1d29", width=70)
save_user_key = Button(root, text="Save key", command=save_userenter_key)
# Place buttons
Generate_new_key.grid(row=1, column=0)
Encrypt_button.grid(row=1, column=1)
Decrypt_button.grid(row=1, column=2)
Enter_new_key.place(relx=.5, rely=.15, anchor="center")
Insert_new_key.place(relx=.5, rely=.12, anchor="center")
save_user_key.place(relx=.5, rely=.20, anchor="center")
root.mainloop()
