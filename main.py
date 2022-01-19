def hashFunction(key, size):
    h = 0
    a = 127
    for v in range(len(key)):
        h = (a * h + (ord(key[v]))) % size
    print(h, '-хэш')
    return h


def rehash(oldhash, size):
    oldhash = (oldhash + 1) % size
    print(oldhash, '-reхэш')
    return oldhash


def insertData(key, data, size):
    cnt = 0
    tmp = [[" "], ] * size
    index = hashFunction(key, size)
    tmp_hash = [hashFunction(key, size)]
    # print( tmp_hash[0])
    if hashTable[index][0] != " ":
        if hashTable[index][0] == key:
            hashTable[index].append(data)
        else:
            for i in range(len(hashTable)):
                newindex = rehash(tmp_hash[0], size)
                tmp_hash.clear()
                tmp_hash.append(newindex)
                if hashTable[newindex][0] == " ":
                    hashTable[newindex] = [key, data]
                    break
    else:
        hashTable[index] = [key, data]
    for i in range(len(hashTable)):
        if hashTable[i][0] != " ":
            cnt += 1
    if cnt == len(hashTable) // 2:
        # tmp = [[0], ] * size
        for i in range(len(hashTable)):
            tmp[i] = hashTable[i]
        print('bjk')
        print(tmp)
        hashTable.clear()
        for i in range(len(tmp) * 2):
            hashTable.append([" "])
        for i in range(len(tmp)):
            # xs = tmp[i][0]
            # print(xs)
            if tmp[i][0] != "":
                new = hashFunction(tmp[i][0], len(hashTable))

            print(new)
            # for x in range(len(tmp)):
            #     for j in range(1):
            hashTable[new] = tmp[i]


def findData(key, size):
    # for i in range(len(hashTable)):
    #     if hashTable[i][0] == key:
    #         print(hashTable[i])
    index = hashFunction(key, size)
    tmp_hash = [hashFunction(key, size)]
    # print(hashTable[index])
    if hashTable[index][0] == key:
        return hashTable[index]
    else:
        for i in range(len(hashTable)):
            newindex = rehash(tmp_hash[0], size)
            tmp_hash.clear()
            tmp_hash.append(newindex)
            if hashTable[newindex][0] == " ":
                return hashTable[newindex]


def removeData(key):
    for i in range(len(hashTable)):
        if hashTable[i][0] == key:
            hashTable[i] = ' '


n = int(input("Введите размер"))
hashTable = [[" "], ] * n

# for i in range(n):
#     key = input("Введите подсказку")
#     if key == "end":
#         break
#     val = input("Введите данные")
#     insertData(key, val, len(hashTable))
#
#
# for i in range(len(hashTable)):
#     print("\n", hashTable[i])
#
# print("Какой элемент найти")
#
# for i in range(len(hashTable)):
#     print("\n", hashTable[i])
#
# find = input("Введите подсказку")
# findData(find)

Menu = input('Введите цифры от 1 до 6:\n'
             '1-Вставка элемента в таблице\n'
             '2-Удалить элемент в таблице\n'
             '3-Найти эллемент\n'
             '4-Вывести таблицу\n'
             '5-Выход\n'
             '------> ')
while Menu != '5':
    if Menu == '1':

        key = input("Введите подсказку")
        if key == "end":
            break
        val = input("Введите данные")
        insertData(key, val, len(hashTable))

        for i in range(len(hashTable)):
            print("\n", hashTable[i])


    elif Menu == '2':
        sl = input('Введите слово:')
        removeData(sl)
        for i in range(len(hashTable)):
            print("\n", hashTable[i])

    elif Menu == '3':
        print("Какой элемент найти")

        for i in range(len(hashTable)):
            print("\n", hashTable[i])

        find = input("Введите подсказку")

        print(findData(find, len(hashTable)))

    elif Menu == '4':
        for i in range(len(hashTable)):
            print("\n", hashTable[i])

    Menu = input('Введите цифры от 1 до 6:\n'
                 '1-Вставка элемента в таблице\n'
                 '2-Удалить элемент в таблице\n'
                 '3-Найти эллемент\n'
                 '4-Вывести таблицу\n'
                 '5-Выход\n'
                 '------> ')
