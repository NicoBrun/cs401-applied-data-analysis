####
####    IO helpers for the ADA project
####
####


import pandas as pd
import gzip



''' This function was provided on the amazon dataset's webpage
    It loads a gzipped file directly into a dataframe
'''
def json_gz_to_dataframe(filepath):
    def parse(path): 
        g = gzip.open(path, 'rb') 
        for l in g: 
            yield eval(l) 
    def getDF(path): 
        i = 0 
        df = {} 
        for d in parse(path): 
            df[i] = d 
            i += 1 
        return pd.DataFrame.from_dict(df, orient='index') 
    return getDF(filepath)
    
def gzip_to_dataframe(filepath) :
    json_gz_to_dataframe(filepath)
