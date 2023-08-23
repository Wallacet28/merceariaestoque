import tkinter as tk


def translate():
    word = entry.get()
    if word == 'olá':
        label.config(text='hello')
    else:
        label.config(text='Desconhecido')


root = tk.Tk()
root.title("Tradutor de Libras")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Traduzir", command=translate)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
