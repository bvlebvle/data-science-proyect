import pandas as pd

# load data
f15 = pd.read_csv('players_15.csv')
f16 = pd.read_csv('players_16.csv')
f17 = pd.read_csv('players_17.csv')
f18 = pd.read_csv('players_18.csv')
f19 = pd.read_csv('players_19.csv')
f20 = pd.read_csv('players_20.csv')
f21 = pd.read_csv('players_21.csv')
f22 = pd.read_csv('players_22.csv')


# print each line from f15
for index, row in f15.iterrows():

    sofifa_id = f15.at[index, 'sofifa_id']
    long_name = f15.at[index, 'long_name']
    player_15_overall = f15.at[index, 'overall']
    player_15_potencial = f15.at[index, 'potential']

    # fifa 16
    player_16 = f16[f16['sofifa_id'] == sofifa_id]

    player_16_overall = -1
    player_16_potencial = -1
    if player_16.empty:
        # print("Player not found in 16")
        continue
    else:
        player_16_overall = player_16['overall'].values[0]
        player_16_potencial = player_16['potential'].values[0]

    # fifa 17
    player_17 = f17[f17['sofifa_id'] == sofifa_id]

    player_17_overall = -1
    player_17_potencial = -1
    if player_17.empty:
        # print("Player not found in 17")
        continue
    else:
        player_17_overall = player_17['overall'].values[0]
        player_17_potencial = player_17['potential'].values[0]

    # fifa 18
    player_18 = f18[f18['sofifa_id'] == sofifa_id]

    player_18_overall = -1
    player_18_potencial = -1
    if player_18.empty:
        # print("Player not found in 18")
        continue
    else:
        player_18_overall = player_18['overall'].values[0]
        player_18_potencial = player_18['potential'].values[0]

    # fifa 19
    player_19 = f19[f19['sofifa_id'] == sofifa_id]

    player_19_overall = -1
    player_19_potencial = -1
    if player_19.empty:
        # print("Player not found in 19")
        continue
    else:
        player_19_overall = player_19['overall'].values[0]
        player_19_potencial = player_19['potential'].values[0]

    # fifa 20
    player_20 = f20[f20['sofifa_id'] == sofifa_id]

    player_20_overall = -1
    player_20_potencial = -1
    if player_20.empty:
        # print("Player not found in 20")
        continue
    else:
        player_20_overall = player_20['overall'].values[0]
        player_20_potencial = player_20['potential'].values[0]

        # fifa 21
    player_21 = f21[f21['sofifa_id'] == sofifa_id]

    player_21_overall = -1
    player_21_potencial = -1
    if player_21.empty:
        # print("Player not found in 21")
        continue
    else:
        player_21_overall = player_21['overall'].values[0]
        player_21_potencial = player_21['potential'].values[0]

    # fifa 22
    player_22 = f22[f22['sofifa_id'] == sofifa_id]

    player_22_overall = -1
    player_22_potencial = -1
    if player_22.empty:
        # print("Player not found in 22")
        continue
    else:
        player_22_overall = player_22['overall'].values[0]
        player_22_potencial = player_22['potential'].values[0]

        # AVG OVERALL

    overalls = [player_15_overall, player_16_overall, player_17_overall, player_18_overall,
                player_19_overall, player_20_overall, player_21_overall, player_22_overall]

    size_overalls = 0
    avg_overalls = 0

    for overall in overalls:
        if overall != -1:
            avg_overalls += overall
            size_overalls += 1
    avg_overalls = avg_overalls / size_overalls

    # AVG POTENCIAL
    potencials = [player_15_potencial, player_16_potencial, player_17_potencial, player_18_potencial,
                  player_19_potencial, player_20_potencial, player_21_potencial, player_22_potencial]

    size_potencials = 0
    avg_potencials = 0

    for potencial in potencials:
        if potencial != -1:
            avg_potencials += potencial
            size_potencials += 1
    avg_potencials = avg_potencials / size_potencials

    # print(sofifa_id, long_name, avg_overalls, avg_potencials)

    # create a new csv file with the data including name of columns
    with open('rating_players.csv', 'a') as f:
        f.write(f'{sofifa_id},{long_name},{avg_overalls},{avg_potencials}\n')
