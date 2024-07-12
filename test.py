import requests
from bs4 import BeautifulSoup
import pandas as pd

url = f'https://www.nba.com/stats'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

Top5Scorers = soup.find_all('a', class_='Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL')
names = []

for person in Top5Scorers:
    names.append(person.text)

titles = soup.find_all('h2', class_='LeaderBoardCard_lbcTitle___WI9J')

awardTitles = []

for title in titles:
    awardTitles.append(title.text)

awardTitles = awardTitles[0:9]

p = 0

while p < 33:
    names.pop()
    p += 1

k=0
i = 0
m = 0

long_text = ''

topScorersPoints = []
topScorers = []

topReboundersPoints = []
topRebounders = []

topAssistersPoints = []
topAssisters = []

topBlockersPoints = []
topBlockers = []

topStealersPoints = []
topStealers = []

topTurnoverPoints = []
topTurnovers = []

topThreePoints = []
topThrees = []

topFreePoints = []
topFreeThrowers = []

FantasyPoints = []
FantasyWinners = []

topPoints = [topScorersPoints, topReboundersPoints, topAssistersPoints, topBlockersPoints, topStealersPoints, topTurnoverPoints, topThreePoints, topFreePoints, FantasyPoints]
top5PlayersList = [topScorers, topRebounders, topAssisters, topBlockers, topStealers, topTurnovers, topThrees, topFreeThrowers, FantasyWinners]

while k < len(awardTitles):
    while i < 10:
        top5PlayersList[k].append(names[m])
        topPoints[k].append(names[m+1])
        i += 2
        m += 2
    k += 1
    i = 0

dict = {'Name': topScorers, 'Score': topScorersPoints}

df = pd.DataFrame(dict)

df.to_csv('topScorers.csv')

dict2 = {'Name': topRebounders, 'Score': topReboundersPoints}

df = pd.DataFrame(dict2)

df.to_csv('topRebounders.csv')

dict3 = {'Name': topAssisters, 'Score': topAssistersPoints}

df = pd.DataFrame(dict3)

df.to_csv('topAssisters.csv')

dict4 = {'Name': topBlockers, 'Score': topBlockersPoints}

df = pd.DataFrame(dict4)

df.to_csv('topBlockers.csv')

dict5 = {'Name': topStealers, 'Score': topStealersPoints}

df = pd.DataFrame(dict5)

df.to_csv('topStealers.csv')

dict6 = {'Name': topTurnovers, 'Score': topTurnoverPoints}

df = pd.DataFrame(dict6)

df.to_csv('topTurnovers.csv')

dict7 = {'Name': topThreePoints, 'Score': topThrees}

df = pd.DataFrame(dict7)

df.to_csv('topThreePoints.csv')

dict8 = {'Name': topFreeThrowers, 'Score': topFreePoints}

df = pd.DataFrame(dict8)

df.to_csv('topFreeThrowers.csv')

dict9 = {'Name': FantasyWinners, 'Score': FantasyPoints}

df = pd.DataFrame(dict9)

df.to_csv('FantasyWinners.csv')