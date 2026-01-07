def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    idx = 0
    t = int(data[idx])
    idx += 1
    result = []
    
    for _ in range(t):
        q = int(data[idx])
        idx += 1
        
        arr = []
        rizziness = 0
        shift_count = 0
        
        for i in range(q):
            op = list(map(int, data[idx].split()))
            idx += 1
            
            if op[0] == 1:  
                shift_count += 1

                if arr:
                    arr = [arr[-1]] + arr[:-1]
                
            elif op[0] == 2:  # Reverse
                shift_count = (shift_count + 1) % 2
                arr.reverse()

            elif op[0] == 3:
                k = op[1]
                arr.append(k)
                rizziness += k * (len(arr))

            if shift_count % 2 == 0:
                result.append(rizziness)
            else:
                result.append(-rizziness)
                
    sys.stdout.write("\n".join(map(str, result)) + "\n")
