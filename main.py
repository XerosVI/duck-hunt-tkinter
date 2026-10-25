import tkinter as tk
import random
import time
import winsound

class DuckHuntGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulatore di 2 in informatica")
    
        # Frame principale
        self.main_frame = tk.Frame(master)
        self.main_frame.pack()

        # Frame area di gioco
        self.game_frame = tk.Frame(self.main_frame, borderwidth=2, relief="sunken")
        self.game_frame.grid(row=0, column=0, padx=10, pady=10)

        self.canvas = tk.Canvas(self.game_frame, width=800, height=600)
        self.canvas.pack()

        self.background_image = tk.PhotoImage(file="background.png")
        self.canvas.create_image(0, 0, image=self.background_image, anchor='nw')
    
        # Frame area di controllo
        self.control_frame = tk.Frame(self.main_frame)
        self.control_frame.grid(row=1, column=0, pady=10)

        self.high_scores = {"Facile": 0, "Media": 0, "Difficile": 0}
        self.load_high_scores()

        self.high_score_label = tk.Label(self.control_frame, text=f"Record: {self.high_scores['Media']}")
        self.high_score_label.grid(row=0, column=4, padx=10)
        
        self.score = 0
        self.lives = 3
        self.score_label = tk.Label(self.control_frame, text=f"Punteggio: {self.score}")
        self.score_label.grid(row=0, column=0, padx=10)

        self.lives_label = tk.Label(self.control_frame, text=f"Vite: {self.lives}")
        self.lives_label.grid(row=0, column=1, padx=10)

        self.reset_button = tk.Button(self.control_frame, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=0, column=2, padx=10)

        self.pause_button = tk.Button(self.control_frame, text="Pausa", command=self.pause_game)
        self.pause_button.grid(row=0, column=3, padx=10)

        self.reset_record_button = tk.Button(self.control_frame, text="Cancella Record", command=self.reset_high_score)
        self.reset_record_button.grid(row=0, column=5, padx=10)

        self.difficulty = tk.StringVar(value="Media")
        self.easy_radio = tk.Radiobutton(self.control_frame, text="Facile", variable=self.difficulty, value="Facile", command=self.change_difficulty)
        self.easy_radio.grid(row=1, column=2, sticky="ew")

        self.medium_radio = tk.Radiobutton(self.control_frame, text="Media", variable=self.difficulty, value="Media", command=self.change_difficulty)
        self.medium_radio.grid(row=1, column=3, sticky="ew")

        self.hard_radio = tk.Radiobutton(self.control_frame, text="Difficile", variable=self.difficulty, value="Difficile", command=self.change_difficulty)
        self.hard_radio.grid(row=1, column=4, sticky="ew")

        self.is_paused = False
        self.direction = [1, 1]
        self.duck = None
        self.duck_image = None
        self.game_over_text = None
        self.game_over_rect = None
        self.start_time = None
        self.pause_start_time = None
        self.game_over_flag = False

        # Carica immagini
        self.explosion_image = tk.PhotoImage(file="explosion.png")
        self.duck_images = {
            "Facile": tk.PhotoImage(file="easy.png"),
            "Media": tk.PhotoImage(file="medium.png"),
            "Difficile": tk.PhotoImage(file="hard.png")
        }
        self.set_difficulty()
        
        self.master.after(1000, self.spawn_duck)  # delay di 1000 ms


    def change_difficulty(self):
        self.reset_game()
        self.set_difficulty()
        self.high_score_label.config(text=f"Record: {self.high_scores[self.difficulty.get()]}")

        
    def set_difficulty(self):
        level = self.difficulty.get()
        if level == "Facile":
            self.remaining_time = 3
            self.duck_image = self.duck_images["Facile"]
            self.duck_speed = 2 
        elif level == "Media":
            self.remaining_time = 2
            self.duck_image = self.duck_images["Media"]
            self.duck_speed = 6
        elif level == "Difficile":
            self.remaining_time = 1
            self.duck_image = self.duck_images["Difficile"]
            self.duck_speed = 10  

    def load_high_scores(self):
        try:
            with open("high_scores.txt", "r") as file:
                self.high_scores = eval(file.read())
        except FileNotFoundError:
            self.high_scores = {"Facile": 0, "Media": 0, "Difficile": 0}

    def save_high_scores(self):
        with open("high_scores.txt", "w") as file:
            file.write(str(self.high_scores))



    def reset_high_score(self):
        current_difficulty = self.difficulty.get()
        self.high_scores[current_difficulty] = 0
        self.high_score_label.config(text=f"Record: {self.high_scores[current_difficulty]}")
        self.save_high_scores()


    def spawn_duck(self):
        if self.duck is None and not self.is_paused and not self.game_over_flag:
            x = random.randint(50, 750)
            y = random.randint(50, 550)
            self.duck = self.canvas.create_image(x, y, image=self.duck_image, anchor='nw')
            self.canvas.tag_bind(self.duck, '<Button-1>', self.shoot_duck)
            self.canvas.tag_raise(self.duck)
            self.move_duck()
            self.start_time = time.time()
            self.master.after(100, self.check_duck_duration)  # Check ogni 100 ms


            
    def move_duck(self):
        if self.duck is not None and not self.is_paused:
            x_move = self.direction[0] * self.duck_speed
            y_move = self.direction[1] * self.duck_speed
            self.canvas.move(self.duck, x_move, y_move)
    
            coords = self.canvas.coords(self.duck)
            if coords[0] <= 0:
                self.direction[0] = 1
                self.canvas.move(self.duck, 1, 0)
            elif coords[0] + self.duck_image.width() >= 800:
                self.direction[0] = -1
                self.canvas.move(self.duck, -1, 0)

            if coords[1] <= 0:
                self.direction[1] = 1
                self.canvas.move(self.duck, 0, 1)
            elif coords[1] + self.duck_image.height() >= 600:
                self.direction[1] = -1
                self.canvas.move(self.duck, 0, -1)

            self.master.after(50, self.move_duck)

    
    def check_duck_duration(self):
        if self.duck is not None and not self.is_paused:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            if elapsed_time >= self.remaining_time:
                self.remove_duck()
            else:
                self.master.after(100, self.check_duck_duration)  # Check ogni 100 ms

    def remove_duck(self):
        if self.duck is not None:
            self.canvas.delete(self.duck)
            self.duck = None
            self.lives -= 1
            self.lives_label.config(text=f"Vite: {self.lives}")
            if self.lives > 0:
                self.master.after(500, self.spawn_duck)  # Cooldown di 0.5 secondi prima di spawnare un altro obiettivo
            else:
                self.game_over()

    def shoot_duck(self, event):
        if self.duck is not None and not self.is_paused and not self.game_over_flag:
            winsound.PlaySound(None, winsound.SND_ASYNC)
            winsound.PlaySound("shoot.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            
            # Get the position of the duck
            coords = self.canvas.coords(self.duck)
            
            # Display the explosion image at the duck's position
            self.explosion = self.canvas.create_image(coords[0], coords[1], image=self.explosion_image, anchor='nw')
            
            # Remove the explosion image after a short delay
            self.master.after(500, self.remove_explosion)
            
            self.canvas.delete(self.duck)
            self.duck = None
            self.score += 1
            self.score_label.config(text=f"Punteggio: {self.score}")
            
            # Check and update high score for current difficulty
            if self.score > self.high_scores[self.difficulty.get()]:
                self.high_scores[self.difficulty.get()] = self.score
                self.high_score_label.config(text=f"Record: {self.high_scores[self.difficulty.get()]}")

            self.master.after(500, self.spawn_duck)

    def remove_explosion(self):
        if self.explosion is not None:
            self.canvas.delete(self.explosion)
            self.explosion = None


    def game_over(self):
        if self.game_over_text is None:
            self.game_over_rect = self.canvas.create_rectangle( 250, 200, 550, 400, fill='white', outline='black' )
            self.game_over_text = self.canvas.create_text(400, 300, text=f"Game Over\nPunteggio: {self.score}\nRecord: {self.high_scores[self.difficulty.get()]}", font=('Helvetica', 30), fill='black')
        self.game_over_flag = True
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound("Game Over.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        if self.duck is not None:
            self.canvas.delete(self.duck)
            self.duck = None

        self.save_high_scores()



    def reset_game(self):
        if self.duck is not None:
            self.canvas.delete(self.duck)
            self.duck = None
        if self.game_over_text is not None:
            self.canvas.delete(self.game_over_text)
            self.game_over_text = None
        if self.game_over_rect is not None:
            self.canvas.delete(self.game_over_rect)
            self.game_over_rect = None
        self.score = 0
        self.lives = 3
        self.score_label.config(text=f"Punteggio: {self.score}")
        self.lives_label.config(text=f"Vite: {self.lives}")
        self.is_paused = False
        self.game_over_flag = False
        self.pause_button.config(text="Pausa")
        self.master.after(500, self.spawn_duck)

    def pause_game(self):
        if not self.game_over_flag:
            self.is_paused = not self.is_paused
            if self.is_paused:
                self.pause_button.config(text="Continua")
                if self.score > 0:
                    self.score -= 1
                self.score_label.config(text=f"Punteggio: {self.score}")
                self.pause_start_time = time.time()
            else:
                self.pause_button.config(text="Pausa")
                self.start_time += (time.time() - self.pause_start_time)  # Correzione tempo
                if self.duck is None:
                    self.master.after(500, self.spawn_duck)  # Riprendi gioco se non ci sono obiettivi
                else:
                    self.master.after(50, self.move_duck)  #Riprendi se ci sono obiettivi
                    self.master.after(100, self.check_duck_duration)  # Continua controllo

if __name__ == "__main__":
    root = tk.Tk()
    game = DuckHuntGame(root)
    root.mainloop()
