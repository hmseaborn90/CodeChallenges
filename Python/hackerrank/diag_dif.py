def diagonalDifference(arr):
    sum_prim = 0
    sum_sec = 0
    for i in range(len(arr)):
        sum_prim += arr[i][i]
        sum_sec += arr[::-1][i][i]
    return abs(sum_prim - sum_sec)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()