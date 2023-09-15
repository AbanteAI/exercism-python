def tally(rows):
    team_results = {}
    for row in rows:
        team1, team2, outcome = row.split(";")
        update_match_results(team_results, team1, team2, outcome)
    
    team_stats = calculate_team_stats(team_results)
    sorted_teams = sort_teams(team_stats)
    table = generate_table(sorted_teams)
    
    return table
def update_match_results(team_results, team1, team2, outcome):
    # Update team1's match results
    if team1 not in team_results:
        team_results[team1] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
    
    team_results[team1]["MP"] += 1
    if outcome == "win":
        team_results[team1]["W"] += 1
        team_results[team1]["P"] += 3
    elif outcome == "draw":
        team_results[team1]["D"] += 1
        team_results[team1]["P"] += 1
    else:
        team_results[team1]["L"] += 1

    # Update team2's match results
    if team2 not in team_results:
        team_results[team2] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
    
    team_results[team2]["MP"] += 1
    if outcome == "win":
        team_results[team2]["L"] += 1
    elif outcome == "draw":
        team_results[team2]["D"] += 1
        team_results[team2]["P"] += 1
    else:
        team_results[team2]["W"] += 1
        team_results[team2]["P"] += 3

def calculate_team_stats(team_results):
    team_stats = []
    for team, results in team_results.items():
        team_stats.append((team, results["MP"], results["W"], results["D"], results["L"], results["P"]))
    
    return team_stats

def sort_teams(team_stats):
    sorted_teams = sorted(team_stats, key=lambda x: (-x[5], x[0]))
    return sorted_teams

def generate_table(sorted_teams):
    table = "Team                           | MP |  W |  D |  L |  P\n"
    for team_stats in sorted_teams:
        team = team_stats[0]
        mp = team_stats[1]
        w = team_stats[2]
        d = team_stats[3]
        l = team_stats[4]
        p = team_stats[5]
        table += f"{team.ljust(30)} | {mp} | {w} | {d} | {l} | {p}\n"
    
    return table