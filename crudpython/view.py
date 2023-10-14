from tkinter import *
from tkinter import scrolledtext, messagebox, ttk
import banco

class App:
    def __init__(self, master):
        self.master = master
        master.title("Formulário de Consultoria")
        master.geometry("800x600")

        # Entry widgets for inputs
        Label(master, text="Nome *").grid(row=1, column=0, padx=20, pady=10, sticky=W)
        self.nome_entry = Entry(master)
        self.nome_entry.grid(row=1, column=1)

        Label(master, text="Email *").grid(row=2, column=0, padx=20, pady=10, sticky=W)
        self.email_entry = Entry(master)
        self.email_entry.grid(row=2, column=1)

        Label(master, text="Telefone *").grid(row=3, column=0, padx=20, pady=10, sticky=W)
        self.telefone_entry = Entry(master)
        self.telefone_entry.grid(row=3, column=1)

        # Adicionando campos para data, estado e consulta
        Label(master, text="Data da consulta *").grid(row=4, column=0, padx=20, pady=10, sticky=W)
        self.data_entry = Entry(master)
        self.data_entry.grid(row=4, column=1)

        Label(master, text="Estado da consulta *").grid(row=5, column=0, padx=20, pady=10, sticky=W)
        self.estado_entry = Entry(master)
        self.estado_entry.grid(row=5, column=1)

        Label(master, text="Informação extra").grid(row=6, column=0, padx=20, pady=10, sticky=NW)
        self.info_extra = scrolledtext.ScrolledText(master, width=40, height=5)
        self.info_extra.grid(row=6, column=1, pady=10)

        # Adding CRUD operation buttons
        Button(master, text="Inserir", command=self.add_data).grid(row=7, column=0, padx=20, pady=10, sticky=W)
        Button(master, text="Atualizar").grid(row=7, column=1, padx=20, pady=10, sticky=W)  # Placeholder for now
        Button(master, text="Deletar").grid(row=7, column=1, padx=100, pady=10, sticky=W)   # Placeholder for now

        # Treeview for data display
        self.tree = ttk.Treeview(master, columns=('ID', 'Nome', 'Email', 'Telefone', 'Data', 'Estado', 'Sobre'), show='headings')
        self.tree.heading('ID', text='Id')
        self.tree.heading('Nome', text='Nome')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Telefone', text='Telefone')
        self.tree.heading('Data', text='Data')
        self.tree.heading('Estado', text='Estado')
        self.tree.heading('Sobre', text='Sobre')
       # Ajuste a largura das colunas

        self.tree.column('ID', width=30)
        self.tree.column('Nome', width=100)
        self.tree.column('Email', width=150)
        self.tree.column('Telefone', width=100)
        self.tree.column('Data', width=100)
        self.tree.column('Estado', width=80)
        self.tree.column('Sobre', width=200)
        self.tree.grid(row=1, column=2, rowspan=6, padx=30, pady=10)

        
    def add_data(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        telefone = self.telefone_entry.get()
        data = self.data_entry.get()
        estado = self.estado_entry.get()
        info_extra = self.info_extra.get(1.0, END).strip()

        banco.insert_data(nome, email, telefone, data, estado, info_extra)
        messagebox.showinfo("Info", "Dados adicionados com sucesso!")
        self.update_treeview()  # Atualizar Treeview após inserção

    def display_data_in_treeview(self):
        data = banco.fetch_all_data()
        for row in data:
            self.tree.insert('', END, values=row)

    def update_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        data = banco.fetch_all_data()  # Usando read_data para buscar os dados
        for item in data:
            self.tree.insert("", "end", values=(item[1], item[2], item[3], item[4], item[5], item[6]))

    def insert_data_button(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        telefone = self.telefone_entry.get()
        data = self.data_entry.get()
        estado = self.estado_entry.get()
        consulta = self.consulta_entry.get()

        banco.insert_data(nome, email, telefone, data, estado, consulta)
        self.update_treeview()  # Atualize a Treeview aqui

def update_treeview(self):
    for row in self.tree.get_children():
        self.tree.delete(row)

    data = banco.fetch_all_data()  # Use fetch_all_data to get the data
    for item in data:
        self.tree.insert("", "end", values=(item[1], item[2], item[3], item[4], item[5], item[6]))
root = Tk()
app = App(root)
root.mainloop()
