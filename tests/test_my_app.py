from pytest import *
from my_app.read_file import *
from my_app.data_analysis import *

class TestMyApp:

    def test_no_file_found(self):
        with raises(FileNotFoundError, match= "no file found"):
            import_data("no_file.xlsx")