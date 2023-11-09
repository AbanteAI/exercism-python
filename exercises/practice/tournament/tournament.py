def tally(rows):
    # Define a dictionary to hold team stats
    teams = {}

    # Function to add or update team stats
    def update_team_stats(team, result):
        if team not in teams:
            teams[team] = {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0}
        teams[team]['MP'] += 1
        if result == 'win':
            teams[team]['W'] += 1
            teams[team]['P'] += 3
        elif result == 'draw':
            teams[team]['D'] += 1
            teams[team]['P'] += 1
        elif result == 'loss':
            teams[team]['L'] += 1

    # Process each row of match results
    for row in rows:
        team1, team2, outcome = row.split(';')
        if outcome == 'win':
            update_team_stats(team1, 'win')
            update_team_stats(team2, 'loss')
        elif outcome == 'loss':
            update_team_stats(team1, 'loss')
            update_team_stats(team2, 'win')
        elif outcome == 'draw':
            update_team_stats(team1, 'draw')
            update_team_stats(team2, 'draw')

    # Sort the teams by points and then alphabetically
    sorted_teams = sorted(teams.items(), key=lambda x: (-x[1]['P'], x[0]))

    # Format the output
    table = [header.strip()]
    for team, stats in sorted_teams:
        row = f"{team:<31}|  {stats['MP']} |  {stats['W']} |  {stats['D']} |  {stats['L']} |  {stats['P']}"
        table.append(row)

    return table
