from logic import Symbol, And, Or, Rule


# Symptoms

fever = Symbol("fever")
cough = Symbol("cough")
fatigue = Symbol("fatigue")
rash = Symbol("rash")
breathing_problem = Symbol("breathing_problem")
headache = Symbol("headache")


# Medical knowledge base

rules = [


Rule(
    And(fever, cough, fatigue),
    "Flu"
),


Rule(
    And(fever, rash),
    "Measles"
),


Rule(
    And(cough, breathing_problem),
    "Pneumonia"
),


Rule(
    And(headache, fever),
    "Migraine Fever"
)

]
