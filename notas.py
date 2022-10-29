import tkinter as tk                        # Importo la librería de GUI
from tkinter import ttk                     # Importo la nueva librería TTK

# DECLARO FUNCIONES PARA EL PROGRAMA

def iniciaSesion():                         # Función de inicio de sesión
    print("Vamos a iniciar sesión")         # Imprime un mensaje en pantalla

# CREACIÓN DE LA VENTANA PRINCIPAL Y ESTILO DE LA VENTANA #

raiz = tk.Tk()                              # Creo una interfaz gráfica de usuario
raiz.title("Notas v0.01")                   # Especifico el título de la ventana
raiz.geometry('200x200+20+50')              # Geomtria de la ventana y margen con la pantalla
raiz.attributes("-topmost",True)            # Siempre encima del resto de las ventanas
raiz.attributes("-alpha",0.9)               # Añado  un efecto de transparencia
raiz.resizable(0,0)                         # Impido que el usuario pueda redimensionar la ventana
estilo = ttk.Style()                        # Añado soporte para estilos
estilo.theme_use('default')                 # Selecciono el estilo clásico de aplicaciones

# AÑADIMOS WIDGETS A LA VENTANA

version = tk.Label(raiz,text="Notas v0.01") # Creamos un label
version.pack()                              # Lo añadimos a la ventana

inputusuario = ttk.Entry(raiz)              # Creo una entrada para que el usuario diga quien es
inputusuario.insert(0,'Introduce tu usuario')# Creo  un texto de inicio en la entrada 
inputusuario.pack(pady=10)                  # Empaqueto la entrada

inputcontrasena = ttk.Entry(raiz)           # Creo una entrada para que el usuario diga quien es
inputcontrasena.insert(0,'Introduce tu contraseña')   # Creo  un texto de inicio en la entrada 
inputcontrasena.pack(pady=10)               # Empaqueto la entrada

inputemail = ttk.Entry(raiz)                # Creo una entrada para que el usuario diga quien es
inputemail.insert(0,'Introduce tu email')   # Creo  un texto de inicio en la entrada 
inputemail.pack(pady=10)                    # Empaqueto la entrada

botonlogin = ttk.Button(raiz,text="Enviar",command=iniciaSesion) # Creo el boton de iniciar sesion
botonlogin.pack(pady=10,expand=True)        # Lo empaqueto

# INTENTO INTRODUCIR ANTIALIAS EN WINDOWS Y LANZO EL BUCLE

try:                                        # Intento ejecutar
    from ctypes import windll               # Importo la libreria específica de GUI de Windows
    windll.shcore.SetProcessDpiAwareness(1) # Activo el antialias para texto etc dentro de las interfaces
except Exception as e:                      # Atrapo la excepción en caso de que se produzca
    print(e)                                # Saco la excepción por pantalla
finally:                                    # En todo caso:
    raiz.mainloop()                         # Detiene la ejecución y previene que la ventana se cierre      

