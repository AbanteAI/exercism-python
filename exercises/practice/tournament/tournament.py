def tally(rows):
    teams = {}
    for row in rows:
        team1, team2, result = row.split(";")
        if team1 not in teams:
            teams[team1] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
        if team2 not in teams:
            teams[team2] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}

        teams[team1]["MP"] += 1
        teams[team2]["MP"] += 1

        if result == "win":
            teams[team1]["W"] += 1
            teams[team2]["L"] += 1
            teams[team1]["P"] += 3
        elif result == "loss":
            teams[team1]["L"] += 1
            teams[team2]["W"] += 1
            teams[team2]["P"] += 3
        else:  # draw
            teams[team1]["D"] += 1
            teams[team2]["D"] += 1
            teams[team1]["P"] += 1
            teams[team2]["P"] += 1

    sorted_teams = sorted(teams.items(), key=lambda x: (-x[1]["P"], x[0]))
header = ["Team                           | MP |  W |  D |  L |  P"]
table = [
    f"{team.ljust(31)}| {str(stats['MP']).rjust(2)} | {str(stats['W']).rjust(2)} | {str(stats['D']).rjust(2)} | {str(stats['L']).rjust(2)} | {str(stats['P']).rjust(2)}"
    for team, stats in sorted_teams
]
return header + table