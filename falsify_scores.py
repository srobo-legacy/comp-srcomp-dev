import argparse
from pathlib import Path
from collections import defaultdict
from sr.comp.comp import SRComp
import random
import yaml

parser = argparse.ArgumentParser(description='falsify scores for matches')
parser.add_argument('compstate', type=Path,
                    help='competition state repository')
parser.add_argument('first', type=int,
                    help='first match ID to falsify')
parser.add_argument('last', type=int,
                    help='last match ID to falsify')
args = parser.parse_args()

competition = SRComp(str(args.compstate))

SKILL_LEVELS = defaultdict(lambda: 0.5)

def update_skill_table(match):
    learning_rate = 0.1
    try:
        points = competition.scores.league.ranked_points[match.arena, match.num]
    except KeyError:
        return
    for team, point_assignment in points.items():
        factor = (point_assignment - 4) / 4
        SKILL_LEVELS[team] *= 1 + (factor * learning_rate)

# Compute approximate skill levels for all teams
for match_slot in competition.schedule.matches:
    for match in match_slot.values():
        update_skill_table(match)

def falsify(match):
    print("Falsifying results for match {} in arena {}".format(match.num, match.arena))
    path = args.compstate / match.type.value / match.arena / '{0:03}.yaml'.format(match.num)
    try:
        path.parent.mkdir(parents=True)
    except FileExistsError:
        pass
    teams = {tla: {'flags': 0,
                   'zone': n,
                   'present': (0.7*random.random()) < SKILL_LEVELS[tla]}
               for n, tla in enumerate(match.teams)
                 if tla is not None}
    for flag in range(5):
        order = list(match.teams)
        random.shuffle(order)
        for team in order:
            if team is None:
                continue
            if (random.random() * 1.3) < SKILL_LEVELS[team]:
                teams[team]['flags'] += 1
                break
    data = {'arena_id': match.arena,
            'match_number': match.num,
            'teams': teams}
    with path.open('w') as f:
        yaml.dump(data, f, default_flow_style=False)

for match_id in range(args.first, args.last + 1):
    for match in competition.schedule.matches[match_id].values():
        falsify(match)

