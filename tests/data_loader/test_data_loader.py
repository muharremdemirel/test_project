import pytest
from uv_pck.src.data_loader import DataLoader

@pytest.fixture
def data_loader():
    return DataLoader()

     
def test_check_if_file_extension_supported(data_loader):
    # Test with a supported file extension
    assert data_loader._check_if_file_extension_supported("data.csv") == ".csv"

    with pytest.raises(ValueError):
        data_loader._check_if_file_extension_supported("test.txt")
   