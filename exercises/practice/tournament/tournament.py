def tally(rows):
    # Define a dictionary to hold team stats
    team_stats = {}

    # Function to add or update team stats
    def update_stats(team, result):
        if team not in team_stats:
            team_stats[team] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
        team_stats[team]["MP"] += 1
        if result == "win":
            team_stats[team]["W"] += 1
            team_stats[team]["P"] += 3
        elif result == "draw":
            team_stats[team]["D"] += 1
            team_stats[team]["P"] += 1
        elif result == "loss":
            team_stats[team]["L"] += 1

    # Process each row of match results
    for row in rows:
        team1, team2, outcome = row.split(";")
        if outcome == "win":
            update_stats(team1, "win")
            update_stats(team2, "loss")
        elif outcome == "draw":
            update_stats(team1, "draw")
            update_stats(team2, "draw")
        elif outcome == "loss":
            update_stats(team1, "loss")
            update_stats(team2, "win")

    # Sort the teams first by points, then by name
    sorted_teams = sorted(team_stats.items(), key=lambda item: (-item[1]["P"], item[0]))

    # Format the output
    # Format the output
    output = ["Team                           | MP |  W |  D |  L |  P"]
    for team, stats in sorted_teams:
        output.append(f"{team:<31}|  {stats['MP']:>2} |  {stats['W']:>2} |  {stats['D']:>2} |  {stats['L']:>2} |  {stats['P']:>2}")
    
    return output