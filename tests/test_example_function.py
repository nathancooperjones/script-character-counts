import pytest


@pytest.mark.usefixtures('example_fixture')
def test_example(example_fixture):
    actual = example_fixture
    expected = 'example_fixture_string'

    assert actual == expected
