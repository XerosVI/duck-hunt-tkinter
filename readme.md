# Duck Hunt - High School Arcade Game 🦆

A simple *Duck Hunt*-style arcade game built in Python using the **Tkinter** GUI library. This project was originally created back in high school as an informatics project. It features sound effects, score tracking across difficulties, customizable controls, and nostalgic arcade mechanics.

---

## 📜 Background & Context

This project serves as an archive of my early programming journey in high school. It was one of my first hands-on experiences with desktop GUI development, event-driven loops, audio integration, and basic state persistence in Python. 

> **Note:** The code is preserved here in its original state for archival and personal memory purposes.

---

## 🎮 Features

- **Three Difficulty Levels:**
  - **Easy:** Slow duck movement, big hitbox, 3 seconds to hit.
  - **Medium:** Balanced speed, medium hitbox, 2 seconds to hit.
  - **Hard:** Fast duck movement, small hitbox, only 1 second to hit!
- **Integrated Audio:** Custom sound effects for shooting and game over scenarios.
- **High Score System:** Automatic saving and loading of high scores per difficulty via a local `high_scores.txt` file.
- **Game Controls:** Pause, reset, and high-score deletion options directly within the control panel.

---

## 📂 Project Structure

Make sure all assets remain in the root directory alongside the main script (or you could replace assets with your own for customization purposes):

```text
.
├── main.py   # Main Python game script
├── background.png          # Game background canvas image
├── easy.png                # Duck sprite (Easy difficulty)
├── medium.png              # Duck sprite (Medium difficulty)
├── hard.png                # Duck sprite (Hard difficulty)
├── explosion.png           # Hit feedback sprite
├── shoot.wav               # Gunshot sound effect
├── Game Over.wav           # Game over sound effect
└── high_scores.txt         # Local score persistence file
```

---

## 🚀 Requirements & Setup

### Requirements
- **Python 3.x**
- **Windows OS** *(The game uses Python's built-in `winsound` library, which is native to Windows)*.

### How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/duck-hunt-tkinter.git
   cd duck-hunt-tkinter
   ```

2. **Run the game:**
   ```bash
   python "main.py"
   ```

---

## 🎯 How to Play

1. Launch the game to start spawning ducks on the field.
2. Left-click on the duck before the timer runs out to shoot it.
3. Every hit increases your score by +1.
4. Missing a duck subtracts 1 life (you start with 3 lives).
5. Running out of lives triggers a Game Over screen and saves your high score.

---

## 💡 What I Learned

- Event loops and scheduled callbacks using Tkinter's `.after()` function.
- Simple physics logic (canvas dynamic coordinate updating and boundary bouncing).
- Basic file I/O operations for local data persistence.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
