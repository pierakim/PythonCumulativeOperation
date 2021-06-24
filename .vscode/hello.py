import csv
import os

# Record object
class Record:
  def __init__(self, objectId, code, elevation, dateConverted, accumulativeElevation):
    self.objectId = objectId
    self.code = code
    self.elevation = elevation
    self.dateConverted = dateConverted
    self.accumulativeElevation = accumulativeElevation

# Root path - file name - file path
root = os.path.realpath('.')
fileName = 'Subset.csv'
filePath = os.path.join(root, fileName)

recordList = [] 

# CSV  - Read
with open(filePath, 'r') as inputFile:
    csv_reader = csv.reader(inputFile, delimiter=',')
    # Skip first line
    inputFile.readline()
    
    # Flags
    line = 0
    cumulative = 0
    previousCode = ''
    isFirstLine = True

    for data in csv_reader:
        # Line counter
        line += 1
        print('line: ', line)

        cumulative +=  float(data[2])
        # Reset cumulative when code change
        if previousCode != data[1] and not isFirstLine:
            cumulative = 0

        previousCode = data[1]

        # Logs
        print('Object ID: ', data[0])
        print('Current elevation: ', data[2])
        print('Cumulative: ', cumulative)

        isFirstLine = False

        # Store object in collection
        recordList.append(Record(data[0], data[1], data[2], data[3], cumulative))


# New CSV - header 
header = ['Object_ID', 'CODE', 'Elevation', 'Dates_Converted', 'Accumulative_Elevation']

# New CSV - process
outputFileName = os.path.splitext(fileName)[0]
with open(os.path.join(root, outputFileName) + '_output.csv', 'w',  newline='', encoding='UTF8') as fw:
    writer = csv.writer(fw)
    writer.writerow(header)
    for record in recordList:
        rowToWrite = [record.objectId, record.code, record.elevation, record.dateConverted, record.accumulativeElevation]
        print(rowToWrite)
        writer.writerow(rowToWrite)
fw.close()
