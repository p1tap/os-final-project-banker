def read_input_file(filename):
    """Read and parse input file containing max matrix, allocation matrix, and available resources"""
    try:
        with open(filename, 'r') as file:
            # Read non-empty lines and clean Windows line endings
            lines = [line.strip().rstrip('\r\n') for line in file if line.strip()]
            
            # Parse matrices (first 5 lines for max, next 5 for allocation)
            max_matrix = [list(map(int, lines[i].split())) for i in range(5)]
            allocation_matrix = [list(map(int, lines[i+5].split())) for i in range(5)]
            available = list(map(int, lines[-1].split()))
            
            return max_matrix, allocation_matrix, available
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        raise

def calculate_need_matrix(max_matrix, allocation_matrix):
    """Calculate need matrix (Max - Allocation)"""
    return [[max_matrix[i][j] - allocation_matrix[i][j] 
             for j in range(len(max_matrix[0]))]
            for i in range(len(max_matrix))]

def is_safe_state(processes, available, max_matrix, allocation_matrix):
    """Check if system is in safe state and return safe sequence"""
    n = len(processes)
    work = available.copy()
    finish = [False] * n
    safe_seq = []
    need = calculate_need_matrix(max_matrix, allocation_matrix)
    
    while not all(finish):
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(len(work))):
                safe_seq.append(f"P{i}")
                finish[i] = True
                work = [work[j] + allocation_matrix[i][j] for j in range(len(work))]
                found = True
                print(f"\nProcess P{i} runs.")
                print(f"Updated Available: {work}")
        
        if not found:
            break
    
    return all(finish), safe_seq, work

def format_matrix(matrix):
    """Format matrix for pretty printing"""
    return '\n'.join([str(row) for row in matrix])

def main():
    try:
        import sys
        filename = sys.argv[1] if len(sys.argv) > 1 else input("Enter file name: ").strip()
        
        # Read input and calculate matrices
        max_matrix, allocation_matrix, available = read_input_file(filename)
        need = calculate_need_matrix(max_matrix, allocation_matrix)
        
        # Display initial state
        print(f"\nInitial Available: {available}")
        print("\nNeed Matrix:")
        print('\n'.join(str(row) for row in need))
        
        # Check system state
        is_safe, safe_sequence, _ = is_safe_state(range(5), available, max_matrix, allocation_matrix)
        
        # Display results
        print(f"\nProcesses: {', '.join(f'P{i}' for i in range(5))}")
        print(f"Available Resources: {available}")
        print("\nSystem is in a safe state." if is_safe else "\nSystem is NOT in a safe state.")
        if is_safe:
            print(f"Safe sequence: {' -> '.join(safe_sequence)}")
            
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()
