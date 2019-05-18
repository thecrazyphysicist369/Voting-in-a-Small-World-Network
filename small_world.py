import networkx as nx
import matplotlib.pyplot as plt
import random



#vertex generator generates each voter with their properties
def gen_vertex(n):
    ver_list=[]
    c=0

    for i in range(n):
        vertex = {'index': c, 			#the unique index of the voter 
                  'endurance': random.randrange(-10, 10), #the enduaring power of the voter
                  'influence': random.randint(5, 10), #the influencing power of the voter
                  'connected': [], #the small world connections between the voters
                  }
        ver_list.append(vertex)

        c+=1
    return ver_list

def gen_graph(n, k, p):
   verlist = gen_vertex(n)
   G = nx.watts_strogatz_graph(n, k, p, seed=10)
   neighbor = []
   for node in list(sorted(G.nodes())):
   	neighbours = list(nx.all_neighbors(G, node))
   	neighbor.append(neighbours)
   for i in range(n):
   	verlist[i]['connected']=neighbor[i]
   #print(conlist)
   return verlist
'''print(gen_graph(20,5,0.5))

n :  The number of nodes
k :  Each node is connected to k nearest neighbors in ring topology
p :  The probability of rewiring each edge
seed  : for the random number'''


#nx.draw(G)   # default spring_layout
#nx.draw(G,pos=nx.spectral_layout(G), nodecolor='r',edge_color='b')
#plt.draw()
#plt.show()



#inf = nx.info(G,19)

