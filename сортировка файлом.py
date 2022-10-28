file = open('сорт.txt')
file_with_lines = file.readlines()
file_with_lines = (file_with_lines[0].split())

list_1 = []
for line in file_with_lines:
    e = int(line)
    list_1.append(e)
    for x in range(1, len(list_1)):
        for i in range(len(list_1)):
            if list_1[i] < list_1[x-i]:
                Y = list_1[i]
                list_1[i] = list_1[x-i]
                list_1[x-i] = Y

        
print("Hello",list_1 )

