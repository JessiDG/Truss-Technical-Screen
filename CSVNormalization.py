#This is a tool which a tool that reads a CSV formatted file on `stdin` and emits a normalized CSV formatted file on `stdout

import csv
import unittest
import string
from shutil import copy2
from datetime import datetime

"""Issues with this tool:
- Methods left to be completed: normalize_timestamp, normalize_zip, normalize_foo_duration, normalize_bar_duration, and normalize_total_duration
- Note: because of the utf checking throughout the tool there was no need for a normalize_address or normalize_notes methods 
"""
class Normalize:
    """
    One object of class Normalize represents a Normalize object, which takes a csv file and normalizes it per the README
    """
    fileCopyName = 'sample_copy.csv'
    normalizedFile = 'normalizedFile.csv'
    copy2('sample.csv', fileCopyName)

    with open(fileCopyName, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        reader = csv.DictReader(csvfile)
        # for row in reader:
        #     # print(row['FooDuration'], row['BarDuration'])
        #     print(row['Timestamp'])

    def __int__(self):
        """This is the initialization method"""

    def normalize(self, filename):
        """This method calls all of the other normalization methods"""
        self.normalize_timestamp()
        self.normalize_foo_duration()
        self.normalize_bar_duration()
        self.normalize_total_duration()
        self.normalize_zip()
        self.normalize_fullname()

    def normalize_timestamp(self):
        """This method takes the timestamp from '%m/%d/%y %I:%M:%S %p' and converts it to ISO-8601 format (%d/%m/%Y %H:%M:%S)"""
        with open(self.fileCopyName, 'r', newline='', encoding='utf-8') as infile, open(self.normalizedFile, 'w') as outfile:
            writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
            reader = csv.DictReader(infile)
            print("normalize_timestamp:")
            for row in reader:
                print(row['Timestamp'])
            print()

        # date = datetime.strptime('Thu, 16 Dec 2010 12:14:05', '%a, %d %b %Y %H:%M:%S')
        # date.isoformat()
        # print(date)


        #     for row in reader:
        #         if row[0] != "Timestamp":
        #             date = datetime.strptime(row[0], '%m/%d/%y %I:%M:%S %p')
        #             row[0] = date.strftime('%d/%m/%Y %H:%M:%S')
        #             writer.writerow(row)
        #         # if row[0] != "":
                #     writer.writerow(row)

    # def normalize_address(self):
    #     """This method"""
    #     print("normalizeAddress: ")
    #     with open(self.fileCopyName, 'w', newline='', encoding='utf-8') as csvfile:
    #         writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #         reader = csv.reader(self.fileCopyName)
    #         for row in reader:
    #             writer.writerow(row)

    def normalize_zip(self):
        """This method adds a zero to the front of any zipcode under length 5"""
        print("normalize_zip: ")
        with open(self.fileCopyName, 'r', newline='', encoding='utf-8') as infile, open(self.normalizedFile, 'w') as outfile:
            writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
            reader = csv.DictReader(infile)
            for row in reader:
                holder = str(row['ZIP'])
                if len(str(row['ZIP'])) < 5:
                    holder = "0" + holder
                writer.writerow([holder])
                print(row['ZIP'])
        print()

    def normalize_fullname(self):
        """This method capitalizes all names in languages with capitalization (e.g., French but not Arabic)"""
        print("normalize_fullname: ")
        with open(self.fileCopyName, 'r', newline='', encoding='utf-8') as infile, open(self.normalizedFile, 'w') as outfile:
            writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
            reader = csv.DictReader(infile)
            for row in reader:
                holder = str(row['FullName'])
                row['FullName'] = holder.upper()
                writer.writerow([holder.upper()])
                print(row['FullName'])
        print()

    def normalize_foo_duration(self):
        """This method converts FooDuration to a floating point format"""
        print("normalize_foo_duration: ")
        with open(self.fileCopyName, 'r', newline='', encoding='utf-8') as infile, open(self.normalizedFile, 'w') as outfile:
            writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
            reader = csv.DictReader(infile)
            for row in reader:
                print(row['FooDuration'])
        print()

    def normalize_bar_duration(self):
        """This method converts BarDuration to a floating point format"""
        print("normalize_bar_duration: ")
        with open(self.fileCopyName, 'r', newline='', encoding='utf-8') as infile, open(self.normalizedFile, 'w') as outfile:
            writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
            reader = csv.DictReader(infile)
            for row in reader:
                print(row['BarDuration'])

        print()

    def normalize_total_duration(self):
        """This method adds FooDuration and BarDuration together"""
        print("normalize_total_duration: ")
        with open(self.fileCopyName, 'r', newline='', encoding='utf-8') as infile, open(self.normalizedFile, 'w') as outfile:
            writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
            reader = csv.DictReader(infile)
            for row in reader:
                print(row['TotalDuration'])
        print()

    # def normalize_notes(self):
    #     print("normalizeNotes: ")

if __name__ == "__main__":
    normalFile = Normalize()
    normalFile.normalize('sample.csv')
    unittest.main()