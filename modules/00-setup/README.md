# Module 00: Environment Setup

Verify Python 3.12, uv, dependency synchronization, Chromium installation, and a first Playwright page fixture. Complete this module before the browser lessons.

This module explains why Python dependencies and browser binaries are separate. `uv sync` installs Python packages into this module's virtual environment; `uv run playwright install chromium` downloads the browser executable that Playwright controls. If either step is missing, an import error and a missing-executable error look similar but have different fixes.

You will also learn how to read a command: `uv run pytest -q` means “run pytest using this module's environment, with quiet output.”

Read Objectives, Concepts, Exercises, then Verification in order.
