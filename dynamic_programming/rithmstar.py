class Rithmstar:
    panmove = [
        [],
        [0, 0, 1, 2, 1, 2, 3],
        [0, 1, 0, 1, 2, 1, 2],
        [0, 2, 1, 0, 3, 2, 1],
        [0, 1, 2, 3, 0, 1, 2],
        [0, 2, 1, 2, 1, 0, 1],
        [0, 3, 2, 1, 2, 1, 0]
    ]
    dp = []

    def __init__(self):
        self.cnt = int(input("노트 수를 입력하세요 : "))
        self.note = list(map(int, input("=> ").split()))
        self.note = [0] + self.note

        for i in range(self.cnt+1):
            n = []
            for j in range(7):
                n.append([-1, -1, -1, -1, -1, -1, -1])
            self.dp.append(n)
        self.dp[0][1][3] = 0
    
    def dp_cal(self):
        for now in range(1, self.cnt+1):
            for i in range(1, 7):
                for j in range(1, 7):
                    if self.dp[now-1][i][j] != -1:
                        if self.note[now]!=j:
                            i_dp = self.dp[now-1][i][j] + self.panmove[i][self.note[now]]
                            if self.dp[now][self.note[now]][j] != -1:
                                self.dp[now][self.note[now]][j] = min(self.dp[now][self.note[now]][j], i_dp)
                            else:
                                self.dp[now][self.note[now]][j] = i_dp
                        if self.note[now]!=i:
                            j_dp = self.dp[now-1][i][j] + self.panmove[j][self.note[now]]
                            if self.dp[now][i][self.note[now]] != -1:
                                self.dp[now][i][self.note[now]] = min(self.dp[now][i][self.note[now]],j_dp)
                            else:
                                self.dp[now][i][self.note[now]] = j_dp

    def find_path(self, x, y, locate, moving):
        if x==y and y==0:
            print("ERROR")
            return
        
        if locate==1:
            print("<1, 3> -> <{}, {}>".format(x, y), end="")
            return

        for i in range(1, 7):
            for j in range(1, 7):
                if self.dp[locate-1][i][j] == -1:
                    continue
                if i==x or j==y:
                    dmove = moving - self.dp[locate-1][i][j]
                    if dmove == self.panmove[i][self.note[locate]] or dmove == self.panmove[self.note[locate]][j]:
                        self.find_path(i, j, locate-1, moving-dmove)
                        print(" -> <{}, {}>".format(x, y), end="")
                        return


    def backtrack(self):
        ans = 30001
        finali = 0
        finalj = 0
        for i in range(1, 7):
            for j in range(1, 7):
                if self.dp[self.cnt][i][j] != -1:
                    if ans > self.dp[self.cnt][i][j]:
                        ans = self.dp[self.cnt][i][j]
                        finali = i
                        finalj = j
        self.find_path(finali, finalj, self.cnt, ans)
                    
my_game = Rithmstar()
my_game.dp_cal()
my_game.backtrack()