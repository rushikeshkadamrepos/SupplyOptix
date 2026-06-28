from preprocessing import DataLoader


def main():

    loader = DataLoader(
        "../data/dynamic_supply_chain_logistics_dataset_with_country.csv"
    )

    df = loader.load_data()

    loader.display_basic_info(df)


if __name__ == "__main__":
    main()