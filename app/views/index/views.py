from flask import Blueprint, render_template, request
from redis import Redis

index_views = Blueprint("index_views", __name__, url_prefix="/")
redis_client = Redis(host="redis", port=6379)

@index_views.route("/")
def index():
    visit_amount = redis_client.incrby(f"ip:{request.remote_addr}", 1)

    return render_template("index.html", visit_amount=visit_amount)
