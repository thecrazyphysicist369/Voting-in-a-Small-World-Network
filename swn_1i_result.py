import small_world
import voting
import matplotlib.pyplot as plt

#The number of voters to campaign
number_of_voters = int(input("please input the number of voters you want to analyze : "))


#Generating a list of numbers
number=[]
for i in range(number_of_voters):
    number.append(i)

#generating the small world
voters_p = small_world.gen_graph(number_of_voters, 6, 0.5)

#status before the vote
#network.show_graph(voters_pre)

#The voting
voters_p,pos,neg,neu=voting.campaining(voters_p)

#Status after the vote
#network.show_graph(voters_p)

#plotting the results
plt.plot( number, pos, color="r", label="Party A")
plt.plot( number, neg, color="b", label="Party B")
#plt.plot( number, neu, color="g", label="Neutral")
plt.legend()
plt.show()
