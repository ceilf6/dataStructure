def inversion_count(lis):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, cnt_left = merge_sort(arr[:mid])
        right, cnt_right = merge_sort(arr[mid:])
        merged = []
        i = j = cnt_merge = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                cnt_merge += len(left) - i
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, cnt_left + cnt_right + cnt_merge
    _, count = merge_sort(lis)
    return count

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print((inversion_count(a) + inversion_count(b)))
