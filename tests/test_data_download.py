import os
import shutil
import pytest

from src.data_download import unzip_data

def test_unzip_data():
    # Create a temporary directory to store the test data
    data_path = "tests/data"
    os.makedirs(data_path, exist_ok=True)

    # Copy a zip file to the test data directory
    shutil.copy("tests/test_data.zip", data_path)

    # Unzip the data
    unzip_data("test", data_path)

    # Check that the unzipped data is present
    assert os.path.isfile(os.path.join(data_path, "test.csv"))

    # Clean up the test data directory
    shutil.rmtree(data_path)
