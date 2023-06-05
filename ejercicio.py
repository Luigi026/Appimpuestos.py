#Ejercicio : Validar edad, en caso de +18 puede ingresar, caso contrario no podra ingresar mnk

import tkinter as tk                 #labelSaludo = tk.Label(ventana, font=("Times New Roman", 12, "bold"), text="Hola "+entryNombre.get()+", como estas ? ")
   # labelSaludo.grid(row=3, column=0, pady=5)
                                            
def verificarEdad():                                                                
    if(int(entryEdad.get()) >= 18 ):
        res = tk.Label(ventana, fg="green", font=("Times New Roman", 12, "bold"), text="Bienvenido, usted puede ingresar")
    else:
        (int(entryEdad.get()) < 18 )
        res = tk.Label(ventana, fg = "red", font=("Times New Roman", 12, "bold"), text="Ustede es menor, no puede ingresar")

    res.grid(row=2, column=1, pady=2)    

ventana = tk.Tk()
ventana.title("Admision para personas mayores a 18 años")
ventana.geometry("500x200")


labelTitulo = tk.Label(ventana, fg="black", font=("Times New Roman", 13, "bold"), text="Sistema de admision +18")
labelTitulo.grid(row=0, column=0)

labelEdad = tk.Label(ventana,  text="Sr. Usuario Ingrese su edad: ")
labelEdad.config(font=("Times New Roman", 13, "bold"))
labelEdad.grid(row=1, column=0)

entryEdad = tk.Entry(ventana)
entryEdad.config(fg="grey")
entryEdad.grid(row=1, column=1)

boton1 = tk.Button(ventana, activebackground="skyblue", bd=5, text="Ingresar", command=verificarEdad)
boton1.config(bg="skyblue", fg="black", font=("Times New Roman", 15, "bold"))
boton1.grid(row=2, column=0, pady=5)

ventana.mainloop()

