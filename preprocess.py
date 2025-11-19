class DataPreprocessor:
    """
    A class to preprocess and merge Massachusetts market data with crime data from 2015 to 2024.
    """
    merged_df = None

    def __init__(self):
        # Imports
        import pandas as pd
        import numpy as np
        from pathlib import Path

        # Create a base directory (relative path)
        data_dir = Path("Data")
        pd.set_option('display.max_columns', None)
        marketData = pd.read_csv(data_dir /"slim_massachusetts_market_data.csv")

        # Skiprows for not reading the reader of the files
        Crime2024 = pd.read_csv(data_dir / "Number of Crimes by Offense Type_2024.csv", skiprows=5)
        Crime2023 = pd.read_csv(data_dir / "Number of Crimes by Offense Type_2023.csv", skiprows=5)
        Crime2022 = pd.read_csv(data_dir / "Number of Crimes by Offense Type_2022.csv", skiprows=5)
        Crime2021 = pd.read_csv(data_dir / "Number of Crimes by Offense Type_2021.csv", skiprows=5)
        Crime2020 = pd.read_csv(data_dir / "Number of Crimes by Offense Type_2020.csv", skiprows=5)
        Crime2019 = pd.read_csv(data_dir / "Number of Crimes by Offense Type_2019.csv", skiprows=5)
        Crime2018 = pd.read_csv(data_dir / "Number of Crimes by Offense Type_2018.csv", skiprows=5)
        Crime2017 = pd.read_csv(data_dir / "Number of Crimes by Offense Type_2017.csv", skiprows=5)
        Crime2016 = pd.read_csv(data_dir / "Number of Crimes by Offense Type_2016.csv", skiprows=5)
        Crime2015 = pd.read_csv(data_dir / "Number of Crimes by Offense Type_2015.csv", skiprows=5)

        # Filtering MA state housing data only
        marketData = marketData[marketData["STATE"] == "Massachusetts"]

        # Fixing the first rows where "Jurisdiction by Geography" is a row with NaN values due to multi-demonsionality
        Crime2015 = Crime2015[1:]
        Crime2016 = Crime2016[1:]
        Crime2017 = Crime2017[1:]
        Crime2018 = Crime2018[1:]
        Crime2019 = Crime2019[1:]
        Crime2020 = Crime2020[1:]
        Crime2021 = Crime2021[1:]
        Crime2022 = Crime2022[1:]
        Crime2023 = Crime2023[1:]
        Crime2024 = Crime2024[1:]

        # Rename "Offense Type" column to "CITY" in all crime dataframes
        for year in range(2015,2025):
            locals()[f"Crime{year}"] = locals()[f"Crime{year}"].rename(
                columns={"Offense Type": "CITY"}
            )

        # Converting NaN values into actuall null values
        Crime2015 = Crime2015.replace(["", " ", "NaN", "nan", "None"], np.nan)
        Crime2016 = Crime2016.replace(["", " ", "NaN", "nan", "None"], np.nan)
        Crime2017 = Crime2017.replace(["", " ", "NaN", "nan", "None"], np.nan)
        Crime2018 = Crime2018.replace(["", " ", "NaN", "nan", "None"], np.nan)
        Crime2019 = Crime2019.replace(["", " ", "NaN", "nan", "None"], np.nan)
        Crime2020 = Crime2020.replace(["", " ", "NaN", "nan", "None"], np.nan)
        Crime2021 = Crime2021.replace(["", " ", "NaN", "nan", "None"], np.nan)
        Crime2022 = Crime2022.replace(["", " ", "NaN", "nan", "None"], np.nan)
        Crime2023 = Crime2023.replace(["", " ", "NaN", "nan", "None"], np.nan)
        Crime2024 = Crime2024.replace(["", " ", "NaN", "nan", "None"], np.nan)

        # List of columns in Crime data - everything except the CITY column
        offense_cols = [c for c in Crime2024.columns if c != "CITY"]

        # Dropping rows where ALL offense columns are NaN
        Crime2015 = Crime2015.dropna(how="all", subset=offense_cols)
        Crime2016 = Crime2016.dropna(how="all", subset=offense_cols)
        Crime2017 = Crime2017.dropna(how="all", subset=offense_cols)
        Crime2018 = Crime2018.dropna(how="all", subset=offense_cols)
        Crime2019 = Crime2019.dropna(how="all", subset=offense_cols)
        Crime2020 = Crime2020.dropna(how="all", subset=offense_cols)
        Crime2021 = Crime2021.dropna(how="all", subset=offense_cols)
        Crime2022 = Crime2022.dropna(how="all", subset=offense_cols)
        Crime2023 = Crime2023.dropna(how="all", subset=offense_cols)
        Crime2024 = Crime2024.dropna(how="all", subset=offense_cols)

        # Resetting column indexes
        Crime2015 = Crime2015.reset_index(drop=True)
        Crime2016 = Crime2016.reset_index(drop=True)
        Crime2017 = Crime2017.reset_index(drop=True)
        Crime2018 = Crime2018.reset_index(drop=True)
        Crime2019 = Crime2019.reset_index(drop=True)
        Crime2020 = Crime2020.reset_index(drop=True)
        Crime2021 = Crime2021.reset_index(drop=True)
        Crime2022 = Crime2022.reset_index(drop=True)
        Crime2023 = Crime2023.reset_index(drop=True)
        Crime2024 = Crime2024.reset_index(drop=True)

        # Dropping unnecessary columns
        Crime2015 = Crime2015.drop(["Missing", "Unnamed: 59"], axis=1)
        Crime2016 = Crime2016.drop(["Missing", "Unnamed: 59"], axis=1)
        Crime2017 = Crime2017.drop(["Missing", "Unnamed: 59"], axis=1)
        Crime2018 = Crime2018.drop(["Missing", "Unnamed: 59"], axis=1)
        Crime2019 = Crime2019.drop(["Missing", "Unnamed: 59"], axis=1)
        Crime2020 = Crime2020.drop(["Missing", "Unnamed: 59"], axis=1)
        Crime2021 = Crime2021.drop(["Missing", "Unnamed: 59"], axis=1)
        Crime2022 = Crime2022.drop(["Missing", "Unnamed: 59"], axis=1)
        Crime2023 = Crime2023.drop(["Missing", "Unnamed: 59"], axis=1)
        Crime2024 = Crime2024.drop(["Missing", "Unnamed: 59"], axis=1)

        Crime2015 = Crime2015.apply(
            lambda col: col.astype(str)
                            .str.replace(',', '', regex=False)
                            .replace('nan', np.nan)
                            .infer_objects(copy=False)
                            .astype(float)
            if col.name != "CITY" else col
        )

        Crime2016 = Crime2016.apply(
            lambda col: col.astype(str)
                            .str.replace(',', '', regex=False)
                            .replace('nan', np.nan)
                            .infer_objects(copy=False)
                            .astype(float)
            if col.name != 'CITY' else col
        )

        Crime2017 = Crime2017.apply(
            lambda col: col.astype(str)
                            .str.replace(',', '', regex=False)
                            .replace('nan', np.nan)
                            .infer_objects(copy=False)
                            .astype(float)
            if col.name != 'CITY' else col
        )

        Crime2018 = Crime2018.apply(
            lambda col: col.astype(str)
                            .str.replace(',', '', regex=False)
                            .replace('nan', np.nan)
                            .infer_objects(copy=False)
                            .astype(float)
            if col.name != 'CITY' else col
        )

        Crime2019 = Crime2019.apply(
            lambda col: col.astype(str)
                            .str.replace(',', '', regex=False)
                            .replace('nan', np.nan)
                            .infer_objects(copy=False)
                            .astype(float)
            if col.name != 'CITY' else col
        )

        Crime2020 = Crime2020.apply(
            lambda col: col.astype(str)
                            .str.replace(',', '', regex=False)
                            .replace('nan', np.nan)
                            .infer_objects(copy=False)
                            .astype(float)
            if col.name != 'CITY' else col
        )

        Crime2021 = Crime2021.apply(
            lambda col: col.astype(str)
                            .str.replace(',', '', regex=False)
                            .replace('nan', np.nan)
                            .infer_objects(copy=False)
                            .astype(float)
            if col.name != 'CITY' else col
        )

        Crime2022 = Crime2022.apply(
            lambda col: col.astype(str)
                            .str.replace(',', '', regex=False)
                            .replace('nan', np.nan)
                            .infer_objects(copy=False)
                            .astype(float)
            if col.name != 'CITY' else col
        )

        Crime2023 = Crime2023.apply(
            lambda col: col.astype(str)
                            .str.replace(',', '', regex=False)
                            .replace('nan', np.nan)
                            .infer_objects(copy=False)
                            .astype(float)
            if col.name != 'CITY' else col
        )

        Crime2024 = Crime2024.apply(
            lambda col: col.astype(str)
                            .str.replace(',', '', regex=False)
                            .replace('nan', np.nan)
                            .infer_objects(copy=False)
                            .astype(float)
            if col.name != 'CITY' else col
        )


        # Add year column to each crime dataset
        Crime2015['year'] = 2015
        Crime2016['year'] = 2016
        Crime2017['year'] = 2017
        Crime2018['year'] = 2018
        Crime2019['year'] = 2019
        Crime2020['year'] = 2020
        Crime2021['year'] = 2021
        Crime2022['year'] = 2022
        Crime2023['year'] = 2023
        Crime2024['year'] = 2024

        # Combine all years into one crime table
        crime_all = pd.concat([
            Crime2015, Crime2016, Crime2017, Crime2018, Crime2019,
            Crime2020, Crime2021, Crime2022, Crime2023, Crime2024
        ], ignore_index=True)

        # Standardize city formatting
        crime_all['CITY'] = crime_all['CITY'].str.title().str.strip()
        marketData['CITY'] = marketData['CITY'].str.title().str.strip()

        crime_all = crime_all[~crime_all['CITY'].str.contains(
            r"State Police|Police|University|College|Campus|Missing",
            case=False, na=False
        )]

        ## Used to manually create name mapping for mismatched cities
        name_mapping = {
            "West Stockbridge": "Stockbridge",
            "West Springfield Town": "West Springfield",
            "Easthampton Town": "Easthampton",
            "Bridgewater Town": "Bridgewater",
            "North Attleborough Town": "North Attleborough",
            "Brookfield Ma": "Brookfield",
            "Southbridge Town": "Southbridge",
            "New Marlborough": "New Marlborough", 
            "West Wareham": "Wareham",
            "Braintree Town": "Braintree",
            "Shirley, Ma": "Shirley",
            "Mansfield Center": "Mansfield",
            "Greenfield Town": "Greenfield",
            "East Walpole": "Walpole",
            "Harwich Center": "Harwich",
            "Palmer Town": "Palmer",
            "North Seekonk": "Seekonk",
            "North Chelmsford": "Chelmsford",
            "South Duxbury": "Duxbury",
            "Mashpee Neck": "Mashpee",
            "Randolph Town": "Randolph",
            "Manchester": "Manchester-By-The-Sea", 
            "North Plymouth": "Plymouth",
            "North Eastham": "Eastham",
            "West Yarmouth": "Yarmouth",
            "Franklin Town": "Franklin",
            "Millis-Clicquot": "Millis",
            "West Townsend": "Townsend",
            "West Concord": "Concord",
            "North Amherst": "Amherst",
            "Acushnet Center": "Acushnet",
            "North Lakeville": "Lakeville",
            "Winthrop Town": "Winthrop",
            "Templeton 01468": "Templeton",
            "West Dennis": "Dennis",
            "East Douglas": "Douglas",
            "Watertown Town": "Watertown",
            "Barnstable Town": "Barnstable",
            "South Deerfield": "Deerfield",
            "West Warren": "Warren"
        }
        marketData['CITY'] = marketData['CITY'].replace(name_mapping)

        #Impute missing numeric columns in crime_all, replacing np.nan with median values
        numeric_cols = crime_all.select_dtypes(include=[np.number]).columns.tolist()
        for col in numeric_cols:
            crime_all[col].fillna(0, inplace=True)


        #Impute missing numeric columns in marketData, replacing np.nan with median values
        numeric_cols_market = marketData.select_dtypes(include=[np.number]).columns.tolist()
        for col in numeric_cols_market:
            marketData[col].fillna(0, inplace=True)

        ## Merged DataFrames
        merged_df = pd.merge(
            marketData,
            crime_all,
            on=["CITY", "year"],
            how="inner"   
        )

        self.merged_df = merged_df
    
    def get_merged_data(self):
        return self.merged_df

