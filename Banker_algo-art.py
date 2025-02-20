import numpy as np 

"""
===Inputs===
"""
processes = int(input("\nEnter the number of processes: "))
resources = int(input("Enter the number of resources: "))

# Create empty lists
allocation = np.zeros((processes, resources))
max_resources = np.zeros((processes, resources))
available_resources = np.zeros(resources)

# Allocation Matrix
print("Enter allocation matrix:")
for i in range(processes):
    allocation[i] = list(map(int, input().split()))

# Max Resources Matrix
print("Enter max resources matrix:")
for i in range(processes):
    max_resources[i] = list(map(int, input().split()))

# Available Resources
print("Enter available resources:")
available_resources = list(map(int, input().split()))

"""
===Algorithm===
"""
# Need Matrix
need = max_resources - allocation

# Find safe sequence
safe_sequence = []
avl_res = list(available_resources)
deadlock_count = 0

while len(safe_sequence) < processes:
    for p in range(processes):
        if p not in safe_sequence:
            if all(need[p] <= avl_res):
                avl_res += allocation[p]
                safe_sequence.append(p)
                break
            else:
                deadlock_count += 1   
                
    if deadlock_count >= processes:
        break


"""
===Outputs===
"""
# print("\n---Allocation Matrix---")
# for i in range(processes):
#     print(allocation[i])

# print("\n---Max Resources Matrix---")
# for i in range(processes):
#     print(max_resources[i])

# print("\n---Need Matrix---")
# for i in range(processes):
#     print(need[i])

# print("\n---Available Resources---")
# print(available_resources)

print("\n---Results---")
if len(safe_sequence) == processes:
    print("System is in safe state")
    print("Safe sequence:", end=" ")
    for i in safe_sequence:
        print(f"P{i}", end=" ")
    print()
else:
    print("Deadlock detected\n")

