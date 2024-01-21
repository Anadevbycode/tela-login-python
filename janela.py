#import tkinter
#janela = tkinter.Tk()

## print("fazer login")


#isso indica o tamanho da janela
#janela.geometry("500x300")
#texto =tkinter.Label(janela,text=" Seu login")
#texto.pack(padx=10,pady=10)

#botao = tkinter.Button(janela,text="login",command=clique)
#botao.pack(padx=10,pady=10)

#janela.mainloop() EXEMPLOS COM O TKINTER
#EXEMPLOS COM O CUSTOMTKINTER
import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()

def clique():
    print("Login realizado")
    

janela .geometry("500x300")

texto = customtkinter.CTkLabel(janela,text="Swift Logística")
texto .pack (padx=10,pady=10)

email = customtkinter.CTkEntry(janela,placeholder_text="Digite seu e-mail")
email.pack(padx=10,pady=10)
senha = customtkinter.CTkEntry(janela,placeholder_text="Digite Sua senha",show="*")
senha.pack(padx=10,pady=10)

checbox = customtkinter.CTkCheckBox(janela,text="Salvar seu login")
checbox.pack(padx=10, pady=10)
botao = customtkinter.CTkButton(janela,text="login",command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()