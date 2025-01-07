if __name__ == "__main__":
    filename = "Day1.txt"
    lIntegers = []
    rIntegers = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.split()
            lIntegers.append(int(line[0]))
            rIntegers.append(int(line[1]))
    lIntegers.sort()
    rIntegers.sort()
    #Answer 1
    #dist = 0
    #for index in range(len(lIntegers)):
    #    dist += abs(lIntegers[index] - rIntegers[index])
    #print(dist)

    #Answer 2
    multiple = 0
    ans = 0
    for nums in lIntegers:
        for mul_num in rIntegers:
            if nums == mul_num:
                multiple += 1
        ans += multiple * nums
        multiple = 0
    print(ans)