import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        # Drop duplicates
        df = df.drop_duplicates()

        # Clean amount column (remove currency symbols)
        if 'amount' in df.columns:
            df['amount'] = df['amount'].replace('[^0-9.]', '', regex=True).astype(float)

        # Normalize text columns
        if 'city' in df.columns:
            df['city'] = df['city'].str.strip().str.upper()

        # Handle missing values
        df = df.fillna({'city': 'UNKNOWN'})

        print("Data transformation completed")
        return df

    except Exception as e:
        print(f"Error transforming data: {e}")
        return df
