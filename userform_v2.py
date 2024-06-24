import tkinter as tk
from tkinter import messagebox

def register():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # Aqui você pode adicionar lógica para processar os dados do formulário, como salvar em um banco de dados ou exibir em uma mensagem

def main():
    root = tk.Tk()
    root.geometry("300x250")
    root.title("registration form")
    root.configure(background="blue")

    form_frame = tk.Frame(root, padx=20, pady=20)
    form_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

    username_label = tk.Label(form_frame, text="username: ")
    username_label.grid(row=0, column=0, sticky=tk.W)
    global username_entry
    username_entry= tk.Entry(form_frame)
    username_entry.grid(row=0, column=1, padx=10,pady=5)

    email_label = tk.Label(form_frame, text="email: ")
    email_label.grid(row=1, column=0, sticky=tk.W)
    global email_entry
    email_entry= tk.Entry(form_frame)
    email_entry.grid(row=1, column=1, padx=10,pady=5)

    password_label = tk.Label(form_frame, text="password: ")
    password_label.grid(row=2, column=0, sticky=tk.W)
    global password_entry
    password_entry= tk.Entry(form_frame, show="*")
    password_entry.grid(row=2, column=1, padx=10,pady=5)

    register_button = tk.Button(form_frame, text="Register", command=register)
    register_button.grid(row=3, column=1, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
