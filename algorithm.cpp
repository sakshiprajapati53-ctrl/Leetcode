#include <iostream>
using namespace std;
#include <vector>
#include <algorithm>
#include <queue>
#include <chrono>
using namespace std;
using namespace chrono;


// ---------- Bubble Sort ----------
void bubbleSort(vector<int>& a) {
    int n = a.size();

    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;

        for (int j = 0; j < n - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                swap(a[j], a[j + 1]);
                swapped = true;
            }
        }

        if (!swapped)
            break;
    }
}

// ---------- Selection Sort ----------
void selectionSort(vector<int>& a) {
    int n = a.size();

    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;

        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[minIndex])
                minIndex = j;
        }

        swap(a[i], a[minIndex]);
    }
}

// ---------- Insertion Sort ----------
void insertionSort(vector<int>& a) {
    int n = a.size();

    for (int i = 1; i < n; i++) {
        int key = a[i];
        int j = i - 1;

        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }

        a[j + 1] = key;
    }
}

//   2. MERGE SORT

void mergeArray(vector<int>& a, int low, int mid, int high) {

    vector<int> temp;

    int i = low;
    int j = mid + 1;

    while (i <= mid && j <= high) {

        if (a[i] <= a[j])
            temp.push_back(a[i++]);
        else
            temp.push_back(a[j++]);
    }

    while (i <= mid)
        temp.push_back(a[i++]);

    while (j <= high)
        temp.push_back(a[j++]);

    for (int k = 0; k < temp.size(); k++)
        a[low + k] = temp[k];
}

void mergeSort(vector<int>& a, int low, int high) {

    if (low >= high)
        return;

    int mid = low + (high - low) / 2;

    mergeSort(a, low, mid);
    mergeSort(a, mid + 1, high);

    mergeArray(a, low, mid, high);
}

//   3. QUICK SORT

int partitionArray(vector<int>& a, int low, int high) {

    int pivot = a[high];

    int i = low - 1;

    for (int j = low; j < high; j++) {

        if (a[j] < pivot) {
            i++;
            swap(a[i], a[j]);
        }
    }

    swap(a[i + 1], a[high]);

    return i + 1;
}

void quickSort(vector<int>& a, int low, int high) {

    if (low < high) {

        int pi = partitionArray(a, low, high);

        quickSort(a, low, pi - 1);
        quickSort(a, pi + 1, high);
    }
}

//   4. FIBONACCI

// Recursive Fibonacci
long long fibRecursive(int n) {

    if (n <= 1)
        return n;

    return fibRecursive(n - 1) + fibRecursive(n - 2);
}

// Iterative Fibonacci
long long fibIterative(int n) {

    if (n <= 1)
        return n;

    long long a = 0;
    long long b = 1;

    for (int i = 2; i <= n; i++) {

        long long c = a + b;

        a = b;
        b = c;
    }

    return b;
}

//   5. LINEAR SEARCH

int linearSearch(vector<int>& a, int key) {

    for (int i = 0; i < a.size(); i++) {

        if (a[i] == key)
            return i;
    }

    return -1;
}

//   6. BINARY SEARCH - ITERATIVE

int binarySearchIterative(vector<int>& a, int key) {

    int low = 0;
    int high = a.size() - 1;

    while (low <= high) {

        int mid = low + (high - low) / 2;

        if (a[mid] == key)
            return mid;

        else if (a[mid] < key)
            low = mid + 1;

        else
            high = mid - 1;
    }

    return -1;
}

//   7. BINARY SEARCH - RECURSIVE

int binarySearchRecursive(vector<int>& a,
                          int low,
                          int high,
                          int key) {

    if (low > high)
        return -1;

    int mid = low + (high - low) / 2;

    if (a[mid] == key)
        return mid;

    if (a[mid] < key)
        return binarySearchRecursive(a, mid + 1, high, key);

    return binarySearchRecursive(a, low, mid - 1, key);
}

//   8. MAXIMUM AND MINIMUM USING DIVIDE AND CONQUER

pair<int, int> findMinMax(vector<int>& a, int low, int high) {

    // Base case: one element
    if (low == high)
        return {a[low], a[low]};

    // Base case: two elements
    if (high == low + 1) {

        if (a[low] < a[high])
            return {a[low], a[high]};

        return {a[high], a[low]};
    }

    int mid = low + (high - low) / 2;

    pair<int, int> left = findMinMax(a, low, mid);
    pair<int, int> right = findMinMax(a, mid + 1, high);

    int minimum = min(left.first, right.first);
    int maximum = max(left.second, right.second);

    return {minimum, maximum};
}

//   9. FRACTIONAL KNAPSACK

struct Item {
    int value;
    int weight;
};

bool compareRatio(Item a, Item b) {

    return (double)a.value / a.weight >
           (double)b.value / b.weight;
}

double fractionalKnapsack(vector<Item> items, int capacity) {

    sort(items.begin(), items.end(), compareRatio);

    double totalValue = 0;

    for (auto item : items) {

        if (capacity >= item.weight) {

            capacity -= item.weight;
            totalValue += item.value;
        }

        else {

            totalValue +=
                (double)item.value / item.weight * capacity;

            break;
        }
    }

    return totalValue;
}

//   10. ACTIVITY SELECTION

struct Activity {
    int start;
    int finish;
    int id;
};

bool compareActivity(Activity a, Activity b) {

    return a.finish < b.finish;
}

void activitySelection(vector<Activity> activities) {

    sort(activities.begin(),
         activities.end(),
         compareActivity);

    cout << "\nSelected Activities:\n";

    int lastFinish = -1;

    for (auto activity : activities) {

        if (activity.start >= lastFinish) {

            cout << "Activity " << activity.id
                 << " (" << activity.start
                 << ", " << activity.finish << ")\n";

            lastFinish = activity.finish;
        }
    }
}

//   11. HUFFMAN CODING

struct HuffmanNode {

    char ch;
    int freq;

    HuffmanNode* left;
    HuffmanNode* right;

    HuffmanNode(char c, int f) {

        ch = c;
        freq = f;

        left = nullptr;
        right = nullptr;
    }
};

struct CompareNode {

    bool operator()(HuffmanNode* a,
                    HuffmanNode* b) {

        return a->freq > b->freq;
    }
};

void generateCodes(HuffmanNode* root,
                   string code) {

    if (root == nullptr)
        return;

    if (!root->left && !root->right) {

        cout << root->ch
             << " : "
             << code
             << endl;

        return;
    }

    generateCodes(root->left, code + "0");
    generateCodes(root->right, code + "1");
}

void huffmanCoding(vector<char> chars,
                   vector<int> freq) {

    priority_queue<HuffmanNode*,
                   vector<HuffmanNode*>,
                   CompareNode> pq;

    for (int i = 0; i < chars.size(); i++) {

        pq.push(new HuffmanNode(chars[i], freq[i]));
    }

    while (pq.size() > 1) {

        HuffmanNode* left = pq.top();
        pq.pop();

        HuffmanNode* right = pq.top();
        pq.pop();

        HuffmanNode* parent =
            new HuffmanNode('$',
                            left->freq + right->freq);

        parent->left = left;
        parent->right = right;

        pq.push(parent);
    }

    cout << "\nHuffman Codes:\n";

    generateCodes(pq.top(), "");
}

//   12. JOB SEQUENCING WITH DEADLINES

struct Job {

    char id;
    int deadline;
    int profit;
};

bool compareJob(Job a, Job b) {

    return a.profit > b.profit;
}

void jobSequencing(vector<Job> jobs) {

    sort(jobs.begin(),
         jobs.end(),
         compareJob);

    int maxDeadline = 0;

    for (auto job : jobs)
        maxDeadline = max(maxDeadline,
                          job.deadline);

    vector<char> slot(maxDeadline + 1, '-');

    int totalProfit = 0;

    for (auto job : jobs) {

        for (int j = job.deadline; j >= 1; j--) {

            if (slot[j] == '-') {

                slot[j] = job.id;

                totalProfit += job.profit;

                break;
            }
        }
    }

    cout << "\nJob Sequence: ";

    for (int i = 1; i <= maxDeadline; i++)
        cout << slot[i] << " ";

    cout << "\nTotal Profit = "
         << totalProfit << endl;
}

//   13. KRUSKAL'S ALGORITHM

struct Edge {

    int u;
    int v;
    int weight;
};

bool compareEdge(Edge a, Edge b) {

    return a.weight < b.weight;
}

class DSU {

    vector<int> parent;
    vector<int> rankValue;

public:

    DSU(int n) {

        parent.resize(n);

        rankValue.resize(n, 0);

        for (int i = 0; i < n; i++)
            parent[i] = i;
    }

    int find(int x) {

        if (parent[x] == x)
            return x;

        return parent[x] =
            find(parent[x]);
    }

    bool unite(int a, int b) {

        a = find(a);
        b = find(b);

        if (a == b)
            return false;

        if (rankValue[a] < rankValue[b])
            swap(a, b);

        parent[b] = a;

        if (rankValue[a] == rankValue[b])
            rankValue[a]++;

        return true;
    }
};

void kruskal(int V, vector<Edge> edges) {

    sort(edges.begin(),
         edges.end(),
         compareEdge);

    DSU dsu(V);

    int totalWeight = 0;

    cout << "\nKruskal MST:\n";

    for (auto edge : edges) {

        if (dsu.unite(edge.u, edge.v)) {

            cout << edge.u
                 << " - "
                 << edge.v
                 << " : "
                 << edge.weight
                 << endl;

            totalWeight += edge.weight;
        }
    }

    cout << "Total MST Weight = "
         << totalWeight << endl;
}

//   14. PRIM'S ALGORITHM

void prim(vector<vector<pair<int, int>>> graph) {

    int V = graph.size();

    vector<int> key(V, INT_MAX);
    vector<bool> inMST(V, false);
    vector<int> parent(V, -1);

    key[0] = 0;

    for (int count = 0; count < V; count++) {

        int u = -1;

        for (int i = 0; i < V; i++) {

            if (!inMST[i] &&
                (u == -1 || key[i] < key[u])) {

                u = i;
            }
        }

        inMST[u] = true;

        for (auto [v, weight] : graph[u]) {

            if (!inMST[v] &&
                weight < key[v]) {

                key[v] = weight;
                parent[v] = u;
            }
        }
    }

    int totalWeight = 0;

    cout << "\nPrim MST:\n";

    for (int i = 1; i < V; i++) {

        cout << parent[i]
             << " - "
             << i
             << " : "
             << key[i]
             << endl;

        totalWeight += key[i];
    }

    cout << "Total MST Weight = "
         << totalWeight << endl;
}

//   15. 0/1 KNAPSACK - DYNAMIC PROGRAMMING

int knapsack01(vector<int> weight,
               vector<int> value,
               int capacity) {

    int n = weight.size();

    vector<vector<int>> dp(
        n + 1,
        vector<int>(capacity + 1, 0)
    );

    for (int i = 1; i <= n; i++) {

        for (int w = 0; w <= capacity; w++) {

            if (weight[i - 1] <= w) {

                dp[i][w] =
                    max(
                        value[i - 1] +
                        dp[i - 1][w - weight[i - 1]],

                        dp[i - 1][w]
                    );
            }

            else {

                dp[i][w] =
                    dp[i - 1][w];
            }
        }
    }

    return dp[n][capacity];
}

//   16. LONGEST COMMON SUBSEQUENCE

int LCS(string X, string Y) {

    int m = X.length();
    int n = Y.length();

    vector<vector<int>> dp(
        m + 1,
        vector<int>(n + 1, 0)
    );

    for (int i = 1; i <= m; i++) {

        for (int j = 1; j <= n; j++) {

            if (X[i - 1] == Y[j - 1]) {

                dp[i][j] =
                    dp[i - 1][j - 1] + 1;
            }

            else {

                dp[i][j] =
                    max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    );
            }
        }
    }

    return dp[m][n];
}

//   17. MATRIX CHAIN MULTIPLICATION

int matrixChain(vector<int> p) {

    int n = p.size() - 1;

    vector<vector<int>> dp(
        n + 1,
        vector<int>(n + 1, 0)
    );

    for (int len = 2; len <= n; len++) {

        for (int i = 1;
             i <= n - len + 1;
             i++) {

            int j = i + len - 1;

            dp[i][j] = INT_MAX;

            for (int k = i;
                 k < j;
                 k++) {

                int cost =
                    dp[i][k] +
                    dp[k + 1][j] +
                    p[i - 1] *
                    p[k] *
                    p[j];

                dp[i][j] =
                    min(dp[i][j], cost);
            }
        }
    }

    return dp[1][n];
}

//   18. DFS

void DFSUtil(int node,
             vector<vector<int>>& graph,
             vector<bool>& visited) {

    visited[node] = true;

    cout << node << " ";

    for (int neighbour : graph[node]) {

        if (!visited[neighbour])
            DFSUtil(neighbour,
                    graph,
                    visited);
    }
}

void DFS(vector<vector<int>>& graph,
         int start) {

    vector<bool> visited(graph.size(), false);

    cout << "DFS: ";

    DFSUtil(start, graph, visited);

    cout << endl;
}

//   19. BFS

void BFS(vector<vector<int>>& graph,
         int start) {

    vector<bool> visited(graph.size(), false);

    queue<int> q;

    q.push(start);

    visited[start] = true;

    cout << "BFS: ";

    while (!q.empty()) {

        int node = q.front();

        q.pop();

        cout << node << " ";

        for (int neighbour : graph[node]) {

            if (!visited[neighbour]) {

                visited[neighbour] = true;

                q.push(neighbour);
            }
        }
    }

    cout << endl;
}

//   20. DIJKSTRA'S ALGORITHM

void dijkstra(
    vector<vector<pair<int, int>>> graph,
    int source) {

    int V = graph.size();

    vector<int> distance(V, INT_MAX);

    priority_queue<
        pair<int, int>,
        vector<pair<int, int>>,
        greater<pair<int, int>>
    > pq;

    distance[source] = 0;

    pq.push({0, source});

    while (!pq.empty()) {

        auto [dist, node] = pq.top();

        pq.pop();

        if (dist > distance[node])
            continue;

        for (auto [neighbour, weight] :
             graph[node]) {

            if (distance[node] + weight <
                distance[neighbour]) {

                distance[neighbour] =
                    distance[node] + weight;

                pq.push(
                    {distance[neighbour],
                     neighbour}
                );
            }
        }
    }

    cout << "\nDijkstra Shortest Paths:\n";

    for (int i = 0; i < V; i++) {

        cout << source
             << " -> "
             << i
             << " = ";

        if (distance[i] == INT_MAX)
            cout << "INF";

        else
            cout << distance[i];

        cout << endl;
    }
}

//   DISPLAY ARRAY

void display(vector<int>& a) {

    for (int x : a)
        cout << x << " ";

    cout << endl;
}


int main() {


    //   1. SORTING + TIME COMPLEXITY

    vector<int> arr = {
        64, 25, 12, 22, 11,
        90, 45, 32, 76, 18
    };

    cout << "\n1. SORTING ALGORITHMS\n";

    vector<int> a1 = arr;

    auto start = high_resolution_clock::now();

    bubbleSort(a1);

    auto end = high_resolution_clock::now();

    cout << "Bubble Sort: ";
    display(a1);

    cout << "Time: "
         << duration_cast<nanoseconds>(
                end - start
            ).count()
         << " ns\n";


    vector<int> a2 = arr;

    start = high_resolution_clock::now();

    selectionSort(a2);

    end = high_resolution_clock::now();

    cout << "Selection Sort: ";
    display(a2);

    cout << "Time: "
         << duration_cast<nanoseconds>(
                end - start
            ).count()
         << " ns\n";


    vector<int> a3 = arr;

    start = high_resolution_clock::now();

    insertionSort(a3);

    end = high_resolution_clock::now();

    cout << "Insertion Sort: ";
    display(a3);

    cout << "Time: "
         << duration_cast<nanoseconds>(
                end - start
            ).count()
         << " ns\n";


//       2. MERGE SORT

    cout << "\n2. MERGE SORT\n";

    vector<int> mergeArrayInput = arr;

    mergeSort(
        mergeArrayInput,
        0,
        mergeArrayInput.size() - 1
    );

    display(mergeArrayInput);

    //   3. QUICK SORT

    cout << "\n3. QUICK SORT\n";

    vector<int> quickArray = arr;

    quickSort(
        quickArray,
        0,
        quickArray.size() - 1
    );

    display(quickArray);


    //   4. FIBONACCI

    cout << "\n4. FIBONACCI\n";

    int n = 30;

    start = high_resolution_clock::now();

    long long recursiveResult =
        fibRecursive(n);

    end = high_resolution_clock::now();

    cout << "Recursive Fibonacci = "
         << recursiveResult << endl;

    cout << "Recursive Time = "
         << duration_cast<microseconds>(
                end - start
            ).count()
         << " microseconds\n";


    start = high_resolution_clock::now();

    long long iterativeResult =
        fibIterative(n);

    end = high_resolution_clock::now();

    cout << "Iterative Fibonacci = "
         << iterativeResult << endl;

    cout << "Iterative Time = "
         << duration_cast<microseconds>(
                end - start
            ).count()
         << " microseconds\n";


//       5. SEARCHING

    cout << "\n5. SEARCHING\n";

    vector<int> searchArray = {
        10, 20, 30, 40, 50,
        60, 70, 80, 90, 100
    };

    int key = 70;

    start = high_resolution_clock::now();

    int linearResult =
        linearSearch(searchArray, key);

    end = high_resolution_clock::now();

    cout << "Linear Search Index = "
         << linearResult << endl;

    cout << "Time = "
         << duration_cast<nanoseconds>(
                end - start
            ).count()
         << " ns\n";


    
//       6. BINARY SEARCH

    int binaryResult =
        binarySearchIterative(
            searchArray,
            key
        );

    cout << "Binary Search Iterative Index = "
         << binaryResult << endl;


    binaryResult =
        binarySearchRecursive(
            searchArray,
            0,
            searchArray.size() - 1,
            key
        );

    cout << "Binary Search Recursive Index = "
         << binaryResult << endl;


    //   7. MAXIMUM AND MINIMUM

    cout << "\n6. MAXIMUM AND MINIMUM\n";

    vector<int> minMaxArray = {
        45, 12, 89, 34, 7,
        56, 90, 23
    };

    pair<int, int> result =
        findMinMax(
            minMaxArray,
            0,
            minMaxArray.size() - 1
        );

    cout << "Minimum = "
         << result.first << endl;

    cout << "Maximum = "
         << result.second << endl;


//       8. FRACTIONAL KNAPSACK

    cout << "\n7(a). FRACTIONAL KNAPSACK\n";

    vector<Item> items = {
        {60, 10},
        {100, 20},
        {120, 30}
    };

    int capacity = 50;

    cout << "Maximum Value = "
         << fractionalKnapsack(
                items,
                capacity
            )
         << endl;


     //  9. ACTIVITY SELECTION

    cout << "\n7(b). ACTIVITY SELECTION\n";

    vector<Activity> activities = {
        {1, 2, 1},
        {3, 4, 2},
        {0, 6, 3},
        {5, 7, 4},
        {8, 9, 5},
        {5, 9, 6}
    };

    activitySelection(activities);

     //  10. HUFFMAN CODING

    cout << "\n7(c). HUFFMAN CODING\n";

    vector<char> chars = {
        'A', 'B', 'C', 'D', 'E', 'F'
    };

    vector<int> freq = {
        5, 9, 12, 13, 16, 45
    };

    huffmanCoding(chars, freq);


     //  11. JOB SEQUENCING

    cout << "\n7(d). JOB SEQUENCING\n";

    vector<Job> jobs = {
        {'A', 2, 100},
        {'B', 1, 19},
        {'C', 2, 27},
        {'D', 1, 25},
        {'E', 3, 15}
    };

    jobSequencing(jobs);


    //   12. KRUSKAL

    cout << "\n7(e). KRUSKAL ALGORITHM\n";

    vector<Edge> edges = {

        {0, 1, 10},
        {0, 2, 6},
        {0, 3, 5},
        {1, 3, 15},
        {2, 3, 4}
    };

    kruskal(4, edges);

      // 13. PRIM

    cout << "\n PRIM ALGORITHM\n";

    vector<vector<pair<int, int>>> mstGraph(4);

    mstGraph[0].push_back({1, 10});
    mstGraph[1].push_back({0, 10});

    mstGraph[0].push_back({2, 6});
    mstGraph[2].push_back({0, 6});

    mstGraph[0].push_back({3, 5});
    mstGraph[3].push_back({0, 5});

    mstGraph[1].push_back({3, 15});
    mstGraph[3].push_back({1, 15});

    mstGraph[2].push_back({3, 4});
    mstGraph[3].push_back({2, 4});

    prim(mstGraph);

     //  14. 0/1 KNAPSACK

    cout << "\n 0/1 KNAPSACK\n";

    vector<int> weights = {
        10, 20, 30
    };

    vector<int> values = {
        60, 100, 120
    };

    int W = 50;

    cout << "Maximum Value = "
         << knapsack01(
                weights,
                values,
                W
            )
         << endl;


       // 15. LCS

    cout << "\n8(b). LONGEST COMMON SUBSEQUENCE\n";

    string X = "ABCBDAB";
    string Y = "BDCABA";

    cout << "LCS Length = "
         << LCS(X, Y)
         << endl;

     //  16. MATRIX CHAIN MULTIPLICATION

    cout << "\n8(c). MATRIX CHAIN MULTIPLICATION\n";

    vector<int> dimensions = {
        40, 20, 30, 10, 30
    };

    cout << "Minimum Multiplications = "
         << matrixChain(dimensions)
         << endl;

     //  17. GRAPH

    cout << "\n9. DFS AND BFS\n";

    vector<vector<int>> graph(6);

    graph[0] = {1, 2};
    graph[1] = {0, 3, 4};
    graph[2] = {0, 4};
    graph[3] = {1, 5};
    graph[4] = {1, 2, 5};
    graph[5] = {3, 4};

    DFS(graph, 0);

    BFS(graph, 0);


     //  18. DIJKSTRA

    cout << "\n10. DIJKSTRA ALGORITHM\n";

    vector<vector<pair<int, int>>> weightedGraph(5);

    weightedGraph[0] = {
        {1, 10},
        {4, 5}
    };

    weightedGraph[1] = {
        {2, 1},
        {4, 2}
    };

    weightedGraph[2] = {
        {3, 4}
    };

    weightedGraph[3] = {
        {0, 7},
        {2, 6}
    };

    weightedGraph[4] = {
        {1, 3},
        {2, 9},
        {3, 2}
    };

    dijkstra(weightedGraph, 0);

    return 0;
}