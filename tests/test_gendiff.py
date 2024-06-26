import pytest
from gendiff import generate_diff
from gendiff import open_file


@pytest.fixture()
def json_files():
    return (
        open_file('tests/fixtures/plane_files/file1.json'),
        open_file('tests/fixtures/plane_files/file2.json')
    )


@pytest.fixture()
def yml_files():
    return (
        open_file('tests/fixtures/plane_files/file1.yml'),
        open_file('tests/fixtures/plane_files/file2.yaml')
    )


def get_expected_string(path):
    with open(path, 'r') as expected_string:
        return expected_string.read()


def test_generate_diff(json_files, yml_files):
    json_file1, json_file2 = json_files
    yml_file1, yml_file2 = yml_files

    assert generate_diff(json_file1, json_file2) == get_expected_string(
        "tests/fixtures/expected/default_expected.txt"
    )
    assert generate_diff(json_file2, json_file1) == get_expected_string(
        "tests/fixtures/expected/default_expected_reversed.txt"
    )
    assert generate_diff(yml_file1, yml_file2) == get_expected_string(
        "tests/fixtures/expected/default_expected.txt"
    )
    assert generate_diff(yml_file2, yml_file1) == get_expected_string(
        "tests/fixtures/expected/default_expected_reversed.txt"
    )


def test_open_file():
    assert open_file("tests/fixtures/plane_files/file1.json") == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    assert (open_file("tests/fixtures/plane_files/file2.yaml") == {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    })
