import io

class CsvReader():
    def __init__(self, filename = None, sep = ',', header = False, skip_top = 0, skip_bottom = 0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.header_line = None
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.dim = -1
        self.data = []
    def __enter__(self):
        try:
            self.file = open(self.filename, "r")
        except:
            return None
        file: str = self.file.read()
        total = file.count("\n")
        buff = io.StringIO(file)
        line = buff.readline()
        if self.header:
            total -= 1
            self.header_line = line.strip("\n").split(self.sep)
            self.dim = len(self.header_line)
            line = buff.readline()
        i = 0
        tmp = None
        while (line):
            if not self.skip_top or (i >= self.skip_top and i < (total - self.skip_bottom)):
                tmp = line.strip("\n").split(self.sep)
                if self.dim == -1:
                    self.dim = len(tmp)
                else:
                    if self.dim != len(tmp):
                        return None
                for x in tmp:
                    if x == "":
                        return None
                self.data.append(tmp)
            i += 1
            line = buff.readline()
        return self
    def __exit__(self, exc_type, exc_value, exc_traceback):
        try:
            # print(exc_type, exc_value, exc_traceback)
            self.file.close()
        except:
            pass
    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        return self.data
    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        return self.header_line