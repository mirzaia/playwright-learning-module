from __future__ import annotations

import threading
from contextlib import contextmanager
from werkzeug.serving import make_server
import pytest

from .app import create_app

# This fixture is intentionally session-scoped for the server process, while
# the Playwright `page` fixture remains function-scoped for browser isolation.


@contextmanager
def running_server():
    server = make_server("127.0.0.1", 0, create_app())
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown(); thread.join(timeout=2)


@pytest.fixture(scope="session")
def demo_url():
    with running_server() as url:
        yield url
