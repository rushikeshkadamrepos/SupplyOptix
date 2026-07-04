import pandas as pd


class FeatureEngineering:

    @staticmethod
    def create_inventory_status(df: pd.DataFrame) -> pd.DataFrame:
        """
        Categorize warehouse inventory into
        LOW / MEDIUM / HIGH.
        """

        df["inventory_status"] = pd.cut(
            df["warehouse_inventory_level"],
            bins=[-1, 200, 600, float("inf")],
            labels=["LOW", "MEDIUM", "HIGH"]
        )

        return df