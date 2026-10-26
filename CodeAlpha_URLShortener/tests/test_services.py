import pytest

from app.services import InvalidURLError, create_short_link, generate_short_code, is_valid_url


def test_valid_urls():
    assert is_valid_url("https://example.com")
    assert is_valid_url("http://example.com/path?q=1")


@pytest.mark.parametrize("bad", ["", "javascript:alert(1)", "example.com", "ftp://x.com"])
def test_invalid_urls(bad):
    assert not is_valid_url(bad)


def test_code_length(app_context):
    code = generate_short_code(7)
    assert len(code) == 7


def test_create_short_link_persists(app_context):
    link = create_short_link("https://example.com", code_length=7)
    assert link.id is not None
    assert len(link.short_code) == 7


def test_create_short_link_rejects_invalid(app_context):
    with pytest.raises(InvalidURLError):
        create_short_link("javascript:alert(1)", code_length=7)