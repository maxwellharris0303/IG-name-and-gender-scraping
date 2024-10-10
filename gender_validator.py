import pandas as pd
import gender_guesser.detector as gender

# Load the CSV file
file_path = 'results.csv'  # Update this with your CSV file path
data = pd.read_csv(file_path, encoding='utf-8')

# Create a gender detector instance
detector = gender.Detector()

# Function to determine gender based on name
def get_gender(name):
    if pd.isna(name):  # Check if the name is NaN
        return 'unknown'
    name_parts = name.split()  # Split the name into individual parts
    for part in name_parts:
        gender_result = detector.get_gender(part)
        if gender_result in ['male', 'female']:
            return gender_result
        elif gender_result == 'mostly_male':
            return 'male'
        elif gender_result == 'mostly_female':
            return 'female'
    return 'unknown'  # Return unknown if no determination can be made

# Determine gender for each row
data['gender'] = data['name'].apply(get_gender)

# Separate into male and female DataFrames
male_data = data[data['gender'] == 'male']
female_data = data[data['gender'] == 'female']
# unknown_data = data[data['gender'] == 'unknown']

# Save the results to separate CSV files
male_data.to_csv('male_users.csv', index=False)
female_data.to_csv('female_users.csv', index=False)
# unknown_data.to_csv('unknown_users.csv', index=False)

print("Male and female users have been saved to 'male_users.csv' and 'female_users.csv'.")
