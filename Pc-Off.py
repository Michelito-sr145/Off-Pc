import tkinter as tk
from tkinter import messagebox, colorchooser
import json
import os
import sys

def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

CONFIG_FILE = resource_path("config.json")

class OffPcApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OffPc - Apagado Automático")
        self.root.iconbitmap(resource_path("icono-OffPc.ico"))
        self.root.geometry("380x200")
        self.root.resizable(False, False)
        self.centrar_ventana()
        self.config = self.cargar_configuracion()  # Carga dict de configuración
        self.color_normal = self.config["color_normal"]  # Fondo normal
        self.color_critico = self.config["color_critico"]  # Fondo en tiempo crítico
        self.color_pocotime = self.config["color_pocotime"]  # Texto en tiempo crítico
        self.tiempo_critico = self.config["tiempo_critico"]  # Tiempo considerado crítico
        self.root.configure(bg=self.color_normal)  # Aplicar color de fondo
        self.tiempo_restante = 0  # Inicializa el contador
        self.en_ejecucion = False  # Bandera de si está contando

        # --- Pantalla principal ---
        self.ventana_entrada = tk.Frame(root, bg=self.color_normal)
        self.vista_principal()  # Crea la pantalla principal

        # --- Pantalla ajustes ---
        self.ventana_ajuste = tk.Frame(root, bg=self.color_normal)
        self.vista_ajustes()  # Crea pantalla de ajustes

    def CargarConfiguracion(self):
        self.config = self.cargar_configuracion()  # Carga dict de configuración
        self.color_normal = self.config["color_normal"]  # Fondo normal
        self.color_critico = self.config["color_critico"]  # Fondo en tiempo crítico
        self.color_pocotime = self.config["color_pocotime"]  # Texto en tiempo crítico
        self.tiempo_critico = self.config["tiempo_critico"]  # Tiempo considerado crítico

    def vista_principal(self):
        self.CargarConfiguracion()
        self.entrada_horas = tk.Entry(self.ventana_entrada, width=3, font=("Arial", 36), justify='center')  # Entrada horas
        self.entrada_minutos = tk.Entry(self.ventana_entrada, width=3, font=("Arial", 36), justify='center')  # Entrada minutos
        self.entrada_segundos = tk.Entry(self.ventana_entrada, width=3, font=("Arial", 36), justify='center')  # Entrada segundos
        self.label_horas = tk.Label(self.ventana_entrada, text="h", font=("Arial", 32), bg=self.color_normal)
        self.label_minutos = tk.Label(self.ventana_entrada, text="m", font=("Arial", 32), bg=self.color_normal)
        self.label_segundos = tk.Label(self.ventana_entrada, text="s", font=("Arial", 32), bg=self.color_normal)

        self.entrada_horas.insert(0, "0")  # Valor por defecto horas
        self.entrada_minutos.insert(0, "0")  # Valor por defecto minutos
        self.entrada_segundos.insert(0, "0")  # Valor por defecto segundos

        #Posicionamos los label y cuadros
        self.ventana_entrada.pack(pady=10)  # Muestra frame
        self.entrada_horas.pack(side=tk.LEFT, padx=5)  # Cuadtro de entrada
        self.label_horas.pack(side=tk.LEFT)  # Etiqueta h
        self.entrada_minutos.pack(side=tk.LEFT, padx=5)  # Cuadtro de entrada
        self.label_minutos.pack(side=tk.LEFT)  # Etiqueta m
        self.entrada_segundos.pack(side=tk.LEFT, padx=5)  # Cuadtro de entrada
        self.label_segundos.pack(side=tk.LEFT)  # Etiqueta s

        # Navegación al presionar Enter
        self.entrada_horas.bind("<Return>", lambda e: self.validar_y_mover(self.entrada_horas, self.entrada_minutos))
        self.entrada_minutos.bind("<Return>", lambda e: self.validar_y_mover(self.entrada_minutos, self.entrada_segundos, 59))
        self.entrada_segundos.bind("<Return>", lambda e: self.validar_y_mover(self.entrada_segundos, self.boton_inicio, 59))

        self.label = tk.Label(self.root, text="00:00:00", font=("Arial", 70), fg=self.color_critico, bg=self.color_normal)  # Etiqueta contador
        self.adios_label = tk.Label(self.root, text="Apagando...", font=("Arial", 53), fg=self.color_pocotime, bg=self.color_critico)  # Mensaje final

        self.boton_inicio = tk.Button(self.root, text="Iniciar", font=("Arial", 20), command=self.toggle_cronometro)  # Botón iniciar/pausar
        self.boton_inicio.pack(pady=5)

        self.boton_ajustes = tk.Button(self.root, text="Ajustes", font=("Arial", 12), command=self.mostrar_ajustes)  # Botón para abrir ajustes
        self.boton_ajustes.pack()

    def vista_ajustes(self):
        self.CargarConfiguracion()
        # Entrada de tiempo crítico
        self.label_tiempo = tk.Label(self.ventana_ajuste, text="Tiempo Aviso (seg):", bg=self.color_normal, font=("Arial", 15))
        self.label_tiempo.grid(row=0, column=0, padx=10, pady=(10, 5), sticky='w')
        self.entry_tiempo_critico = tk.Entry(self.ventana_ajuste, width=10, font=("Arial", 12))
        self.entry_tiempo_critico.insert(0, str(self.tiempo_critico))
        self.entry_tiempo_critico.grid(row=0, column=1, padx=10, pady=(10, 5), sticky='e')

        # Botones de selección de color
        self.boton_color_normal = tk.Button(self.ventana_ajuste, text="Color del Fondo IIIIIIIII", font=("Arial", 11), fg=self.color_normal, command=self.cambiar_color_normal)
        self.boton_color_normal.grid(row=1, column=0, columnspan=2, pady=5, padx=10, sticky='we')

        self.boton_color_critico = tk.Button(self.ventana_ajuste, text="Color del Contador IIIIIIIII", font=("Arial", 11), fg=self.color_critico , command=self.cambiar_color_critico)
        self.boton_color_critico.grid(row=2, column=0, columnspan=2, pady=5, padx=10, sticky='we')

        self.boton_color_pocotime = tk.Button(self.ventana_ajuste, text="Color del Texto Final IIIIIIIII", font=("Arial", 11), fg=self.color_pocotime , command=self.cambiar_color_pocotime)
        self.boton_color_pocotime.grid(row=3, column=0, columnspan=2, pady=5, padx=10, sticky='we')

        # Guardar ajustes
        self.boton_guardar = tk.Button(self.ventana_ajuste, text="Guardar ajustes", font=("Arial", 12), command=self.guardar_ajustes)
        self.boton_guardar.grid(row=4, column=0, columnspan=2, pady=(10, 5), padx=10, sticky='we')

        # Expansión de columnas
        self.ventana_ajuste.grid_columnconfigure(0, weight=1)
        self.ventana_ajuste.grid_columnconfigure(1, weight=1)

    def mostrar_ajustes(self):
        self.CargarConfiguracion()
        # Ocultar elementos principales
        self.ventana_entrada.pack_forget()
        self.label.pack_forget()
        self.boton_inicio.pack_forget()
        self.boton_ajustes.pack_forget()
        # Muestra ajustes
        self.ventana_ajuste.pack(fill='both', expand=True)

    def ocultar_ajustes(self):
        self.ventana_ajuste.pack_forget()
        self.ventana_entrada.pack(pady=10)
        self.boton_inicio.pack(pady=5)
        self.boton_ajustes.pack()

    def cambiar_color_normal(self):
        color = colorchooser.askcolor(title="Color normal")[1]
        if color:
            self.color_normal = color
            self.root.configure(bg=color)
            self.ventana_entrada.configure(bg=color)
            self.boton_color_normal.configure(fg=color)

    def cambiar_color_critico(self):
        color = colorchooser.askcolor(title="Color crítico")[1]
        if color:
            self.color_critico = color
            self.boton_color_critico.configure(fg=color)

    def cambiar_color_pocotime(self):
        color = colorchooser.askcolor(title="Color texto crítico")[1]
        if color:
            self.color_pocotime = color
            self.boton_color_pocotime.configure(fg=color)
    
    def ActualizarDiseño(self,color_normal,color_critico,color_pocotime):
        #Zona de Pantalla Principal
        self.label_horas.configure(bg=color_normal)
        self.label_minutos.configure(bg=color_normal)
        self.label_segundos.configure(bg=color_normal)
        self.root.configure(bg=color_normal)
        self.ventana_entrada.configure(bg=color_normal)
        #Zona de Ajustes:
        self.ventana_ajuste.configure(bg=color_normal)
        self.label_tiempo.configure(bg=color_normal)
        self.adios_label.configure(fg=color_pocotime, bg=color_critico)
        
        #Zona de Aviso
        self.label.configure(fg=color_critico, bg=color_normal)


    def guardar_ajustes(self):
        try:
            tiempo_critico = int(self.entry_tiempo_critico.get())
            if tiempo_critico < 25:
                raise ValueError("El tiempo crítico no puede ser menor a 25 segundos.")
            self.tiempo_critico = tiempo_critico

            # Crear nuevo diccionario y guardar
            nueva_config = {
                "color_normal": self.color_normal,
                "color_critico": self.color_critico,
                "color_pocotime": self.color_pocotime,
                "tiempo_critico": self.tiempo_critico
            }

            with open(CONFIG_FILE, "w") as f:
                json.dump(nueva_config, f)
            self.ActualizarDiseño(self.color_normal,self.color_critico,self.color_pocotime)
            self.ocultar_ajustes()
            self.CargarConfiguracion()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def cargar_configuracion(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r") as f:
                    return json.load(f)
            except:
                pass
        # Valores por defecto
        return {
            "color_normal": "#0ab2ff",
            "color_critico": "black",
            "color_pocotime": "red",
            "tiempo_critico": 25
        }

    def centrar_ventana(self):
        # Centrar la ventana principal en la pantalla con dimensiones fijas de 380x200 píxeles
        self.root.update_idletasks()
        ancho, alto = 380, 200
        x = (self.root.winfo_screenwidth() - ancho) // 2
        y = (self.root.winfo_screenheight() - alto) // 2
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")

    def validar_y_mover(self, campo_actual, siguiente, max_val=None):
        # Valida que el contenido del campo actual sea un número, aplica un máximo si se define,
        # lo corrige si es necesario, y mueve el foco al siguiente campo de entrada
        valor = campo_actual.get().strip()
        numero = int(valor) if valor.isdigit() else 0
        if max_val and numero > max_val:
            numero = max_val
        campo_actual.delete(0, tk.END)
        campo_actual.insert(0, str(numero))
        siguiente.focus()
        # Selecciona todo el contenido del siguiente campo si es un Entry
        if isinstance(siguiente, tk.Entry):
            self.root.after_idle(lambda: siguiente.select_range(0, tk.END))
        return "break"

    def toggle_cronometro(self):
        # Inicia o pausa el cronómetro según el estado actual.
        # Valida la entrada, actualiza la interfaz, y comienza el conteo si es válido.
        self.CargarConfiguracion()
        if not self.en_ejecucion:
            try:
                h = int(self.entrada_horas.get())
                m = int(self.entrada_minutos.get())
                s = int(self.entrada_segundos.get())
                self.tiempo_restante = h * 3600 + m * 60 + s
            except ValueError:
                messagebox.showerror("Error", "Por favor ingresa solo números")
                return
            if self.tiempo_restante <= 0:
                messagebox.showwarning("Aviso", "El tiempo debe ser mayor a 0")
                return
            self.en_ejecucion = True
            self.boton_ajustes.pack_forget()
            self.boton_inicio.config(text="Pausar")
            self.ventana_entrada.pack_forget()
            self.label.pack()
            self.actualizar_cronometro()
        else:
            self.en_ejecucion = False
            self.boton_ajustes.pack()
            self.boton_inicio.config(text="Iniciar")
            self.label.pack_forget()
            self.actualizar_entradas_desde_tiempo()
            self.ventana_entrada.pack(pady=10)
            self.root.configure(bg=self.color_normal)

    def actualizar_entradas_desde_tiempo(self):
        # Convierte los segundos restantes en horas, minutos y segundos,
        # y actualiza los campos de entrada correspondientes.
        h = self.tiempo_restante // 3600
        m = (self.tiempo_restante % 3600) // 60
        s = self.tiempo_restante % 60
        self.entrada_horas.delete(0, tk.END)
        self.entrada_minutos.delete(0, tk.END)
        self.entrada_segundos.delete(0, tk.END)
        self.entrada_horas.insert(0, str(h))
        self.entrada_minutos.insert(0, str(m))
        self.entrada_segundos.insert(0, str(s))

    def actualizar_cronometro(self):
        # Actualiza la cuenta regresiva cada segundo, ajusta el color de fondo según el tiempo restante,
        # y ejecuta el apagado al llegar a cero
        self.CargarConfiguracion()
        if self.en_ejecucion and self.tiempo_restante >= 0:
            h = self.tiempo_restante // 3600
            m = (self.tiempo_restante % 3600) // 60
            s = self.tiempo_restante % 60
            self.label.config(text=f"{h:02d}:{m:02d}:{s:02d}")
            # Cambia los colores si se alcanzó el tiempo crítico
            if self.tiempo_restante <= self.tiempo_critico:
                self.label.config(fg=self.color_pocotime, bg=self.color_critico)
                self.root.configure(bg=self.color_critico)
            else:
                self.label.configure(fg=self.color_critico, bg=self.color_normal)
            # Al llegar a cero, se detiene el cronómetro, muestra "Adiós" y luego apaga la PC
            if self.tiempo_restante == 0:
                self.CargarConfiguracion()
                self.en_ejecucion = False
                self.label.pack_forget()
                self.boton_inicio.config(text="Iniciar")
                self.adios_label.pack(expand=True)
                self.root.after(5000, self.apagar_pc)
            else:
                self.tiempo_restante -= 1
                self.root.after(1000, self.actualizar_cronometro)

    def apagar_pc(self):
        if os.name == 'nt':
            # messagebox.showinfo("Compatible", "Se apago Windows.")  # Solo muestra mensaje durante pruebas
            os.system('shutdown /s /t 1')  # Apaga PC
        else:
            messagebox.showinfo("No compatible", "Este código solo apaga en Windows.")
        self.root.destroy()  # Cierra la app

# --- Ejecución de la app ---
if __name__ == "__main__":
    root = tk.Tk()
    app = OffPcApp(root)
    root.mainloop()
