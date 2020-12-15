import os
import json


for seasondir in ['season0']:

    seasonfile = os.path.join(seasondir, 'season.json')
    flatseasonfile = os.path.join(seasondir, 'flatseason.json')

    print("***************************")
    print(f"Now flattening {seasonfile}")

    with open(seasonfile, 'r') as f:
        season = json.load(f)

    flat_season = []
    for iday, day in enumerate(season):
        games = day
        for igame, game in enumerate(games):

            flat_season.append(game)

    with open(flatseasonfile, 'w') as f:
        json.dump(flat_season, f, indent=4)

    
    ################################################


    postseasonfile = os.path.join(seasondir, 'postseason.json')
    flatpostseasonfile = os.path.join(seasondir, 'flatpostseason.json')

    print("***************************")
    print(f"Now flattening {postseasonfile}")

    with open(postseasonfile, 'r') as f:
        postseason = json.load(f)

    flat_postseason = []
    for series in postseason:
        miniseason = postseason[series]
        for iday, day in enumerate(miniseason):
            games = day
            for igame, game in enumerate(games):
                game['series'] = series
                flat_postseason.append(game)

    with open(flatpostseasonfile, 'w') as f:
        json.dump(flat_postseason, f, indent=4)

