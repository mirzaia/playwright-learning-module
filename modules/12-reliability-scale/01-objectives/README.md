# Objectives

- separate smoke tests from broader regression checks;
- configure trace, screenshot, video, and output directories for failures;
- make tests safe for workers and repeated runs;
- use retries only as a diagnostic signal and report the original failure;
- run selected tests with `-k`, markers, browser projects, and `--numprocesses`;
- design a failure triage loop that produces actionable evidence.
