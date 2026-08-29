# Concepts

This module explains storage state, login, uploads, downloads, dialogs, and new pages..

## Authentication state

The login form changes server-side session state and gives the browser a cookie. A new context has no cookie, so it behaves like a signed-out user. `storage_state(path=...)` serializes cookies and local storage; creating a new context with that state restores the signed-in condition without repeating the UI login. This is a speed optimization, not a reason to commit credentials.

## File events

For an upload, locate the file input and call `set_input_files(path)`. For a download, start waiting before clicking:

```python
with page.expect_download() as event:
    page.get_by_role("link", name="Download orders").click()
download = event.value
download.save_as("artifacts/orders.csv")
```

The `with` block pairs an action with the event it causes. Afterward, verify file contents—not only the presence of a file name.
