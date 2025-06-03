
➡️ Calculate the shortest route (like a delivery or travel path) between a list of cities in Kenya using real-world distances via the OpenRouteService API, and
➡️ Visualize the route on a graph where cities are nodes and roads are edges.


---

📦 Libraries Used

import openrouteservice          # To get real distances between cities using OpenRouteService
import networkx as nx            # To represent cities and roads as a graph
import matplotlib
matplotlib.use('TkAgg')          # Choose a backend that supports interactive plots
import matplotlib.pyplot as plt  # For drawing graphs


---

🔧 Helper Functions


---

1. get_distance_matrix(client, locations)

Purpose: Get a table showing the distances between every pair of cities.

How it works: It sends a request to OpenRouteService and returns a matrix (2D list) of distances between all given coordinates.



---

2. dfs(...)

Purpose: This is a Depth-First Search (DFS) function that explores all possible routes starting from the first city.

Goal: Find the shortest total distance to visit all cities once and return to the starting city.

It uses recursion to try every possible path, remembering the shortest one found so far.

We implemented a custom DFS that recursively explores all possible routes starting from Nairobi.
🔍 Maintains visited set, path list, and cumulative distance
📈 Returns to Nairobi when a complete path is formed
🏆 Updates the shortest path if a better one is found
✅ Advantages:
Exact optimal solution
Simple and deterministic
⚠️ Limitations:
O(n!) time complexity
Not scalable beyond small datasets


---

3. calculate_shortest_route(client, locations)

Steps:

1. Convert city names (e.g. "Nairobi, Kenya") to GPS coordinates using pelias_search.


2. Get the distance matrix between those coordinates.


3. Use the dfs function to find the best (shortest) route through all cities.


4. Return the route and its total distance.





---

4. generate_city_graph(locations, distances)

Purpose: Create a graph (like a map) where:

Cities = nodes

Roads = edges (lines connecting cities), weighted by actual distance




---

5. plot_graph_step(...) and visualize_route(...)

These functions are for visualizing the route:

Show the graph step by step as the route is built.

Highlight the current city in green and draw the red path between cities.




---

🚀 main() Function

This is the starting point of the program:

1. Define your API key for OpenRouteService (you need an account to get one).


2. Provide a list of cities you want to visit.


3. Call calculate_shortest_route() to find the best route.


4. Print the result.


5. Visualize it on a graph.




---

Example Output

If successful, it prints:

Shortest route:
Nairobi, Kenya
Nakuru, Kenya
...
Total distance: 532.12 km

And opens a pop-up window showing the route visually.


---

🧠 Concepts You're Using

Concept	Explanation

API usage	Talking to a service (OpenRouteService) to get real-world data
Recursion (DFS)	Trying all possible routes to find the shortest one
Graphs	Representing cities and distances as nodes and edges
Visualization	Showing the route with matplotlib step-by-step
Error handling	Using try/except to avoid crashing if something goes wrong with the API



---

🧼 Suggestions for Beginners

If you're learning, focus on these parts one at a time:

Try printing results from pelias_search() to understand how API responses work.

Experiment with a smaller list of cities (e.g. 3) to make the logic clearer.

Comment out the visualization if it's overwhelming at first.



---

Would you like a simplified version of this code to practice with?

