import sys
import heapq

input = sys.stdin.readline


def pop(heap):
    while len(heap) > 0:
        data, idx = heapq.heappop(heap)

        if not deleted[idx]:
            deleted[idx] = True
            return data

    return None


for _ in range(int(input())):
    k = int(input())
    min_heap = []
    max_heap = []
    idx = 0
    deleted = [False] * (k + 1)

    # 주어진 K만큼 연산 반복
    for i in range(k):
        command = input().split()
        op, data = command[0], int(command[1])

        if op == 'D':
            if data == -1:
                pop(min_heap)
            elif data == 1:
                pop(max_heap)
        elif op == 'I':
            heapq.heappush(min_heap, (data, idx))
            heapq.heappush(max_heap, (-data, idx))
            idx += 1

    max_val = pop(max_heap)

    if max_val == None:
        print("EMPTY")
    else:
        # max_value는 min_heap에서도 꺼내지기 때문에
        heapq.heappush(min_heap, (-max_val, idx))
        print(-max_val, pop(min_heap))
