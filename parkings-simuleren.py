import heapq


class PriorityQueue:
    def __init__(self):
        self.content = []

    def add(self, item):
        heapq.heappush(self.content, item)

    def peek(self):
        return self.content[0]  # Grootste priority komt automatisch eerste te staan !!!

    def poll(self):
        return heapq.heappop(self.content) if len(self.content) > 0 else None

    def is_empty(self):
        return len(self.content) == 0

    def __str__(self):
        return str(heapq.nsmallest(len(self.content), self.content))


def simuleer_parking(plaatsen, bloktijd, klanten):
    pass
    wachtrij = PriorityQueue()
    for klant in klanten:
        wachtrij.add(klant)
    tijd = [0] * plaatsen

    while not wachtrij.is_empty():
        aankomsttijd, winkellengte = wachtrij.poll()
        plaats = False
        for i in range(plaatsen):
            if tijd[i] <= aankomsttijd:
                tijd[i] = aankomsttijd + winkellengte
                plaats = True
                break
        if not plaats:
            aankomsttijd += bloktijd
            wachtrij.add((aankomsttijd, winkellengte))
    eindtijdstip = max(tijd)
    return eindtijdstip