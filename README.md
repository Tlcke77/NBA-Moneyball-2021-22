# NBA Moneyball
![NBArdme](https://user-images.githubusercontent.com/83333358/227303726-1d76941f-0bc2-46e1-ab49-68d693e66896.jpg)

## Intorduction
The objective of this project was to identify undervalued NBA players from the 2021-22 season and assemble a team composed of such players. The project subsequently employs machine learning algorithms to predict the number of team wins based on relevant metrics, which will be elaborated upon in later sections

## Data
### 2021-22 Player Statistics
I got this data set from [Basketball Reference 2021-22 player statsitcs](https://www.basketball-reference.com/leagues/NBA_2022_per_game.html) using their "Share & Export" function that allows you to export the data to a csv file. I did this for both the "Per Game" and "Advanced" statsitcs pages. As well as I there is an option to "Hide Partail Rows" that hides the multiple rows of a player statsitcs. This occurs when a player is either traded or realsed and signed by a new team during the NBA season. Then manualy combing the two datasets into one using Excel, givng me one collective dataset with both "Per Game" and "Advanced" statsitcs.

### 2021-22 Player Salaries
I got this data from web scrapping the [ESPN NBA Player Salaries 2021-2022](http://www.espn.com/nba/salaries/_/year/2022) using python. You can find the code I used for this here. It should noted that I could never figure out a way to elminate the code from printing "NAME" and "SALARY" as new data when trying the different pages of the data source. So due to this I had to manually delete the duplicate values in the Excel file.

### Cleaning and Merging the Datasets
In order to properly join these two dataset it required some cleaning up at first.

First, I deleted the players who had null values in their statistics, except for the "3P%" column. This mainly occurred for players who play the center position ("C"). Since a team requires a center, I did not want to eliminate centers from this project. Therefore, I chose to allow players with null values in this particular column.

Then I decided to clean up the players statisitics database first. My first move was to delete the first column of the database as it would be of no use as it's ranks Basketball Reference ranking of the players and would be no use for this project.

Next I had to simply the players names in order to get them to merge together the two datasets as I would be using the player names as the unique identifer to link their statsitcs to the salary they recived in the 2021-22 season.
 - Removed special characters from names (Ex: Dragić -> Dragic)
 - Removed "III", "II", "Jr", "Sr", and "." the ends of player names

Then after merging these two databases togehter I was left with 440 rows or players to analyze.

## Looking For Undervalued Players
Now after making our dataset to our liking we get to finding players that me deem "undervauled" and building our roster. To start we have to choose what metrics I deem are the most important to me such as 

In this project, I utilized metrics and linear regression modeling to identify undervalued basketball players. By analyzing the dataset containg a range of player statistics, I developed a model that took into account the TS%, WS, PER, and BPM features.
- True Shooting Percentage (TS%): This is a measure of shooting efficiency that takes into account two-point field goals, three-point field goals, and free throws. It is calculated as total points divided by total field goal attempts.
- WS (Win Shares): This is a statistic that attempts to measure a player's overall contribution to winning games. It takes into account offensive and defensive performance as well as playing time.
- Player Efficiency Rating (PER): This is a rating of a player's overall per-minute productivity. It takes into account a range of statistics, including points, rebounds, assists, steals, and blocks.
- Box Plus/Minus (BPM): This is a measure of a player's overall impact on the game, taking into account both offensive and defensive performance as well as playing time. It is expressed as the number of points per 100 possessions above or below the league average that a player contributes when on the court.
