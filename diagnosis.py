# Define symptoms for each disease
common_cold_symptoms = ["runny nose", "sore throat", "cough"]
flu_symptoms = ["fever", "headache", "muscle aches"]
covid19_symptoms = ["fever", "cough", "shortness of breath", "loss of taste or smell"]

# Function to get user input
def get_user_symptoms():
    print("Enter your symptoms (comma-separated): ")
    symptoms = input().split(",")
    symptoms = [symptom.strip().lower() for symptom in symptoms]
    return symptoms

# Function to diagnose based on symptoms
def diagnose(symptoms):
    diagnoses = []
    
    if any(symptom in symptoms for symptom in common_cold_symptoms):
        diagnoses.append("Common Cold")
    if any(symptom in symptoms for symptom in flu_symptoms):
        diagnoses.append("Flu")
    if any(symptom in symptoms for symptom in covid19_symptoms):
        diagnoses.append("COVID-19")
    
    return diagnoses

# Main function to run the diagnosis system
def main():
    user_symptoms = get_user_symptoms()
    diagnoses = diagnose(user_symptoms)
    
    if diagnoses:
        print("Based on your symptoms, you might have: " + ", ".join(diagnoses))
    else:
        print("No matching diagnosis found. Please consult a medical professional.")

# Run the program
if __name__ == "__main__":
    main()