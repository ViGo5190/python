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

def is_hidden_dir(d):
    import sys, subprocess
    if sys.platform.startswith("win"):
        p = subprocess.check_output(["attrib", d])
        return True if 'H' in p[:12] else False
    else:
        return True if os.path.basename(d)[0] == '.' else False

def search_midle():
    return 0


def load_data(G=nx.Graph()):
    h=nx
    f = open('input.txt','r')
    data = f.readlines()
    f.close()

    for i in xrange(0,len(data)/2,1):
        ii = long(data[i])
        G.add_node(ii)
        
        if i>0:
            iid = long(data[i/2])
            G.add_edge(iid,ii)

    
    #pos = {0:(1,1)}

    
    pos=nx.spring_layout(G)
    #print pos
    nx.draw(G, pos, with_labels=True, node_color="blue", node_size=300)

    plt.savefig("edge_colormap.png")

    plt.show()


def make_tree(G=nx.Graph()):
    return 0

def main():
    G = get_tree()

    nx.draw(G, with_labels=False, node_color="blue", alpha= 0.6, node_size=50)

    plt.savefig("edge_colormap.png")

    plt.show()

load_data()