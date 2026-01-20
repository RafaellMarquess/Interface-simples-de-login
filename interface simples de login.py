import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

janela = tk.Tk()
janela.title("Gestor Online")
janela.geometry("800x600")

#pega a foto
papel_de_parede = Image.open("logo.png")
#pega a variavel da foto e reajusta
papel_de_parede_ajustado = papel_de_parede.resize((800,600))
#pega a variavel da foto reajustada e guarda em uma outra para usar depois
papel_de_parede_foto = ImageTk.PhotoImage(papel_de_parede_ajustado)
#relheight e realwidth fazem a foto cobrir 100% da tela
label_bg = tk.Label(janela, image=papel_de_parede_foto).place(x=0,y=0,relheight=1,relwidth=1)

janela.grid_rowconfigure(0, weight=1)#centraliza os conteudos
janela.grid_columnconfigure(0, weight=1)

frame_login = tk.LabelFrame(janela, text="Dados de Acesso", padx=100, pady=15)
#sticky = n é o norte = acima
frame_login.grid(row=0, column=0, sticky="n")

frame_dashboard = tk.LabelFrame(janela, text="Painel de Controle", padx=20, pady=20)
frame_dashboard.grid(row=0, column=0, sticky="n", pady=50) # Mantém centralizado

def clique():
    usuario = caixa_texto.get()
    senha = caixa_senha.get()
    cargo = menu_cargo.get()
    aceitou = valor_check.get()
    caixa_texto.delete(0, tk.END)
    caixa_senha.delete(0, tk.END)

    if usuario == "" or senha == "" or cargo == "Selecione o cargo" or aceitou == 0:
        messagebox.showerror("Atenção", "Por favor, preencha todos os campos!")
    else:
        messagebox.showinfo("Sucesso", f"Login: {usuario}\nCargo: {cargo} \nRedirecionado...")
        abrir_dashboard(usuario) # <--- Aqui a mágica acontece

def sair():
    resposta = messagebox.askyesno("Sair", "Deseja realmente fechar o Gestor Online?")
    if resposta:
        janela.destroy()

def abrir_ajuda():
    # Cria uma nova janela independente
    janela_ajuda = tk.Toplevel(janela)
    janela_ajuda.title("Ajuda do Sistema")
    janela_ajuda.geometry("300x200")
    
    # Você pode colocar qualquer coisa nela, como se fosse a principal
    tk.Label(janela_ajuda, text="Para suporte, contate o admin.").pack(pady=20)
    tk.Button(janela_ajuda, text="Fechar", command=janela_ajuda.destroy).pack()

def abrir_dashboard(usuario_logado):
    # Destrói o frame de login com tudo o que tem dentro
    frame_login.destroy()
    
    #nao criou variavel porque voce só vai criar quando nao for mudar a cor tamanho etc, se for ficar estatico nao precisa criar    
    tk.Label(frame_dashboard, text=f"Bem-vindo, {usuario_logado}!", font=("Arial", 16, "bold")).grid(row=0, column=0)
    tk.Button(frame_dashboard, text="Logout / Sair", command=sair).grid(row=1, column=0, pady=20)


tk.Label(frame_login,text="Usuario").grid(row=0,column=0)
caixa_texto = tk.Entry(frame_login)
caixa_texto.grid(row=0, column=1)

tk.Label(frame_login, text="Senha").grid(row=1,column=0)
caixa_senha = tk.Entry(frame_login, show="*")
caixa_senha.grid(row=1,column=1)

opcoes = ["Administrador", "Vendedor", "Gerente", "Recepicionista"]
tk.Label(frame_login, text="Cargo").grid(row=2,column=0)
menu_cargo = ttk.Combobox(frame_login,values=opcoes)
menu_cargo.grid(row=2, column=1, padx=10,pady=10)

valor_check = tk.IntVar() 
check_termos = tk.Checkbutton(frame_login, text="Aceite os termos de uso", variable=valor_check)
check_termos.grid(row=3, column=1)

botao = tk.Button(frame_login, text="Login", bg="green", fg="white", command=clique, width=10)
botao.grid(row=4, column=0, pady=10)

botao_sair = tk.Button(frame_login, text="Sair", bg="red", fg="white", command=sair, width=10)
botao_sair.grid(row=4, column=1, pady=10)

janela.mainloop()

#input
#caixa_texto = tk.Entry(janela)
#css linha e coluna
#caixa_texto.grid(row=0, column=5)
#texto ao lado do input
#placeholder_texto =tk.Label(janela,text="Usuario")
#css linha e coluna
#placeholder_texto.grid(row=0, column=0)
#pega o valor
#caixa_texto.get()

#show é oque vai ser exibido                             
#caixa_senha = tk.Entry(janela, show="*")
#caixa_senha.grid(row=1, column=5)
#placeholder_senha = tk.Label(janela, text="Senha")
#placeholder_senha.grid(row=1, column=0)
#caixa_senha.get()

#botao = tk.Button(janela, text="Login", bg="green", fg="white", command=clique)
#botao.grid(row=1, column=7)
#botao_sair = tk.Button(janela, text="Sair", bg="red", fg="white", command=sair)
#botao_sair.grid(row=1, column=8, pady=20)

#placeholder_cargo = tk.Label(janela, text="cargo:")
#placeholder_cargo.grid(row=2,column=0)
#tk.Label(janela, text="Cargo:").grid(row=2, column=0)  da pra fazer desse jeito tbm

#pcoes = ["Administrador", "Vendedor", "Gerente", "Recepicionista"]
#combobox é a caixa de opções e o value recebe as informações
#menu_cargo = ttk.Combobox(janela, values=opcoes)
#set é só o some do placeholder ou para não ficar vazio
#menu_cargo.set("Selecione o cargo")
#menu_cargo.grid(row=2, column=5)

# Variável para guardar 0 = desmarcado e 1 = marcado
#valor_check = tk.IntVar() 
#variable é o sensor que detecta se for clicado no botao
#check_termos = tk.Checkbutton(janela, text="Aceite os termos de uso", variable=valor_check)
#check termos é só para fazer o css (grid)
#check_termos.grid(row=3, column=5)