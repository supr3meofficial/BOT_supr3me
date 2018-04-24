import hltv

#if "Pro League" in hltv.get_matches()[0]:
#    print(True)

match1_date = str(hltv.get_matches()[0]['date'])[2:-1]
match1_time = str(hltv.get_matches()[0]['time'])[2:-1]
match1_event = str(hltv.get_matches()[0]['event'])[2:-1]
match1_team1 = str(hltv.get_matches()[0]['team1'])[2:-1]
match1_team2 = str(hltv.get_matches()[0]['team2'])[2:-1]