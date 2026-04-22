import pandas as pd
import os

def load_to_csv(df: pd.DataFrame, output_path: str):
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"Data successfully loaded to {output_path}")
    except Exception as e:
        print(f"Error loading data: {e}")
