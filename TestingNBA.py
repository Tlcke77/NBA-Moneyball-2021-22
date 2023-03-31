import pandas as pd

# Read the CSV file into a DataFrame
merged_df = pd.read_csv('Final NBA 2021-22.csv')

# Filter the data frame to only include players who played at least 15 mpg and 20 games
merged_df = merged_df[(merged_df['MP'] >= 17) & (merged_df['G'] >= 25)]

# Define the formula for calculating Value
def calculate_value(df):

    # Get the players efficiency rating
    per = df['PER']

    # Get the players offensive and defensive real plus-minus
    bpm = df['BPM']
    vorp = df['VORP']

    # Calculate the player's Value
    value = (per + bpm + vorp) / 3

    return value

# Define the formula for calculating Value per Salary
def player_salaryvalue(df):
    
    # Get the players salary
    salary = df['Salary']
    
    # Calculate the player's Value per Salary
    vps = calculate_value(df) / salary

    return vps

# Prompt the user to input a position
pos = input("Enter a position (e.g. PG, SG, SF, PF, C): ")

# Filter the DataFrame to only include players at the specified position
pos_df = merged_df[merged_df['Pos'] == pos]

# Check if the pos_df is empty
if pos_df.empty:
    print("No players found for the specified position.")
else:
    # Apply the calculate_value function to the pos_df DataFrame and add a new column for Value
    pos_df['Value'] = pos_df.apply(calculate_value, axis=1)

    # Apply the player_salaryvalue function to the pos_df DataFrame and add a new column for Value per Salary
    pos_df['Value per Salary'] = pos_df.apply(player_salaryvalue, axis=1)

    # Display the top three highest Value per Salary
    pos_df = pos_df.sort_values('Value per Salary', ascending=False).head(3)
    print(pos_df[['Player', 'Value per Salary']])
