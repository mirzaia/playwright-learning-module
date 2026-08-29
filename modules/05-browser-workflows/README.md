# Module 05: Authenticated Browser Workflows

Practice login, storage state, uploads, downloads, and browser events against the local commerce portal.

Authentication has two separate ideas: proving identity through the login form, and reusing the resulting cookies/local storage. `storage_state` stores browser state for later contexts; it is convenient but sensitive. Treat it like a password file: generate it locally, ignore it, and never commit it.

Uploads and downloads are browser events. The test must wait for the event while performing the action, then verify the actual filename or file contents. Seeing a button is not proof that a file was transferred.

Read Objectives, Concepts, Exercises, then Verification in order.
