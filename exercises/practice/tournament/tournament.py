def tally(rows):
    # Define a dictionary to hold team stats
    teams = {}

    # Function to add or update team stats
    def update_team_stats(team, result):
        if team not in teams:
            teams[team] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
        teams[team]["MP"] += 1
        if result == "win":
            teams[team]["W"] += 1
            teams[team]["P"] += 3
        elif result == "draw":
            teams[team]["D"] += 1
            teams[team]["P"] += 1
        elif result == "loss":
            teams[team]["L"] += 1

    # Process each row of input
    for row in rows:
        team1, team2, outcome = row.split(';')
        if outcome == "win":
            update_team_stats(team1, "win")
            update_team_stats(team2, "loss")
        elif outcome == "draw":
            update_team_stats(team1, "draw")
            update_team_stats(team2, "draw")
        elif outcome == "loss":
            update_team_stats(team1, "loss")
            update_team_stats(team2, "win")

    # Sort the teams first by points, then by name
    sorted_teams = sorted(teams.items(), key=lambda item: (-item[1]["P"], item[0]))

    # Create the header for the table
    header = "Team                           | MP |  W |  D |  L |  P\n"

    # Format the sorted team stats into the table
    table = [header]
    for team, stats in sorted_teams:
        row = f"{team:<31}|  {stats['MP']:>2} |  {stats['W']:>2} |  {stats['D']:>2} |  {stats['L']:>2} |  {stats['P']:>2}"
        table.append(row)

    return table
