"""Tests for article.py

Run with:

    ls article.py test_article.py |
    entr -cs 'coverage run --branch -m pytest && coverage html'

"""
from importlib import import_module
from json import loads
from tempfile import NamedTemporaryFile
from unittest.mock import patch


def test_article(capsys):
    content = "test file content\n"
    with NamedTemporaryFile() as file_:
        file_.write(content.encode())
        file_.seek(0)
        with patch("sys.argv", [file_.name]):
            import_module("article")
    captured = capsys.readouterr()
    json = loads(captured.out)
    assert "article" in json, "JSON object has an article key"
    assert (
        "body_markdown" in json["article"]
    ), "JSON article has body_markdown key"
    assert (
        json["article"]["body_markdown"] == content
    ), "body_markdown matches content written earlier"
