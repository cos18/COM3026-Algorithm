N = int(input(''))
M, F = 1, 1
while True:
    F = F*M
    if M==N:
        break
    M+=1
print(F)