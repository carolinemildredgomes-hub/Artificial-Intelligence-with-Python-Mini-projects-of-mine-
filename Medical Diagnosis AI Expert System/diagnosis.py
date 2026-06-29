from diseases import rules


def load_symptoms():

    symptoms = set()


    print("Enter patient symptoms")
    print("Type done when finished\n")


    while True:

        symptom = input("> ")


        if symptom == "done":
            break


        symptoms.add(symptom)


    return symptoms



def diagnose(symptoms):


    results = []


    for rule in rules:


        disease = rule.check(symptoms)


        if disease:

            results.append(disease)



    return results



def main():


    symptoms = load_symptoms()


    diseases = diagnose(symptoms)


    print("\nDiagnosis Result:")


    if diseases:


        for d in diseases:

            print("-", d)


    else:

        print("No matching disease found")



main()
