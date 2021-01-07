"""
최단경로 찾기
"""
import copy

departure = 'home'
destination = 'school'

landscape = {
    'home': {'hair_shop': 5, 'super_market': 10, 'english_academy': 9},
    'hair_shop': {'home': 5, 'super_market': 3, 'bank': 11},
    'super_market': {'hair_shop': 3, 'home': 10, 'english_academy': 7, 'restaurant': 3},
    'english_academy': {'home': 9, 'super_market': 7, 'school': 12},
    'restaurant': {'super_market': 3, 'bank': 4},
    'bank': {'hair_shop': 11, 'restaurant': 4, 'english_academy': 7, 'school': 2},
    'school': {'bank': 2, 'english_academy': 12}
}

routing = dict()
for place in landscape.keys():
    routing[place] = {'shortest_distance': 0, 'route': [], 'visited': 0}


def visit_place(visit):
    routing[visit]['visited'] = 1
    for to_go, between_distance in landscape[visit].items():
        to_distance = routing[visit]['shortest_distance'] + between_distance
        if (routing[to_go]['shortest_distance'] >= to_distance) or not routing[to_go]['route']:
            routing[to_go]['shortest_distance'] = to_distance
            routing[to_go]['route'] = copy.deepcopy(routing[visit]['route'])
            routing[to_go]['route'].append(visit)


visit_place(departure)

while 1:
    minimum_distance = max(routing.values(), key=lambda x: x['shortest_distance'])['shortest_distance']
    to_visit = ''
    for name, search in routing.items():
        if 0 < search['shortest_distance'] <= minimum_distance and not search['visited']:
            minimum_distance = search['shortest_distance']
            to_visit = name
    if to_visit == '':
        break
    visit_place(to_visit)

print(routing)
print('route: ', routing[destination]['route'])
print('shortest_distance: ', routing[destination]['shortest_distance'])