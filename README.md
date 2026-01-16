# Dice Game 🎲

A fun and interactive **Dice Game** developed using **Python Tkinter**, where the user competes against the computer to reach more than 70 points first.

---

## 🚀 Features

- Graphical User Interface using Tkinter
- Random dice roll (1–6)
- Custom scoring rules
- Roll and Hold gameplay
- Points and score tracking
- Automatic winner detection
- New Game / Reset option

---

## 🛠️ Technologies Used

- Python
- Tkinter (GUI)
- Random module

---

## 📂 Project Structure

dice-game/
│
├── Dice Game.py
└── README.md

---

## ▶️ How to Run the Project

1. Make sure Python is installed on your system.
2. Run the program:

---

## 🎯 Game Rules

### Dice Roll Rules

| Dice Value | Points Effect |
|-----------|---------------|
| 1 or 5 | Points reset to 0 |
| 2 | Adds `2 × 7 = 14` points |
| 4 | Adds `4 × 3 = 12` points |
| 6 | Adds 3 points |
| 3 | Adds 3 points |

### Gameplay

- **Roll**: Rolls the dice and updates points based on rules.
- **Hold**: Skips user roll, allowing strategy play.
- Computer rolls every turn.
- First player to cross **70 points** wins the round.
- Scores are updated after each win.

---

