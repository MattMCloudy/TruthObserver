import pandas as pd
import numpy as np


class Parser:
    
    def __init__(self, politifact_path, snopes_path):
        self.politifact_data = pd.DataFrame()
        self.snopes_data = pd.DataFrame()
    
    def readCSV(self):
        self.politifact_data = pd.read_csv('data/politifact_climate_scrape.csv')
        self.snopes_data = pd.read_csv('data/snopes_factcheck_scrape.csv')
        print politifact_data
        print snopes_data
        

if __name__ == '__main__':
    obj = Parser()
    obj.readCSV()

