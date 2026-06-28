import pandas as pd
from pathlib import Path


class DataLoader:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):

        path = Path(self.file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {self.file_path}"
            )

        df = pd.read_csv(self.file_path)

        print("Dataset loaded successfully")

        return df

    @staticmethod
    def display_basic_info(df):

        print("\n========== DATASET INFO ==========")

        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")

        print("\nColumn Names:")

        for column in df.columns:
            print(column)

        print("\n==================================")
