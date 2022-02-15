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
                index_List.append(i)
                print(1, str, index_List, i)
                return 1, i, index_List
        if str[i] == "x":
            index_List.append(i)
            i += 1
            a, b, _ = count(str[i:])
            c_count += a
            i += b
        if c_count == 4:
            index_List.append(i)
            print(3, str, index_List, i)
            return 1, i, index_List

str2 = "xwwwbxwxwbbbwwxxxwwbbbwwwwbb"
# 음.. 각 u_L, u_R, l_L, l_R 의 인덱스를 구하는 함수를 구했다.. 근데 이 이상으로 활용
# 할 수 있는지는 모르겠다.
# 어쩌다보니 이것의 기능은 쿼드트리인지 아닌지를 검사하게 되는 것이 되었다.
