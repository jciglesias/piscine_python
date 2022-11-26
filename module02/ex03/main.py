from csvreader import CsvReader
import sys 

if __name__ == "__main__":
    if len(sys.argv) > 0:
        filename = sys.argv[1]
        with CsvReader(filename, skip_top = 16, skip_bottom = 2) as csvreader:
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