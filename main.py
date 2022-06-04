import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read dataframe
nba = pd.read_csv('nba_elo_latest.csv')

################
#Subsetting the data

#subsetting team elos starting at the conference qualifiers
nba22 = nba.loc[1238:, ["date","team1","team2","elo1_post","elo2_post"]]

#subsetting to only the top 4 teams
celticsgames = nba22[(nba22['team1'] == 'BOS') | (nba22['team2'] == 'BOS')]

heatgames = nba22[(nba22['team1'] == 'MIA') | (nba22['team2'] == 'MIA')]

warriorsgames = nba22[(nba22['team1'] == 'GSW') | (nba22['team2'] == 'GSW')]

mavericksgames = nba22[(nba22['team1'] == 'DAL') | (nba22['team2'] == 'DAL')]

#filtering so it will only show the date, and the teams elo after each playoff game. sets NaN values to 0. takes out data where the games havent happened yet (identified by having an elo of 0)

#Celtics
ct1 = celticsgames.loc[ (celticsgames["team1"] == 'BOS'), ["date", "elo1_post"]]
ct2 = celticsgames.loc[ (celticsgames["team2"] == 'BOS'), ["date", "elo2_post"]]
celtics_elo = pd.concat([ct1,ct2])
celtics_elo.fillna(0, inplace=True)
celtics_elo['elo'] = (celtics_elo['elo1_post'] + celtics_elo['elo2_post'])
celtics_elo = celtics_elo.loc[ (celtics_elo["elo"] > 0), ["date", "elo"]]
celtics_elo = celtics_elo.sort_values(by="date")

#Heat
ht1 = heatgames.loc[ (heatgames["team1"] == 'MIA'), ["date", "elo1_post"]]
ht2 = heatgames.loc[ (heatgames["team2"] == 'MIA'), ["date", "elo2_post"]]
heat_elo = pd.concat([ht1,ht2])
heat_elo.fillna(0, inplace=True)
heat_elo['elo'] = (heat_elo['elo1_post'] + heat_elo['elo2_post'])
heat_elo = heat_elo.loc[ (heat_elo["elo"] > 0), ["date", "elo"]]
heat_elo = heat_elo.sort_values(by="date")

#Warriors
wt1 = warriorsgames.loc[ (warriorsgames["team1"] == 'GSW'), ["date", "elo1_post"]]
wt2 = warriorsgames.loc[ (warriorsgames["team2"] == 'GSW'), ["date", "elo2_post"]]
warriors_elo = pd.concat([wt1,wt2])
warriors_elo.fillna(0, inplace=True)
warriors_elo['elo'] = (warriors_elo['elo1_post'] + warriors_elo['elo2_post'])
warriors_elo = warriors_elo.loc[ (warriors_elo["elo"] > 0), ["date", "elo"]]
warriors_elo = warriors_elo.sort_values(by="date")

#Mavericks
mt1 = mavericksgames.loc[ (mavericksgames["team1"] == 'DAL'), ["date", "elo1_post"]]
mt2 = mavericksgames.loc[ (mavericksgames["team2"] == 'DAL'), ["date", "elo2_post"]]
mavericks_elo = pd.concat([mt1,mt2])
mavericks_elo.fillna(0, inplace=True)
mavericks_elo['elo'] = (mavericks_elo['elo1_post'] + mavericks_elo['elo2_post'])
mavericks_elo = mavericks_elo.loc[ (mavericks_elo["elo"] > 0), ["date", "elo"]]
mavericks_elo = mavericks_elo.sort_values(by="date")

#####################
#Make the plots on figure

fig, ax = plt.subplots(2, 2, figsize=(9, 10), sharey=True)

#Celtics
ax[1, 0].plot(celtics_elo['date'],celtics_elo['elo'])
ax[1, 0].set_title('Celtics', fontsize=14, c="green")
ax[1,0].tick_params(axis='x', which='major', labelsize=5, labelcolor='black', rotation=30)

# Heat
ax[0, 0].plot(heat_elo['date'],heat_elo['elo'])
ax[0, 0].set_title('Heat', fontsize=14, c="red")
ax[0,0].tick_params(axis='x', which='major', labelsize=5, labelcolor='black', rotation=30)

#Warriors
ax[1, 1].plot(warriors_elo['date'],warriors_elo['elo'])
ax[1, 1].set_title('Warriors', fontsize=14,c="blue")
ax[1,1].tick_params(axis='x', which='major', labelsize=5, labelcolor='black', rotation=30)

#Mavericks
ax[0, 1].plot(mavericks_elo['date'],mavericks_elo['elo'])
ax[0, 1].set_title('Mavericks', fontsize=14, c="navy")
ax[0,1].tick_params(axis='x', which='major', labelsize=5, labelcolor='gray', rotation=30)

fig.suptitle('NBA 2022 Playoffs Team ELOs', ha='center', fontsize=18)
fig.text(0.5, 0.02, 'Game Date', ha='center', fontsize=18)
fig.text(0.04, 0.5, 'ELO Score', va='center', rotation='vertical', fontsize=18)

fig.savefig('nba22elo.png')
fig.show()

########################