data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
def peaks(data):
    #return peaks
    i = 0
    peak_indexes =[]
    for i in range(len(data)):
        if i != 0 and i != len(data) - 1:
            if data[i] > data[i-1] and data[i] > data[i+1]:
                peak_indexes.append(i)
    return peak_indexes

def valleys(data):
    valley_indexes = []
    for i in range(len(data)):
        if i != 0 and i != len(data) - 1:
            if data[i] < data[i-1] and data[i] < data[i+1]:
                valley_indexes.append(i)
    return valley_indexes
        
my_peaks = peaks(data)
print(my_peaks)
my_valleys = valleys(data)
print(my_valleys)

peaks_and_valleys = my_peaks.extend(my_valleys)
peaks_and_valleys = sorted(my_peaks)
print(peaks_and_valleys)
