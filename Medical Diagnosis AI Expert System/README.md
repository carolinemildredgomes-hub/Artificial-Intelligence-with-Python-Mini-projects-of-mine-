# Medical Diagnosis AI Expert System

## Project Title

**Medical Diagnosis Expert System using Propositional Logic**

## Submitted By

**Caroline Mildred Gomes**


---

# Overview

This project is an Artificial Intelligence based medical diagnosis system.

The system uses propositional logic and a knowledge-based reasoning approach
to analyze patient symptoms and identify possible diseases.

The AI stores medical knowledge as logical rules and applies inference
to reach a diagnosis.


---

# Objective

The main objective of this project is to demonstrate how Artificial Intelligence
can use logical reasoning to solve real-world problems.

The system accepts symptoms from a user and compares them with stored medical
rules to generate possible disease predictions.


---

# Features

- Knowledge-based AI system
- Propositional logic implementation
- Rule-based reasoning
- Symptom analysis
- Disease prediction
- Easy to extend with new diseases and symptoms


---

# Technologies Used

- Python 3
- Artificial Intelligence
- Propositional Logic
- Knowledge Representation
- Logical Inference


---

# Project Structure
Medical_Diagnosis_AI/

│
├── README.md
│
├── logic.py
│ Contains logical operations and rule evaluation
│
├── diseases.py
│ Contains medical facts and knowledge base
│
├── diagnosis.py
│ Main AI program for diagnosis
│
├── data/
│ └── symptoms.txt
│ Sample patient data
│
└── explanation.md
Step-by-step project explanation



---

# How the AI Works

The system follows these steps:


## Step 1: Collect Symptoms

The user enters patient symptoms.

Example:


fever
cough
fatigue



## Step 2: Knowledge Representation

Symptoms are represented as logical symbols.

Example:


fever = True
cough = True



## Step 3: Apply Medical Rules

The AI checks stored rules.

Example:


IF fever AND cough AND fatigue
THEN Flu



## Step 4: Logical Reasoning

The AI compares the patient's symptoms with the knowledge base.

If the conditions are satisfied, the disease is selected.


## Step 5: Display Result

The system shows the possible diagnosis.


Example:


Diagnosis Result:

Flu


---

# How to Run the Project

Open the project folder in VS Code.

Run:


python diagnosis.py



---

# Example Input


Enter patient symptoms

fever
cough
fatigue
done



# Example Output


Diagnosis Result:

Flu


---

# Applications

This type of AI system can be used in:

- Healthcare assistance
- Medical decision support
- Expert systems
- Automated reasoning systems


---

# Conclusion

The Medical Diagnosis AI Expert System demonstrates how artificial intelligence
can represent knowledge and use logical reasoning to make decisions.

The project shows the practical application of propositional logic in solving
real-world problems.


---

## Created By

**Caroline Mildred Gomes**
