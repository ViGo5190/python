__author__ = 'vigo@vigo.su'

# -*- coding: utf-8 -*-

import networkx as nx

import matplotlib.pyplot as plt

import os

import math




#---------------------

G=nx.Graph()


def is2pow(xxk):
    #print 'k=',xxk
    #ii = math.log(xxk)
    #ii /=math.log(2)
    #ll = 2**ii
    #return (xxk==ll)
    return (xxk==(2**int(math.log(xxk,2))))
def low2pow(xxk):
    return int(math.log(xxk,2))




def print_pic(pic_n=0):
    labels=dict((n,str(d['label'])) for n,d in G.nodes(data=True))
    pos2=dict((n,(d['x'],d['y'])) for n,d in G.nodes(data=True))
    pos=nx.graphviz_layout(G,prog='dot',args='-y')
    print labels
    print pos
    print pos2
    print G.nodes(data=True)[1][1]['x']
    nx.draw(G, pos2, with_labels=True,labels=labels, node_color="blue", node_size=1000)

    plt.savefig("edge_colormap"+str(pic_n)+".png")
    

    plt.show()
    


def load_data():
    pic_n = 0
    h=nx
    f = open('input.txt','r')
    data = f.readlines()
    f.close()
    mylen = len(data)
    some = low2pow(len(data))+1
    xx = 0
    yy = 1.0
    znak = 1;
    for i in xrange(0,len(data)/2,1):
        ii = long(data[i])

        
        print i+1,ii,
        iid = 1
        parentx = 0;
        #nx.draw_networkx_nodes( G,pos=[(1/(i+1),1/(i+1))],nodelist=G.nodes() )
        if i>0:
            if i>2:
                iid = long((i+1)/2)
                parentx = float(G.nodes(data=True)[iid-1][1]['x'])
                print ">",parentx,"<",float(G.nodes(data=True)[iid-1][1]['z']),
            else:
                iid = 1
                parentx = 0

            #iid = low2pow(i+1)
            #if i< (2**(low2pow(i+1)+1)/2):
            #    print i,"-"
            #    znak = -1
            #else:
            #    print i,"+"
            znak*=-1
            print "parent=",iid,

            #print G.nodes(data=True)[iid][1]['x']
            #myxx = 1.0/+znak*myx;



        if i>0:
            G.add_node(i+1,label=ii,x=float((parentx + ((some-low2pow(i))*znak* (1.0/(low2pow(i+1)+1)) )   )),y=-1*low2pow(i+1),z=znak)
            G.add_edge(iid,i+1)
        else:
            G.add_node(i+1,label=ii,x=0,y=0,z=znak)



        k=int(i)
        if is2pow(i+1):
            yy/=2
        print


    
    print_pic()
    #labels=dict((n,str(d['z'])+" "+str(d['label'])+"  "+str(d['x'])+"  "+str(d['y'])) for n,d in G.nodes(data=True))




def make_tree(G=nx.Graph()):
    return 0

def main():
    G = get_tree()

    nx.draw(G, with_labels=False, node_color="blue", alpha= 0.6, node_size=50)
    #nx.draw_networkx_nodes(G,nodelist=(0))
    plt.savefig("edge_colormap.png")

    plt.show()

load_data()