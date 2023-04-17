import heapq


def solution(operations):
    heap = []

    for ope in operations:
        if (ope[0] == "I"):
            heapq.heappush(heap, int(ope[1:]))
        else:
            if len(heap) == 0:
                continue
            if ope == "D -1":
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))
                heapq.heapify(heap)

    if len(heap) == 0:
        return [0, 0]
    else:
        return [max(heap), heap[0]]