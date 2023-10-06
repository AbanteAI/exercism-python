def tally(rows):
    table = {}
    for row in rows:
        team1, team2, result = row.split(';')
        table.setdefault(team1, {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0})
        table.setdefault(team2, {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0})
        table[team1]['MP'] += 1
        table[team2]['MP'] += 1
        if result == 'win':
            table[team1]['W'] += 1
            table[team1]['P'] += 3
            table[team2]['L'] += 1
        elif result == 'loss':
            table[team1]['L'] += 1
            table[team2]['W'] += 1
            table[team2]['P'] += 3
        else:
            table[team1]['D'] += 1
            table[team1]['P'] += 1
            table[team2]['D'] += 1
            table[team2]['P'] += 1

    sorted_table = sorted(table.items(), key=lambda x: (-x[1]['P'], x[0]))
    result.append(
        f"{team.ljust(30)} | {stats['MP']} | {stats['W']} | {stats['D']} | {stats['L']} | {stats['P']:2}"
    )

