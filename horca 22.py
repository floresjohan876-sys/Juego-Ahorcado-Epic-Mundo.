import tkinter as tk
from tkinter import messagebox
import random
import winsound

palabras = ["python", "programacion", "honduras", "computadora", "teclado", "ventana", "impresora"]

class JuegoAhorcadoPro:
    def __init__(self, root):
        self.root = root
        self.root.title("Epic Mundo - Ahorcado PRO")
        self.root.geometry("850x650")
        self.root.configure(bg="#2c3e50")

        self.victorias = 0
        self.derrotas = 0
        self.intentos = 10
        self.adivinadas = []
        self.palabra = random.choice(palabras)
        
        self.canvas = tk.Canvas(root, width=350, height=400, bg="#87CEEB", highlightthickness=0)
        self.canvas.place(x=20, y=150)
        
        self.lbl_stats = tk.Label(root, text="Victorias: 0 | Derrotas: 0", font=("Arial", 14), bg="#2c3e50", fg="white")
        self.lbl_stats.place(x=400, y=20)
        
        self.lbl_intentos = tk.Label(root, text="Intentos Restantes: 10", font=("Arial", 14, "bold"), bg="#c0392b", fg="white", padx=10)
        self.lbl_intentos.place(x=400, y=60)
        
        self.lbl_palabra = tk.Label(root, text="", font=("Consolas", 24, "bold"), bg="#2c3e50", fg="#f1c40f")
        self.lbl_palabra.place(x=400, y=120)
        
        self.frame_teclado = tk.Frame(root, bg="#2c3e50")
        self.frame_teclado.place(x=400, y=200)
        
        tk.Button(root, text="Reiniciar Partida", command=self.resetear_total, bg="#e74c3c", fg="white", font=("Arial", 12)).place(x=400, y=550)
        
        self.dibujar_escenario()
        self.actualizar_palabra()
        self.crear_teclado()

    def dibujar_escenario(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(150, 350, 200, 150, fill="#5D4037", outline="") 
        self.canvas.create_oval(50, 50, 300, 200, fill="#2E7D32", outline="") 
        self.canvas.create_line(175, 150, 250, 100, width=10, fill="#5D4037")

    def dibujar_muñeco(self):
        fallos = 10 - self.intentos
        # Dibujamos las partes del cuerpo
        if fallos >= 1: self.canvas.create_line(250, 100, 250, 130, width=4, fill="black")
        if fallos >= 2: self.canvas.create_oval(230, 130, 270, 170, fill="#FFCCBC", width=2)
        if fallos >= 3: 
            # Ojos (los agregamos en el paso 3)
            self.canvas.create_oval(240, 140, 245, 145, fill="black") # Ojo izquierdo
            self.canvas.create_oval(255, 140, 260, 145, fill="black") # Ojo derecho
        if fallos >= 4: self.canvas.create_line(250, 170, 250, 250, width=4, fill="#37474F") # Torso
        if fallos >= 5: self.canvas.create_line(250, 190, 220, 220, width=3, fill="#37474F") # Brazo izq
        if fallos >= 6: self.canvas.create_line(250, 190, 280, 220, width=3, fill="#37474F") # Brazo der
        if fallos >= 7: self.canvas.create_line(250, 250, 230, 320, width=4, fill="#37474F") # Pierna izq
        if fallos >= 8: self.canvas.create_line(250, 250, 270, 320, width=4, fill="#37474F") # Pierna der

    def crear_teclado(self):
        letras = "abcdefghijklmnopqrstuvwxyz"
        for i, letra in enumerate(letras):
            tk.Button(self.frame_teclado, text=letra.upper(), width=4, height=2,
                      command=lambda l=letra: self.probar_letra(l)).grid(row=i//6, column=i%6, padx=2, pady=2)

    def actualizar_palabra(self):
        self.lbl_palabra.config(text=" ".join([l if l in self.adivinadas else "_" for l in self.palabra]))

    def probar_letra(self, letra):
        winsound.Beep(1000, 50)
        if letra in self.adivinadas: return
        self.adivinadas.append(letra)
        
        if letra in self.palabra:
            self.actualizar_palabra()
            if "_" not in self.lbl_palabra.cget("text").replace(" ", ""):
                self.victorias += 1
                winsound.Beep(1500, 500)
                messagebox.showinfo("Victoria", "¡Ganaste!")
                self.nueva_partida()
        else:
            self.intentos -= 1
            self.lbl_intentos.config(text=f"Intentos Restantes: {self.intentos}")
            self.dibujar_muñeco()
            if self.intentos == 0:
                self.derrotas += 1
                winsound.Beep(300, 800)
                messagebox.showerror("Fin", f"Perdiste. Era: {self.palabra}")
                self.nueva_partida()
        self.lbl_stats.config(text=f"Victorias: {self.victorias} | Derrotas: {self.derrotas}")

    def nueva_partida(self):
        self.palabra = random.choice(palabras)
        self.adivinadas = []
        self.intentos = 10
        self.lbl_intentos.config(text="Intentos Restantes: 10")
        self.dibujar_escenario()
        self.actualizar_palabra()

    def resetear_total(self):
        self.victorias = 0
        self.derrotas = 0
        self.lbl_stats.config(text="Victorias: 0 | Derrotas: 0")
        self.nueva_partida()

def lanzar_juego():
    root_inicio.destroy()
    juego = tk.Tk()
    JuegoAhorcadoPro(juego)
    juego.mainloop()

root_inicio = tk.Tk()
root_inicio.title("Menu")
root_inicio.geometry("300x200")
tk.Label(root_inicio, text="BIENVENIDO A EPIC MUNDO", font=("Arial", 12, "bold")).pack(pady=30)
tk.Button(root_inicio, text="INICIAR JUEGO", command=lanzar_juego, bg="#FF5722", fg="white").pack()
root_inicio.mainloop()

