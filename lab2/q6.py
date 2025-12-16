graph = {"A": {"B", "C"}, "B": {"A", "D"}, "C": {"A", "D"}, "D": {"B", "C"}}

def is_valid_path(path):
    for i in range(len(path)-1):
        if path[i+1] not in graph.get(path[i], {}):
            return False
    return True

path = input("Enter path separated by spaces: ").split()

print("Valid path" if is_valid_path(path) else "Invalid path")
