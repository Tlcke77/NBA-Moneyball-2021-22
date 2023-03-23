# NBA Moneyball
![NBArdme](https://user-images.githubusercontent.com/83333358/227303726-1d76941f-0bc2-46e1-ab49-68d693e66896.jpg)

## Intorduction
The objective of this project was to identify undervalued NBA players from the 2021-22 season and assemble a team composed of such players. The project subsequently employs machine learning algorithms to predict the number of team wins based on relevant metrics, which will be elaborated upon in later sections

## Data
### 2021-22 Player Statistics
I got this data set from [Basketball Reference 2021-22 player statsitcs](https://www.basketball-reference.com/leagues/NBA_2022_per_game.html) using their "Share & Export" function that allows you to export the data to a csv file. I did this for both the "Per Game" and "Advanced" statsitcs pages. As well as I there is an option to "Hide Partail Rows" that hides the multiple rows of a player statsitcs. This occurs when a player is either traded or realsed and signed by a new team during the NBA season. Then manualy combing the two datasets into one using Excel, givng me one collective dataset with both "Per Game" and "Advanced" statsitcs.

### 2021-22 Player Salaries
I got this data from web scrapping the [ESPN NBA Player Salaries 2021-2022](http://www.espn.com/nba/salaries/_/year/2022) using python. You can find the code I used for this here.

### Cleaning and Merging the Datasets
In order to properly join these two dataset it required some cleaning up at first.

I first decided to clean up the players statisitics database first. My first move was to delete the first column of the database as it would be of no use as it's ranks Basketball Reference ranking of the players and would be no use for this project.

Next I had to simply the players names in order to get them to merge together the two datasets as I would be using the player names as the unique identifer to link their statsitcs to the salary they recived in the 2021-22 season.
 - Removed special characters from names (Ex: Dragić -> Dragic)
 - Removed "III", "II", "Jr", "Sr", and "." the ends of player names

