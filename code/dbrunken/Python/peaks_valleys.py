'''
8/11
dbrunk
lab 9
visualize peaks and valleys
'''


pv_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peak(data):
    peaks = []
    for i in range(len(data[: -1])):
        if i == 0:
            continue
        if data[i-1] < data[i] and data[i+1] < data[i]:
            peaks.append(i)
    # print(peaks)
    return peaks

def valley(data):
    valleys = []
    for i in range(len(data[: -1])):
        if i == 0:
            continue
        if data[i-1] > data[i] and data[i+1] > data[i]:
            valleys.append(i)
    # print(valleys)
    return valleys

def peaks_valleys(data):
    pv_list = []
    for i in range(len(data[1:-1])):
        if data[i -1] == data[i + 1]:
            pv_list.append(i)
    return pv_list

print(peak(pv_data))
print(valley(pv_data))
print(peaks_valleys(pv_data))