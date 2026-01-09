# AI-LAB
# 🧠 AI Lab – Interactive Search & Puzzle Games

This repository contains **two interactive games developed using Python and Pygame** as part of an **Artificial Intelligence Lab**.

The objective of this project is to **understand AI problem-solving concepts and search techniques** by transforming them into **playable, visual applications** instead of limiting them to theoretical implementation.

---

## 🎮 Project 1 — Human vs AI Maze Game  
**File:** `maze_game.py`

### Description
Human vs AI Maze Game is a grid-based maze game where a **human player competes against an AI agent** to reach the goal first.

The AI uses **Breadth-First Search (BFS)** to compute the shortest path from the start to the goal, while the human navigates the maze manually.

---

### Features
- Grid-based maze visualization  
- Human player movement using keyboard  
- AI opponent using **Breadth-First Search (BFS)**  
- AI moves automatically at fixed time intervals  
- Start screen and end screen  
- Win/Lose detection  

---

### How to Run
```bash
pip install pygame
python maze_game.py
Controls

W / A / S / D or Arrow Keys – Move player

ENTER – Start game

Close Window – Exit

🧩 Project 2 — 8-Puzzle Game

File: eight_puzzle.py

Description

The 8-Puzzle Game is a classic sliding tile puzzle where the goal is to arrange numbers from 1 to 8 in order, with the empty tile at the end.

The puzzle generates only solvable configurations, ensuring the game is always winnable.

Features

Random solvable puzzle generation

Keyboard-based tile movement

Mouse-based tile clicking

Move counter

Restart option

Win detection

How to Run
pip install pygame
python eight_puzzle.py

Controls

Arrow Keys – Move tiles

Mouse Click – Slide adjacent tile

R – Restart puzzle

ESC – Quit game

🎯 Learning Objectives

Understand how Breadth-First Search (BFS) finds optimal paths

Learn grid-based problem representation

Apply AI concepts to interactive applications

Visualize problem-solving instead of only coding algorithms

🛠 Requirements

Python 3

pygame

Install pygame:

pip install pygame

👨‍💻 Author

Created as part of an Artificial Intelligence Lab Project to demonstrate search concepts through interactive games.
