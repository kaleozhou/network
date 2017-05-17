import networkx as nx  
import matplotlib.pyplot as plt  
f = open('qingdao.txt','r')  
l = open('qingdao.txt','r')  
G = nx.Graph()  
i=0
colors=[1]*len(l.readlines())
for linefile in f:  
    list = linefile.split(',')  
    x=list[0]  
    y=list[1]  
    c=list[2]
    colors[i]=c
    G.add_edge(x,y);  
    i=i+1
nx.draw(G,with_labels=True,node_size=500)  
plt.show()  
