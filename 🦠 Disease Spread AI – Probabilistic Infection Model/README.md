# 🦠 Disease Spread AI – Probabilistic Infection Model

## Author
**Caroline Mildred Gomes**

---

## 📌 Overview

This project simulates the spread of an infectious disease in a small community using probabilistic reasoning.

Instead of deterministic rules, it uses a **Bayesian-style model** to estimate:

- Probability a person is infected
- Influence of social contacts
- Uncertainty in transmission

---

## 🧠 Core Idea

A person’s infection status depends on:

- Base infection probability
- Contact with infected individuals
- Probability of disease transmission

We compute probabilities over **all possible infection combinations**.

---

## 📊 Model Assumptions

- Base infection probability: `0.2`
- Transmission probability: `0.6`
- Independence between individuals (conditional on contacts)

---

## 📁 Project Structure
disease-ai/
│
├── disease.py
└── data/
└── community0.csv


---

## 📄 Dataset Format

CSV file format:

```
name,contacts,infection
Alice,Bob;Charlie,1
Bob,Alice,
Charlie,Alice,
David,,0
```

- `contacts`: people this person interacts with
- `infection`:
  - `1` → infected
  - `0` → not infected
  - empty → unknown

---

## ⚙️ How It Works

The program:

1. Loads community data
2. Generates all possible infection combinations
3. Computes joint probabilities
4. Aggregates results
5. Normalizes final distributions

---

## 🧮 Functions Implemented

### joint_probability()

Computes probability of a full infection scenario.

---

### update()

Adds computed probability to distribution totals.

---

### normalize()

Ensures probabilities sum to 1.

---

## 🚀 How to Run

```bash
python disease.py

📊 Example Output
Alice: {True: 0.62, False: 0.38}
Bob: {True: 0.41, False: 0.59}
Charlie: {True: 0.35, False: 0.65}
David: {True: 0.10, False: 0.90}

📚 Concepts Used
Bayesian reasoning
Probability distributions
Graph-based modeling
Combinatorics (powerset enumeration)
Epidemiological modeling

🎯 Applications
Disease spread modeling
Epidemic prediction systems
Contact tracing simulations
Risk analysis

✨ Learning Outcome

This project demonstrates how AI can model uncertainty in real-world systems using probability instead of fixed rules.

🙌 Credits

Inspired by CS50 AI concepts.

✍️ Author

Caroline Mildred Gomes
