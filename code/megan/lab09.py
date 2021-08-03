def peak(list):
    
    all_peaks = []

    for i in range(1, len(list)-1):

        if list[i] > list[i-1] and list[i] > list[i+1]:
            all_peaks.append(i)
        else:
            pass

    return all_peaks
            

def valleys(list):

    all_valleys = []

    for i in range(1, len(list)-1):

        if list[i] < list[i-1] and list[i] < list[i+1]:
            all_valleys.append(i)
        else:
            pass

    return all_valleys

def peaks_and_valleys(list):

    all_peaks_and_valleys = []

    for i in range(1, len(list)-1):

        if list[i] > list[i-1] and list[i] > list[i+1]:
            all_peaks_and_valleys.append(i)
        elif list[i] < list[i-1] and list[i] < list[i+1]:
            all_peaks_and_valleys.append(i)
        else:
            pass
    
    return all_peaks_and_valleys

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

print(peak(data)) 
print(valleys(data))

print(peaks_and_valleys(data))
