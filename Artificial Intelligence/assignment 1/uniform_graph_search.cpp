#include <bits/stdc++.h>

using namespace std;

vector < int > bfsOfGraph(int V, vector < int > adj[]) {
      vector < int > bfs;
      vector < int > vis(V+1, 0);
      queue < int > q;
      q.push(1);
      vis[1] = 1;
      while (!q.empty()) {
        int node = q.front();
        q.pop();
        bfs.push_back(node);
        

        for (auto it: adj[node]) {
          if (!vis[it]) {
            q.push(it);
            vis[it] = 1;
          }
        }
      }

      return bfs;
    }

void dfs(int node, vector<int> &vis, vector<int> adj[], vector<int> &storeDfs) {
        storeDfs.push_back(node); 
        vis[node] = 1; 
        for(auto it : adj[node]) {
            if(!vis[it]) {
                dfs(it, vis, adj, storeDfs); 
            }
        }
    }

vector<int>dfsOfGraph(int V, vector<int> adj[]){
	    vector<int> storeDfs; 
	    vector<int> vis(V+1, 0); 
      for(int i = 1;i<=V;i++) {
        if(!vis[i]) dfs(i, vis, adj, storeDfs); 
      }
	    return storeDfs; 
	}

void addEdge(vector < int > adj[], int u, int v) {
  adj[u].push_back(v);
  adj[v].push_back(u);
}

void printAns(vector < int > & ans) {
  for (int i = 0; i < ans.size(); i++) {
    cout << ans[i] << " ";
  }
  cout<<endl;
}


int main() {
  vector < int > adj[11];

  addEdge(adj, 1, 8);
  addEdge(adj, 1, 5);

  addEdge(adj, 1, 2);
  addEdge(adj, 8, 6);
  addEdge(adj, 8, 4);
  addEdge(adj, 8, 3);
  addEdge(adj, 6, 10);
  addEdge(adj, 6, 7);
  addEdge(adj, 2, 9);

  int src = 1 ;
  

  cout<<"BFS traversal for graph : ";
  vector < int > ans = bfsOfGraph(10, adj);
  printAns(ans);
  cout<<"DFS traversal for graph : ",
  ans = dfsOfGraph(10,adj) ;
  printAns(ans);
  cout << endl;
  //cout<<"hello world";

  return 0;
}
