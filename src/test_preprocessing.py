from preprocessing import DataLoader
from data_quality import DataQuality
from feature_engineering import FeatureEngineering


def main():

    loader = DataLoader(
        "../data/dynamic_supply_chain_logistics_dataset_with_country.csv"
    )

    df = loader.load_data()

    loader.display_basic_info(df)

    # Feature Engineering
    df = FeatureEngineering.create_inventory_status(df)

    print("\nInventory Status Sample")

    print(
        df[
            [
                "warehouse_inventory_level",
                "inventory_status"
            ]
        ].head(10)
    )

    # Data Quality Checks
    DataQuality.check_missing_values(df)

    DataQuality.check_duplicates(df)

    DataQuality.display_statistics(df)


if __name__ == "__main__":
    main()