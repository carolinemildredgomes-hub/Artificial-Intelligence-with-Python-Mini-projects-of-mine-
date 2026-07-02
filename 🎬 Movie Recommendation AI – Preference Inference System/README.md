
---

# 🎬 PROJECT 2 — Movie Recommendation AI (README.md)

```markdown
# 🎬 Movie Recommendation AI – Preference Inference System

## Author
**Caroline Mildred Gomes**

---

## 📌 Overview

This project predicts user movie preferences using a probabilistic model.

It estimates:

- Likelihood a user prefers action movies
- Likelihood a user prefers romance movies
- Hidden preference patterns

Instead of fixed rules, it uses **probabilistic inference over user groups**.

---

## 🧠 Core Idea

Users belong to hidden preference types such as:

- Action lovers
- Romance lovers
- Mixed preference
- Neutral viewers

The system infers preferences based on observed likes.

---

## 📊 Model Assumptions

- Preference groups exist but are hidden
- Each group influences movie choices probabilistically
- Observations are noisy (not perfect indicators)

---

## 📁 Project Structure
movie-ai/
│
├── recommend.py
└── data/
└── users.csv


---

## 📄 Dataset Format

```
name,likes_action,likes_romance
Alice,1,0
Bob,1,1
Charlie,0,1
David,0,0
```

- `1` → likes genre
- `0` → does not like genre

---

## ⚙️ How It Works

The system:

1. Loads user preference data
2. Enumerates possible preference groups
3. Computes probability of each group
4. Aggregates results
5. Normalizes final probabilities

---

## 🧮 Functions Implemented

### joint_probability()

Computes probability of a given preference assignment.

---

### update()

Accumulates probability into user preference distribution.

---

### normalize()

Ensures all probability values sum to 1.

---

## 🚀 How to Run

```bash
python recommend.py

📊 Example Output
Alice: {True: 0.72, False: 0.28}
Bob: {True: 0.65, False: 0.35}
Charlie: {True: 0.40, False: 0.60}
David: {True: 0.25, False: 0.75}

📚 Concepts Used
Probabilistic inference
Hidden variable modeling
User behavior analysis
Enumeration of possible worlds
AI recommendation systems

🎯 Applications
Movie recommendation engines
Netflix-style ranking systems
User personalization systems
Behavioral prediction AI

✨ Learning Outcome

This project demonstrates how AI can infer hidden preferences from partial user data using probability theory.

🙌 Credits

Inspired by CS50 AI principles.

✍️ Author

Caroline Mildred Gomes
