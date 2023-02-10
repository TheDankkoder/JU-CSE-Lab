#include <bits/stdc++.h>

using namespace std;

vector<int> best_first_search(int actual_src, int target, int V,vector < pair<int,int>> adj[])
{
	vector<int> vis(V, 0);
	// MIN HEAP priority queue
    vector<int> bfs;

	priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
	// sorting in pq gets done by first value of pair
	pq.push(make_pair(0, actual_src));
	int s = actual_src;
	vis[s] = 1;
	while (!pq.empty()) {
		int x = pq.top().second;
		// Displaying the path having lowest cost
		bfs.push_back(x);
		pq.pop();
		if (x == target)
			break;

		for (int i = 0; i < adj[x].size(); i++) {
			if (!vis[adj[x][i].second]) {
				vis[adj[x][i].second] = 1;
				pq.push(make_pair(adj[x][i].first,adj[x][i].second));
			}
		}
	}
    return bfs;
}

void addEdge(vector < pair<int,int>> adj[], int u, int v,int cost) {
  adj[u].push_back(make_pair(cost,v));
  //adj[v].push_back(u);
}

void printAns(vector < int > & ans) {
  for (int i = 0; i < ans.size(); i++) {
    cout << ans[i] << " ";
  }
  cout<<endl;
}


int main() {
  vector <pair<int,int>> adj[11];

  //  a = 1, b =2 , c= 3 ,d=4,e=5,f=6,g=7,

  addEdge(adj, 1, 2,5);
  addEdge(adj, 1, 4,3);
  addEdge(adj, 2, 3,1);
  addEdge(adj, 3, 5,6);
  addEdge(adj, 3, 7,8);
  addEdge(adj, 4, 5,2);
  addEdge(adj, 5, 2,4);
  addEdge(adj,5,6,2);
  addEdge(adj, 6, 7,3);
  addEdge(adj, 7, 5,4);

  cout<<"Best First traversal for graph : ";
  int source = 1;
  int target = 7;
  vector < int > ans = best_first_search(1,7,10, adj);
  printAns(ans);
  cout << endl;
  //cout<<"hello world";

  return 0;
}

