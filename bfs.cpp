#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void bfs(int start, vector<vector<int>>& graph, int n) { // start , graph , node
    vector<bool> visited(n, false); // at first node is not visited
    queue<int> q; // create a queue

    q.push(start); // push started node into queue
    visited[start] = true; // start ko visited marks kar do

    while (!q.empty()) { // jab tak q empty nhi ho jata
        int node = q.front(); // front ko
        q.pop(); // pop kar do

        cout << node << " ";

        for (int neighbour : graph[node]) { // node ke neighbour me jao
            if (!visited[neighbour]) { // neighbour visited nhi hai to visited mark karo
                visited[neighbour] = true;
                q.push(neighbour); // push kar do me neighbour ko queue me 

                // level wise ,search to find sortest path 
            }
        }
    }
}

int main() {
    int n = 5;

    vector<vector<int>> graph(n);

    graph[0] = {1, 2};
    graph[1] = {3};
    graph[2] = {4};

    bfs(0, graph, n);

    return 0;
}