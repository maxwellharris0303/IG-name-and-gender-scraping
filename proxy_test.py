import pandas as pd

# Step 1: Read the content of the two text files
with open('usernames.txt', 'r', encoding='utf-8') as f:
    usernames = f.read().splitlines()

with open('results.txt', 'r', encoding='utf-8') as f:
    names = f.read().splitlines()

# Step 2: Create a DataFrame using the data
df = pd.DataFrame({
    'username': usernames,
    'name': names[:len(usernames)]  # Adjusting if name list is longer than usernames
})

# Step 3: Save the DataFrame to a CSV file
df.to_csv('username_name_combined.csv', index=False)

print("CSV file created successfully!")
