import openrouteservice

def get_distance_matrix(client, locations):
    try:
        matrix = client.distance_matrix(
            locations,
            metrics=['distance'],
            units='km'
        )
        return matrix['distances']
    except openrouteservice.exceptions.ApiError as e:
        print(f"API error: {e}")
        return None

def dfs(current_node, current_distance, visited, path, distances, n):
    global shortest_distance, shortest_route
    if len(path) == n:
        current_distance += distances[current_node][0]
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_route = path + [0]
        return

    for next_node in range(n):
        if next_node not in visited:
            visited.add(next_node)
            dfs(next_node, current_distance + distances[current_node][next_node], visited, path + [next_node], distances, n)
            visited.remove(next_node)

def calculate_shortest_route(client, locations):
    coordinates = []
    for place in locations:
        try:
            result = client.pelias_search(place)
            if result['features']:
                coordinates.append(result['features'][0]['geometry']['coordinates'])
            else:
                print(f"Could not find coordinates for {place}")
                return None, None
        except openrouteservice.exceptions.ApiError as e:
            print(f"API error for location {place}: {e}")
            return None, None

    distances = get_distance_matrix(client, coordinates)
    if distances is None:
        return None, None

    global shortest_distance, shortest_route
    shortest_distance = float('inf')
    shortest_route = None

    n = len(locations)
    dfs(0, 0, {0}, [0], distances, n)

    shortest_route_locations = [locations[i] for i in shortest_route]
    return shortest_route_locations, shortest_distance

def main():
    api_key = '5b3ce3597851110001cf62483a7ef6b3f2ea4f02b858dce85ab66f4b'  
    client = openrouteservice.Client(key=api_key)
    
    locations = [
        'Nairobi, Kenya',
        'Nyeri, Kenya',
        'Nakuru, Kenya',
        'Laikipia, Kenya',
        'Nandi, Kenya',
        'Meru, Kenya'
    ]
    
    print("Calculating shortest route...")
    shortest_route, shortest_distance = calculate_shortest_route(client, locations)
    
    if shortest_route and shortest_distance is not None:
        print('Shortest route:')
        for location in shortest_route:
            print(location)
        print(f'Total distance: {shortest_distance:.2f} km')
    else:
        print("Could not calculate the route. Please check your API key and input locations.")

if __name__ == '__main__':
    main()
