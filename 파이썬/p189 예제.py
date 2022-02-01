def count(str):
    if str == "w" or str == "b":
        return 0
    c_count = 0
    i = 0
    index_List = []
    while c_count != 4:
        while str[i] == "w" or str[i] == "b":
            index_List.append(i)
            i += 1
            c_count += 1
            if c_count == 4:
                print(1, str, index_List)
                return 1, i, index_List
        if str[i] == "x":
            index_List.append(i)
            i += 1
            a, b, c = count(str[i:])
            c_count += a
            i += b
        if c_count == 4:
            print(2, str, index_List)
            return 1, i, index_List

def sep(str):
    if str
    upperLeft = ""
    upperRight = ""
    lowerLeft = ""
    lowerRight = ""
    pass

# str1 = """wxwbbbxwwbbxwxbbbwbb"""
# print(count(str1), len(str1))

str2 = "xwwwxbbwwxwxwbbbwwxxxwwbbbwwwwbxbbww"
# "xwwwb xwxwbbbww xxxwwbbbwwwwb b"
print(count(str2), len(str2))
str3 = "w"
print(count(str3), len(str3))