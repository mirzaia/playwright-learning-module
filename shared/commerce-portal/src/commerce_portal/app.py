from __future__ import annotations

import csv
import io
import secrets
from flask import Flask, jsonify, redirect, render_template_string, request, session, url_for

"""Small deterministic teaching application.

The application intentionally keeps its data in memory. Learners are testing
browser behavior, not learning database setup. Each pytest session starts a
fresh server, and each Playwright context owns its cookies so tests can run
without relying on order or a pre-existing account.
"""

ORDERS = [
    {"id": "ORD-1001", "customer": "Ada", "status": "paid"},
    {"id": "ORD-1002", "customer": "Grace", "status": "pending"},
    {"id": "ORD-1003", "customer": "Linus", "status": "shipped"},
]

LOGIN_HTML = """
<!doctype html><title>Sign in</title><h1>Sign in</h1>
<form method=post aria-label="Sign in form">
  <label>Email <input name=email type=email></label>
  <label>Password <input name=password type=password></label>
  <button type=submit>Sign in</button>
</form>{% if error %}<p role=alert>{{ error }}</p>{% endif %}
"""

ORDERS_HTML = """
<!doctype html><title>Orders</title><h1>Orders</h1>
<p>Signed in as {{ email }}</p><a href="{{ url_for('account') }}">Account</a>
<a href="{{ url_for('download') }}">Download orders</a>
<form action="{{ url_for('upload') }}" method="post" enctype="multipart/form-data">
  <label>Document <input type="file" name="document"></label><button type="submit">Upload document</button>
</form>
<label>Status <select aria-label="Status" id="status-filter">
  <option value="">All</option>{% for status in statuses %}<option value="{{ status }}">{{ status }}</option>{% endfor %}<option value="missing">missing</option>
</select></label>
<table aria-label="Orders"><thead><tr><th>Order</th><th>Customer</th><th>Status</th></tr></thead><tbody id="orders-body"></tbody></table>
<script>
const rows = {{ orders|tojson }};
const body = document.querySelector('#orders-body');
function render() { const status = document.querySelector('#status-filter').value;
 body.innerHTML = rows.filter(r => !status || r.status === status).map(r => `<tr data-testid="order-row"><td>${r.id}</td><td>${r.customer}</td><td>${r.status}</td></tr>`).join('') || '<tr><td colspan="3">No orders found</td></tr>'; }
document.querySelector('#status-filter').addEventListener('change', render); render();
</script>
"""


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "learning-module-only-secret"

    @app.get("/")
    def home():
        return redirect(url_for("orders")) if session.get("email") else redirect(url_for("login"))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        error = None
        if request.method == "POST":
            if request.form.get("email") == "learner@example.test" and request.form.get("password") == "playwright-demo":
                session["email"] = request.form["email"]
                return redirect(url_for("account"))
            error = "Invalid email or password"
        return render_template_string(LOGIN_HTML, error=error)

    @app.get("/account")
    def account():
        if not session.get("email"):
            return redirect(url_for("login"))
        return redirect(url_for("orders"))

    @app.get("/orders")
    def orders():
        if not session.get("email"):
            return redirect(url_for("login"))
        return render_template_string(ORDERS_HTML, email=session["email"], orders=ORDERS, statuses=["paid", "pending", "shipped"])

    @app.get("/api/orders")
    def api_orders():
        return jsonify(ORDERS)

    @app.post("/upload")
    def upload():
        uploaded = request.files.get("document")
        if not uploaded or not uploaded.filename:
            return jsonify({"error": "document is required"}), 400
        return jsonify({"filename": uploaded.filename, "message": "Upload complete"})

    @app.get("/download/orders.csv")
    def download():
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=["id", "customer", "status"])
        writer.writeheader(); writer.writerows(ORDERS)
        from flask import Response
        return Response(output.getvalue(), mimetype="text/csv", headers={"Content-Disposition": "attachment; filename=orders.csv"})

    return app
