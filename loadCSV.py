import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class LoadCSV():
    def __init__(self):
        self.name = 'src/listings_summary_dec18.csv'
        self.load()

    def load(self):
        summary = pd.read_csv(self.name)
        return summary



#LoadCSV()