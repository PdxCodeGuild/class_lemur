let data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
function peaks(data){
    let peakIndexes =[]
    for (let i=0; i<peaks.length;)
        if (peaks[i] != 0 && peaks[i] != data.length - 1)
            if (data[i] > data[i--] && data[i] > data[i+1])
                peakIndexes.append(i)
    return peakIndexes
}

function valleys(data){
    let valleyIndexes = []
    for let i=0 in range(len(data)):
        if i != 0 && i != len(data) - 1:
            if data[i] < data[i-1] && data[i] < data[i+1]:
                valleyIndexes.append(i)
    return valleyIndexes
}
        
myPeaks = peaks(data)
print(my_peaks)
myValleys = valleys(data)
print(myValleys)

peaksAndValleys = my_peaks.extend(myValleys)
peaksAndValleys = sorted(myPeaks)
print(peaksAndValleys)