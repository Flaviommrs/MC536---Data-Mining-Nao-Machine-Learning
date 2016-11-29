from data import data
from pytrends.request import TrendReq
import numpy as np
import pandas as pd
import time
import datetime

class trends:
        
    google_username = "machinelearningnaoedataminingail.com"
    google_password = "MLneDM42"

    PERIOD_SIZE = 670

    TERMS_PER_REQUEST = 5
    
    #regions = {'AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'}
    regions = {'SC', 'PR', 'RS'}
    #regions = {'SP'}

    dates = ['01/2004 36m', '01/2007 36m', '01/2010 36m', '01/2013 36m', '01/2016 10m']

    file_path = "db.txt"
    base_csv_file = "csv"
    
    def get_trends_safe(self, terms_array):

        # Parses array into a list of 4-term lists
        self.termsCount = len(terms_array)
        self.termsList = [None] * int(np.ceil(self.termsCount/self.TERMS_PER_REQUEST))
        for termIndex, termValue in enumerate(self.termsList):
            self.startIndex = termIndex * self.TERMS_PER_REQUEST
            self.endIndex = np.min([(self.startIndex+self.TERMS_PER_REQUEST),len(terms_array)])
            self.termsList[termIndex] = terms_array[self.startIndex:self.endIndex]
            self.termsList[termIndex] = [s.lower() for s in self.termsList[termIndex]]

        self.pytrend = TrendReq(self.google_username, self.google_password, custom_useragent = "My Pytrends Class")

        self.db = data()
        self.db.push_period(np.arange(0, self.PERIOD_SIZE))

        self.count = 1
        
        for regionIndex, region in enumerate(self.regions):
            print(region + ". " + str(regionIndex) + " of " + str(len(self.regions)))
            
            # The region for the request
            self.geo_tag = 'BR-' + region

            for termsListIndex, terms in enumerate(self.termsList):
                print("Terms " + str(termsListIndex) + " of " + str(len(self.termsList)))
                
                # The initial empty dataframe list
                self.dataframeList = [None] * len(self.dates)

                # The terms for the request
                self.terms_tag = ",".join(terms)
            
                # Requests trends for all set periods and stores in a sorted list
                for date in self.dates:
                    self.trend_payload = {'q':self.terms_tag, 'geo':self.geo_tag, 'date':date}
                    
                    while(True):
                        try:
                            self.df = self.pytrend.trend(self.trend_payload, return_type = 'dataframe')
                            self.dataframeList.insert(self.dates.index(date), self.df)
                            print(date)
                            time.sleep(120)
                            self.count = np.max([self.count-1,0])
                            break;
                        except Exception as exp:
                            print("Não rolou")
                            self.count = self.count + 1
                            self.wait = np.exp2([self.count])
                            print("Espera " + str(datetime.datetime.now()) + ", " + str(self.wait/60))
                            time.sleep(self.wait)

                # Concats all dataframes in list into a single dataframe
                self.dataframe = self.dataframeList[0]
                for i, df in enumerate(self.dataframeList):
                    if i > 0:
                        self.dataframe = self.dataframe.append(df)

                self.csvFile = self.base_csv_file + region + str(termsListIndex) + str(datetime.datetime.now()) + ".csv"
                self.dataframe.to_csv(self.csvFile, sep = ',', encoding = "utf-8")
                
                # Pushes data for each term for this region
                for term in terms:
                    self.db.push_sympthom(term, region, self.dataframe[term].values)
                
        self.db.save("data" + str(datetime.datetime.now()) + ".txt")
        
        return self.db

    
    def default_trends(self):
        
        self.terms = {"dor de cabeça,febre,dengue,amor,fogo"}
        self.splitTerms = list(self.terms)[0].split(',')

        self.pytrend = TrendReq(self.google_username, self.google_password, custom_useragent = "My Pytrends Script")

        self.db = data()
        self.db.push_period(np.arange(0, self.PERIOD_SIZE))

        for region in self.regions:
            self.dataframeList = [None] * len(self.dates)
            self.geo_tag = 'BR-' + region
            
            # Requests trends for all set periods and stores in a sorted list
            for date in self.dates:
                self.trend_payload = {'q':self.terms, 'geo':self.geo_tag, 'date':date}    
                try:
                    self.df = self.pytrend.trend(self.trend_payload, return_type = 'dataframe')
                    self.dataframeList.insert(self.dates.index(date), self.df)
                    print(date)
                except Exception as exp:
                    print(exp.args)
                    print("Não rolou")
                    
                time.sleep(40)

                # Concats all dataframes in list into a single dataframe
                self.dataframe = self.dataframeList[0]
                for i, df in enumerate(self.dataframeList):
                    if i > 0:
                        self.dataframe = self.dataframe.append(df)
                        
                print(region)
                print(self.dataframe)
                    
                # Pushes data for each term for this region
                for term in self.splitTerms:
                    self.db.push_sympthom(term, region, self.dataframe[term].values)
                            
                time.sleep(180)
                
        return self.db
