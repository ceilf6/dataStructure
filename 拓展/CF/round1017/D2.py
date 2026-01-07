def can_be_heard(t, test_cases):
    results = []
    
    for p, s in test_cases:
        flag=1
        i, j = 0, 0
        while i < len(p) and j < len(s):
            if p[i] == s[j]:
                j += 1  # Match one occurrence
                if j < len(s) and s[j] == s[j - 1]:
                    j += 1  # Try to match two occurrences if possible
            else:
                results.append("NO")
                flag=0
                break
                
            i += 1
        if not flag:
            continue
        if j == len(s):
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Input reading
t = int(input())  # number of test cases
test_cases = []
for _ in range(t):
    p = input().strip()
    s = input().strip()
    test_cases.append((p, s))

# Output result
results = can_be_heard(t, test_cases)
for result in results:
    print(result)
