def peak(list):
    peak = []

    for i in range(1, len(list)-1):

        if list[i] > list[i-1] and list[i] > list[i+1]:
            peak.append(i)
        else:
            pass

    print(peak)
            

def valleys(list):
    valleys = []

    for i in range(1, len(list)-1):

        if list[i] < list[i-1] and list[i] < list[i+1]:
            valleys.append(i)
        else:
            pass

    print(valleys)

def peaks_and_valleys(list, list2):
    return list + list2


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peak(data) 
valleys(data) 

# peaks_and_valleys

