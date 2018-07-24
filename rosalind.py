__author__ = 'Luke'
import os.path
import time
import re
def openfile(filename):
    start = time.time()
    with open(filename) as f:
        data = f.readlines()
        distance = 0
        for i in range(0, len(data[0])-1):
            if data[0][i] != data[1][i]:
                distance += 1
        print(distance)
        end = time.time()
        print(end - start)



def gccontent(filename):
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

#Mendel's First Law
#count times where it doesn't work, it'll go faster
#50% chance of het x rec = rec
#25% chance of het x het = rec
#100% chance of rec x rec = rec
def mendelian(filename):
    start = time.time()
    with open(filename) as f:
        data = f.read().split(" ")
        pop = 0
        chance = 0
        for i in range(0, 3):
            pop += int(data[i])
        dom = int(data[0])
        het = int(data[1])
        rec = int(data[2])
        #chances of het x het,
        chance += ((het/pop) * ((het-1)/(pop-1)) * 0.25)
        #het x rec,
        chance += ((het/pop) * (rec/(pop-1)) * 0.5)
        #then rec x rec
        chance += ((rec/pop) * ((rec-1)/(pop-1)))
        #then rec x het
        chance += ((rec/pop) * (het/(pop-1)) * 0.5)
        print(1 - chance)
    end = time.time()
    print(end - start)

#RNA to protein translation
def rnaprotein(filename):
    start = time.time()
    table = {
        'UUU':'F',
        'CUU':'L',
        'AUU':'I',
        'GUU':'V',
        'UUC':'F',
        'CUC':'L',
        'AUC':'I',
        'GUC':'V',
        'UUA':'L',
        'CUA':'L',
        'AUA':'I',
        'GUA':'V',
        'UUG':'L',
        'CUG':'L',
        'AUG':'M',
        'GUG':'V',
        'UCU':'S',
        'CCU':'P',
        'ACU':'T',
        'GCU':'A',
        'UCC':'S',
        'CCC':'P',
        'ACC':'T',
        'GCC':'A',
        'UCA':'S',
        'CCA':'P',
        'ACA':'T',
        'GCA':'A',
        'UCG':'S',
        'CCG':'P',
        'ACG':'T',
        'GCG':'A',
        'UAU':'Y',
        'CAU':'H',
        'AAU':'N',
        'GAU':'D',
        'UAC':'Y',
        'CAC':'H',
        'AAC':'N',
        'GAC':'D',
        'UAA':'stop',
        'CAA':'Q',
        'AAA':'K',
        'GAA':'E',
        'UAG':'stop',
        'CAG':'Q',
        'AAG':'K',
        'GAG':'E',
        'UGU':'C',
        'CGU':'R',
        'AGU':'S',
        'GGU':'G',
        'UGC':'C',
        'CGC':'R',
        'AGC':'S',
        'GGC':'G',
        'UGA':'stop',
        'CGA':'R',
        'AGA':'R',
        'GGA':'G',
        'UGG':'W',
        'CGG':'R',
        'AGG':'R',
        'GGG':'G'
    }
    with open(filename) as f:
        data = f.read()
        protein = ''
        for i in range(0, len(data)):
            if i == 0 or (i) % 3 == 0:
                codon = ''
                for x in range(i, i+3):
                    codon += data[x]
                print(codon)
                if table[codon] == 'stop':
                    print(protein)
                    break
                else:
                    protein += table[codon]

#Finding all ocurrences of a motif in a strand of dna
def findmotif(filename):
    with open(filename) as f:
        data = f.readline()
        motif = f.readline()
        points = []
        print(motif)
        for i in range(0, len(data)-len(motif)):
            newmotif = ''
            for x in range(i, i+len(motif)):
                newmotif += data[x]
            if motif == newmotif:
                points.append(str(i+1))
        str1 = ' '.join(points)
        print(str1)

#Consensus and profile
def consensus(filename):
    with open(filename) as f:
        lines = f.read()
        slines = re.sub('\d', '', lines)
        slines = slines.replace("\n", "").replace("", "").split(">Rosalind_")
        slines.pop(0)
        alist = ["A:"]
        clist = ["C:"]
        glist = ["G:"]
        tlist = ["T:"]
        ancestor = []
        
        for i in range(len(slines[0])):
            alist.append(0)
            clist.append(0)
            glist.append(0)
            tlist.append(0)
            ancestor.append(" ")

        for i in range(len(slines)):
            for x in range(len(slines[i])):
                if slines[i][x] == "A":
                    alist[x+1] += 1
                elif slines[i][x] == "C":
                    clist[x+1] += 1
                elif slines[i][x] == "G":
                    glist[x+1] += 1
                else:
                    tlist[x+1] += 1

        for i in range(1, len(alist)):
            if alist[i] >= clist[i] and alist[i] >= glist[i] and alist[i] >= tlist[i]:
                ancestor[i-1] = "A"
            elif clist[i] > alist[i] and clist[i] >= glist[i] and clist[i] > tlist[i]:
                ancestor[i-1] = "C"
            elif glist[i] > alist[i] and glist > clist[i] and glist[i] > tlist[i]:
                ancestor[i-1] = "G"
            elif tlist[i] > alist[i] and tlist[i] >= clist[i] and tlist[i] >= glist[i]:
                ancestor[i-1] = "T"
                
        print("".join(ancestor))
        print(" ".join(str(a) for a in alist))
        print(" ".join(str(c) for c in clist))
        print(" ".join(str(g) for g in glist))
        print(" ".join(str(t) for t in tlist))


consensus("rosalind_cons.txt")