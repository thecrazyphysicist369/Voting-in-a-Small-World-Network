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

