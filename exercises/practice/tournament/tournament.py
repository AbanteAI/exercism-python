from collections import defaultdict

def tally(rows):
    teams = defaultdict(lambda: {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0})
    for row in rows:
        team1, team2, result = row.split(";")
        teams[team1]["MP"] += 1
        teams[team2]["MP"] += 1
        if result == "win":
            teams[team1]["W"] += 1
            teams[team1]["P"] += 3
            teams[team2]["L"] += 1
        elif result == "loss":
            teams[team2]["W"] += 1
            teams[team2]["P"] += 3
            teams[team1]["L"] += 1
        elif result == "draw":
            teams[team1]["D"] += 1
            teams[team2]["D"] += 1
            teams[team1]["P"] += 1
            teams[team2]["P"] += 1

    header = "Team                           | MP |  W |  D |  L |  P"
    table = [header]
    for team, stats in sorted(teams.items(), key=lambda x: (-x[1]["P"], x[0])):
        table.append(
            f"{team:<30} | {stats['MP']:>2} | {stats['W']:>2} | {stats['D']:>2} | {stats['L']:>2} | {stats['P']:>2}"
        )
    return table