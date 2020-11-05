import network
import voting
import matplotlib.pyplot as plt

number_of_voters = int(input("please input the number of voters you want to analyze : "))

iterations = int(input("please enter the number of iterations you want the campaining to run : "))

#for the list of voters
number=[]
for i in range(number_of_voters):
    number.append(i)

#Generating the small world network
voters_p = network.gen_graph(number_of_voters)

#To see the state before voting
#network.show_graph(voters_p)


posi = []
negi = [] 
neut = []
count = []
#The voting takes place as many times the iteration is chosen
for j in range (iterations):
	voters_p,pos,neg,neu=voting.campaining(voters_p)
	posi.append(pos[number_of_voters-1]) #Keeps track of party A
	print(pos[number_of_voters-1])
	negi.append(neg[number_of_voters-1]) #Keeps track of party B
	print(neg[number_of_voters-1])
	neut.append(neu[number_of_voters-1]) #Keeps track of Neutral
	count.append(j)
	
#To see the state after voting
#network.show_graph(voters_p)


plt.plot(count, posi, color='r', label = "party A")
plt.plot(count, negi, color='b', label = "party B")
#plt.plot(count, neut, color='g', label = "Neutral")
plt.legend()
plt.show()
