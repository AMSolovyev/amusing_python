n = int(input())
teams = []
wins = {}
draws = {}
losts = {}


for i in range(n):
    data_list = input()
    data_list = data_list.split(';')
    if data_list[0] not in teams:
        teams.append(data_list[0])
    if data_list[2] not in teams:
        teams.append(data_list[2])
    if data_list[1] > data_list[3]:
        wins[data_list[0]] = wins.get(data_list[0], 0) + 1
        losts[data_list[2]] = losts.get(data_list[2], 0) + 1
    elif data_list[1] < data_list[3]:
        wins[data_list[2]] = wins.get(data_list[2], 0) + 1
        losts[data_list[0]] = losts.get(data_list[0], 0) + 1
    elif data_list[1] == data_list[3]:
        draws[data_list[0]] = draws.get(data_list[0], 0) + 1
        draws[data_list[2]] = draws.get(data_list[2], 0) + 1
        

for team in teams:
    win = wins.get(team, 0)
    draw = draws.get(team, 0)
    lost = losts.get(team, 0)
    play = win + draw + lost
    scores = win * 3 + draw * 1 
    print(team+ ':', play, win, draw, lost, scores) 
