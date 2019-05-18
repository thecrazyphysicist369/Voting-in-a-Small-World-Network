import random
#random.seed(100)
vertex = {'index': 0,
          'endurance': 0,
          'influence': 0,
          'connected': [],
          }

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


#matrix generator generates the connection between the voters
def mat_gen(n):
    mat = []
    c = 0
    for i in range(n):
        mat.append(random.sample(range(n), n))
        for j in range(i):
            mat[i][j] = mat[j][i] = random.randint(0, 1)
        mat[i][i] = 0
    return mat




#the graph generator generates the small world in which the voting will take place
def gen_graph(n):

    mat=mat_gen(n)
    #print(mat[:][:])
    verlist = gen_vertex(n)
    for i in range(n):
        conlist=[]
        for j in range(n):
            if mat[i][j] == 1:
                conlist.append(j)
                verlist[i]['connected']=conlist
        #print(conlist)
    return verlist

import networkx as nx
import matplotlib.pyplot as plt

#To visualise the generated small world. Also visualises the state of voting of the parties
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
