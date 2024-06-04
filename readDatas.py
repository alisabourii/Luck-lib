# importing pandas package 
import pandas as pd 
  
# making data frame from csv file 
data = pd.read_csv("results.csv") 
  

TeamOneHome=data.query("home_team == 'Sheffield United' and away_team  == 'Liverpool'")
TeamTwoeHome=data.query("home_team == 'Liverpool' and away_team  == 'Sheffield United'")
# display 
print(TeamOneHome)
print(TeamTwoeHome)
