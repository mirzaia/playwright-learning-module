from pathlib import Path

ROOT = Path(__file__).parents[1]
MODULES = ["00-setup", "01-browser-fundamentals", "02-locators-assertions", "03-pytest-debugging", "04-bdd-playwright", "05-browser-workflows", "06-network-browser-matrix", "07-capstone", "08-async-appendix", "09-reusable-architecture", "10-advanced-network", "11-complex-workflows", "12-reliability-scale"]


def test_all_modules_have_learning_layers_and_environment_files():
    required = ["01-objectives", "02-concepts", "03-exercises", "04-verification", "README.md", "pyproject.toml", ".python-version", ".gitignore"]
    for name in MODULES:
        module = ROOT / "modules" / name
        assert module.exists(), name
        for item in required:
            assert (module / item).exists(), f"{name} missing {item}"


def test_shared_portal_exists():
    assert (ROOT / "shared/commerce-portal/src/commerce_portal/app.py").exists()
    assert (ROOT / "shared/commerce-portal/src/commerce_portal/fixtures.py").exists()
