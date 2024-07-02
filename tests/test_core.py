import pytest
from gendiff import (
    generate_diff,
    open_file
)


@pytest.fixture()
def plane_json():
    return (
        'tests/fixtures/plain_files/file1.json',
        'tests/fixtures/plain_files/file2.json'
    )


@pytest.fixture()
def plane_yml():
    return (
        'tests/fixtures/plain_files/file1.yml',
        'tests/fixtures/plain_files/file2.yaml'
    )


@pytest.fixture()
def nested_json():
    return (
        'tests/fixtures/nested_files/file1.json',
        'tests/fixtures/nested_files/file2.json'
    )


@pytest.fixture()
def nested_yml():
    return (
        'tests/fixtures/nested_files/file1.yml',
        'tests/fixtures/nested_files/file2.yml'
    )


def get_expected_string(path):
    with open(path, 'r') as expected_string:
        return expected_string.read()


def test_generate_diff(plane_json, plane_yml,
                       nested_json, nested_yml):

    plane_json1, plane_json2 = plane_json
    plane_yml1, plane_yml2 = plane_yml

    nested_json1, nested_json2 = nested_json
    nested_yml1, nested_yml2 = nested_yml

    assert generate_diff(plane_json1, plane_json2, 'stylish') == get_expected_string(
        "tests/fixtures/expected/stylish_regular_expected.txt"
    )
    assert generate_diff(plane_yml1, plane_yml2, 'stylish') == get_expected_string(
        "tests/fixtures/expected/stylish_regular_expected.txt"
    )
    assert generate_diff(nested_json1, nested_json2, 'stylish') == get_expected_string(
        "tests/fixtures/expected/stylish_nested_expected.txt"
    )
    assert generate_diff(nested_yml1, nested_yml2, 'stylish') == get_expected_string(
        "tests/fixtures/expected/stylish_nested_expected.txt"
    )

    assert generate_diff(plane_json1, plane_json2, 'plain') == get_expected_string(
        "tests/fixtures/expected/plain_regular_expected.txt"
    )
    assert generate_diff(plane_yml1, plane_yml2, 'plain') == get_expected_string(
        "tests/fixtures/expected/plain_regular_expected.txt"
    )
    assert generate_diff(nested_json1, nested_json2, 'plain') == get_expected_string(
        "tests/fixtures/expected/plain_nested_expected.txt"
    )
    assert generate_diff(nested_yml1, nested_yml2, 'plain') == get_expected_string(
        "tests/fixtures/expected/plain_nested_expected.txt"
    )

    assert generate_diff(plane_json1, plane_json2, 'json') == get_expected_string(
        "tests/fixtures/expected/json_plain_expected.txt"
    )
    assert generate_diff(nested_json1, nested_json2, 'json') == get_expected_string(
        "tests/fixtures/expected/json_nested_expected.txt"
    )


def test_open_file():
    assert open_file("tests/fixtures/plain_files/file1.json") == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    assert open_file("tests/fixtures/plain_files/file2.yaml") == {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }
