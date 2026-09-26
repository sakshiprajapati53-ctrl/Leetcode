import time
import heapq


# ============================================================
# 1. SORTING ALGORITHMS + TIME COMPLEXITY
# ============================================================

# ---------- Bubble Sort ----------
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        if not swapped:
            break

    return a


# ---------- Selection Sort ----------
def selection_sort(arr):
    a = arr.copy()
    n = len(a)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    return a


# ---------- Insertion Sort ----------
def insertion_sort(arr):
    a = arr.copy()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


# ============================================================
# 2. MERGE SORT
# ============================================================

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# ============================================================
# 3. QUICK SORT
# ============================================================

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for x in arr[:-1]:

        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


# ============================================================
# 4. FIBONACCI
# ============================================================

# ---------- Recursive Fibonacci ----------
def fibonacci_recursive(n):

    if n <= 1:
        return n

    return (
        fibonacci_recursive(n - 1)
        + fibonacci_recursive(n - 2)
    )


# ---------- Iterative Fibonacci ----------
def fibonacci_iterative(n):

    if n <= 1:
        return n

    a = 0
    b = 1

    for _ in range(2, n + 1):

        c = a + b

        a = b
        b = c

    return b


# ============================================================
# 5. LINEAR SEARCH
# ============================================================

def linear_search(arr, key):

    for i in range(len(arr)):

        if arr[i] == key:
            return i

    return -1


# ============================================================
# 6. BINARY SEARCH - ITERATIVE
# ============================================================

def binary_search_iterative(arr, key):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# ============================================================
# 7. BINARY SEARCH - RECURSIVE
# ============================================================

def binary_search_recursive(arr, low, high, key):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    elif arr[mid] < key:
        return binary_search_recursive(
            arr, mid + 1, high, key
        )

    else:
        return binary_search_recursive(
            arr, low, mid - 1, key
        )


# ============================================================
# 8. MAXIMUM AND MINIMUM USING DIVIDE AND CONQUER
# ============================================================

def find_min_max(arr, low, high):

    # One element
    if low == high:
        return arr[low], arr[low]

    # Two elements
    if high == low + 1:

        if arr[low] < arr[high]:
            return arr[low], arr[high]

        return arr[high], arr[low]

    mid = (low + high) // 2

    left_min, left_max = find_min_max(
        arr, low, mid
    )

    right_min, right_max = find_min_max(
        arr, mid + 1, high
    )

    minimum = min(left_min, right_min)
    maximum = max(left_max, right_max)

    return minimum, maximum


# ============================================================
# 9(a). FRACTIONAL KNAPSACK
# ============================================================

def fractional_knapsack(items, capacity):

    # items = [(value, weight), ...]

    items.sort(
        key=lambda x: x[0] / x[1],
        reverse=True
    )

    total_value = 0

    for value, weight in items:

        if capacity >= weight:

            capacity -= weight
            total_value += value

        else:

            total_value += (
                value / weight
            ) * capacity

            break

    return total_value


# ============================================================
# 9(b). ACTIVITY SELECTION
# ============================================================

def activity_selection(activities):

    # activities = [(start, finish, id), ...]

    activities.sort(key=lambda x: x[1])

    selected = []

    last_finish = -1

    for start, finish, activity_id in activities:

        if start >= last_finish:

            selected.append(
                (activity_id, start, finish)
            )

            last_finish = finish

    return selected


# ============================================================
# 9(c). HUFFMAN CODING
# ============================================================

def huffman_coding(chars, frequencies):

    heap = []

    for char, freq in zip(chars, frequencies):

        heapq.heappush(
            heap,
            (freq, char, None, None)
        )

    while len(heap) > 1:

        freq1, char1, left1, right1 = heapq.heappop(heap)
        freq2, char2, left2, right2 = heapq.heappop(heap)

        node = (
            freq1 + freq2,
            char1 + char2,
            (freq1, char1, left1, right1),
            (freq2, char2, left2, right2)
        )

        heapq.heappush(heap, node)

    root = heap[0]

    codes = {}

    def generate_codes(node, code):

        freq, chars, left, right = node

        if left is None and right is None:

            codes[chars] = code
            return

        generate_codes(left, code + "0")
        generate_codes(right, code + "1")

    generate_codes(root, "")

    return codes


# ============================================================
# 9(d). JOB SEQUENCING WITH DEADLINES
# ============================================================

def job_sequencing(jobs):

    # jobs = [(id, deadline, profit), ...]

    jobs.sort(
        key=lambda x: x[2],
        reverse=True
    )

    max_deadline = max(
        job[1] for job in jobs
    )

    slots = [None] * (max_deadline + 1)

    total_profit = 0

    for job_id, deadline, profit in jobs:

        for j in range(deadline, 0, -1):

            if slots[j] is None:

                slots[j] = job_id
                total_profit += profit

                break

    return slots[1:], total_profit


# ============================================================
# 9(e). KRUSKAL'S ALGORITHM
# ============================================================

class DSU:

    def __init__(self, n):

        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):

        if self.parent[x] != x:
            self.parent[x] = self.find(
                self.parent[x]
            )

        return self.parent[x]

    def union(self, a, b):

        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False

        if self.rank[a] < self.rank[b]:
            a, b = b, a

        self.parent[b] = a

        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1

        return True


def kruskal(vertices, edges):

    # edges = [(u, v, weight), ...]

    edges.sort(key=lambda x: x[2])

    dsu = DSU(vertices)

    mst = []
    total_weight = 0

    for u, v, weight in edges:

        if dsu.union(u, v):

            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


# ============================================================
# 9(f). PRIM'S ALGORITHM
# ============================================================

def prim(graph):

    # graph = adjacency list
    # graph[u] = [(v, weight), ...]

    n = len(graph)

    visited = [False] * n

    min_heap = [(0, 0, -1)]

    mst = []
    total_weight = 0

    while min_heap:

        weight, u, parent = heapq.heappop(
            min_heap
        )

        if visited[u]:
            continue

        visited[u] = True

        if parent != -1:

            mst.append(
                (parent, u, weight)
            )

            total_weight += weight

        for v, w in graph[u]:

            if not visited[v]:

                heapq.heappush(
                    min_heap,
                    (w, v, u)
                )

    return mst, total_weight


# ============================================================
# 10(a). 0/1 KNAPSACK - DYNAMIC PROGRAMMING
# ============================================================

def knapsack_01(weights, values, capacity):

    n = len(weights)

    dp = [
        [0] * (capacity + 1)
        for _ in range(n + 1)
    ]

    for i in range(1, n + 1):

        for w in range(capacity + 1):

            if weights[i - 1] <= w:

                dp[i][w] = max(
                    values[i - 1]
                    + dp[i - 1][
                        w - weights[i - 1]
                    ],

                    dp[i - 1][w]
                )

            else:

                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# ============================================================
# 10(b). LONGEST COMMON SUBSEQUENCE
# ============================================================

def lcs(X, Y):

    m = len(X)
    n = len(Y)

    dp = [
        [0] * (n + 1)
        for _ in range(m + 1)
    ]

    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:

                dp[i][j] = (
                    dp[i - 1][j - 1] + 1
                )

            else:

                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    return dp[m][n]


# ============================================================
# 10(c). MATRIX CHAIN MULTIPLICATION
# ============================================================

def matrix_chain_multiplication(p):

    n = len(p) - 1

    dp = [
        [0] * (n + 1)
        for _ in range(n + 1)
    ]

    for length in range(2, n + 1):

        for i in range(1, n - length + 2):

            j = i + length - 1

            dp[i][j] = float("inf")

            for k in range(i, j):

                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i - 1]
                    * p[k]
                    * p[j]
                )

                dp[i][j] = min(
                    dp[i][j],
                    cost
                )

    return dp[1][n]


# ============================================================
# 11. DFS
# ============================================================

def dfs(graph, start):

    visited = [False] * len(graph)

    result = []

    def dfs_recursive(node):

        visited[node] = True
        result.append(node)

        for neighbour in graph[node]:

            if not visited[neighbour]:

                dfs_recursive(neighbour)

    dfs_recursive(start)

    return result


# ============================================================
# 12. BFS
# ============================================================

from collections import deque


def bfs(graph, start):

    visited = [False] * len(graph)

    queue = deque()

    queue.append(start)

    visited[start] = True

    result = []

    while queue:

        node = queue.popleft()

        result.append(node)

        for neighbour in graph[node]:

            if not visited[neighbour]:

                visited[neighbour] = True

                queue.append(neighbour)

    return result


# ============================================================
# 13. DIJKSTRA'S ALGORITHM
# ============================================================

def dijkstra(graph, source):

    # graph[u] = [(v, weight), ...]

    n = len(graph)

    distance = [float("inf")] * n

    distance[source] = 0

    priority_queue = [
        (0, source)
    ]

    while priority_queue:

        current_distance, u = heapq.heappop(
            priority_queue
        )

        if current_distance > distance[u]:
            continue

        for v, weight in graph[u]:

            new_distance = (
                current_distance + weight
            )

            if new_distance < distance[v]:

                distance[v] = new_distance

                heapq.heappush(
                    priority_queue,
                    (new_distance, v)
                )

    return distance


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("DESIGN AND ANALYSIS OF ALGORITHMS")
    print("=" * 60)


    # --------------------------------------------------------
    # 1. SORTING
    # --------------------------------------------------------

    arr = [
        64, 25, 12, 22, 11,
        90, 45, 32, 76, 18
    ]

    print("\n1. SORTING ALGORITHMS")

    start = time.perf_counter()
    result = bubble_sort(arr)
    end = time.perf_counter()

    print("Bubble Sort   :", result)
    print(
        "Time          :",
        (end - start) * 1_000_000,
        "microseconds"
    )


    start = time.perf_counter()
    result = selection_sort(arr)
    end = time.perf_counter()

    print("Selection Sort:", result)
    print(
        "Time          :",
        (end - start) * 1_000_000,
        "microseconds"
    )


    start = time.perf_counter()
    result = insertion_sort(arr)
    end = time.perf_counter()

    print("Insertion Sort:", result)
    print(
        "Time          :",
        (end - start) * 1_000_000,
        "microseconds"
    )


    # --------------------------------------------------------
    # 2. MERGE SORT
    # --------------------------------------------------------

    print("\n2. MERGE SORT")

    print(
        merge_sort(arr)
    )


    # --------------------------------------------------------
    # 3. QUICK SORT
    # --------------------------------------------------------

    print("\n3. QUICK SORT")

    print(
        quick_sort(arr)
    )


    # --------------------------------------------------------
    # 4. FIBONACCI
    # --------------------------------------------------------

    print("\n4. FIBONACCI")

    n = 30

    start = time.perf_counter()

    recursive_result = fibonacci_recursive(n)

    end = time.perf_counter()

    print(
        "Recursive:",
        recursive_result
    )

    print(
        "Recursive Time:",
        (end - start) * 1_000_000,
        "microseconds"
    )


    start = time.perf_counter()

    iterative_result = fibonacci_iterative(n)

    end = time.perf_counter()

    print(
        "Iterative:",
        iterative_result
    )

    print(
        "Iterative Time:",
        (end - start) * 1_000_000,
        "microseconds"
    )


    # --------------------------------------------------------
    # 5. SEARCHING
    # --------------------------------------------------------

    print("\n5. SEARCHING")

    search_array = [
        10, 20, 30, 40, 50,
        60, 70, 80, 90, 100
    ]

    key = 70

    start = time.perf_counter()

    index = linear_search(
        search_array,
        key
    )

    end = time.perf_counter()

    print(
        "Linear Search Index:",
        index
    )

    print(
        "Time:",
        (end - start) * 1_000_000,
        "microseconds"
    )


    # --------------------------------------------------------
    # 6. BINARY SEARCH
    # --------------------------------------------------------

    print("\n6. BINARY SEARCH")

    print(
        "Iterative:",
        binary_search_iterative(
            search_array,
            key
        )
    )

    print(
        "Recursive:",
        binary_search_recursive(
            search_array,
            0,
            len(search_array) - 1,
            key
        )
    )


    # --------------------------------------------------------
    # 7. MAXIMUM AND MINIMUM
    # --------------------------------------------------------

    print("\n7. MAXIMUM AND MINIMUM")

    min_max_array = [
        45, 12, 89, 34,
        7, 56, 90, 23
    ]

    minimum, maximum = find_min_max(
        min_max_array,
        0,
        len(min_max_array) - 1
    )

    print("Minimum:", minimum)
    print("Maximum:", maximum)


    # --------------------------------------------------------
    # 8(a). FRACTIONAL KNAPSACK
    # --------------------------------------------------------

    print("\n8(a). FRACTIONAL KNAPSACK")

    items = [
        (60, 10),
        (100, 20),
        (120, 30)
    ]

    capacity = 50

    print(
        "Maximum Value:",
        fractional_knapsack(
            items,
            capacity
        )
    )


    # --------------------------------------------------------
    # 8(b). ACTIVITY SELECTION
    # --------------------------------------------------------

    print("\n8(b). ACTIVITY SELECTION")

    activities = [
        (1, 2, 1),
        (3, 4, 2),
        (0, 6, 3),
        (5, 7, 4),
        (8, 9, 5),
        (5, 9, 6)
    ]

    selected = activity_selection(
        activities
    )

    print("Selected Activities:")

    for activity in selected:
        print(activity)


    # --------------------------------------------------------
    # 8(c). HUFFMAN CODING
    # --------------------------------------------------------

    print("\n8(c). HUFFMAN CODING")

    chars = [
        "A", "B", "C",
        "D", "E", "F"
    ]

    frequencies = [
        5, 9, 12,
        13, 16, 45
    ]

    codes = huffman_coding(
        chars,
        frequencies
    )

    for char, code in codes.items():

        print(
            char,
            ":",
            code
        )


    # --------------------------------------------------------
    # 8(d). JOB SEQUENCING
    # --------------------------------------------------------

    print("\n8(d). JOB SEQUENCING")

    jobs = [
        ("A", 2, 100),
        ("B", 1, 19),
        ("C", 2, 27),
        ("D", 1, 25),
        ("E", 3, 15)
    ]

    sequence, profit = job_sequencing(
        jobs
    )

    print(
        "Job Sequence:",
        sequence
    )

    print(
        "Total Profit:",
        profit
    )


    # --------------------------------------------------------
    # 8(e). KRUSKAL
    # --------------------------------------------------------

    print("\n8(e). KRUSKAL")

    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]

    mst, total = kruskal(
        4,
        edges
    )

    print("MST:")

    for edge in mst:
        print(edge)

    print(
        "Total Weight:",
        total
    )


    # --------------------------------------------------------
    # 8(f). PRIM
    # --------------------------------------------------------

    print("\n8(f). PRIM")

    graph = [
        [(1, 10), (2, 6), (3, 5)],
        [(0, 10), (3, 15)],
        [(0, 6), (3, 4)],
        [(0, 5), (1, 15), (2, 4)]
    ]

    mst, total = prim(graph)

    print("MST:")

    for edge in mst:
        print(edge)

    print(
        "Total Weight:",
        total
    )


    # --------------------------------------------------------
    # 9(a). 0/1 KNAPSACK
    # --------------------------------------------------------

    print("\n9(a). 0/1 KNAPSACK")

    weights = [
        10, 20, 30
    ]

    values = [
        60, 100, 120
    ]

    capacity = 50

    print(
        "Maximum Value:",
        knapsack_01(
            weights,
            values,
            capacity
        )
    )


    # --------------------------------------------------------
    # 9(b). LCS
    # --------------------------------------------------------

    print("\n9(b). LONGEST COMMON SUBSEQUENCE")

    X = "ABCBDAB"
    Y = "BDCABA"

    print(
        "LCS Length:",
        lcs(X, Y)
    )


    # --------------------------------------------------------
    # 9(c). MATRIX CHAIN MULTIPLICATION
    # --------------------------------------------------------

    print("\n9(c). MATRIX CHAIN MULTIPLICATION")

    dimensions = [
        40, 20, 30, 10, 30
    ]

    print(
        "Minimum Multiplications:",
        matrix_chain_multiplication(
            dimensions
        )
    )


    # --------------------------------------------------------
    # 10. DFS AND BFS
    # --------------------------------------------------------

    print("\n10. DFS AND BFS")

    graph = [
        [1, 2],
        [0, 3, 4],
        [0, 4],
        [1, 5],
        [1, 2, 5],
        [3, 4]
    ]

    print(
        "DFS:",
        dfs(graph, 0)
    )

    print(
        "BFS:",
        bfs(graph, 0)
    )


    # --------------------------------------------------------
    # 11. DIJKSTRA
    # --------------------------------------------------------

    print("\n11. DIJKSTRA")

    weighted_graph = [
        [(1, 10), (4, 5)],
        [(2, 1), (4, 2)],
        [(3, 4)],
        [(0, 7), (2, 6)],
        [(1, 3), (2, 9), (3, 2)]
    ]

    distances = dijkstra(
        weighted_graph,
        0
    )

    print(
        "Shortest distances from vertex 0:"
    )

    for vertex, distance in enumerate(
        distances
    ):

        print(
            "0 ->",
            vertex,
            "=",
            distance
        )


    print("\n" + "=" * 60)
    print("PROGRAM COMPLETED")
    print("=" * 60)