# Robot Navigation AI System

## Project Title

**Robot Navigation AI using Knowledge-Based Reasoning**


## Submitted By

**Caroline Mildred Gomes**


---

# Overview

This project is an Artificial Intelligence based robot navigation system.

The AI robot learns about its environment and uses logical reasoning
to find a safe path from a starting position to a target location.

The robot uses a knowledge base to understand:

- Safe locations
- Obstacles
- Available movements
- Goal position


---

# Objective

The main objective of this project is to build an intelligent agent
that can make decisions based on stored knowledge.

The robot analyzes the environment and selects the best possible movement
without entering blocked areas.


---

# Features

- AI-based navigation
- Knowledge representation
- Logical decision making
- Grid environment simulation
- Obstacle detection
- Path finding


---

# Technologies Used

- Python 3
- Artificial Intelligence
- Knowledge-Based Agents
- Logical Inference
- Search Algorithms


---

# Project Structure
Robot_Navigation_AI/

│
├── README.md
│
├── robot.py
│ Main robot decision program
│
├── knowledge.py
│ Stores robot knowledge and reasoning
│
├── environment.py
│ Creates the navigation environment
│
├── data/
│
│ ├── map1.txt
│ │ Sample navigation map
│ │
│ └── map2.txt
│ Second test map
│
└── explanation.md
Complete project explanation



---

# Environment Representation

The robot works on a grid map.

Symbols:


S = Starting Point

G = Goal

X = Obstacle

. = Safe Path



Example:


S . .
X . .
. . G



---

# How the AI Works


## Step 1: Read Environment

The robot loads the map file.


Example:


S . .
. X .
. . G



---

## Step 2: Build Knowledge

The AI identifies:

- Starting position
- Goal position
- Blocked cells
- Safe cells


---

## Step 3: Reasoning Process

The robot checks possible movements.

Example:


Current position:

(0,0)

Possible moves:

Right -> Safe

Down -> Obstacle



The AI chooses:


Move Right



---

## Step 4: Reach Goal

The robot continues making decisions until it reaches:


G



---

# How to Run


Open terminal:


python robot.py



---

# Example Input

Map:


S . .
. X .
. . G



---

# Example Output


Robot Starting...

Current Position:
(0,0)

Thinking...

Safe move found:
(0,1)

Moving...

Goal Reached!

Path:

(0,0)
(0,1)
(0,2)
(1,2)
(2,2)



---

# Applications

Robot navigation AI can be used in:

- Autonomous robots
- Self-driving systems
- Smart warehouses
- Navigation assistants


---

# Conclusion

This project demonstrates how Artificial Intelligence can use
knowledge representation and reasoning to allow robots to make
intelligent decisions in an unknown environment.


---

## Created By

**Caroline Mildred Gomes**
