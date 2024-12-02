import os
# file_input = open("test_input.txt", "r")
file_input = open("day1-input.txt", "r")
input_string = file_input.read()
input_string = input_string.splitlines()

# Problem 1
total = 0
list1 = []
list2 = []
for line in input_string:
    num_list = line.split()
    list1.append(int(num_list[0]))
    list2.append(int(num_list[1]))
list1.sort()
list2.sort()
print(list1)
print(list2)
for i in range(len(list1)):
        print(abs(list1[i] - list2[i]))
        total += abs(list1[i] - list2[i])
print(total)

#     num_list[0] = list(num_list[0])
#     num_list[1] = list(num_list[1])
#     for i in range(len(num_list[0])):
#         num_list[0][i] = int(num_list[0][i])
#     for i in range(len(num_list[1])):
#         num_list[1][i] = int(num_list[1][i])
#     num_list[0].sort()
#     num_list[1].sort()
#     print(num_list[0])
#     print(num_list[1])
#     for i in range(len(num_list[1])):
#         print(abs(num_list[0][i] - num_list[1][i]))
#         total += abs(num_list[0][i] - num_list[1][i])



total1 = 0
for num in list1:
    total1 += num * list2.count(num)
print(total1)