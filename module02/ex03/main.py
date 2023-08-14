from csvreader import CsvReader
import sys 

if __name__ == "__main__":
    if len(sys.argv) > 0:
        filename = sys.argv[1]
        with CsvReader(filename, skip_top = 18, skip_bottom = 0) as csvreader:
            if csvreader != None:
                print("Header:\t", csvreader.getheader())
                print("Data:\t", csvreader.getdata(), "\n---------------------")
            else:
                print("File is corrupted or missing")

        with CsvReader(filename, header = True, skip_top = 17, skip_bottom = 0) as csvreader:
            if csvreader != None:
                print("Header:\t", csvreader.getheader())
                print("Data:\t", csvreader.getdata(), "\n---------------------")
            else:
                print("File is corrupted or missing")

# python main.py good.csv
# None
# [['Ruth', '       "F"', '   28', '       65', '      131']]
# ['Name', '     "Sex"', ' "Age"', ' "Height (in)"', ' "Weight (lbs)"']
# [['Ruth', '       "F"', '   28', '       65', '      131']]

# python main.py bad.csv
# File is corrupted or missing
# File is corrupted or missing

# python main.py unicorn.csv
# File is corrupted or missing
# File is corrupted or missing