from collections import deque

def water_jug_BFS(x, y, z):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        jug_a, jug_b = queue.popleft()

        if jug_a == z or jug_b == z or jug_a + jug_b == z:
            return True

        if (jug_a, jug_b) in visited:
            continue

        visited.add((jug_a, jug_b))

        # Fill jug A
        if jug_a < x:
            queue.append((x, jug_b))

        # Fill jug B
        if jug_b < y:
            queue.append((jug_a, y))

        # Empty jug A
        if jug_a > 0:
            queue.append((0, jug_b))

        # Empty jug B
        if jug_b > 0:
            queue.append((jug_a, 0))

        # Pour from A to B
        if jug_a + jug_b >= y:
            queue.append((jug_a - (y - jug_b), y))
        else:
            queue.append((0, jug_a + jug_b))

        # Pour from B to A
        if jug_a + jug_b >= x:
            queue.append((x, jug_b - (x - jug_a)))
        else:
            queue.append((jug_a + jug_b, 0))

    return False

x = 4  # Capacity of jug A
y = 3  # Capacity of jug B
z = 2  # Desired amount of water

if water_jug_BFS(x, y, z):
    print(f'You can measure {z} liters of water using {x}-liter and {y}-liter jugs.')
else:
    print(f'You cannot measure {z} liters of water using {x}-liter and {y}-liter jugs.')