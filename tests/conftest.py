import pytest
from sevendparser.src.main import SevendParser

@pytest.fixture
def parser():
    return SevendParser(file_path="/home/hxl/projects/sevendparser/config")
