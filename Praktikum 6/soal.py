def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] < alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1
alist=[43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
shortBubbleSort(alist)
print(alist)

# Kandidat yang lolos adalah mereka yang memiliki nilai 98, 89, 76, 68, 57.
