
#include<bits/stdc++.h>

using namespace std;

const int N = 4;  // size of the graph

// calculate the Euclidean distance heuristic
double heuristic(int x1, int y1, int x2, int y2) {
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}

// A* search algorithm implementation
void a_star(int start_x, int start_y, int goal_x, int goal_y, int graph[N][N]) {
    // pair to store the coordinates of a cell
    pair<int, int> curr;

    // priority queue to sort the cells based on their f value (g + h)
    priority_queue<pair<double, pair<int, int>>, vector<pair<double, pair<int, int>>>, greater<>> pq;

    // unordered map to store the g value for each cell
    unordered_map<pair<int, int>, double> g_value;

    // vector to store the search sequence
    vector<pair<int, int>> search_seq;

    // add the start node to the priority queue and the search sequence
    pq.push({0, {start_x, start_y}});
    search_seq.push_back({start_x, start_y});

    // calculate the g value for the start node
    g_value[{start_x, start_y}] = 0;

    while (!pq.empty()) {
        // get the cell with the lowest f value (g + h)
        curr = pq.top().second;
        pq.pop();

        // if the current cell is the goal, break the loop
        if (curr.first == goal_x && curr.second == goal_y) {
            break;
        }

        // check the neighbors of the current cell
        for (int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {
                int x = curr.first + i;
                int y = curr.second + j;

                // if the neighbor is inside the graph and not an obstacle
                if (x >= 0 && x < N && y >= 0 && y < N && graph[x][y] != -1) {
                    // calculate the new g value
                    double new_g = g_value[{curr.first, curr.second}] + 1;

                    // if the new g value is smaller than the current g value for the neighbor
                    if (g_value.find({x, y}) == g_value.end() || new_g < g_value[{x, y}]) {
                        // update the g value for the neighbor
                        g_value[{x, y}] = new_g;

                        // add the neighbor to the priority queue and the search sequence
                        pq.push({g_value[{x, y}] + heuristic(x, y, goal_x, goal_y),{x, y}});
						search_seq.push_back({x, y});
					}
				}
			}
		}
	}



// print the search sequence
cout << "Search Sequence: ";
for (auto& cell : search_seq) {
    cout << "(" << cell.first << ", " << cell.second << ") ";
}

}

int main() {
// example graph with obstacles represented by -1
int graph[N][N] = {{0, 0, 0, 0},
{0, -1, 0, -1},
{0, 0, 0, 0},
{0, 0, 0, 0}};



// starting and goal coordinates
int start_x = 0, start_y = 0;
int goal_x = 3, goal_y = 3;

// call the A* search algorithm
a_star(start_x, start_y, goal_x, goal_y, graph);

return 0;

}



