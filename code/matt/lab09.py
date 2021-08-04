'''
Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both
the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a
higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list
 of the peaks and valleys in order of appearance in the original data.
'''
elevation = [1,	2,	3,	4,	5,	6,	7,	6,	5,	4,	5,	6,	7,	8,	9,	8,	7,	6,	7,	8,	9]


def peaks(elevation):
    peaks = []
    for i in range(len(elevation) - 1):
        if elevation[i] >= elevation[i - 1] and elevation[i] >= elevation[i + 1]:
            peaks.append(i)
    return peaks


def valleys(elevation):
    valleys = []
    for i in range(1, len(elevation)):
        if elevation[i] <= elevation[i - 1] and elevation[i] <= elevation[i + 1]:
            valleys.append(i)
    return valleys


def peaks_and_valleys(elevation):
    peaks_and_valleys = peaks(elevation) + valleys(elevation)
    peaks_and_valleys.sort()
    return peaks_and_valleys


for i in range(len(elevation)):
    print('x' * elevation[i])


def water_in_hill(elevation):
    water = 0
    peak = peaks(elevation)
    peak1 = 7
    peak2 = 9

    for i in range(peak[0], peak[1]):
        if elevation[i] < peak1:
            water += peak1 - elevation[i]
    for i in range(peak[1], len(elevation)):
        if elevation[i] <= peak2:
            water += peak2 - elevation[i]

    return water


print(water_in_hill(elevation))
