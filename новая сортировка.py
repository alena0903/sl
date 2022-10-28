N = 6
spisok = [5, 7, 3, 8, 2, 8]
for C in range(N-1):
    for i in range(N-1):
        if spisok[i] > spisok[i+1]:
            tmp = spisok[i]
            spisok[i] = spisok[i+1]
            spisok[i+1] = tmp

        
print("Hello",spisok )
