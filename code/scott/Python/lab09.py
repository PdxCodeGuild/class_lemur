# Class Lemur Day Course
# Lab 9, Peaks and Valleys
# Scott Cormack
# Python 3.9.6

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peaks_lst = []
    for i in range(len(data[:-1])):
        if i == 0:
            continue
        if data[i - 1] < data[i] and data[i + 1] < data[i]:
            peaks_lst.append(i)
    return peaks_lst

def valleys(data):
    valleys_lst = []
    for i in range(len(data[:-1])):
        if i == 0:
            continue
        if data[i - 1] > data[i] and data[i + 1] > data[i]:
            valleys_lst.append(i)
    return valleys_lst

def peaks_valleys(data):
    both_lst = []
    for i in range(len(data[1:-1])):
        if data[i - 1] == data[i + 1]:
            both_lst.append(i)
    return both_lst

print(peaks(data))
print(valleys(data))
print(peaks_valleys(data))
