'''
8/11
dbrunk
lab 9
visualize peaks and valleys
'''


pv_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peak(data):
    peaks = []
    highest_peak = max(data)
    for i in range(len(data)):
        if data[i] >= highest_peak:
            peaks.append[i]
    print(peaks)

def valley(data):
    valleys = []
    lowest_valley = min(data)
    for i in range(len(data)):
        if data[i] <= lowest_valley:
            valleys.append[i]
    print(valleys)

# def peaks_valleys():
