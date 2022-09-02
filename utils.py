import pandas as pd

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
    







    
                
