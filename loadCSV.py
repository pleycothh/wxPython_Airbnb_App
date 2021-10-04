import csv

import numpy as np
class LoadCSV():
    def __init__(self):
        self.name = 'src/listings_summary_dec18.csv'
        self.load()


    def load(self):
        with open(self.name, newline='',encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                print(row)
                break








LoadCSV()