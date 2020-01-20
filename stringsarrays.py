from collections import Counter, defaultdict


def isPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    sum1, sum2 = 0, 0
    for s in str1:
        sum1 += ord(s)
    for s in str2:
        sum2 += ord(s)
    return sum1 == sum2


def uniqueChars(s):
    if len(s) > 256:
        return False
    found = [False] * 256
    for char in s:
        if found[ord(char)]:
            return False
        found[ord(char)] = True
    return True


def urlify(string, length):
    spaceCount = 0
    for i in range(length):
        if string[i] == ' ':
            spaceCount += 1
    index = len(string) + (2 * spaceCount)
    charArray = [''] * index
    for i in range(length-1, -1, -1):
        if string[i] == ' ':
            charArray[index-1] = '0'
            charArray[index-2] = '2'
            charArray[index-3] = '%'
            index -= 3
        else:
            charArray[index-1] = string[i]
            index -= 1
    return charArray


def palindromePerm(string):
    string = string.lower()
    c = Counter(string)
    singleDigitFound = False
    for elem, count in c.most_common():
        if elem != ' ':
            if count == 1:
                if not singleDigitFound:
                    singleDigitFound = True
                else:
                    return False
            elif count != 2:
                return False
    return True


def oneAway(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False
    elif str1 == str2:
        return True
    else:
        if len(str1) > len(str2):
            diffChar = False
            d = defaultdict(bool)
            for s in str2:
                d[s] = True
            print(d.keys())
            for s in str1:
                if s not in d.keys():
                    if not diffChar:
                        diffChar = True
                    else:
                        return False
        elif len(str2) > len(str1):
            diffChar = False
            d = defaultdict(bool)
            for s in str1:
                d[s] = True
            print(d.keys())
            for s in str2:
                if s not in d.keys():
                    if not diffChar:
                        diffChar = True
                    else:
                        return False
        else:
            diffChar = False
            d = defaultdict(bool)
            for s in str1:
                d[s] = True
            print(d.keys())
            for s in str2:
                if s not in d.keys():
                    if not diffChar:
                        diffChar = True
                    else:
                        return False
    return True


def stringCompression(string):
    if len(string) == 1:
        return string
    count = 1
    final = ""
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            final += (string[i] + str(count))
            count = 1
    final += (string[i] + str(count))
    return final


def rotateMatrix(matrix):
    for j in range(len(matrix)//2):
        first = j
        last = len(matrix) - 1 - j
        for i in range(first, last):
            offset = i - first
            temp = matrix[first][i]
            matrix[first][i] = matrix[last-offset][first]
            matrix[last-offset][first] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i][last]
            matrix[i][last] = temp
    return matrix


def zeroMatrix(matrix):
    changed = [[False for i in range(len(matrix))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                if not changed[i][j]:
                    for k in range(j, -1, -1):
                        matrix[i][k] = 0
                        changed[i][k] = True
                    for k in range(j, len(matrix)):
                        matrix[i][k] = 0
                        changed[i][k] = True
                    for k in range(i, -1, -1):
                        matrix[k][j] = 0
                        changed[k][j] = True
                    for k in range(i, len(matrix)):
                        matrix[k][j] = 0
                        changed[k][j] = True
                    changed[i][j] = True
    return matrix


def rotation(s1, s2):
    dup = s1 + s1
    if s2 in dup:
        return True
    return False