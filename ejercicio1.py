   # Ejercicio 1 : Cobro de ganancias en sueldos mayores a 400mill con 9%
import tkinter as tk
# Evaluo el entrySueldo : En caso de que el sueldo sea mayor o igual a 400mil calculo su 9 % de 400mil
# y restarlo y mostrar el mensaje correspondiente segun la condicional

def funcionCalcular():
    if(float(entrySueldo.get()) < 400000):
        texto = tk.Label(ventana, fg="blue", font=("Times New Roman", 13, "bold"), text="Usted no debe pagar impuestos (★‿★)")
    else:
        neto = float(entrySueldo.get()) - float(entrySueldo.get()) * 0.09     # A 400 mil le restamos el 9%
        texto = tk.Label(ventana, fg="green", font=("Times New Roman", 12, "bold"), text="Su sueldo neto es de " + str(neto) + " $ pesos")
        
    texto.grid(row=1, column=1, pady=5)

ventana = tk.Tk()
ventana.title("Calculo   de   ganancias ")
ventana.geometry("500x200")

labelSueldo = tk.Label(ventana, font=("Times New Roman", 13, "bold"), text="Ingrese sueldo: ")    #creo el obejto LABEL
labelSueldo.grid(row=0, column=0)

entrySueldo = tk.Entry(ventana)     #creamos el objeto ENTRY
#entrySueldo.config(fg="grey")
entrySueldo.grid(row=0, column=1)

boton = tk.Button(ventana, bg="skyblue", font=("Times New Roman", 15, "bold"), bd=5, activebackground="skyblue", text="Calcular", command=funcionCalcular)    #Creo el objeto BUTTON
boton.grid(row=1, column=0)

ventana.mainloop()  # La ventana se mantiene en vista sin cerrarse
