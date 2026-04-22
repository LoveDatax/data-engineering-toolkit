import pandas as pd

def extract_from_csv(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        print(f"Data extracted successfully from {file_path}")
        return df
    except Exception as e:
        print(f"Error extracting data: {e}")
        return pd.DataFrame()