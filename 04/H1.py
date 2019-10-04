def getFileLines(fname):
    fhandle = open(fname)
    lines = []
    for line in fhandle:
        line = int(line.rstrip())
        if line:
            lines.append(line)
    fhandle.close()
    return lines
filelist = getFileLines("MH8811-04-Data.csv")
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
print("Min", my_min(filelist))
print("Max", my_max(filelist))
print("Average", my_average(filelist))
print("Median", my_median(filelist))
print("Range", my_range(filelist))
avg = my_average(filelist)
def my_variance(num_list):
    diffsum = 0.0
    count = 0.0
    for i in num_list:
        diffsum = diffsum + pow(i - avg,2)
        count = count + 1
    return diffsum/count
print("Variance", my_variance(filelist))
