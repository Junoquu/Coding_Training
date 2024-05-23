def calculate_container_size(n, container_lengths):
    total_volume = sum(c**3 for c in container_lengths)
    
    single_cube_side = total_volume ** (1/3)
    
    return single_cube_side

n = int(input())
container_lengths = list(map(float, input().split()))

result = calculate_container_size(n, container_lengths)

print(f"{result:.6f}")