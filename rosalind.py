__author__ = 'Luke'
import os.path
import time
def openfile(filename):
    start = time.time()
    with open(filename) as f:
        data = f.read().split(">")
        newdata = {}
        percentages = {}
        for i in range(0, len(data)):
            tn = 0
            gc = 0
            data[i] = data[i].replace('\n','')
            title = data[i][:13]
            newdata[title] = data[i][13:]
            for i in range(0,len(newdata[title])):
                tn += 1
                if newdata[title][i] == "G" or newdata[title][i] == "C":
                    gc+= 1
                percentages[title] = (gc/tn) * 100
        newperc = 0
        newkey = ""
        for key in percentages:
            if percentages[key] > newperc:
                newperc = percentages[key]
                newkey = key
        end = time.time()
        print(end - start)
        print(newkey)
        print(round(newperc,6))


openfile("rosalind_gc.txt")