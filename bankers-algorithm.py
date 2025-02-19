def read_input_file(filename):
    """Read and parse the input file containing resource allocation data"""
    try:
        with open(filename, 'r') as file:
            # Read and clean lines, handling Windows line endings
            lines = [line.strip().rstrip('\r\n') for line in file.readlines()]
            lines = [line for line in lines if line]  # Remove empty lines
            
            # Determine the number of resources by checking first line
            num_resources = len(lines[0].split())
            
            # Parse maximum resource matrix
            max_matrix = []
            for i in range(5):  # First 5 non-empty lines are max matrix
                row = list(map(int, lines[i].split()))
                max_matrix.append(row)
            
            # Parse allocation matrix
            allocation_matrix = []
            for i in range(5):  # Next 5 lines are allocation matrix
                row = list(map(int, lines[i+5].split()))
                allocation_matrix.append(row)
            
            # Parse available resources (last line)
            available = list(map(int, lines[-1].split()))
            
            return max_matrix, allocation_matrix, available

    except Exception as e:
        print(f"Error reading file: {str(e)}")
        raise

def calculate_need_matrix(max_matrix, allocation_matrix):
    """Calculate the need matrix (Max - Allocation)"""
    need_matrix = []
    for i in range(len(max_matrix)):
        need_row = []
        for j in range(len(max_matrix[0])):
            need_row.append(max_matrix[i][j] - allocation_matrix[i][j])
        need_matrix.append(need_row)
    return need_matrix

def is_safe_state(processes, available, max_matrix, allocation_matrix):
    """Check if the system is in a safe state and return the safe sequence"""
    n = len(processes)
    work = available.copy()
    finish = [False] * n
    safe_seq = []
    need = calculate_need_matrix(max_matrix, allocation_matrix)
    
    while True:
        # Find a process that can be executed
        found = False
        for i in range(n):
            if not finish[i]:
                # Check if process can be allocated required resources
                can_allocate = True
                for j in range(len(work)):
                    if need[i][j] > work[j]:
                        can_allocate = False
                        break
                
                if can_allocate:
                    # Add process to safe sequence
                    safe_seq.append(f"P{i}")
                    # Mark process as finished
                    finish[i] = True
                    # Release resources
                    for j in range(len(work)):
                        work[j] += allocation_matrix[i][j]
                    found = True
                    print(f"\nProcess P{i} runs.")
                    print(f"Updated Available: {work}")
                    
        if not found:
            break
    
    # Check if all processes are finished
    return all(finish), safe_seq, work

def format_matrix(matrix):
    """Format matrix for pretty printing"""
    return '\n'.join([str(row) for row in matrix])

def main():
    try:
        # Get filename from command line argument or input
        import sys
        if len(sys.argv) > 1:
            filename = sys.argv[1]
        else:
            filename = input("Enter file name: ").strip()
        
        # Read input file
        max_matrix, allocation_matrix, available = read_input_file(filename)
        
        print(f"\nInitial Available: {available}")
        
        # Calculate and display need matrix
        need = calculate_need_matrix(max_matrix, allocation_matrix)
        print("\nNeed Matrix:")
        print(format_matrix(need))
        
        # Check system state
        processes = [i for i in range(5)]  # 5 processes P0 to P4
        is_safe, safe_sequence, final_available = is_safe_state(processes, available, max_matrix, allocation_matrix)
        
        print(f"\nProcesses: {', '.join([f'P{i}' for i in range(5)])}")
        print(f"Available Resources: {available}")
        
        if is_safe:
            print("\nSystem is in a safe state.")
            print(f"Safe sequence: {' -> '.join(safe_sequence)}")
        else:
            print("\nSystem is NOT in a safe state.")
            
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()