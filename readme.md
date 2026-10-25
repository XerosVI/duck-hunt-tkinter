# Duck Hunt - Simulatore di 2 in Informatica 🦆

Un semplice videogioco arcade in stile *Duck Hunt* realizzato in Python utilizzando la libreria grafica **Tkinter**. Il gioco include effetti sonori, salvataggio automatico dei record, diversi livelli di difficoltà e un'interfaccia utente interattiva.

---

## 🎮 Features

- **Tre Livelli di Difficoltà:**
  - **Facile:** Anatra lenta, 3 secondi per colpirla.
  - **Media:** Velocità bilanciata, 2 secondi per colpirla.
  - **Difficile:** Anatra ad alta velocità, solo 1 secondo per colpirla!
- **Effetti Sonori Integrati:** Suoni per lo sparo e per la schermata di *Game Over*.
- **Gestione dei Punteggi:** Salvataggio permanente dei record per ciascun livello di difficoltà tramite `high_scores.txt`.
- **Controlli di Gioco:** Funzioni di *Pausa*, *Reset* e *Cancellazione Record*.

---

## 📂 Struttura del Progetto

Assicurati che la directory di progetto contenga i seguenti file prima di eseguire il codice:

```text
.
├── Gioco (con audio).py   # Script principale del gioco
├── background.png          # Sfondo dell'area di gioco
├── easy.png                # Immagine dell'anatra (modalità Facile)
├── medium.png              # Immagine dell'anatra (modalità Media)
├── hard.png                # Immagine dell'anatra (modalità Difficile)
├── explosion.png           # Effetto visivo al momento dell'impatto
├── shoot.wav               # Effetto sonoro dello sparo
├── Game Over.wav           # Effetto sonoro alla fine della partita
└── high_scores.txt         # File di testo per il salvataggio dei record
```

---

## 🚀 Requisiti e Installazione

### Requisiti
- **Python 3.x**
- Sistema Operativo: **Windows** *(la libreria `winsound` è nativa per ambienti Windows)*.

### Come Eseguire il Gioco

1. **Clona il repository:**
   ```bash
   git clone https://github.com/tuo-username/duck-hunt-tkinter.git
   cd duck-hunt-tkinter
   ```

2. **Esegui lo script Python:**
   ```bash
   python "Gioco (con audio).py"
   ```

---

## 🎯 Come Giocare

1. Avvia il gioco per far apparire le anatre nell'area verde.
2. Clicca con il tasto sinistro del mouse sull'anatra prima che lo scadere del tempo la faccia scomparire.
3. Ogni anatra colpita aumenta il punteggio di +1.
4. Ogni anatra mancata riduce le tue vite residue (inizio a 3 vite).
5. Raggiunto lo zero con le vite, la partita termina (Game Over).

---

## 📜 Licenza

Questo progetto è distribuito sotto la licenza Open Source **MIT License**. Sii libero di modificarlo e migliorarlo!