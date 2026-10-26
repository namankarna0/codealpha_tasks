from flask import Blueprint, abort, current_app, jsonify, redirect, render_template, request

from app.services import InvalidURLError, create_short_link, resolve_short_code

bp = Blueprint("urls", __name__)


@bp.get("/")
def index():
    return render_template("index.html")


@bp.post("/api/shorten")
def shorten():
    data = request.get_json(silent=True) or {}
    try:
        link = create_short_link(
            original_url=data.get("url", ""),
            code_length=current_app.config["SHORT_CODE_LENGTH"],
        )
    except InvalidURLError as exc:
        return jsonify(error=str(exc)), 400

    short_url = f"{current_app.config['BASE_URL']}/{link.short_code}"
    return jsonify(short_url=short_url, code=link.short_code, original_url=link.original_url), 201


@bp.get("/<code>")
def follow(code: str):
    link = resolve_short_code(code)
    if link is None:
        abort(404)
    return redirect(link.original_url, code=302)