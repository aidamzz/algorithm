n = int(input())
l = []
for i in range(n):
    j = input()
    scores = input()
    Q = scores.count('Q')
    C = scores.count('C')
    if Q > C:
        l.append("Quera")
    else:
        l.append('CodeCup')
for i in l:
    print(i)