import pytest
from uv_pck.src.data_loader import DataLoader
import re 

@pytest.fixture
def data_loader():
    return DataLoader()

@pytest.mark.parametrize("extension", ['.csv', '.parquet'])
def test_check_if_file_extension_returns_correct_result(data_loader, extension):
    file_path = f'test{extension}'

    assert data_loader._check_if_file_extension_supported(file_path) == extension

def test_check_if_file_extension_throws_value_error_when_unsupported(data_loader):

    with pytest.raises(ValueError, match= re.escape("File extension not supported: .txt Please use one of the following: ['.csv', '.parquet']")):
        data_loader._check_if_file_extension_supported("test.txt")
   