import pandas as pd

"""
    Preprocesses the given DataFrame by performing the following steps:
    - Converts 'release_date' to datetime.
    - Drops specified columns.
    - Drops rows with missing 'release_date'.
    - Fills missing values with zero for specified columns.
    - Converts 'console' column values to lowercase.


    Parameters:
    df (pd.DataFrame): The DataFrame to preprocess.


    Returns:
    pd.DataFrame: The preprocessed DataFrame.
    """


def preprocess_data(df):
    df = df.copy()
    df['release_date'] = pd.to_datetime(df['release_date'])
    df.drop(['img', 'last_update'], axis=1, inplace=True)
    df = df.dropna(subset=['release_date'])
    columns_to_fill_zero = ['critic_score', 'total_sales', 'na_sales', 'jp_sales', 'pal_sales', 'other_sales']
    df.loc[:, columns_to_fill_zero] = df.loc[:, columns_to_fill_zero].fillna(0)
    df['console'] = df['console'].str.lower()
    return df
