import numpy as np 
# inputs
processes = int(input("\nEnter the number of processes: "))
resources = int(input("Enter the number of resources: "))

# Initialize Empty Arrays
allocation = np.zeros((processes, resources), dtype=int)
max_resources = np.zeros((processes, resources), dtype=int)
available_resources = np.zeros(resources, dtype=int)

# Initiate Matrices 
print("Enter maximum resources matrix:")
for i in range(processes):
    max_resources[i] = list(map(int, input().split()))
    
print("Enter allocation matrix:")
for i in range(processes):
    allocation[i] = list(map(int, input().split()))

print("Enter available resources:")
available_resources = np.array(list(map(int, input().split())), dtype=int)

# need matrix, called during loops
need = max_resources - allocation

# Find safe sequence
safe_sequence = []  # store the safe order of processes
work = available_resources.copy()  # available pool clones to be modified during checking
finish = [False] * processes  # track which processes have been completed
deadlock_counter = 0  # Counter to detect if we're stuck in a deadlock

while len(safe_sequence) < processes:  # continue until all processes are scheduled
    found = False  # flag to track if we found any safe process in this iteration
    
    for p in range(processes):
        # Check if process hasn't finished and its needs can be met
        if not finish[p]:
            can_allocate = True
            # Check if all resource needs can be met
            for r in range(resources):
                if need[p][r] > work[r]:
                    can_allocate = False
                    break
            
            if can_allocate:
                work += allocation[p]  # Add back to available pool
                safe_sequence.append(p)  # Mark as safe
                finish[p] = True  # Mark as finished
                found = True
                deadlock_counter = 0  # Reset counter when we make progress
                break
    
    if not found:
        deadlock_counter += 1
        # If we've gone through all processes twice without finding a safe one, it's a deadlock
        if deadlock_counter >= processes:
            break

# Output
print("\n=== OUTPUT ===")
if len(safe_sequence) == processes:
    print("System returns safe state")
    print("Safe sequence:", end=" ")
    for i in safe_sequence:
        print(f"P{i}", end=" ")
else:
    print("Found Deadlock")
    print("Processes in deadlock:", end=" ")
    for i in range(processes):
        if not finish[i]:
            print(f"P{i}", end=" ")
    print()