import secrets
import string
from urllib.parse import urlparse

from sqlalchemy.exc import IntegrityError

from app.models import ShortURL, db

ALPHABET = string.ascii_letters + string.digits  # base62
MAX_COLLISION_RETRIES = 5


class InvalidURLError(ValueError):
    """Raised when the supplied URL is not a valid http(s) URL."""


def generate_short_code(length: int) -> str:
    """Return a cryptographically random base62 code of the given length."""
    return "".join(secrets.choice(ALPHABET) for _ in range(length))


def is_valid_url(url: str) -> bool:
    """True only for absolute http/https URLs with a host."""
    if not url:
        return False
    try:
        parsed = urlparse(url)
    except ValueError:
        return False
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def create_short_link(original_url: str, code_length: int) -> ShortURL:
    """Validate the URL, generate a unique code, and persist the mapping."""
    original_url = (original_url or "").strip()
    if not is_valid_url(original_url):
        raise InvalidURLError("invalid URL (must be http/https)")

    for _ in range(MAX_COLLISION_RETRIES):
        code = generate_short_code(code_length)
        link = ShortURL(short_code=code, original_url=original_url)
        db.session.add(link)
        try:
            db.session.commit()
            return link
        except IntegrityError:
            # Another request claimed this code between our check and commit.
            db.session.rollback()
            continue

    raise RuntimeError("could not generate a unique short code")


def resolve_short_code(code: str, count_click: bool = True):
    """Return the ShortURL for `code`, or None. Optionally increments clicks."""
    link = ShortURL.query.filter_by(short_code=code).first()
    if link and count_click:
        link.clicks += 1
        db.session.commit()
    return link