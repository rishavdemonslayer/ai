def dfs_jug(capacity_a, capacity_b, target):
    stack=[]
    visited = set()
    stack.append(((0, 0), 0, []))
    visited.add((0, 0))

    while stack:
        (current_a, current_b), steps, sequence = stack.pop()
        if current_a == target or current_b == target:
            return sequence
        next_states = []

        # Fill jug A
        next_state = (capacity_a, current_b)
        if next_state not in visited:
            next_states.append((next_state, steps + 1, sequence + [(current_a, current_b, 'Fill A')]))
            visited.add(next_state)

        # Fill jug B
        next_state = (current_a, capacity_b)
        if next_state not in visited:
            next_states.append((next_state, steps + 1, sequence + [(current_a, current_b, 'Fill B')]))
            visited.add(next_state)    

        # Empty jug A
        next_state = (0, current_b)
        if next_state not in visited:
            next_states.append((next_state, steps + 1, sequence + [(current_a, current_b, 'Empty A')]))
            visited.add(next_state)   

        # Empty jug B
        next_state = (current_a, 0)
        if next_state not in visited:
            next_states.append((next_state, steps + 1, sequence + [(current_a, current_b, 'Empty B')]))
            visited.add(next_state)     

        # Pour A to B
        pour_amount = min(current_a, capacity_b - current_b)
        next_state = (current_a - pour_amount, current_b + pour_amount)
        if next_state not in visited:
            next_states.append((next_state, steps + 1, sequence + [(current_a, current_b, 'Pour A to B')])) 
            visited.add(next_state)

        # Pour B to A
        pour_amount = min(capacity_a - current_a, current_b)
        next_state = (current_a + pour_amount, current_b - pour_amount)
        if next_state not in visited:
            next_states.append((next_state, steps + 1, sequence + [(current_a, current_b, 'Pour B to A')])) 
            visited.add(next_state)        

        for state in next_states:
            stack.append(state)
    return None

def print_steps(sequence_of_steps):
    if sequence_of_steps is not None:
        print(f"Steps to get {target} liters:")
        for step in sequence_of_steps:
            print(step)
    else:
        print(f"No solution found to get {target} liters.")

capacity_a = 3
capacity_b = 5
target = 4
sequence_of_steps = dfs_jug(capacity_a, capacity_b, target)
print_steps(sequence_of_steps)
