import csv
import os

class Hangul:
    def __init__(self):
        # 조사
        self.josa = []
        f = open(os.getcwd()+'/library/j.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.josa.append(line[0])
        f.close()
        self.josa.sort(key = lambda s: -len(s))

        # 대명사
        self.pronoun=[]
        f = open(os.getcwd()+'/library/np.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.pronoun.append(line[0])
        f.close()

        # 수사
        self.numeral=[]
        f = open(os.getcwd()+'/library/nr.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.numeral.append(line[0])
        f.close()

        #연결어미
        self.connection=[]
        f = open(os.getcwd()+'/library/ec.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.numeral.append(line[0])
        f.close()

        #선어말어미
        self.preamal=[]
        f = open(os.getcwd()+'/library/ep.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.numeral.append(line[0])
        f.close()

        #종결어미
        self.end=[]
        f = open(os.getcwd()+'/library/ef.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.numeral.append(line[0])
        f.close()

# h = Hangul()