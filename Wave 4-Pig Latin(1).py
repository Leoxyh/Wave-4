from F import Wor
L = input("Sentence: ")
L = str(L)

x = L.split(" ")
lenth = len(x)

for num in range (0, lenth):
    print(W(x[num]), end=" ")
