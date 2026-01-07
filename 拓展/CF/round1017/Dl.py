def check_match(p, s):
    i, j = 0, 0
    while i < len(p) and j < len(s):
        if p[i] == s[j]:

            if j + 1 < len(s) and s[j] == s[j + 1]:
                j += 2
            else:
                j += 1 
            i += 1
        else:
            return "NO"
    

    if i == len(p) and j == len(s):
        return "YES"
    return "NO"

def main():
    t = int(input()) 
    for _ in range(t):
        p = input().strip()
        s = input().strip()
        print(check_match(p, s))

if __name__ == "__main__":
    main()
