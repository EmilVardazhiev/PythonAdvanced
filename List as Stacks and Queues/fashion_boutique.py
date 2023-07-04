from collections import deque

clothes = deque([int(x) for x in input().split()])

rack_capacity = int(input())

rack_counter = 1
current_rack_space = rack_capacity
while clothes:
    current_clothe = clothes.pop()

    if current_rack_space >= current_clothe:
        current_rack_space -= current_clothe
    else:
        rack_counter += 1
        current_rack_space = rack_capacity
        current_rack_space -= current_clothe

print(rack_counter)
