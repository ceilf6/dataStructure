from collections import Counter

TARGET = "CHICKEN"
LEN_TARGET = len(TARGET)

def is_subsequence(s, target):
    it = iter(s)
    return all(c in it for c in target)

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        n = int(input[ptr])
        ptr +=1
        s = input[ptr]
        ptr +=1
        if is_subsequence(s, TARGET):
            # Check remaining characters
            sum_rest = len(s) - LEN_TARGET
            if sum_rest % 2 != 0:
                print("NO")
                continue
            # Calculate remaining characters
            t_ptr = 0
            remaining = []
            s_ptr = 0
            for c in s:
                if t_ptr < LEN_TARGET and c == TARGET[t_ptr]:
                    t_ptr +=1
                else:
                    remaining.append(c)
            count = Counter(remaining)
            max_count = max(count.values()) if count else 0
            if max_count > sum_rest // 2:
                print("NO")
            else:
                print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
