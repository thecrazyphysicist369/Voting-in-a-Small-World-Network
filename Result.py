import network
import voting
import matplotlib.pyplot as plt

voters_pre = network.gen_graph(500)
'''
for i in voters_pre:
    print(i)
'''
network.show_graph(voters_pre)

voters_post,pos,neg,neu=voting.campaining(voters_pre)
'''
print('\n')

for i in voters_post:
    print(i)
'''
number=[]
for i in range(len(voters_post)):
    number.append(i)


network.show_graph(voters_post)

plt.plot( number, pos, color="r", label="Party A")
plt.plot( number, neg, color="b", label="Party B")
plt.plot( number, neu, color="g", label="Neutral")
#plt.xlim(0,360)
plt.legend()
#plt.savefig("abcd.jpg")
plt.show()
