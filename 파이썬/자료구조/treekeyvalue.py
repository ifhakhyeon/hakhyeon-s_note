class Node:
    """생성자"""
    def __init__(self, key, value, left, right):
        self.key = key      # 키
        self.value = value  # 값
        self.left = left    # 왼쪽 자식 참조
        self.right = right  # 오른쪽 자식 참조

class BinarySearchTree(object):
    def __init__(self) -> None:       # 생성자  /  -> 기능주석임
        self.root = None              # 루트 설정

    def find(self, key) -> int:
        node = self.root              # 루트에 주목
        while True:
            if node is None:          # 더 이상 진행할 수 없으면
                return False          # 검색 실패
            if key == node.key:       # key와 노드 p의 키가 같으면
                return node.value     # 검색 성공
            elif key < node.key:      # key가 작으면
                node = node.left      # 왼쪽 서브 트리에서 검색
            else:                     # key가 작으면
                node = node.right     # 오른쪽 서브 트리에서 검색

    def insert(self, key, value) -> bool:
        def add_node(node, key, value) -> bool:         # 노드 추가하는 내부 함수
            if key == node.key:                         # 탐색하고 적절한 자리에 삽입
                return False                            # 이미 삽입하려는 키가 있으면 false 처리
            elif key < node.key:                        # 삽입하려는 키가 현재 탐색 노드의 키보다 작으면
                if node.left is None:                   # 그 탐색 노드의 왼쪽 자식이 없다면 바로 그 자리에 삽입
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)     # 자식이 있으면 재귀함수 호출로 한번 더 들어감
            else:                                       # 삽입하려는 키가 현재 탐색 노드의 키보다 크다면
                if node.right is None:                  # 그 탐색 노드의 오른쪽 자식이 없다면 바로 그 자리에 삽입
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)    # 자식이 있으면 재귀함수 호출로 한번 더 들어감
            return True

        if self.root is None:                           # 루트가 있는 경우
            self.root = Node(key, value, None, None)
            return True
        else:                                           # 루트가 없는 경우
            return add_node(self.root, key, value)      # 리턴값은 내부함수 리턴 값

    def delete(self, key) -> bool:
        node = self.root                                # 현재 노드로 지정
        parent = None                                   # 현재 노드의 부모 노드
        is_left_child = True                            # node는 parent의 왼쪽 자식 노드인지 오른쪽 자식 노드인지 확인

        while True:                                     # 삭제할 노드 탐색
            if node is None:
                return False
            if key == node.key:
                break
            else:
                parent = node
                if key <= node.key:
                    node = node.left
                    is_left_child = True                # 왼쪽 자식 노드로 내려가니까 플래그를 True로 설정
                else:
                    node = node.right
                    is_left_child = False               # 오른쪽 자식 노드로 내려가니까 플래그를 True로 설정

        # 키를 찾은 뒤에 자식이 없는 노드이면 or 자식이 1개 있는 노드이면
        if node.left is None:                           # 왼쪽 자식이 없으면
            if node is self.root:                       # 만약 삭제 노드가 root이면, 바로 오른쪽 자식으로 대체한다.
                self.root = node.right
            # 아래의 parent는 탐색 시 찾은 노드의 바로 위 부모가 됨.(탐색 로직에서 그렇게 적용)
            # parent - node - node의 자식의 구도가 있으면 node라는 중간이 빠지기 때문에 parent의 자식과 node의 자식을 연결
            # (node의 자식이 없으면 자연스레 None이 들어감)
            elif is_left_child:                         # 왼쪽 자식 노드가 있는 것이니까
                parent.left = node.right                # 부모의 왼쪽 참조가 오른쪽 자식을 가리킴
            else:                                       # 오른쪽 자식 노드가 있는 것이니까
                parent.right = node.right               # 부모의 오른쪽 참조가 오른쪽 자식을 가리킴

        elif node.right is None:                        # 오른쪽 자식이 없으면
            if node is self.root:
                self.root = node.left                   # 만약 삭제 노드가 root이면, 바로 왼쪽 자식으로 대체한다.
            elif is_left_child:
                parent.left = node.left                 # 부모의 왼쪽 참조가 왼쪽 자식을 가리킴
            else:
                parent.right = node.left                # 부모의 오른쪽 참조가 왼쪽 자식을 가리킴

        # 자식이 2개 있는 노드이면
        else:                                           # 무조건 오른쪽 서브트리에서 대체할 노드를 찾는다.
            parent = node                               # 오른쪽 서브트리에서 가장 작은 노드로 대체한다.

            # parent를 지정한 이유 : 지우는 노드로 지정되는데, 하위 자식 노드가 많으면 node 삭제 시 조정이 일어남.
            # node말고 그 하위 노드들을 관리할 주체가 필요함.
            # 그때 가장 하단의 자식 노드의 연결을 끊기위해 parent를 일단 삭제할 node로 지정.
            # 자세한건 그림으로 그려봄 아무튼 그렇다네..

            node_min_right = node.right                 # 오른쪽 서브트리에서 가장 작은 노드를 찾기 위해 초기값 설정
            is_right_child = True                       # 오른쪽 서브트리에서 가장 작은 노드가 부모 노드와
                                                        # 어떤 관계(왼쪽,오른쪽)인지 파악하기 위해 세팅

            while node_min_right.left is not None:      # 가장 작은 노드를 찾기 위해 탐색
                parent = node_min_right
                node_min_right = node_min_right.left
                is_right_child = False

            node.key = node_min_right.key               # 가장 작은 노드를 찾았으니 삭제하려는 노드를 대체
            node.value = node_min_right.value           # 이 과정에서 이미 node 의 값은 삭제됐고 링크 후처리를 해야함

            # is_right_child가 트루가 되려면, 삭제 노드의 오른쪽 서브트리중 왼쪽 자식이 없어야 함.
            if is_right_child:
                # node_min_right.right 로 지정하는 이유 :
                # 가장 작은 노드가 오른쪽 자식을 갖고 있을 수 있음.
                # node_max_left의 왼쪽 자식 노드만 있거나 자식이 없는 경우만 가능. 자식이 없으면 None으로 적용됨.
                parent.right = node_min_right.right
            else:
                parent.left = node_min_right.right

        return True  # 정상적으로 조정되었으니 true

    def dump(self):
        def print_subtree(node):
            # 전위 순회로 출력
            if node is not None:
                print(f'{node.key} {node.value}')
                print_subtree(node.left)
                print_subtree(node.right)

        root = self.root
        print_subtree(root)
