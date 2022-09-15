import matplotlib.pyplot as plt
import networkx as nx

def plotGraph(G, node_size = 10):
    
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G,pos, node_size=node_size, with_labels=True, node_color="skyblue", alpha=0.5)
    plt.tight_layout()
    #plt.show(block=False)
    plt.show()

def plotGraphSave(G, file_name=  "nxplot.png"):
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G,pos, with_labels=True, node_color="skyblue", alpha=0.5)
    plt.tight_layout()
    plt.savefig(file_name, format="PNG")
    plt.clf()

