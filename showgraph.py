import networkx as nx
import matplotlib.pyplot as plt
import network
def show_graph(ver_list):
    G = nx.Graph()
    for i in range(len(ver_list)):
        G.add_node(i)

    for i in range(len(ver_list)):
        conlist=ver_list[i]['connected']
        for j in conlist:
            G.add_edge(i,j)
    nx.draw(G)
    plt.show()


ver_list = network.gen_graph(4)
print(ver_list)
show_graph(ver_list)
