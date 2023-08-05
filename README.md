# NoLimits2Fusion360

This is a Python program to import NoLimits2 Roller Coasters into Fusion 360.

Note: NoLimits2 Roller Coaster Professional Edition is needed for use of this program.

In NoLimits2 Professional Edition:
1. Open the roller coaster
2. Go to Professional > Export Track Spline
3. Export "Editor Spline". Distance between points may vary, but you may want to use  0.5 meters or 1.0 meters.

![NoLimits2screenshot](https://imgur.com/TVdKicZ)

In File Explorer:
1. Download NoLimits2Fusion360.py and put it in the same folder as your exported CSV.
2. Change line 10 of the Python code to match the expected file name.

In Python:
1. Run the Python program and complete the following prompts:
2. Type in maximum height in millimeters. The entire array and coaster will be scaled accordingly.
3. Type '0' for number of points - makes each piece X points long OR type '1' for segments - splits ride into equal pieces.
4. Type in the number of points OR the number of segments.
5. The new CSV files will automatically populate in the same location as NoLimits2Fusion360.py.

In Fusion360:
1. Go to Utilities > Add-ins > ImportSplineCSV
2. Import all files starting with '3', '4', and '5'.

![Fusion360screenshot](https://imgur.com/4FQ3TR0)

Further Fusion360 instructions - see the following video: https://youtu.be/7zUMft1ZAg4



