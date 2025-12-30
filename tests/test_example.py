from pathlib import Path
from hexlet_pytest.example import reverse


def test_reverse():
    assert reverse('asdfghjkl') == 'lkjhgfdsa'


def test_reverse_fixture(string, reverse_string):
    assert reverse(string) == reverse_string


def test_reverse_empty():
    assert reverse('') == ''


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_revers_test_data():
    assert reverse(read_file('after')) == read_file('before')
