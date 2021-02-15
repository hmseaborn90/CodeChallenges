def countingValleys(steps, path):
    # instantiate depth and valley_count vars
    #loop through path if U increase depth if depth after U increase is == 0 
    # this means we exited a valley so increase valley count
    #otherwise its D so decrease depth and continue
    #return valley_count 
    depth = 0
    valley_count = 0
    for direction in path:
        if direction == "U":
            depth += 1
            if depth == 0:
                valley_count += 1
        else:
            depth -= 1
    return valley_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()