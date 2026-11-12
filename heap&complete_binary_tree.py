import heapq
import math

h = []
for x in [5,3,8,1,4]:
    heapq.heappush(h, x) # heappush 함수를 이용해 자식과 부모를 비교하면서 완전이진트리를 만듦

example = [1,5,7,9,9,1,3,4,5,10] # 평범한 리스트, 완전이진트리 등으로 해석할 수 있음(2i+1,2i+2 규칙을 적용한다면)

def complete_binary_tree(arr):
    for i in range(len(arr)):
        # if (arr[2*i+1] and arr[2*i+2]) is True:
        if 2*i+1 < len(arr) and 2*i+2 < len(arr):
            print(f"parent:{arr[i]}, child1:{arr[2*i+1]}, child2:{arr[2*i+2]}")
        elif 2*i+1 < len(arr):
            print(f"parent:{arr[i]}, child1:{arr[2*i+1]}, child2:X")
complete_binary_tree(example)

# 이걸 텍스트로 형상화 하는 코드를 짜고 싶다
# def show_sideway(arr,index=0,depth=0):
#     if depth < 1:
#         if arr[index]:
#             print(arr[index],end="\t")
#             show_sideway(arr,1,1)
#         else :
#             print("변환할 리스트가 없습니다")
#     else :
#         if index >= len(arr):
#             print("반환 완료")
#         elif math.log2(index) < depth:
#             print(arr[index])
#             print("\t" * depth)
#             show_sideway(arr,index+1,depth)
#         elif math.log2(index) == depth:
#             print(arr[index],end="\t")
#             show_sideway(arr,index+1,depth+1)

# show_sideway(example)

# def show_sideway(arr):
#     parent=[] #[0, 1, 2, 3, 4]
#     for i in range(len(arr)):
#         if 2*i+1 < len(arr) or 2*i+2 < len(arr):
#             parent.append(i)
#     for i in range(len(arr)-1,-1,-1):
#         depth = math.floor(math.log2(i+1))
#         for z in parent[:]: #z= [0, 1, 2, 3, 4] ,i =[9,8,7,6,5,4,3,2,1,0]
#             if not parent:
#                 print("반환완료")
#             elif z*2+1 == i:
#                 print("\t" * (depth -1)+ str(arr[z]))
#                 print("\t" * depth + str(arr[i]))
#                 parent.remove(z)
#             elif z*2+2 ==i:
#                 print("\t" * depth + str(arr[i]))
# 구현 실패

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def build(arr,i=0):
    if i>= len(arr): # len(arr) = 10 
        return None # i가 len 범위를 벗어나면 종료
    node = Node(arr[i]) # 노드 생성
    node.left = build(arr,2*i+1) #왼쪽 자식 노드 생성
    node.right = build(arr,2*i+2) #오른쪽도 마찬가지
    return node

def show_sideway(node,depth=0):
    if node is None: #모든 노드를 출력하면 종료
        return
    show_sideway(node.right,depth+1) # 오른쪽 끝 노드로 이동
    print("\t" * depth +str(node.key)) # 출력
    show_sideway(node.left, depth +1)



root = build(example)
show_sideway(root)

# 힙 자료구조 구현 
'''
    힙 자료구조는 한 라인별로 최소값이 맨 위에 최대값이 가장 아래에 위치하게 되는 자료구조이다
    만약 값이 동일하다면 위치를 변경하지 않는다 
'''
# 최소 힙 구현
def find_leap(node,leap=[]):
    # 잎에서 뿌리를 찾는 역산 방법
    # 잎은 자식이 없는 녀석들
    if node.left:
        find_leap(node.left)
    if node.right:
        find_leap(node.right)
    leap.append() 