def tally(rows):
    # Define a dictionary to hold team stats
    teams_stats = {}

    # Function to update team stats
    def update_stats(team, result):
        if team not in teams_stats:
            teams_stats[team] = {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0}
        teams_stats[team]['MP'] += 1
        if result == 'win':
            teams_stats[team]['W'] += 1
            teams_stats[team]['P'] += 3
        elif result == 'draw':
            teams_stats[team]['D'] += 1
            teams_stats[team]['P'] += 1
        elif result == 'loss':
            teams_stats[team]['L'] += 1

    # Process each match result
    for row in rows:
        team1, team2, result = row.split(';')
        if result == 'win':
            update_stats(team1, 'win')
            update_stats(team2, 'loss')
        elif result == 'draw':
            update_stats(team1, 'draw')
            update_stats(team2, 'draw')
        elif result == 'loss':
            update_stats(team1, 'loss')
            update_stats(team2, 'win')

    # Sort the teams by points and then alphabetically
    sorted_teams = sorted(teams_stats.items(), key=lambda item: (-item[1]['P'], item[0]))

    # Format the output
    # Format the output as a list of strings
    output = ["Team                           | MP |  W |  D |  L |  P"]
    for team, stats in sorted_teams:
        output.append(f"{team:<31}|  {stats['MP']:>2} |  {stats['W']:>2} |  {stats['D']:>2} |  {stats['L']:>2} |  {stats['P']:>2}")

    return output
