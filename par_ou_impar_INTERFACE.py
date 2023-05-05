import random
import tkinter as tk
from tkinter import messagebox


class ParImparGUI:
        
    def __init__(self, master):
        self.master = master
        self.master.title("Par ou Ímpar")
        self.master.resizable(False, False)

        self.player1_label = tk.Label(self.master, text="Jogador 1:")
        self.player1_label.grid(row=0, column=0, padx=(20, 0), pady=(20, 5))

        self.player1_name = tk.Entry(self.master)
        self.player1_name.grid(row=0, column=1, padx=(20, 5), pady=(20, 5))

        self.player2_label = tk.Label(self.master, text="CPU")
        self.player2_label.grid(row=1, column=0, padx=(20, 0), pady=5)

        self.par_button = tk.Button(self.master, text="Par", width=10, command=lambda: self.play("par"))
        self.par_button.grid(row=2, column=0, padx=20, pady=(5, 20))

        self.imp_button = tk.Button(self.master, text="Ímpar", width=10, command=lambda: self.play("ímpar"))
        self.imp_button.grid(row=2, column=1, padx=20, pady=(5, 20))

        self.number_label = tk.Label(self.master, text="Número (0-10):")
        self.number_label.grid(row=3, column=0, padx=(20, 0), pady=5)

        self.number_entry = tk.Entry(self.master)
        self.number_entry.grid(row=3, column=1, padx=(20, 5), pady=(20, 5))

        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=20)

        self.play_again_button = tk.Button(self.master, text="Jogar Novamente", command=self.play_again, state=tk.DISABLED)
        self.play_again_button.grid(row=5, column=0, columnspan=2, pady=20)

    def play(self, player1_choice):
        player1_name = self.player1_name.get()
        if not player1_name:
            messagebox.showerror("Erro", "Por favor, insira um nome para o Jogador 1.")
            return

        try:
            player1_number = int(self.number_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido entre 0 e 10.")
            return

        if player1_number < 0 or player1_number > 10:
            messagebox.showerror("Erro", "Por favor, insira um número válido entre 0 e 10.")
            return

        if player1_choice == "par":
            player2_choice = "ímpar"
        else:
            player2_choice = "par"

        player2_number = random.randint(0, 10)
        sum_numbers = player1_number + player2_number
        if sum_numbers % 2 == 0:
            winner = player1_name if player1_choice == "par" else "CPU"
        else:
            winner = player1_name if player1_choice == "ímpar" else "CPU"

        messagebox.showinfo("Resultado", f"O resultado foi {sum_numbers}, portanto {winner} venceu!")
        self.play_again_button.config(state=tk.NORMAL)
        self.par_button.config(state=tk.DISABLED)
        self.imp_button.config(state=tk.DISABLED)
        self.number_entry.config(state=tk.DISABLED)

    def play_again(self):
        self.result_label.config(text="")
        self.number_entry.delete(0, tk.END)
        self.play_again_button.config(state=tk.DISABLED)
        self.par_button.config(state=tk.NORMAL)
        self.imp_button.config(state=tk.NORMAL)
        self.number_entry.config(state=tk.NORMAL)

    def quit(self):
        self.master.destroy()

root = tk.Tk()
app = ParImparGUI(root)
root.protocol("WM_DELETE_WINDOW", app.quit)
root.mainloop()
