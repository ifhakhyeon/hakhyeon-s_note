#hasWord(y,x,word) = 보글 게임판의 (y,x)에서 시작하는 단어 word의
#존재여부를 반환한다.
#보글 게임판은 5*5 이다.

#완전 탐색을 사용할 것이다.
#word 의 첫글자 위치에서 다음글자로 갈 방향을 순서대로 탐색하고 없으면 재귀호출로
#본래 함수를 반환한다.

boggle = [["N","N","N","N","S"],["N","E","E","E","N"],["N","E","Y","E","N"],["N","E","E","E","N"],["N","N","N","N","S"]]
# boggle = [["U","R","L","P","M"],["X","P","R","E","T"],["G","I","A","E","T"],["X","T","N","Z","Y"],["X","O","Q","R","S"]]
# x와 y가 움직일 수 있는 목록
move = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

def hasWord(y,x,str):
    # print("처음y",y)
    # print("처음x",x)
    # print("비교대상",boggle[y][x])
    # print("문자",str,len(str))

    #기저 사례 판단.

    #위치가 범위에 없으면 False 반환
    if not(0 <= y <= 4 and 0 <= x <= 4):
        return False
    #시작하는 위치의 첫글자가 str 의 첫글자랑 다르면 False 반환
    if boggle[y][x] != str[0]:
        # print(8888)
        return False
    #str의 길이가 1 이면 참 반환
    # and boggle[y][x] == str 의 조건을 추가 할 필요가 없는게 어짜피 위에서 검사.
    if len(str) == 1:
        # print(7777)
        return True
        # print(9999)



    for i in range(len(str)-1):
        #첫째칸은 검사를 했으니 바로 다음칸으로 이동
        for M in move:
            # print("좌표",M)
            if boggle[y+M[0]][x+M[1]] == str[i+1]:
                # print("갈위치",boggle[y+M[0]][x+M[1]])
                # print("갈위치랑 비교",str[i+1])
                # print("다음 들어갈것",str[1:])

                #여기서 if 문을 넣고 결과가 True 가 되도록 반환해야지 위에 len(str) == 1 에서 True 가 반환되기를 바라면
                #안된다. 왜냐하면 그건 if 문을 돌려 나온 결과지 hasWord를 돌려 나온 return이 아니기 때문이다. 이건
                #재귀함수를 만들 떄 중요한 스킬인거 같다.
                if(hasWord(y+M[0],x+M[1],str[1:])):
                    return True


    #마찬가지로 여기서 return False가 없으면 틀린 값에 대해서 결과값은 NONE이 나오기 때문에 이것또한 주의해야한 사항이다.
    return False

print(hasWord(2,2,"YES"))
