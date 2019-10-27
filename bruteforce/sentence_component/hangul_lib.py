import csv

class Hangul:
    def __init__(self):
        # 조사
        self.josa = []
        f = open('library/j.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.josa.append(line[0])
        f.close()
        self.josa.sort(key = lambda s: -len(s))

        # 대명사
        self.pronoun=[]
        f = open('library/np.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.pronoun.append(line[0])
        f.close() 

        # 수사
        self.numeral=[]
        f = open('library/nr.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.numeral.append(line[0])
        f.close()

# h = Hangul()