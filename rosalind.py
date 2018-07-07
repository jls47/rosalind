__author__ = 'Luke'
import os.path
import time
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




rnaprotein("rosalind_prot.txt")