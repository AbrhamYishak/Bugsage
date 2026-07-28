import pytest
from Bugsage.utils.similaritycheck import similaritycheck
def test_similaritycheck():
    assert similaritycheck("builtins","built-ins")