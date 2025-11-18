import heapq
from functools import total_ordering


@total_ordering
class SpecialSorted:

    def __init__(self, element, value):
        self.element = element
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value


class PriorityQueue:

    def __init__(self, sortkey=lambda x: x):
        self.content = []
        self.sortkey = sortkey

    def add(self, item):
        heapq.heappush(self.content, SpecialSorted(item, self.sortkey(item)))

    def peek(self):
        return self.content[0].element if self.content else None

    def poll(
            self):  # haalt element met de hoogste prioriteit (de laagste sortkey) uit de wachtrij en verwijdert het uit de queue.
        return heapq.heappop(self.content).element if len(self.content) > 0 else None

    def is_empty(self):
        return len(self.content) == 0

    def __str__(self):
        return str(heapq.nsmallest(len(self.content), [item.element for item in self.content]))


def shortest_path(graph, src, dest):
    nodes = {src: 0}
    vorige = {}
    bezocht = set()

    #sortkey = distance, want prioriteit alleen afh van distance, item=(distance,node)
    pq = PriorityQueue(sortkey=lambda item: item[0])
    pq.add((0, src))

    while not pq.is_empty(): #'oneindige' lus met inwendige stopconditie
        distance, node = pq.poll()

        if node in bezocht:
            continue
        bezocht.add(node)

        if node == dest:
            pad = [dest]
            current = dest
            while current in vorige:
                current = vorige[current]
                pad.append(current)
            pad.reverse()
            return pad

        for neighbour in graph.get_neighbours(node):
            edges = graph.get_edges(node, neighbour)
            if not edges:
                continue

            weight = min(edge.weight for edge in edges) #multigraaf = (mmeerdere)(unidirectionele)knopen
            afstand = distance + weight

            if neighbour not in nodes or afstand < nodes[neighbour]:
                nodes[neighbour] = afstand
                vorige[neighbour] = node
                pq.add((afstand, neighbour))

    # geen pad gevonden
    return None