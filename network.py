<<<<<<< HEAD
import random
#random.seed(100)
vertex = {'index': 0,
          'endurance': 0,
          'influence': 0,
          'connected': [],
          }

#vertex generator
def gen_vertex(n):
    ver_list=[]
    c=0
    for i in range(n):
        vertex = {'index': c,
                  'endurance': random.randrange(-10, 10),
                  'influence': random.randint(0, 10),
                  'connected': [],
                  }
        ver_list.append(vertex)

        c+=1
    return ver_list


#matrix generator
def mat_gen(n):
    mat = []
    c = 0
    for i in range(n):
        mat.append(random.sample(range(n), n))
        for j in range(i):
            mat[i][j] = mat[j][i] = random.randint(0, 1)
        mat[i][i] = 0
    return mat





#the graph generator
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


'''    for i in gen_graph(10):
        print (i,'\n')'''


import networkx as nx
import matplotlib.pyplot as plt

#Function to show the display the graph
def show_graph(voters):
    G = nx.empty_graph(len(voters))
    pos = nx.shell_layout(G)  # positions for all nodes
    list_A=[]
    list_B=[]
    list_N=[]
    for i in range(len(voters)):
        if int(voters[i]['endurance'])>0:
            list_A.append(voters[i]['index'])
        elif int(voters[i]['endurance'])<0:
            list_B.append(voters[i]['index'])
        else :
            list_N.append(voters[i]['index'])
    nx.draw_networkx_nodes(G, pos,
                                   nodelist=list_A,
                                   node_color='r',
                                   node_size=5,
                                   alpha=0.8)

    nx.draw_networkx_nodes(G, pos,
                                   nodelist=list_B,
                                   node_color='b',
                                   node_size=5,
                                   alpha=0.8)
    nx.draw_networkx_nodes(G, pos,
                                   nodelist=list_N,
                                   node_color='g',
                                   node_size=5,
                                   alpha=0.8)

    '''for i in range(len(voters)):
        conlist=voters[i]['connected']
        for j in conlist:
            #if not G.edges(i,j): #if we want to avoid double edge
            nx.draw_networkx_edges(G, pos,
                                   edgelist=[(i,j)],
                                   width=0.1, alpha=0.1, edge_color='k')'''
    #nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)



    #nx.draw(G)
    plt.show()



=======
import random
vertex = {'index': 0,
          'endurance': 0,
          'influence': 0,
          'connected': [],
          }

#vertex generator
def gen_vertex(n):
    ver_list=[]
    c=0
    for i in range(n):
        vertex = {'index': c,
                  'endurance': random.randrange(-10, 10),
                  'influence': random.randint(0, 10),
                  'connected': [],
                  }
        ver_list.append(vertex)

        c+=1
    return ver_list


#matrix generator
def mat_gen(n):
    mat = []
    c = 0
    for i in range(n):
        mat.append(random.sample(range(n), n))
        for j in range(i):
            mat[i][j] = mat[j][i] = random.randint(0, 1)
        mat[i][i] = 0
    return mat





#the graph generator
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

print(len(gen_graph(10)))

>>>>>>> edf083fa342f522d46bb2e274d781af3e1c9182e
