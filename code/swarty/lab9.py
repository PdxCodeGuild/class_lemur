"""
Lab 9
Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
"""
elevation=[1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peak_list=[]
def peaks(ups):
    for i in range(len(ups[1:-1])):
        if ups[i+1] > ups[i] and ups[i+1] > ups[i+2]:
            peak_list.append(i)
    return peak_list

def valleys(downs,peak_list):
    for i in range(len(downs[1:-1])):
        if downs[i+1] < downs[i] and downs[i+1] < downs[i+2]:
            peak_list.append(i)
    return peak_list

#def terrain():
    
#V2 create image
pixels=""
rowpixels=""
for i in range(max(elevation),0,-1):
    for elev in elevation:
        pixels+=("   " if i>elev else " X ")
    pixels+="\n"
print(pixels)    


peak_valley=(valleys(elevation,peaks(elevation)))
peak_valley.sort()



print(peak_valley)


