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
print("\n=== Initial State ===")
print("Need Matrix:")
print(need)
print("\nInitial Available Resources:", available_resources)

# Find safe sequence
safe_sequence = []  # store the safe order of processes
work = available_resources.copy()  # available pool clones to be modified during checking
finish = [False] * processes  # track which processes have been completed

while len(safe_sequence) < processes:  # continue until all processes are scheduled
    found = False  # flag to track if we found any safe process in this iteration
    print("\n--- New Iteration ---")
    print(f"Current working resources: {work}")
    
    for p in range(processes):
        if not finish[p]:
            print(f"\nChecking P{p}:")
            print(f"Need: {need[p]}")
            print(f"Available: {work}")
            
            if all(need[p] <= work):  # Process p is safe to execute:
                print(f"✓ P{p} can be executed")
                work += allocation[p]  # Add back to avail pool
                print(f"After P{p} returns resources: {work}")
                safe_sequence.append(p) # Mark as safe
                finish[p] = True # Mark as finished
                found = True
            else:
                print(f"✗ P{p} must wait - insufficient resources")
    
    # If cannot find any execution, return deadlock
    if not found:
        break

# Output
print("\n=== OUTPUT ===")
if len(safe_sequence) == processes:
    print("System returns safe state")
    print("Safe sequence:", end=" ")
    for i in safe_sequence:
        print(f"P{i}", end=" ")
else:
    print("\nFound Deadlock\n")