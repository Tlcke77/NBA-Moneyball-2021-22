from unidecode import unidecode
import pandas as pd

# Load the CSV file into a data frame
dfstat = pd.read_csv('NBA Stats 2021-22.csv')
# Drop any entries that have null values besides the "3p%" column
dfstat = dfstat.dropna(subset=[col for col in dfstat.columns if col != '3P%'])
# Drop the first column ("Rank") of the dataframe
dfstat = dfstat.drop(dfstat.columns[0], axis=1)
# Remove special characters from the player names
dfstat['Player'] = dfstat['Player'].apply(unidecode)
# Remove suffixes from the player names
dfstat['Player'] = dfstat['Player'].str.replace('III$|Jr.$|Sr.$|II$', '', regex=True)
# Remove periods from the ends of player names
dfstat['Player'] = dfstat['Player'].str.rstrip('.')

# Load the CSV file into a data frame
dfsal = pd.read_csv('nba_salaries.csv')
# Remove special characters from the player names
dfsal['Player'] = dfsal['Player'].apply(unidecode)
# Remove suffixes from the player names
dfsal['Player'] = dfsal['Player'].str.replace('III$|Jr.$|Sr.$|II$', '', regex=True)
# Remove periods from the ends of player names
dfsal['Player'] = dfsal['Player'].str.rstrip('.')

# Merge NBA Stats with Salareis
merged_df = pd.merge(dfstat, dfsal, on='Player', how='inner')


# Save the modified dataframe to the original CSV file (overwriting it)
merged_df.to_csv('Final NBA 2021-22.csv', index=False)






