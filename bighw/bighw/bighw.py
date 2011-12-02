__author__ = 'vigo@vigo.su'

# -*- coding: utf-8 -*-

import networkx as nx

import matplotlib.pyplot as plt

import os

def get_tree(tree=[u"/home/vigo/python/",], G=nx.Graph(), itr=0, max_itr=900):
    point = tree.pop(0)
    itr = itr + 1
    sub_tree = [os.path.join(point, x) for x in os.listdir(point) if os.path.isdir(os.path.join(point, x)) and not is_hidden_dir(os.path.join(point, x))]
    if sub_tree:
        tree.extend(sub_tree)
        G.add_edges_from(map(lambda b : (point, b), sub_tree))
    if tree and itr <= max_itr:
        return get_tree(tree, G, itr)
    else:
        return G

def search_midle():
    return 0


def load_data(G=nx.Graph()):
    h=nx
    f = open('input.txt','r')
    data = f.readlines()
    f.close()

    for i in xrange(0,len(data)/2,1):
        ii = long(data[i])
        G.add_node(i+1,attr_dict={'label':ii},label=ii)
        
        print i
        #nx.draw_networkx_nodes( G,pos=[(1/(i+1),1/(i+1))],nodelist=G.nodes() )
        if i>0:
            #iid = long(data[i/2])
            iid = (i+1)/2

            G.add_edge(iid,i+1)

    
    #pos = {0:(1,1)}

    
    #pos=nx.spring_layout(G)
    #H = nx.balanced_tree(2,2,G)

    #pos=nx.graphviz_layout(G,prog='dot',args='-x -y')
    pos=nx.graphviz_layout(G,prog='dot',args='-x')
    #print pos
    nx.draw(G, pos, with_labels=True, node_color="blue", node_size=300)

    plt.savefig("edge_colormap.png")

    plt.show()


def make_tree(G=nx.Graph()):
    return 0

def main():
    G = get_tree()

    nx.draw(G, with_labels=False, node_color="blue", alpha= 0.6, node_size=50)
    #nx.draw_networkx_nodes(G,nodelist=(0))
    plt.savefig("edge_colormap.png")

    plt.show()

load_data()