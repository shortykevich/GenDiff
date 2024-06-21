import pytest
from tests import (
    generate_diff,
    open_file
)


@pytest.fixture()
def json_files():
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }, {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }


def test_generate_diff(json_files):
    file1, file2 = json_files
    assert generate_diff(file1, file2) == (
        "{\n"
        "- follow: false\n"
        "  host: hexlet.io\n"
        "- proxy: 123.234.53.22\n"
        "- timeout: 50\n"
        "+ timeout: 20\n"
        "+ verbose: true"
        "\n}"
    )
    assert generate_diff(file2, file1) == (
        "{\n"
        "+ follow: false\n"
        "  host: hexlet.io\n"
        "+ proxy: 123.234.53.22\n"
        "- timeout: 20\n"
        "+ timeout: 50\n"
        "- verbose: true"
        "\n}"
    )
    assert generate_diff(file1, {}) == (
        "{\n"
        "- follow: false\n"
        "- host: hexlet.io\n"
        "- proxy: 123.234.53.22\n"
        "- timeout: 50"
        "\n}"
    )
    assert generate_diff({}, {}) == "{\n\n}"
    assert generate_diff({}, file2) == (
        "{\n"
        "+ host: hexlet.io\n"
        "+ timeout: 20\n"
        "+ verbose: true"
        "\n}"
    )


__all__ = [
    'open_file',
]
