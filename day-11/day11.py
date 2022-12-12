import sys
infile = sys.argv[1] 
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]
start_coord = None
start_coords = []
map = [[0 for _ in range(101)]  for _ in range(50)]
s = 'abcdefghijklmnopqrstuvwxyz'
start_coord = end_coord = None
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == 'S':
            map[i][j] = 0
            start_coord = (i, j)
            start_coords.append((i, j))
        elif c == 'E':
            map[i][j] = s.index('z')
            end_coord = (i, j)
        else:
            if c == 'a':
                start_coords.append((i, j))
            map[i][j] = s.index(c)

def bfs(start_coord, end_coord):
    steps = float('inf')
    queue = [(start_coord, 0)]
    visited = set()

    while queue:

        current_node, step = queue.pop(0)
        i, j = current_node
        if current_node == end_coord:
            steps = min(steps, step)
        if current_node not in visited:
            visited.add(current_node)
            for dx, dy in [(0,1) , (0, -1), (1, 0), (-1 ,0)]:

                if 0 <= (i + dx) < len(map) and 0 <= j + dy < len(map[0]):
                    if map[i + dx][j + dy] - map[i][j]  <= 1:
                        queue.append(((i + dx, j + dy), step + 1))
    return steps

print('part 1: ' + str(bfs(start_coord, end_coord)))
minimal_dist = float('inf')
for start_coord in start_coords:
    minimal_dist = min(minimal_dist, bfs(start_coord, end_coord))
print('part 2: ' + str(minimal_dist))





        



    



