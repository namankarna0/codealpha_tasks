def test_shorten_ok(client):
    resp = client.post("/api/shorten", json={"url": "https://example.com"})
    assert resp.status_code == 201
    body = resp.get_json()
    assert body["code"]
    assert body["short_url"].endswith(body["code"])


def test_shorten_invalid(client):
    resp = client.post("/api/shorten", json={"url": "not-a-url"})
    assert resp.status_code == 400


def test_redirect_ok(client):
    code = client.post("/api/shorten", json={"url": "https://example.com"}).get_json()["code"]
    resp = client.get(f"/{code}")
    assert resp.status_code == 302
    assert resp.headers["Location"] == "https://example.com"


def test_redirect_missing_returns_404(client):
    assert client.get("/nope123").status_code == 404