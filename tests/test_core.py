import pytest
from gendiff import (
    generate_diff,
    open_file,
    stylish_format
)


@pytest.fixture()
def plane_json_files():
    return (
        open_file('tests/fixtures/plane_files/file1.json'),
        open_file('tests/fixtures/plane_files/file2.json')
    )


@pytest.fixture()
def plane_yml_files():
    return (
        open_file('tests/fixtures/plane_files/file1.yml'),
        open_file('tests/fixtures/plane_files/file2.yaml')
    )


@pytest.fixture()
def nested_json_files():
    return (
        open_file('tests/fixtures/nested_files/nested1.json'),
        open_file('tests/fixtures/nested_files/nested2.json')
    )


@pytest.fixture()
def nested_yml_files():
    return (
        open_file('tests/fixtures/nested_files/nested1.yml'),
        open_file('tests/fixtures/nested_files/nested2.yml')
    )


def get_expected_string(path):
    with open(path, 'r') as expected_string:
        return expected_string.read()


def test_generate_diff(plane_json_files, plane_yml_files):
    json_file1, json_file2 = plane_json_files
    yml_file1, yml_file2 = plane_yml_files

    yml_diff = generate_diff(yml_file1, yml_file2)
    json_diff = generate_diff(json_file1, json_file2)

    yml_diff_reversed = generate_diff(yml_file2, yml_file1)
    json_diff_reversed = generate_diff(json_file2, json_file1)

    assert stylish_format(json_diff) == get_expected_string(
        "tests/fixtures/expected/plane_expected.txt"
    )
    assert stylish_format(json_diff_reversed) == get_expected_string(
        "tests/fixtures/expected/plane_expected_reversed.txt"
    )
    assert stylish_format(yml_diff) == get_expected_string(
        "tests/fixtures/expected/plane_expected.txt"
    )
    assert stylish_format(yml_diff_reversed) == get_expected_string(
        "tests/fixtures/expected/plane_expected_reversed.txt"
    )
    # assert generate_diff(yml_file2, json_file1) == get_expected_string(
    #     "tests/fixtures/expected/nested_expected.txt"
    # )


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
