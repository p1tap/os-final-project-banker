# Banker's Algorithm Implementation

A Python implementation of the Banker's Algorithm for deadlock avoidance in operating systems.

## Description

This program implements the Banker's Algorithm, which is used for deadlock avoidance in operating systems. The algorithm determines whether a system is in a safe state by simulating resource allocation and checking if there exists a safe sequence of process execution.

## Features

- Handles multiple resources and processes
- Supports both 3-resource and 4-resource input formats
- Calculates and displays Need Matrix
- Shows step-by-step process execution
- Determines system safety and safe sequence

## Usage

```bash
python bankers-algorithm.py <input_file>
```

Or run without arguments to enter filename interactively:
```bash
python bankers-algorithm.py
```

### Input File Format

The input file should contain:
1. Maximum resource matrix (5 processes)
2. Allocation matrix (5 processes)
3. Available resources vector

Example input file (3 resources):
```
7 5 3
3 2 2
9 0 2
2 2 2
4 3 3

0 1 0
2 0 0
3 0 2
2 1 1
0 0 2

3 3 2
```

## Output

The program outputs:
1. Initial Available Resources
2. Need Matrix
3. Process execution sequence
4. System safety status
5. Safe sequence (if system is safe) 