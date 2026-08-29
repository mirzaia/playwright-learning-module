# Playwright Python Learning Module

Self-guided Playwright training for junior through mid-level engineers. The course assumes basic Python syntax, but does not assume prior knowledge of web browsers, HTML, pytest, or test automation. The course follows the reference project's four layers—objectives, concepts, exercises, and verification—while using isolated contexts and deterministic local verification.

## How to study

Do not begin with the solution files. For each module, follow this loop:

1. Read the objective and glossary. The glossary defines terms such as browser, page, locator, fixture, assertion, and context before they appear in code.
2. Run each concept example and predict what it will do before reading the output.
3. Complete the starter exercise one TODO at a time. A failing test is useful feedback, not evidence that Playwright is broken.
4. Read the failure output from top to bottom. Find the first line in your own file, identify what Playwright was waiting for, and compare the expected and actual values.
5. Compare with the solution only after making an attempt, then explain each line in your own words.

The learning path intentionally introduces one new idea at a time. Browser automation is not just a list of commands: a test has a subject (the web page), actions (what a user does), and observations (what the test verifies).

Read the [beginner theory guide](./shared/learning-guide.md) before Module 01. It explains the browser boundary, action-versus-observation, flaky tests, and the categories of failure output used throughout the course.

## Quick start

```bash
cd modules/00-setup
uv sync
uv run playwright install chromium
uv run pytest -q
```

Each module has its own environment and lockfile. Run `uv sync` from the module directory before starting it. Modules 06–07 and the advanced browser-matrix exercises also install Firefox and WebKit; Module 08 installs the async pytest plugin. The public TodoMVC exercise is optional and never gates completion.

## Learning path

00 setup → 01 browser fundamentals → 02 locators/assertions → 03 pytest/debugging → 04 BDD → 05 authenticated workflows → 06 API/network/browser matrix → 07 capstone → 08 async appendix → 09 reusable architecture → 10 advanced network control → 11 complex browser workflows → 12 reliability and scale.

The shared `shared/commerce-portal` package supplies a tiny local orders application for deterministic login, filtering, upload, download, API, and failure-state tests. It is teaching infrastructure, not a framework to copy into production.

## Scope

The course covers E2E testing, browser task automation, controlled API/network testing, mobile emulation, cross-browser execution, reusable test architecture, multi-role authentication, frames/popups, WebSockets, and reliability at scale. It does not cover Allure, full-scale scraping, bypassing access controls, or building a proprietary automation framework.

## Minimum vocabulary

- **Browser**: the program that renders a website, such as Chromium, Firefox, or WebKit.
- **Context**: an isolated browser profile, similar to a fresh private window with separate cookies and local storage.
- **Page**: one tab inside a context.
- **Locator**: a reusable description of an element, such as a button named “Save”.
- **Action**: an interaction such as `click()`, `fill()`, or `check()`.
- **Assertion**: a statement about an expected result, such as `expect(page).to_have_title(...)`.
- **Fixture**: pytest-managed setup that supplies an object such as `page` or `demo_url` to a test.
