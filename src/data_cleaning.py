import pandas as pd

class ColumnSplitter:
    def __init__(self, df: pd.DataFrame, column: str, sep: str):
        """Initialize the ColumnSplitter.

        Parameters:
        df (pd.DataFrame): the DataFrame to split the column from
        column (str): the name of the column to split
        sep (str): the separator to use for splitting the column
        """
        self.df = df
        self.column = column
        self.sep = sep

    def split_column(self, ordered_required_columns: list):
        """Split the column into three new columns: 'column1', 'column2', 'column3'

        Returns:
        None
        """
        new_columns = self.df[self.column].str.split(self.sep, expand=True)
        self.df[ordered_required_columns[0]] = new_columns[0]
        self.df[ordered_required_columns[1]] = new_columns[1]
        self.df[ordered_required_columns[2]] = new_columns[2]
        self.df = self.df.drop(columns=[self.column])


class DataFrameImputation:
    """A class for transforming a Pandas DataFrame.

    Parameters:
    df (pandas.DataFrame): the DataFrame to transform
    impute_numeric_with_mean (bool): whether to impute missing values in numeric columns with the mean (default: True)
    impute_string_with_mode (bool): whether to impute missing values in string columns with the mode (default: True)
    drop_string_columns (bool): whether to drop string columns (default: False)
    """
    def __init__(self, df: pd.DataFrame, impute_numeric_with_mean: bool = True, 
                 impute_string_with_mode: bool = True, drop_string_columns: bool = False):
        self._df = df.copy()
        self.impute_numeric_with_mean = impute_numeric_with_mean
        self.impute_string_with_mode = impute_string_with_mode
        self.drop_string_columns = drop_string_columns

    @property
    def df(self):
        return self._df

    @df.setter
    def df(self, input_df):
        self._df = input_df

    def impute_numeric_columns(self):
        """Impute the numeric columns with the mean.
        
        Modifies the DataFrame in place.
        """
        numeric_columns = self.df.select_dtypes(include=["int", "float"]).columns
        self.df[numeric_columns] = self.df[numeric_columns].fillna(self.df[numeric_columns].mean())

    def impute_string_columns(self):
        """Impute the string columns with the mode, or drop them.
        
        Modifies the DataFrame in place.
        """
        string_columns = self.df.select_dtypes(include=["object"]).columns
        if self.impute_string_with_mode:
            for s in string_columns:
                self.df[s] = self.df[s].fillna(self.df[s].mode()[0])
        elif self.drop_string_columns:
            self.df = self.df.dropna(subset=string_columns)


    def extract_features(self, features: list):
        """Extract the desired features from the DataFrame.
        
        Modifies the DataFrame in place.
        
        Parameters:
        features (list): a list of the desired features
        """
        self.df = self.df[features]
