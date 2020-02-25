import pandas as pd

t = pd.read_csv('/Users/seangao/Desktop/Research/data/transactions.csv')

def listofLists(t):
    p1 = t.drop('transaction', axis=1)
    p1 = p1.groupby('cid')['date'].apply(list)
    p1 = p1.to_frame()
    p1 = p1.reset_index()

    p2 = t.groupby(['cid', 'date'])['transaction'].apply(list).groupby(level=0).apply(list)
    p2 = p2.to_frame()
    p2 = p2.reset_index()

    df = pd.merge(p1, p2, on='cid')
    return df

#TEST
df = listofLists(t)



