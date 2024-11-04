import tkinter as tk
from tkinter import filedialog, messagebox

# Função para salvar o conteúdo do texto no arquivo
def salvar_arquivo():
    # Abre a janela para escolher o local e o nome do arquivo
    arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if arquivo:  # Se um arquivo foi selecionado
        with open(arquivo, "w", encoding="utf-8") as f:  # Abre o arquivo em modo de escrita
            f.write(caixa_texto.get(1.0, tk.END))  # Salva o conteúdo da caixa de texto no arquivo
        messagebox.showinfo("Salvar", "Arquivo salvo com sucesso!")  # Mostra uma mensagem de sucesso

# Função para abrir um arquivo e carregar o conteúdo na caixa de texto
def abrir_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if arquivo:  # Se um arquivo foi selecionado
        with open(arquivo, "r", encoding="utf-8") as f:  # Abre o arquivo em modo de leitura
            conteudo = f.read()  # Lê o conteúdo do arquivo
            caixa_texto.delete(1.0, tk.END)  # Limpa o conteúdo atual da caixa de texto
            caixa_texto.insert(tk.END, conteudo)  # Insere o conteúdo do arquivo na caixa de texto

# Função para limpar o conteúdo da caixa de texto
def limpar_texto():
    caixa_texto.delete(1.0, tk.END)  # Remove o conteúdo do início (1.0) até o final (tk.END)

# Função para exibir informações sobre o editor
def sobre():
    messagebox.showinfo("Sobre", "Editor de Texto em Python\nDesenvolvido com Tkinter")  # Mostra informações sobre o programa

# Função para sair do programa
def sair():
    resposta = messagebox.askyesno("Sair", "Tem a certeza que quer sair?")  # Pergunta ao usuário se deseja sair
    if resposta:
        janela.quit()  # Fecha a janela principal

# Configuração da janela principal
janela = tk.Tk()
janela.title("Editor de Texto")  # Título da janela
janela.geometry("600x400")  # Define o tamanho da janela
janela.resizable(True, True)  # Permite redimensionar a janela

# Menu principal
menu_principal = tk.Menu(janela)
janela.config(menu=menu_principal)

# Menu de Arquivo com opções Abrir, Salvar e Sair
menu_arquivo = tk.Menu(menu_principal, tearoff=0)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo, accelerator="Ctrl+O")
menu_arquivo.add_command(label="Salvar", command=salvar_arquivo, accelerator="Ctrl+S")
menu_arquivo.add_separator()  # Adiciona uma linha de separação
menu_arquivo.add_command(label="Sair", command=sair, accelerator="Ctrl+Q")
menu_principal.add_cascade(label="Arquivo", menu=menu_arquivo)

# Menu de Ajuda com opção Sobre
menu_ajuda = tk.Menu(menu_principal, tearoff=0)
menu_ajuda.add_command(label="Sobre", command=sobre)
menu_principal.add_cascade(label="Ajuda", menu=menu_ajuda)

# Barra de ferramentas com botões para abrir, salvar e limpar texto
frame_botoes = tk.Frame(janela)
frame_botoes.pack(fill="x")

btn_abrir = tk.Button(frame_botoes, text="Abrir", command=abrir_arquivo)
btn_abrir.pack(side="left", padx=5, pady=5)

btn_salvar = tk.Button(frame_botoes, text="Salvar", command=salvar_arquivo)
btn_salvar.pack(side="left", padx=5, pady=5)

btn_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar_texto)
btn_limpar.pack(side="left", padx=5, pady=5)

# Caixa de texto onde o usuário digita o conteúdo
caixa_texto = tk.Text(janela, wrap="word", undo=True)  # "wrap='word'" quebra as linhas entre palavras
caixa_texto.pack(expand=1, fill="both")  # Expande a caixa de texto para preencher a janela

# Adiciona atalhos de teclado para abrir, salvar e sair
janela.bind("<Control-o>", lambda event: abrir_arquivo())  # Ctrl+O para abrir
janela.bind("<Control-s>", lambda event: salvar_arquivo())  # Ctrl+S para salvar
janela.bind("<Control-q>", lambda event: sair())  # Ctrl+Q para sair

# Inicia o loop principal da aplicação
janela.mainloop()
