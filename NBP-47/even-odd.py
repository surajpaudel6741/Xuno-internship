a = 516
sequence = []

while True:
    a = a // 2 if a % 2 == 0 else a * 3 + 1
    sequence.append(a)
    
    print(sequence)

    if len(sequence) == 4:
        if sequence[1] == 4 and sequence[2] == 2:
            break
        sequence = []

print(a)
