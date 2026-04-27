from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox




class Application(ctk.CTk):

    def __init__(self):
        super().__init__()

        
        from main import Backend
        self.services = Backend()
        self.builder()



    def builder(self):

        self.initializer()



    def initializer(self):

        set_appearance_mode("light")
        self.centralizar_janela(900, 500)
        self.title("Auto-Converter by Tremura")
        self.button()



    def centralizar_janela(janela, largura=0, altura=0):
        
        janela.update_idletasks()
        
   
        largura_tela = janela.winfo_screenwidth()
        altura_tela = janela.winfo_screenheight()
        

        pos_x = int((largura_tela / 2) - (largura / 2))
        pos_y = int((altura_tela / 2) - (altura / 2))
        

        janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")


    def button(self):


        self.labels = CTkLabel(
            self,
            text="FORMATOS ACEITOS: .avif, .heic, .heif, .webp, .raw, .jpg, .jpeg",
            font= ("Segoe UI", 20, "bold"),
            text_color="black"
        )
        self.labels.place(relx = 0.05, rely= 0.2, relwidth = 0.9, relheight = 0.1)


        self.converter = CTkButton(
            self,
            corner_radius= 20,
            bg_color="transparent",
            fg_color="blue",
            text="CONVERTER",
            text_color="white",
            font= ("Segoe UI", 14, "bold"),
            hover_color="#00eeff",
            command= lambda: self.services.converter_e_limpar(self)
        )
        self.converter.place(relx = 0.36, rely= 0.45, relwidth = 0.3, relheight = 0.1)

        



        


if __name__ == "__main__":
    app = Application()
    app.mainloop()