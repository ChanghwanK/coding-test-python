import sys
import heapq
input = sys.stdin.readline
heap = []


def int_input():
    return int(input())


N = int_input()

for _ in range(N):
    val = int_input()
    if val == 0:
        if len(heap) == 0:
            print(0)
        else:
            absolute, origin = heapq.heappop(heap)
            print(origin)
    else:
        heapq.heappush(heap, (abs(val), val))
