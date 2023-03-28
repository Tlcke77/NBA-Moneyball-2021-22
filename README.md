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

In this project, I in order to identify undervalued basketball players I chose to use the "Real Plus-Minus" (RPM) system, which was developed by ESPN's analytics team. RPM is a proprietary metric that attempts to measure a player's overall impact on his team's performance, taking into account both offensive and defensive contributions, as well as other factors such as player usage rate and the quality of his teammates. RPM is calculated using a combination of play-by-play data and box score statistics, and is expressed in terms of "plus-minus" points per 100 possessions. The formula being RPM = 0.5 * (ORPM + DRPM) * (MP / 48) Where: Where:

    ORPM is the player's offensive real plus-minus
    DRPM is the player's defensive real plus-minus
    MP is the player's total minutes played


