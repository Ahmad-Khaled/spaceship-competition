import pandas as pd
from sklearn.preprocessing import StandardScaler

def standardize_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Standardizes the numeric columns in a pandas dataframe.

    Args:
        df: The dataframe to standardize.

    Returns:
        A new dataframe with the numeric columns standardized.
    """
    # Clone dataframe before doing any transformation
    df = df.copy()
    # Select only the numeric columns
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

    # Create the StandardScaler object
    scaler = StandardScaler()

    # Fit the scaler to the numeric columns
    scaler.fit(df[numeric_columns])

    # Transform the numeric columns
    df[numeric_columns] = scaler.transform(df[numeric_columns])

    return df
