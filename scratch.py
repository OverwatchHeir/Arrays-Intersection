from collections import defaultdict

def intersection(array1, array2, array3):

    array_set = set(array1 + array2 + array3)

    hash_map = defaultdict(list)

    for element in array_set:
        hash_map[element] = [0] * 3

    for element in array1:
        hash_map[element][0] += 1

    for element in array2:
        hash_map[element][1] += 1

    for element in array3:
        hash_map[element][2] += 1


    for element in hash_map:
        if hash_map[element][0] >= 1 and hash_map[element][1] >= 1 and hash_map[element][2] >= 1  :
            print(element)

array1 = [1, 4, 5, 6, 7, 8, 3, 0, 9,1, 4, 5, 6, 7, 8,1,82 , 34, 86, 302, 45, 61,3,180,  3, 9 ,82, 3, 0, 9,1, 4, 5, 6, 7, 8, 3, 0, 9,1, 4, 5, 6, 7, 8, 1,  3, 9 ,82,1, 4, 5, 6, 7, 8, 3, 0, 9,1,  3, 9 ,82 , 34, 86, 302, 45, 61,3,180]
array2 = [1, 4, 5, 6, 7, 8, 1,  3, 9 ,82,1, 4, 5, 6, 7, 8, 3, 0, 9,1,  3, 9 ,82 , 34, 86, 302, 45, 61,3,180, 1, 4, 5, 6, 7, 8, 1,  3, 9 ,82,1, 4, 5, 6, 7, 8, 3, 0, 9,1,  3, 9 ,82 , 34, 86, 302, 45, 61,3,180]
array3 = [1, 4, 64, 7, 82, 3, 2,1,  3, 9 ,8,1,82 , 34, 86, 302, 45, 61,3,180, 82, 1, 4, 5, 6, 7, 8, 1,  3, 9 ,82,1, 4, 5, 6, 7, 8, 3, 0, 9,1,  3, 9 ,82, 1, 4, 5, 6, 7, 8, 1,  3, 9 ,82,1, 4, 5, 6, 7, 8, 3, 0, 9,1,  3, 9 ,82 , 34, 86, 302, 45, 61,3,180]

intersection(array1, array2, array3)