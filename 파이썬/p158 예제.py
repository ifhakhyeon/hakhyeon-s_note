# for i in range(n):
#     pass
#
# a =[[0 for _ in range(n)] for _ in range(n)]
# print(a)


# friend_done = []
# def find_friend(ret,friend_done):
#     for i in range(n):
#         if i in friend_done:
#             continue
#         print(i)
#         print(friend_done)
#         for j in range(m):
#             if friends[j][0] == i and not(friends[j][1] in friend_done) and not(friends[j][0] in friend_done):
#                 실패원인 1 여기서 append를 한거
#                 friend_done.append(i)
#                 friend_done.append(friends[j][1])
#     if len(friend_done) == n:
#         ret += 1
#
#     return(ret)
#
#
# print(find_friend(0,friend_done))

# 찾은 목록 = taken
# n = 사람수
# friends_list = 입력받은 짝꿍 목록

import sys
input = sys.stdin.readline

# 이미 고른 숫자가 주어지면 짝이 없는 최소숫자 함수 반환
def min_num(taken):
    ret = -1
    for i in range(n):
        if not(i in taken):
            ret = i
            break
    return ret

# 숫자가 주어지면 그 숫자랑 가능한 짝을 모두 골라주는 것 리턴값이 이 차원 리스트임.
def find_friends(num):
    ret = []
    for i in friends_list:
        if num in i and (i[0] > num or i[1] > num):
            ret.append(i)
    return ret

#C는 반복횟수
C = int(input())
for _ in range(C):
    n, m = map(int, input().split())

    # 이 아래는 입려값은 수를 2차원 리스트로 바꾸는 것. 처음부터 친구목록은 2차원 리스트로 생각해서
    # 불필요한 짓을 해야함.. 조금 더 깔끔하게 만들 수도 있을거 같았음.
    save_input = map(int, input().split())
    friends_list = [[0 for _ in range(2)] for _ in range(m)]
    for i, j in enumerate(save_input):
        friends_list[i // 2][i % 2] = j

    # taken은 이미 골라진 숫자 따라서 처음 실행할때는 taken = [] 으로 해야함
    def final(taken):
        # 최소 숫자를 고르고
        n = min_num(taken)

        # 기저사례를 판단 최소숫자가 -1(최소숫자가 없다 = 이미 다 짝을 찾았다.)
        # 이면 1을 리턴 이건 아래 최종으로 리턴해야하는 횟수를 + 해주기 위해서
        # 제귀함수를 짤 때 이런 스킬은 꼭 필요할 듯!
        if n == -1:
            return 1

        # 처음 ret 값을 0 으로 지정하고 이후 제귀에서 0으로 되도 되는 이유는
        # 어짜피 ret 1즉 횟수만 추가하기 위해 아래로 내려간 제귀들은 최대 1만 반환해야함
        ret = 0
        canfriend = find_friends(n)
        for i in canfriend:
            # 기저사례 만약 친구가능 목록에 있는 수가 이미 taken 안에 들어가 있으면
            # 그 for 문은 continue 하는 것
            if i[0] in taken or i[1] in taken:
                continue

            # 여기서 중요한것 taken 에 append 를 하면 taken 은 이전 제귀로 돌아갈 때
            # 값이 바뀌므로
            # 제귀 안에서 들어갈 taken 을 조작해준다1
            ret += final(taken + i)
        return ret


    print(final([]))

# 처음 생각한 풀이.
# ret = 0
# fuc(찾은목록):
#     ret가장작은수
#
# fuc(숫자):
#     ret짝꿍목록을 찾고
#
# fuc(찾은목록):
#     n = ret가장작은수
#
#     if 가장 작은 수가 기저사례이면:
#         return 1
#
#     ret = 0
#
#     list = ret짝꿍목록
#
#     for 짝꿍목록:
#         !!! 여기서 append를 시킨다는 생각 때문에 고생했음 !!!
#         append를시키고
#         ret += fuc(찾은목록)
