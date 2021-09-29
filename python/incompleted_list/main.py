
# Dada uma lista ordenada de 0 até 9, encontre o número que está faltando.
def findTheLostOne(list): # O(n) linear
    for i in range(0, 10):
        if len(list) == 9:
            return 9
        if list[i] != i:
            return i
    
print(findTheLostOne([0, 1, 2, 3, 4, 5, 6, 7, 8]))

# Dada uma lista não ordenada de 0 até 9, encontre o número que está duplicado.
def findTheDuplicatedOneNaive(list): # O(n^2) quadratic
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if i != j and list[i] == list[j]:
                return list[i]
    return False

print(findTheDuplicatedOneNaive([0, 1, 2, 2, 3, 4, 5, 6, 7, 8]))

# Dada uma lista não ordenada de 0 até 9, encontre o número que está duplicado.
def findTheDuplicatedOneImproved(list): # O(n) linear
    previous_values = {}
    for i in range(0, len(list)):
        if previous_values.get(list[i]) is not None:
            return list[i]
        else:
            previous_values[list[i]] = True
    return False

print(findTheDuplicatedOneImproved([0, 1, 2, 3, 4, 5, 6, 7, 8]))