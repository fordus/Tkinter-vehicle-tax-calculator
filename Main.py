from time import sleep
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk

# TRISTAN VIDAL

class App():
    def __init__(self):
        self.r_root = tk.Tk()
        self.t_text = tk.StringVar()
        self.r_root.iconbitmap("icon.ico")
        self.r_root.title("Universidad")
        self.r_root.tk.call("source", "azure.tcl")
        self.r_root.tk.call("set_theme", "light")


        # TAMAÑO DE VENTANA
        width = 600
        height = 500
        screenwidth = self.r_root.winfo_screenwidth()
        screenheight = self.r_root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        self.r_root.geometry(alignstr)
        self.r_root.resizable(width=False, height=False)

        # LABEL SUPERIOR
        self.Label1 = tk.Label(self.r_root)
        Label1 = self.Label1
        Label1["font"] = tkFont.Font(family='Arial', size=10, weight='bold')
        Label1["text"] = "TRISTAN VIDAL"
        Label1["bg"] = "#e5e5e5"
        Label1.place(x=200, y=10)

        self.Label1 = tk.Label(self.r_root)
        Label1 = self.Label1
        Label1["font"] = tkFont.Font(family='Arial', size=10, weight='bold')
        Label1["text"] = "CALCULADORA IMPUESTOS"
        Label1["fg"] = "red"
        Label1["bg"] = "#e5e5e5"
        Label1.place(x=6, y=10)
        
        # FORMULARIO
        self.Label = tk.Label(self.r_root)
        Label = self.Label
        Label["text"] = "Ingrese un vehículo"
        Label["font"] = tkFont.Font(weight='bold', size=10)
        Label["fg"] = "black"
        Label.place(x=150, y=210, width=270, height=25)

        self.Button1 = ttk.Button(self.r_root)
        Button1 = self.Button1
        Button1["text"] = "Borrar BD"
        Button1.place(x=120, y=400, width=120, height=35)
        Button1["command"] = self.Boton1

        self.Button2 = ttk.Button(self.r_root)
        Button2 = self.Button2
        Button2["text"] = "Calcular"
        Button2.place(x=320, y=400, width=120, height=35)
        Button2["command"] = self.Boton2
        Button2["style"] = "Accent.TButton"

        self.Line = ttk.Entry(self.r_root)
        Line = self.Line
        Line.place(x=190, y=240, width=190, height=35)

        self.LabelLine1 = tk.Label(self.r_root)
        LabelLine1 = self.LabelLine1
        LabelLine1["text"] = "Placa:"
        LabelLine1.place(x=120, y=245)

        self.Line2 = ttk.Entry(self.r_root)
        Line2 = self.Line2
        Line2.place(x=190, y=280, width=190, height=35)

        self.LabelLine2 = tk.Label(self.r_root)
        LabelLine2 = self.LabelLine2
        LabelLine2["text"] = "Año modelo:"
        LabelLine2.place(x=90, y=285)

        self.Line3 = ttk.Entry(self.r_root)
        Line3 = self.Line3
        Line3.place(x=190, y=320, width=190, height=35)

        self.LabelLine3 = tk.Label(self.r_root)
        LabelLine3 = self.LabelLine3
        LabelLine3["text"] = "Tipo:"
        LabelLine3.place(x=113, y=325)
        
        self.Line4 = ttk.Entry(self.r_root)
        Line4 = self.Line4
        Line4.place(x=190, y=360, width=190, height=35)

        self.LabelLine4 = tk.Label(self.r_root)
        LabelLine4 = self.LabelLine4
        LabelLine4["text"] = "Valor:"
        LabelLine4.place(x=113, y=365)


        # DETALLES COLUMNAS
        self.paned = ttk.PanedWindow(self.r_root)
        self.paned.grid(row=0, column=2, pady=40,
                        padx=70, sticky="nsew", rowspan=3)
        self.pane_1 = ttk.Frame(self.paned, padding=10)
        self.paned.add(self.pane_1, weight=1)
        self.scrollbar = ttk.Scrollbar(self.pane_1)
        self.scrollbar.pack(side="right", fill="y")

        # COLUMNAS(Treeview)
        self.treeview = ttk.Treeview(
            self.pane_1,
            selectmode="browse",
            yscrollcommand=self.scrollbar.set,
            columns=(1, 2),
            height=4,
        )
        self.treeview.pack(expand=True, fill="both")

        self.treeview.column("#0", anchor="center", width=120)
        self.treeview.column(1, anchor="center", width=120)
        self.treeview.column(2, anchor="center", width=120)

        # TÍTULO COLUMNAS
        self.treeview.heading("#0", text="Placa", anchor="center")
        self.treeview.heading(1, text="Modelo", anchor="center")
        self.treeview.heading(2, text="Impuesto", anchor="center")

        # DATOS DE EJEMPLO PARA COLUMNAS
        treeview_data = [
            ("DSGFER", ("2000", "40000")),
        ]

        # INSERTAR LOS DATOS DE EJEMPLO EN LAS COLUMNAS
        for item in treeview_data:
            self.treeview.insert("", tk.END, text=item[0], values=item[1])

        self.r_root.mainloop()

    def Boton1(self):
        self.Label["text"] = "Datos borrados"
        self.Label["fg"] = "black"
        self.treeview.delete(*self.treeview.get_children())

    def Boton2(self):
        placa = self.Line.get()
        modelo = self.Line2.get()
        tipo = self.Line3.get()
        valor = self.Line4.get()
        
        if placa == '':
            placa = 'Ninguna'
        if modelo == '':
            modelo = 0
        if tipo == '':
            tipo = 0
        if valor == '':
            valor = 0
        
        modelo =int(modelo)
        tipo =int(tipo)
        valor =int(valor)
        
        
        tipos = (1,2,3)
        tipos_impuesto1 = (1,2)
        impuesto = 0   
        correcto1 = False if len(placa) > 6 else True
        correcto2 = False if modelo < 2000 or modelo > 2022 else True
        correcto3 = False if tipo not in tipos else True
        
        if correcto1 and correcto2 and correcto3:
            impuesto = self.Calcular_impuesto(modelo, tipo, tipos_impuesto1, valor)
            
        if impuesto != 0:
            self.Impuesto_0(placa,modelo,impuesto)
        else:
            self.Comprobar_errores(correcto3,correcto2, correcto1)
        #Comprobar que no esté vacío
        # self.Label["text"] = input1 if input1 else "Campo requerido"

    def Impuesto_0(self, placa, modelo, impuesto):
        self.treeview.insert("", tk.END, text=placa, values=(modelo, impuesto))
        self.Label["text"] = "Datos insertados"
        self.Label["fg"] = "green"
        # Limpiar los entry
        self.Line.delete(0, tk.END)
        self.Line2.delete(0, tk.END)
        self.Line3.delete(0, tk.END)
        self.Line4.delete(0, tk.END)
        
    def Comprobar_errores(self, correcto3,correcto2, correcto1):
        if correcto3 == False:
            self.Label["text"] = "Tipo inválido"
            self.Label["fg"] = "red"
        if correcto2 == False:
            self.Label["text"] = "Modelo inválido"
            self.Label["fg"] = "red"
        if correcto1 == False:
            self.Label["text"] = "Tamaño de placa inválido"
            self.Label["fg"] = "red"
            
    def Calcular_impuesto(self, modelo, tipo, tipos_impuesto1, valor):
        
        # Si 
        # modelo <= 2010 
        # tipo 1,2 
        # 10% valor

        # Si 
        # modelo <= 2010 
        # tipo 3 
        # 15% valor

        # Si 
        # modelo > 2010 
        # tipo 1,2 
        # 20% valor

        # Si 
        # modelo > 2010 
        # tipo 3 
        # 55% valor
        
        if modelo <= 2010 and tipo in tipos_impuesto1:
            impuesto = valor * 0.1 
        
        if modelo <= 2010 and tipo == 3:
            impuesto = valor * 0.15
        
        if modelo > 2010 and tipo in tipos_impuesto1:
            impuesto = valor * 0.2
        
        if modelo > 2010 and tipo == 3:
            impuesto = valor * 0.55
        return impuesto

if __name__ == "__main__":
    app = App()
