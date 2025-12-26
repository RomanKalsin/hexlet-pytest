import pytest


@pytest.fixture
def string():
    return 'Roman'

@pytest.fixture
def reverse_string():
    return "namoR"