__author__ = 'vigo@vigo.su'

for i in range(int("391", 16),int("3AA",16)) :
    if i != int("3A2", 16) :
        print unichr(i)+unichr(i+32),
