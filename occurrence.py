# Name = Smit Mataliya
# Id = 20CE053
#  You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
# Sample Input
# 4
# bcdef
# abcdefg
# bcde4
# bcdef
# Sample Output
# 3
# 2 1 1
# Explanation: There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
# Github Link : 

k = int(input())
array = []
for i in range(k):
    p = input()
    array.append(p)

set1 = set(array)
print(len(set1))
array2 = []
array3 = []
for i in array:
    if i in array2:
        pass
    else:
        array2.append(i)
        array3.append(array.count(i))
for i in array3:
    print(i, end=' ')
