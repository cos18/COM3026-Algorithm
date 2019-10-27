import csv
import os

class Hangul:
    def __init__(self):
        # 조사
        self.josa = []
        f = open(os.path.normpath(os.getcwd()+'/library/j.csv'), 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.josa.append(line[0])
        f.close()
        self.josa.sort(key = lambda s: -len(s))

        

        # 대명사
        self.pronoun=[]
        f = open(os.path.normpath(os.getcwd()+'/library/np.csv'), 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.pronoun.append(line[0])
        f.close()
        self.pronoun.sort(key = lambda s: -len(s))
        

        # 수사
        self.numeral=[]
        f = open(os.path.normpath(os.getcwd()+'/library/nr.csv'), 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.numeral.append(line[0])
        f.close()
        self.numeral.sort(key = lambda s: -len(s))

        

        #연결어미
        self.connection=[]
        f = open(os.path.normpath(os.getcwd()+'/library/ef.csv'), 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.connection.append(line[0])
        f.close()
        self.connection.sort(key = lambda s: -len(s))

        

        #선어말어미
        self.preamal=[]
        f = open(os.path.normpath(os.getcwd()+'/library/ep.csv'), 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.preamal.append(line[0])
        f.close()
        self.preamal.sort(key = lambda s: -len(s))

        #종결어미
        self.endword=[]
        f = open(os.path.normpath(os.getcwd()+'/library/ec.csv'), 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.endword.append(line[0])
        f.close()
        self.endword.sort(key = lambda s: -len(s))

# h = Hangul()