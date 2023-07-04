from collections import deque

stack = deque()

#map

map_functions = {
    1: lambda x: stack.append(x[1]), # x == number_data => [1, 97]
    2: lambda x: stack.pop() if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None,
}

for _ in range(int(input())):
    number_data = [int(x) for x in input().split()]
    command = number_data[0]

    map_functions[number_data[0]](number_data)

stack.reverse()

print(*stack, sep=", ")

