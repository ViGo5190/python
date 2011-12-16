from test import get_tree

__author__ = 'vigo@vigo.su'

# -*- coding: utf-8 -*-

import networkx as nx

from networkx import graphviz_layout as gl

import matplotlib.pyplot as plt

import os

import math




#---------------------

G=nx.Graph()
pic_n=0



def is2pow(xxk):
    #print 'k=',xxk
    #ii = math.log(xxk)
    #ii /=math.log(2)
    #ll = 2**ii
    #return (xxk==ll)
    return (xxk==(2**int(math.log(xxk,2))))
def low2pow(xxk):
    return int(math.log(xxk,2))




def print_pic(pic_q):
    labels=dict((n,str(d['label'])) for n,d in G.nodes(data=True))
    colors=dict((n,str(d['color'])) for n,d in G.nodes(data=True))
    pos2=dict((n,(d['x'],d['y'])) for n,d in G.nodes(data=True))
    pos=nx.graphviz_layout(G,prog='dot',args='-y')
    #print labels
    #print pos
    #print '----'
    #print pos2
    
    #print G.nodes(data=True)[1][1]['x']
    plt.cla()
    nx.draw(G, pos2, with_labels=True,labels=labels, node_color="red", node_size=600)

    plt.savefig("zzzedge_colormap"+str(pic_q).rjust(3,"0")+".png")
    

    #plt.show()
    pic_q+=1
    return pic_q
    
def siftdown(start, end):
    return 0


def checkParent(i,x_n):
    if i>2 :
        iid = long((i+1)/2)

    else:
        iid = 1

    if int(G.nodes(data=True)[i][1]['label']) > int(G.nodes(data=True)[iid-1][1]['label']):
        G.nodes(data=True)[i][1]['label'],G.nodes(data=True)[iid-1][1]['label'] = G.nodes(data=True)[iid-1][1]['label'], G.nodes(data=True)[i][1]['label']
        x_newn = print_pic(x_n)
    else:
        x_newn = x_n
        
    if i>1:
        return checkParent(iid, x_newn)
    else:
        return x_newn

def load_data():
    pic_n = 0
    h=nx
    f = open('input.txt','r')
    data = f.readlines()
    f.close()
    mylen = len(data)
    some = low2pow(len(data))
    xx = 0
    yy = 1.0
    znak = 1;
    for i in xrange(0,len(data),1):
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
            #G.add_node(i+1,label=ii,x=float((parentx + ((some-low2pow(i))*znak* (1.0/(low2pow(i+1)+1)) )   )),y=-1*low2pow(i+1),z=znak)
            G.add_node(i+1,label=ii,x=float((parentx  + 100*((some-low2pow(i))*znak* (1.0/(low2pow(i+2))) )   )),y=-1*low2pow(i+1),z=znak,color="blue")
            G.add_edge(iid,i+1)
            pic_n = print_pic(pic_n)
            #if int(G.nodes(data=True)[i][1]['label']) > int(G.nodes(data=True)[iid-1][1]['label']):
                #lastlbl = G.nodes(data=True)[i][1]['label']
                #G.nodes(data=True)[i][1]['label'] = G.nodes(data=True)[iid-1][1]['label']
                #G.nodes(data=True)[iid-1][1]['label'] = lastlbl
                ##swap(G.nodes(data=True)[i][1]['label'],G.nodes(data=True)[iid-1][1]['label'])
            #    G.nodes(data=True)[i][1]['label'],G.nodes(data=True)[iid-1][1]['label'] = G.nodes(data=True)[iid-1][1]['label'], G.nodes(data=True)[i][1]['label']
            #    pic_n = print_pic(pic_n)
            pic_n = checkParent(i,pic_n)
        else:
            G.add_node(i+1,label=ii,x=0-some,y=0,z=znak,color="blue")
            pic_n = print_pic(pic_n)

        for i in xrange (0,len(G.nodes(data=True)),1):
            print G.nodes(data=True)[i][1]['label'],
        print ";"
        print '----------------------------------------------------------',G.nodes(data=True)[i][1]['label']



        k=int(i)
        if is2pow(i+1):
            yy/=2
        print

    return pic_n

    
    #pic_n = print_pic(pic_n)
    #labels=dict((n,str(d['z'])+" "+str(d['label'])+"  "+str(d['x'])+"  "+str(d['y'])) for n,d in G.nodes(data=True))




#def make_tree(G=nx.Graph()):
#    return 0



def moveDown(i,x_n):
    x_new = x_n
    if i*2+2<len(G.nodes(data=True)):
        if (int(G.nodes(data=True)[i][1]['label']) < int(G.nodes(data=True)[i*2+1][1]['label'])) or (int(G.nodes(data=True)[i][1]['label']) < int(G.nodes(data=True)[i*2+2][1]['label'])):


            if int(G.nodes(data=True)[i*2+1][1]['label']) > int(G.nodes(data=True)[i*2+2][1]['label']):
                G.nodes(data=True)[i][1]['label'],G.nodes(data=True)[i*2+1][1]['label'] = G.nodes(data=True)[i*2+1][1]['label'], G.nodes(data=True)[i][1]['label']
                x_new = print_pic(x_n)
                moveDown(i*2+1,x_new)
                return x_new
            else:
                G.nodes(data=True)[i][1]['label'],G.nodes(data=True)[i*2+2][1]['label'] = G.nodes(data=True)[i*2+2][1]['label'], G.nodes(data=True)[i][1]['label']
                x_new = print_pic(x_n)
                x_new = moveDown(i*2+2,x_new)
                return x_new


        else:
            return x_new

    elif i*2+1<len(G.nodes(data=True)):
        if int(G.nodes(data=True)[i][1]['label']) < int(G.nodes(data=True)[i*2+1][1]['label']):
            G.nodes(data=True)[i][1]['label'],G.nodes(data=True)[i*2+1][1]['label'] = G.nodes(data=True)[i*2+1][1]['label'], G.nodes(data=True)[i][1]['label']
            x_new = print_pic(x_n)
            x_new = moveDown(i*2+1,x_new)
            return x_new
        else:
            return x_new

    else:
        return x_new
        

        

if __name__ == '__main__':

    pic_n = load_data()
    start = (len(G.nodes(data=True))-2)/2
    leng = len(G.nodes(data=True))
    #print G.edges(data=True)
    for i in xrange (0,leng,1):
        print G.nodes(data=True)[i][1]['label'],
    print ";"
    while leng>0:
        G.nodes(data=True)[0][1]['label'],G.nodes(data=True)[leng-1][1]['label'] = G.nodes(data=True)[leng-1][1]['label'], G.nodes(data=True)[0][1]['label']

        if leng>2 :
            iid = long((leng+1)/2)
        else:
            iid = 1


        leng-=1
        #print leng, iid, "!",
        #print "remove", leng+1
        print  G.nodes(data=True)[leng][1]['label'],
        G.remove_node(leng+1)
        pic_n = print_pic(pic_n)

        if leng>1:
            pic_n = moveDown(0,pic_n)
        
