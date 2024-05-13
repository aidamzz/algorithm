sangs = input().split(' ')
sangs = sangs[::-1]
n = input()
counter = 0
for i in sangs:
    if i == n:
        counter += 1
        break
    counter += 1
if counter == len(sangs):

    print(counter-1)
else:
    print(counter)