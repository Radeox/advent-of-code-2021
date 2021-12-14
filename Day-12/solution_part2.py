from os import sep


class Graph:
    def __init__(self, filename):
        self.nodes = {}
        self.read_input(filename)
        self.cleanup_edges()

    def __str__(self):
        return "".join(f"{node} -> {self.nodes[node]}\n" for node in self.nodes)

    def read_input(self, filename):
        with open(filename) as f:
            for line in f.readlines():
                line = line.strip()
                node1, node2 = line.split('-')
                self.add_edge(node1, node2)

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = []

    def add_edge(self, node1, node2):
        # Add nodes to graph if they don't exist
        self.add_node(node1)
        self.add_node(node2)

        self.nodes[node1].append(node2)
        self.nodes[node2].append(node1)

    def cleanup_edges(self):
        for node in self.nodes:
            for edge in self.nodes[node]:
                if edge == 'start':
                    self.nodes[node].remove(edge)

    def search_all_paths(self, start_node, end_node):
        self.__visited = []
        self.__current_path = []
        self.__paths = []
        self.__dfs(start_node, end_node)
        return self.__paths

    def __dfs(self, start_node, end_node):
        if start_node in self.__visited:
            # Check if we already visited a small cave
            extra_visit = not any(
                edge.islower() and self.__visited.count(edge) > 1
                for edge in self.__visited
            )

            if not start_node.islower() or not extra_visit:
                return

        # Add only small caves (lowercase) to visited
        if start_node.islower():
            self.__visited.append(start_node)

        # Add start node to path
        self.__current_path.append(start_node)

        # If start node is end node, add path to paths
        if start_node == end_node:
            self.__paths.append(self.__current_path.copy())
            self.__current_path.pop()

            if start_node in self.__visited:
                self.__visited.remove(start_node)
            return

        # Recursively search all paths
        for neighbor in self.nodes[start_node]:
            self.__dfs(neighbor, end_node)

        if start_node in self.__visited:
            self.__visited.remove(start_node)

        self.__current_path.pop()


def main():
    cave_system = Graph('input.txt')
    print(f"Solution: {len(cave_system.search_all_paths('start', 'end'))}")


if __name__ == "__main__":
    main()
