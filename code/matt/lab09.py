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

# Peaks goes through elevation and finds the index where the index to
# either side is smaller than it and appends that index to a list
# and then returns the list.


def peaks(elevation):
    peaks = []
    for i in range(len(elevation) - 1):
        if elevation[i] >= elevation[i - 1] and elevation[i] >= elevation[i + 1]:
            peaks.append(i)
    return peaks

# Valleys goes through elevation and finds the index where the index to
# either side is larger than it and appends that index to a list
# and then returns the list.


def valleys(elevation):
    valleys = []
    for i in range(1, len(elevation)):
        if elevation[i] <= elevation[i - 1] and elevation[i] <= elevation[i + 1]:
            valleys.append(i)
    return valleys

# Peaks_and_valleys calls peaks and valleys and appends both returned lists
# to a new list and sorts them into numerical order and returns the list.


def peaks_and_valleys(elevation):
    peaks_and_valleys = peaks(elevation) + valleys(elevation)
    peaks_and_valleys.sort()
    return peaks_and_valleys

# water_in_hill goes from each peak until a index in elevation is the same
# height. It then takes the indeices between the two and adds the amount
# needed to equal the peak and then adds that number to water.


def water_in_hill(elevation):
    water = 0
    peak = peaks(elevation)

    for i in range(peak[0], peak[1]):
        if elevation[i] < elevation[peak[0]]:
            water += elevation[peak[0]] - elevation[i]
    for i in range(peak[1], len(elevation)):
        if elevation[i] <= elevation[peak[1]]:
            water += elevation[peak[1]] - elevation[i]

    return water


print(f'Peaks are at {peaks(elevation)}')
print(f'Valleys are at {valleys(elevation)}')

# Version 2 use for loop to draw the data
for i in range(len(elevation)):
    print('x' * elevation[i])

print(f'The amount of water in valleys: {water_in_hill(elevation)}')
