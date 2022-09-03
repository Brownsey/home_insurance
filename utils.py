import pandas as pd
import pickle

def get_missing_column_values(df):
    """Generates a table containing the columns which contain missing data
     and their missing data counts

    Args:
        df (pd.DataFrame): original pd.DataFrame to 
    Returns:
        df (pd.DataFrame): new table containing columns with missing data and their ratio
    """
    count = df.isna().sum()
    df = (pd.concat([count.rename('missing_count'),
                       100* count.div(len(df))
                            .rename('missing_percentage')], axis = 1)
                .loc[count.ne(0)]).reset_index().rename(columns={"index":"column"}).round(2)
    
    return df.sort_values("missing_percentage", ascending=False)


#pickle functions for saving model outputs and option to import them back in
def pickle_model(params, file):
    f = open(file,"wb")
    pickle.dump(params,f)
    f.close()

def import_pickled_model(file):    
    infile = open(file,'rb')
    pickled_model = pickle.load(infile)
    infile.close()
    return pickled_model








    
                
