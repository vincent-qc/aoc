from util import next_int, next_line, next_word, read_whole


def main():
    nums = []
    hashmap2 = {}
    for _ in range(1000):
        i1 = next_int()
        i2 = next_int()
        nums.append(i1)
        hashmap2[i2] = hashmap2.get(i2, 0) + 1

    sum = 0
    for i in range(1000):
        num = nums[i]
        sum += num * hashmap2.get(num, 0)

    print(sum)


main()
