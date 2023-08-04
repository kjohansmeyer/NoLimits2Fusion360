import numpy as np
import pandas as pd

# Citation: https://www.youtube.com/watch?v=dHXfdS6XF8g&t=53s&ab_channel=PrintMyRideDetroit
# This program automates the Excel work to open NoLimits2 coordinates as splines in Fusion 360

print("Instructions: Export from NoLimits2 Professional Edition")
print("In NoLimits2: Professional > Export Track Spline > Editor Spline")

filename = "editorsplinetest.csv" #put the CSV in this directory

# The entire coaster is scaled to make this the maximum height
maxHeight = float(input("Maximum Height (mm): "))

# Import CSV
dataframe = np.array(pd.read_csv(filename,delim_whitespace=True))
numPoints = dataframe.shape[0]

# Define Arrays:
leftArray = np.zeros((numPoints,3))
centerArray = np.zeros((numPoints,3))
rightArray = np.zeros((numPoints,3))

# Array Calculations:
for n in range(0,numPoints-1):
    # Note: x, y, and z are switched to match Fusion's coordinate system
    leftArray[n][0] = dataframe[n][3]+dataframe[n][9] #Lx
    leftArray[n][1] = dataframe[n][1]+dataframe[n][7] #Ly
    leftArray[n][2] = dataframe[n][2]+dataframe[n][8] #Lz
    leftArray[numPoints-1] = leftArray[0] #copy first row to the last to make a circuit
    
    centerArray[n][0] = dataframe[n][3] #Cx
    centerArray[n][1] = dataframe[n][1] #Cy
    centerArray[n][2] = dataframe[n][2] #Cz
    centerArray[numPoints-1] = centerArray[0] #copy first row to the last to make a circuit
    
    rightArray[n][0] = dataframe[n][3]-dataframe[n][9] #Rx
    rightArray[n][1] = dataframe[n][1]-dataframe[n][7] #Ry
    rightArray[n][2] = dataframe[n][2]-dataframe[n][8] #Rz
    rightArray[numPoints-1] = rightArray[0] #copy first row to the last to make a circuit

# Rescale Arrays to Proper Height:
zCenterMax = np.amax(centerArray[:, 2])
leftArray = (maxHeight/zCenterMax)*leftArray
centerArray = (maxHeight/zCenterMax)*centerArray
rightArray = (maxHeight/zCenterMax)*rightArray

# Save Arrays as CSVs:
np.savetxt("0leftArrayAll.csv",leftArray,delimiter=",")
np.savetxt("1centerArrayAll.csv",centerArray,delimiter=",")
np.savetxt("2rightArrayAll.csv",rightArray,delimiter=",")

print("Type '0' for number of points - makes each piece X points long")
print("Type '1' for segments - splits ride into equal pieces")
selection = int(input("Selection: "))

if selection == 0:

    nValues = int(input("Enter the number of values per file: "))
    for n in range(0,int(np.ceil(numPoints/nValues))):
        leftArraySlice = leftArray[n*nValues:(n+1)*nValues+1]
        np.savetxt("3leftArray{}.csv".format(n),leftArraySlice,delimiter=",")
        centerArraySlice = centerArray[n*nValues:(n+1)*nValues+1]
        np.savetxt("4centerArray{}.csv".format(n),centerArraySlice,delimiter=",")
        rightArraySlice = rightArray[n*nValues:(n+1)*nValues+1]
        np.savetxt("5rightArray{}.csv".format(n),rightArraySlice,delimiter=",")

elif selection == 1:
    nSegments = int(input("Enter the number of segments: "))
    nValues = numPoints // nSegments
    nRemainder = numPoints % nSegments
    for n in range(0,int(nSegments)):
        leftArraySlice = leftArray[n*nValues:(n+1)*nValues+1]
        np.savetxt("3leftArray{}.csv".format(n),leftArraySlice,delimiter=",")
        centerArraySlice = centerArray[n*nValues:(n+1)*nValues+1]
        np.savetxt("4centerArray{}.csv".format(n),centerArraySlice,delimiter=",")
        rightArraySlice = rightArray[n*nValues:(n+1)*nValues+1]
        np.savetxt("5rightArray{}.csv".format(n),rightArraySlice,delimiter=",")
        
        if nRemainder != 0:
            leftArraySlice = leftArray[-nRemainder:]
            leftArraySlice = np.vstack((leftArraySlice,leftArray[0]))
            np.savetxt("3leftArrayRemainder.csv",leftArraySlice,delimiter=",")
            centerArraySlice = centerArray[-nRemainder:]
            centerArraySlice = np.vstack((centerArraySlice,centerArray[0]))
            np.savetxt("4centerArrayRemainder.csv",centerArraySlice,delimiter=",")
            rightArraySlice = rightArray[-nRemainder:]
            rightArraySlice = np.vstack((rightArraySlice,rightArray[0]))
            np.savetxt("5rightArrayRemainder.csv",rightArraySlice,delimiter=",")
            
else:
    print("Please type a valid selection")
    
print("\nComplete - check folder for new CSV files")

print("Fusion 360: Utilities > Add-ins > ImportSplineCSV")
print("Import all files starting with '3', '4', and '5'")
