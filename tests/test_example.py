from hexlet_pytest.example import reverse


def test_reverse():
    assert reverse('asdfghjkl') == 'lkjhgfdsa'


def test_reverse_fixture(string, reverse_string):
    assert reverse(string) == reverse_string


def test_reverse_empty():
    assert reverse('') == ''
