import pandas as pd

def list_to_df(a_list):
    df = pd.DataFrame({'my_list' : a_list})
    print(df)
    return df

my_list = [2,3,4,5,6]
my_list_df = list_to_df(my_list)
