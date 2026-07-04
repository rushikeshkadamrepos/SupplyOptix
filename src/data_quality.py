class DataQuality:

    @staticmethod
    def check_missing_values(df):

        print("\n========== MISSING VALUES ==========")

        missing_values = df.isnull().sum()

        print(missing_values)

        print("\n====================================")

    @staticmethod
    def check_duplicates(df):

        print("\n========== DUPLICATES ==========")

        duplicate_count = df.duplicated().sum()

        print(f"Duplicate Records: {duplicate_count}")

        print("\n===============================")

    @staticmethod
    def display_statistics(df):

        print("\n========== STATISTICS ==========")

        print(df.describe())

        print("\n===============================")