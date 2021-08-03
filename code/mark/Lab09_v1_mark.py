
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peaks_list = []
    for i in range(1,len(data)-1): # -1 to prevent it from going out of range
        if data[i] > data[i-1] and data[i] > data [i+1]:
            peaks_list.append(i)
    return peaks_list


def valleys(data):
    valleys_list = []
    for i in range(1, len(data)-1):
        if data[i] < data[i-1] and data[i] < data[i+1]:
            valleys_list.append(i)
    return valleys_list

def peaks_and_valleys(data):
    complete_list = []
    for point in valleys(data):
        complete_list.append(point)
    for point in peaks(data):
        complete_list.append(point)
    return sorted(complete_list)

print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))