چ# 🎯 Cursor Hunt – Python Edition

A simple and fun **two-player cursor hunting game** built with **Python** and **Tkinter**.

The first player secretly chooses a target location on the screen, and the second player has to find it within a limited number of attempts.

---

## 📸 Preview

> Fullscreen game with hidden cursor mechanics.

**Game Flow**

1. Player 1 starts the game.
2. Player 1 double-clicks anywhere on the screen to hide the target.
3. The mouse cursor disappears.
4. Player 2 has **5 attempts** to find the hidden location.
5. If the click is close enough to the target, Player 2 wins.
6. Otherwise, after all attempts are used, Player 1 wins.

---

## ✨ Features

* 🎮 Two-player gameplay
* 🖥️ Fullscreen interface
* 🖱️ Hidden mouse cursor
* 📍 Distance-based target detection
* ❤️ Simple and lightweight
* ⚡ Built only with Python standard libraries
* ❌ No external dependencies

---

## 🛠️ Technologies Used

* Python 3.x
* Tkinter
* math

---

## 📂 Project Structure

```text
Cursor-Hunt/
│
├── cursor_hunt.py
└── README.md
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/your-username/Cursor-Hunt.git
```

### Navigate into the project

```bash
cd Cursor-Hunt
```

### Run the game

```bash
python cursor_hunt.py
```

---

## 🎯 Game Rules

* Player 1 hides the target by **double-clicking**.
* The cursor becomes invisible.
* Player 2 has **5 attempts**.
* A click is considered correct if it is within **50 pixels** of the hidden target.
* Press **ESC** at any time to exit.

---

## ⚙️ Configuration

You can customize the game by editing these values:

```python
self.attempts = 5
self.tolerance = 50
```

| Variable  | Description                     |
| --------- | ------------------------------- |
| attempts  | Number of tries allowed         |
| tolerance | Radius (pixels) required to win |

---

## 📖 How It Works

The game calculates the Euclidean distance between the player's click and the hidden target.

```python
distance = math.sqrt(
    (x1 - x2)**2 +
    (y1 - y2)**2
)
```

If the calculated distance is less than or equal to the tolerance value, the player wins.

---

## ⌨️ Controls

| Key               | Action                    |
| ----------------- | ------------------------- |
| Double Left Click | Hide the target           |
| Left Click        | Guess the target location |
| ESC               | Exit the game             |

---

## 💡 Future Improvements

* 🔊 Sound effects
* 🎵 Background music
* 🌈 Animations
* 🎯 Difficulty levels
* 👥 Multiplayer over network
* 📊 Scoreboard
* 🏆 Best score history
* 🌍 Multi-language support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Yasin Fallahati**

* Python Developer
* GitHub: https://github.com/yasinfallahati

---

⭐ If you like this project, don't forget to **Star** the repository!
