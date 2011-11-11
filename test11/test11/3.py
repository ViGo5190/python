
# -*- coding: utf-8 -*-
__author__ = 'vigo@vigo.su'
#encoding:utf8
import operator
import string

filename = raw_input()
infile = open(filename)
text = infile.read()
infile.close()

rows = []
ii = 0
letters_counts = {}
#rows.append(letters_counts)
for letter in text:
    if letter == '\n':
        rows.append(letters_counts)
        letters_counts= {}

    if letter != " " and letter != '\n':
        #letter = letter.lower()
        letters_counts.setdefault(letter, 0)
        letters_counts[letter] += 1
sorted(letters_counts)

#print letters_counts
ll = len(rows)
for i in xrange(0,ll,1):
    b = rows[i].keys()
    b = list(rows[i].items())
    b.sort(key=lambda item: item[1])
    b.reverse()
    for item in b:
        print(item[0] +''+ str(item[1])),
    print



#b = rows[0].keys()

#b = list(rows[0].items())
#b.sort(key=lambda item: item[1])
#b.reverse()
#for item in b:
#    print(item[0] +''+ str(item[1])),

#for key in sorted(letters_counts):
#    print(key +'=>'+ str(letters_counts[key]))
