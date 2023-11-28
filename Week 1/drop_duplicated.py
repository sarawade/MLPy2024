# Run inside Juypter notebook cell. Example use:
# %run show_solutions.py W1_ex3
# Shows a button to toggle solutions tagged with 'W1_ex3'
# in the solutions script 'W1_solutions.txt'.

def drop_duplicated(X,y):
    df = pd.concat([X,y], axis=1)
    df = df.drop_duplicates()
    return df.iloc[:,:-1], df.iloc[:,-1]


