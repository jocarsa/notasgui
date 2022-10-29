import tkinter as tk                        # Importo la librería de GUI

raiz = tk.Tk()                              # Creo una interfaz gráfica de usuario
raiz.title("Notas v0.01")                   # Especifico el título de la ventana
raiz.geometry('200x200+20+50')              # Geomtria de la ventana y margen con la pantalla

try:                                        # Intento ejecutar
    from ctypes import windll               # Importo la libreria específica de GUI de Windows
    windll.shcore.SetProcessDpiAwareness(1) # Activo el antialias para texto etc dentro de las interfaces
except Exception as e:                      # Atrapo la excepción en caso de que se produzca
    print(e)                                # Saco la excepción por pantalla
finally:                                    # En todo caso:
    raiz.mainloop()                         # Detiene la ejecución y previene que la ventana se cierre      

