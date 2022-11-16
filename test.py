import networkx as nx
import matplotlib.pyplot as plt
coin_count = int(input())
move_count = int(input())
moves = [int(input()) for _ in range(move_count)]
states = ['gray'] * coin_count
win_color = 'green'
lose_color = 'red'
class GraphVisualization:
    def __init__(self):
        self.visual = []
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G, node_color=states)
        plt.show()
def get_result(index):
    results = []
    destinations = []
    for i in range(move_count):
        if index-moves[i] >= 0:
            results.append(states[index-moves[i]])
            destinations.append(index-moves[i])
    if lose_color in results:
        return destinations,win_color
    return destinations,lose_color
Graph = GraphVisualization()
for i in range(coin_count):
    destinations,states[i] = get_result(i)
    for destination in destinations:
        Graph.addEdge(destination, i)
Graph.visualize()
#print(states)
