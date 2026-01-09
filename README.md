# 🧠 AI Lab – Interactive Search & Puzzle Games

This repository contains two interactive games created as part of an **Artificial Intelligence Lab**.  
The goal of this project is to understand how classical AI problem-solving concepts such as **Breadth-First Search (BFS)** and **state-space representation** work by turning them into **real, playable games**.

Instead of only implementing algorithms theoretically, these projects let you **visualize and interact with AI concepts**.

---

## 🌿 Project 1 — Human vs AI Maze Game  
**File:** `maze_game.py`

### Description
Human vs AI Maze Game is a 2D grid-based maze game built using **pygame**.  
A human player competes against an AI agent to reach the goal first.

The AI uses **Breadth-First Search (BFS)** to find the shortest path through the maze, while the human player navigates manually.

### Features
- Grid-based maze visualization  
- Start screen and end screen  
- Player movement using keyboard  
- AI opponent using **Breadth-First Search (BFS)**  
- AI moves automatically at fixed time intervals  
- Clear win and lose conditions  

### How to Run
pip install pygame  
python maze_game.py  

### Controls
W A S D / Arrow Keys – Move player  
ENTER – Start game  
Esc / Close Window – Quit  

---

## 🧩 Project 2 — 8-Puzzle Game  
**File:** `eight_puzzle.py`

### Description
The 8-Puzzle Game is a classic **sliding puzzle game**.  
The objective is to arrange the tiles numbered **1 to 8** in the correct order, with the empty space at the end.

Only **solvable puzzle configurations** are generated to ensure the game can always be completed.

### Features
- Random solvable puzzle generation  
- Keyboard-based tile movement  
- Mouse-based tile clicking  
- Move counter display  
- Restart functionality  
- Win detection with visual feedback  

### How to Run
pip install pygame  
python eight_puzzle.py  

### Controls
Arrow Keys – Move tiles  
Mouse Click – Slide adjacent tile  
R – Restart puzzle  
ESC – Quit  

---

## 🎯 Learning Objectives
- Understand how **Breadth-First Search (BFS)** finds optimal paths  
- Learn grid and state-space representation  
- Apply AI concepts to interactive applications  
- Visualize problem-solving instead of only coding algorithms  

---

## 🛠 Requirements
Python 3  
pygame  

Install pygame:
pip install pygame  

---

## 👨‍💻 Author
Created as part of an **Artificial Intelligence Lab Project** to demonstrate AI concepts through interactive games.
