
def quad(str, ind):
    head = str[ind]  # 인덱스 번째의 글자
    if head == 'w' or head == 'p':  # 상하 바꿔도 변함이 없음
        return head
    # let이 w나 b가 아닌 경우=let이 x일때
    ind += 1  # x가 나온 위치로부터 1칸 뒤
    upperLeft = quad(tree, ind)
    ind += len(upperLeft)  # 왼쪽 위가 차지하는 칸수 만큼 뒤
    upperRight = quad(tree, ind)
    ind += len(upperRight)  # 오른 위가 차지하는 칸수 만큼 뒤
    lowerLeft = quad(tree, ind)
    ind += len(lowerLeft)  # 왼쪽 아래가 차지하는 칸수 만큼 뒤
    lowerRight = quad(tree, ind)
    return 'x' + lowerLeft + lowerRight + upperLeft + upperRight


case = int(input())
for i in range(case):
    tree = input()
    print(quad(tree, 0))  # 인덱스=0

# 솔직히 직관적으로 이해가안된다.
# 직관이 좋다고 스스로 생각하지 말자 아닐 경우
# 그 직관이 무너지면 다 무너지게 된다.
# 손으로 어떻게 돌아가는지 확인해보자
