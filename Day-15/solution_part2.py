from collections import defaultdict


def read_input(filename):
    rv = []
    with open(filename) as f:
        for line in f.readlines():
            rv.append([int(d) for d in line.strip()])
    return rv


def get_neighbors(node, distance_matrix):
    max_x = len(distance_matrix)
    max_y = len(distance_matrix[0])
    x, y = node

    rv = []

    if x > 0:
        rv.append((x-1, y))
    if x < max_y - 1:
        rv.append((x+1, y))
    if y > 0:
        rv.append((x, y-1))
    if y < max_x - 1:
        rv.append((x, y+1))
    return rv

def get_full_map(distance_matrix, tiles):
    tmp = []

    for row in distance_matrix:
        new_row = []

        for i in range(tiles):
            for distance in row:
                if (distance + i) > 9:
                    new_row.append((distance + i) % 9)
                else:
                    new_row.append(distance + i)
        tmp.append(new_row) 
    
    map = tmp.copy()
    for i in range(1, tiles):
        for row in tmp:
            new_row = []
            for distance in row:
                if (distance + i) > 9:
                    new_row.append((distance + i) % 9)
                else:
                    new_row.append(distance + i)
            map.append(new_row)
    
    return map



def dijkstra(distance_matrix, start):
    visited = {start: 0}
    path = defaultdict(list)
    nodes = set()

    for y, row in enumerate(distance_matrix):
        for x, node in enumerate(row):
            nodes.add((x, y))

    while nodes != set():
        minNode = None

        for node in nodes:
            if node in visited and (
                minNode is None or visited[node] < visited[minNode]
            ):
                minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        current_distance = visited[minNode]

        for edge in get_neighbors(minNode, distance_matrix):
            distance = current_distance + distance_matrix[edge[0]][edge[1]]
            if edge not in visited or distance < visited[edge]:
                visited[edge] = distance
                path[edge].append(minNode)

    return path


def main():
    distance_matrix = read_input("input.txt")
    distance_matrix = get_full_map(distance_matrix, 5)
    max_x = len(distance_matrix) - 1
    max_y = len(distance_matrix[0]) - 1
    
    # This solution is not optimal, but it works :D
    path = dijkstra(distance_matrix, (0, 0))

    position = (max_x, max_y)
    total_risk = 0
    while position != (0, 0):
        total_risk += distance_matrix[position[0]][position[1]]
        position = path[position][0]
    print(total_risk)


if __name__ == '__main__':
    main()
