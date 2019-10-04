def my_min(num_list): 
    min = None
    for i in num_list:
        if min == None:
            min=i
        elif i < min:
            min = i
    return min
def my_max(num_list): 
    max = None
    for i in num_list:
        if max is None:
            max=i
        elif i > max:
            max = i
    return max
def my_average(num_list): 
    count = 0
    sum = None
    for i in num_list:
        count = count +1
        if sum is None:
            sum=i
        else:
            sum = sum + i
    return sum/count
def my_median(num_list): 
    num_list.sort()
    r = int(len(num_list)/2)
    if (len(num_list) % 2) == 0:
        #even
        return (num_list[r] +num_list[r+1])/2
    else:
        #odd
        return num_list[r]
def my_range(num_list): 
    return max(num_list)-min(num_list)

list = [9,41,12,3,74,15]
print(list)
print("Min", my_min(list))
print("Max", my_max(list))
print("Average", my_average(list))
print("Median", my_median(list))
print("Range", my_range(list))