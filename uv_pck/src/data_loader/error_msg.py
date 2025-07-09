from enum import Enum

SUPPORTED_FILE_EXTENSIONS = [".csv", ".parquet"]




class DataReadingErrorMessages(Enum):
    INVALID_FILE_TYPE = "Invalid file type. Supported formats are: .csv, .xlsx, .json"
    FILE_NOT_FOUND = "File not found. Please check the file path."
    INVALID_DATA_FORMAT = "Invalid data format. Please ensure the data is in the correct format."
    MISSING_REQUIRED_FIELD = "Missing required field: {}"
    DATA_LOAD_ERROR = "Error loading data from file: {}"
    EXT_NOT_SUPPORTED = 'File extension not supported: {ext} Please use one of the following: {supported_extensions}'
    UNEXPECTED_ERROR = "An unexpected error occurred: {}"
    INVALID_COLUMN_NAME = "Invalid column name: {}. Available columns are: {}"  