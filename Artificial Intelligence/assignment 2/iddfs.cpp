#include <bits/stdc++.h>
using namespace std;

bool dfs(int node,int target,  vector<int> adj[], int limit) {
       
        if(node == target)
        {
            return true;
        }
        else if(limit <= 0)
        {
            return false;
        } 
        for(auto it : adj[node])
        {
            //cout<<node<<" "<<it<<endl; 
        
                if(dfs(it, target , adj,limit-1) == true )
                {
                    return true; 
                }
        
        }
        return false;
    }

bool iddfs(int src,int target , vector<int> adj[] ,int maxdepth){

        for (int i = 0; i <= maxdepth; i++)
        {
            if (dfs(src, target, adj ,i ) == true)
            return true;
        }
   
        return false;
}

void addEdge(vector < int > adj[], int u, int v) {
  adj[u].push_back(v);
}


int main() {
  
  vector < int > adj[17];

  addEdge(adj, 1, 2);
  addEdge(adj, 1, 3);

  addEdge(adj, 2, 4);
  addEdge(adj, 2, 5);
  addEdge(adj, 3, 6);
  addEdge(adj, 3, 7);
  addEdge(adj, 3, 8);
  addEdge(adj, 4, 9);
  addEdge(adj, 4, 10);
  addEdge(adj, 5, 11);
  addEdge(adj, 5, 12);
  addEdge(adj, 5, 13);
  addEdge(adj, 6, 14);
  addEdge(adj, 8, 15);
  addEdge(adj, 8, 16);

  int src = 1;
  int target = 14;
  int maxdepth;
  cout<<"set max depth : ";
  cin >> maxdepth;

  if(iddfs(src,target,adj,maxdepth))
  {
     cout<<"Target reachable"<<endl;
  }
  else{
    cout<<"Target unreachable"<<endl;
  }

  return 0;
}
