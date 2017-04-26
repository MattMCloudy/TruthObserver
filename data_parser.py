import pandas as pd
import numpy as np


class Parser:   
    def __init__(self):
        self.politifact_data = pd.DataFrame()
        self.snopes_data = pd.DataFrame()
        self.politiface_whole_data = pd.DataFrame()
        self.trainable = pd.DataFrame()
   
    def readCSV(self):
        self.politifact_data = pd.read_csv('data/politifact_climate_scrape.csv')
        self.snopes_data = pd.read_csv('data/snopes_factcheck_scrape.csv')
        self.politifact_whole_data = pd.read_csv('data/politifact_whole_scrape.csv')

    def pantsOnFire(self):
        return 0.0

    def false(serlf):
        return 0.2

    def mostlyFalse(self):
        return 0.4

    def halfTrue(self):
        return 0.6

    def mostlyTrue(self):
        return 0.8
    
    def true(self):
        return 1.0

    def flipFlop(self):
        return 0.5
    
    def parseData(self):
        del self.politifact_data['pagination']
        del self.politifact_data['pagination-href']
        
        self.trainable['text'] = self.politifact_data['text']
        self.trainable['truthVals'] = 1
        for i,x in enumerate(self.politifact_data['link_to_truth_page-src']):
            switch_dict = { 'http://static.politifact.com.s3.amazonaws.com/rulings/tom-pantsonfire.gif': self.pantsOnFire(),
                            'http://static.politifact.com.s3.amazonaws.com/rulings/tom-false.png': self.false(),
                            'http://static.politifact.com.s3.amazonaws.com/rulings/tom-mostlyfalse.png': self.mostlyFalse(),
                            'http://static.politifact.com.s3.amazonaws.com/rulings/tom-halftrue.png': self.halfTrue(),
                            'http://static.politifact.com.s3.amazonaws.com/rulings/tom-mostlytrue.png': self.mostlyTrue(),
                            'http://static.politifact.com.s3.amazonaws.com/rulings/tom-true.png': self.true(),
                            'http://static.politifact.com.s3.amazonaws.com/rulings/fom-fullFlop.png': self.flipFlop(),
                            'http://static.politifact.com.s3.amazonaws.com/rulings/fom-halfFlip.png': self.flipFlop()}
            self.trainable.loc[0, 'truthVals']  = switch_dict[x]
        
        
        print(self.trainable) 
        

if __name__ == '__main__':
    obj = Parser()
    obj.readCSV()
    obj.parseData()
