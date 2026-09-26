#include <iostream>
#include <vector>
using namespace std;

void dfs(int node, vector<vector<int>>& graph, vector<bool>& visited) {
    if(visited[node] == true) return;

    for (int neighbour : graph[node]) {
        if (!visited[neighbour]) {
            dfs(neighbour, graph, visited);
        }
    }
}

int main() {
    int n = 5;

    vector<vector<int>> graph(n);

    graph[0] = {1, 2};
    graph[1] = {3};
    graph[2] = {4};

    vector<bool> visited(n, false);

    dfs(0, graph, visited);

    return 0;
}