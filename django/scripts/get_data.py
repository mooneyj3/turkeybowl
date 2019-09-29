#Script for collecting data from NFL API
import requests
import json
response = requests.get('http://www.nfl.com/liveupdate/game-center/2019092200/2019092200_gtd.json')
game_date = "2019092200"
json_data = response.json()
out_dict = {
    "away_team": {},
    "home_team": {},

}
#two "##" means it works, easier to test when commenting out the code.



#outdicts for defense
##out_dict["home_team"]["defenses"] = json_data[game_date]["home"]["stats"]["defense"]
##out_dict["away_team"]["defenses"] = json_data[game_date]["away"]["stats"]["defense"]

#outdicts for fumbles
##out_dict["home_team"]["fumbles"] = json_data[game_date]["home"]["stats"]["fumbles"]
##out_dict["away_team"]["fumbles"] = json_data[game_date]["away"]["stats"]["fumbles"]

#outdicts for games-- Not sure what this is supposed to be

#outdicts for Kick Returns
##out_dict["home_team"]["kickret"] = json_data[game_date]["home"]["stats"]["kickret"]
##out_dict["away_team"]["kickret"] = json_data[game_date]["away"]["stats"]["kickret"]

#outdicts for Kickings
##out_dict["home_team"]["kickings"] = json_data[game_date]["home"]["stats"]["kicking"]
##out_dict["away_team"]["kickings"] = json_data[game_date]["away"]["stats"]["kicking"]

#outdicts for Passings
##out_dict["home_team"]["Passings"] = json_data[game_date]["home"]["stats"]["passing"]
##out_dict["away_team"]["Passings"] = json_data[game_date]["away"]["stats"]["passing"]

#outdicts for Player Stats... Not sure what this is supposed to be?

#outdicts for Players
##out_dict["home_team"]["kicking"] = json_data[game_date]["home"]["players"]
##out_dict["away_team"]["kicking"] = json_data[game_date]["away"]["players"]

#outdicts for puntings
##out_dict["home_team"]["puntings"] = json_data[game_date]["home"]["stats"]["punting"]
##out_dict["away_team"]["puntings"] = json_data[game_date]["away"]["stats"]["punting"]

#outdicts for Receivings
##out_dict["home_team"]["Recievings"] = json_data[game_date]["home"]["stats"]["receiving"]
##out_dict["away_team"]["Recievings"] = json_data[game_date]["away"]["stats"]["receiving"]

#outdicts for Rushings
##out_dict["home_team"]["Rushings"] = json_data[game_date]["home"]["stats"]["rushing"]
##out_dict["away_team"]["Rushings"] = json_data[game_date]["away"]["stats"]["rushing"]

#outdicts for Team performances
##out_dict["home_team"]["Team performances"] = json_data[game_date]["home"]["score"]
##out_dict["away_team"]["Team performances"] = json_data[game_date]["away"]["score"]

#outdicts for Team Stats
##out_dict["home_team"]["Team stat"] = json_data[game_date]["home"]["stats"]["team"]
##out_dict["away_team"]["Team stat"] = json_data[game_date]["away"]["stats"]["team"]

#outdicts for Teams
##out_dict["home_team"]["Teams"] = json_data[game_date]["home"]["abbr"]
##out_dict["away_team"]["Teams"] = json_data[game_date]["away"]["abbr"]


