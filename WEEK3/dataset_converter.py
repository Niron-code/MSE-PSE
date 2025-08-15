import pandas as pd
import numpy as np
import os

class DatasetConverter:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None

    def load_csv(self):
        self.df = pd.read_csv(self.csv_path)
        print(f"Loaded dataset with shape: {self.df.shape}")

    def to_parquet(self, parquet_path):
        if self.df is not None:
            self.df.to_parquet(parquet_path, index=False)
            print(f"Saved Parquet file to: {parquet_path}")
        else:
            print("DataFrame is empty. Load CSV first.")

    def compute_statistics(self):
        if self.df is None:
            print("DataFrame is empty. Load CSV first.")
            return None
        stats = {}
        for col in self.df.select_dtypes(include=[np.number]).columns:
            stats[col] = {
                'max': self.df[col].max(),
                'min': self.df[col].min(),
                'mean': self.df[col].mean(),
                'abs': self.df[col].abs().tolist() if np.issubdtype(self.df[col].dtype, np.number) else None
            }
        return stats

    def print_statistics(self):
        stats = self.compute_statistics()
        if stats:
            for col, stat in stats.items():
                print(f"Column: {col}")
                print(f"  Max: {stat['max']}")
                print(f"  Min: {stat['min']}")
                print(f"  Mean: {stat['mean']}")
                print(f"  Abs: {stat['abs'][:5]} ... (showing first 5)")

if __name__ == "__main__":
    csv_file = os.path.join(os.path.dirname(__file__), "name_gender_dataset.csv")
    parquet_file = os.path.join(os.path.dirname(__file__), "name_gender_dataset.parquet")
    converter = DatasetConverter(csv_file)
    converter.load_csv()
    converter.to_parquet(parquet_file)
    converter.print_statistics()
