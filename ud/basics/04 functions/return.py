#               Definiowanie funkcji - return
# Return na końcu funkcji jest opcjonalne, umożliwia wyjście z funkcji w dowolnym momencie

def printList(listData):
    if len(listData) <= 3:     #funkcja konczy działanie jeśli lista jest mniejsza niż 3 elementy
        return
    print(listData)
printList(["a", "b", "c"])  # to nie zostanie wyświetlone bo długość listy spełnia ifa z funkcji więc jest return
printList(["a", "b", "c", "d", "e"])  # to zostanie wyświetlone bo długość listy nie spełnia ifa z funkcji więc program jest dalej wykonywany


def sumListElements(listData):
    if len(listData) == 0:
        print("Pusta lista")
        return None
    result = 0
    for v in listData:
        result += v
    return result
print(sumListElements([]))
print(sumListElements([1,2,3,4,5,6,7,8,9]))         # 45

# return nie jest obowiązkowe jeśli a końcu funkcji nie zwracamy wartości:
def printList(listData):
    if len(listData) == 0:
        return
    for v in listData:
        print(listData)
printList([])
print([1,2,3,4,5])