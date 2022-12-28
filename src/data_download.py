import os
import kaggle
import zipfile

def download_data(competition_name: str, kaggle_json_path: str):
    """Download data from Kaggle for a given competition.

    Parameters:
    competition_name (str): the name of the Kaggle competition
    kaggle_json_path (str): the path to the Kaggle API JSON file
    """
    # Load the Kaggle API JSON file
    os.environ["KAGGLE_CONFIG_DIR"] = os.path.dirname(kaggle_json_path)
    kaggle.api.authenticate()

    # Download the data
    kaggle.api.competition_download_files(competition_name, path="data/raw/")

def unzip_data(competition_name: str, data_path: str):
    """Unzip the downloaded data for a given competition.

    Parameters:
    competition_name (str): the name of the Kaggle competition
    data_path (str): the path to the directory containing the downloaded data
    """
    # Check if the data_path is a valid directory 
    if not os.path.isdir(data_path):
        raise ValueError(f"{data_path} is not a valid directory")

    # Initialize the zip path to None
    zip_path = None

    # Find the zip file for the competition
    for root, dirs, files in os.walk(data_path):
        for file in files:
            if file.endswith(".zip") and competition_name in file:
                zip_path = os.path.join(root, file)
                break

    # Check if the zip file was found
    if zip_path is None:
        raise ValueError(f"Zip file for competition {competition_name} not found in {data_path}")

    # Unzip the data
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(data_path)
