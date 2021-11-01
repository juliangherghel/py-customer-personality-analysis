
import os
from typing import List
import pandas as pd


def get_datafile_path() -> str:
    absolute_path = os.path.abspath(__file__)
    return os.path.dirname(absolute_path) + "\\data\\"


def list_data_files(data_directory: str) -> List:
    # Rename files in data folder
    list_of_files = []
    for data_file in os.listdir(data_directory):
        file_path = os.path.join(data_directory, data_file)

        # Check that a file exists and does not have a "raw_" prefix in name
        if os.path.isfile(file_path) and "raw_" not in data_file:
            if "clean_" not in data_file:
                # If there is only one data file in the folder
                if len(os.listdir(data_directory)) == 1:
                    os.rename(file_path,
                              os.path.join(data_directory, "raw_data.csv"))
                # If more than 1 file then add "raw_" prefix
                else:
                    os.rename(file_path,
                              os.path.join(data_directory, f"raw_{data_file}"))

        # Append to list of files to be read into pandas DataFrames
        if "raw_" in data_file:
            list_of_files.append(file_path)

    return list_of_files


def load_to_dataframe(data_directory: str) -> pd.DataFrame:
    return pd.read_csv(data_directory, sep='\t')  # Tab separator


def remove_missing_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe.dropna(axis=0, inplace=True, how="any")


def remove_duplicates(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe.drop_duplicates(subset=None, keep="first", inplace=True,
                                     ignore_index=False)


def export_dataset(dataframe: pd.DataFrame, data_directory: str) -> None:
    dataframe.to_csv(data_directory, sep=',', index=False)


def main():
    data_path = get_datafile_path()
    csv_list = list_data_files(data_path)

    # # Load each csv into a DataFrame and key by "df_x" where x is csv number
    df_list = []
    for item in range(0, len(csv_list)):
        df_list.append(load_to_dataframe(csv_list[item]))
    for df in df_list:
        remove_missing_data(df)
        remove_duplicates(df)
    for i in range(0, len(df_list)):
        export_dataset(df, data_path + "\\clean_df_" + f"{i + 1}" + ".csv")


if __name__ == '__main__':
    main()
