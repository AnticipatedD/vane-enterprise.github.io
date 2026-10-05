# Contributing to my-railways-agent

Thank you for your interest in contributing to **Vane Enterprise LLC** infrastructure. To maintain the integrity of our zero-hallucination processing pipelines, we require all contributions to strictly follow this workflow.

## Code Quality Standards
* **Type Hinting:** All new modules in `app/` must use strict Pydantic configurations or explicit type hints.
* **Deterministic Logic:** Code alterations must not bypass the `0.0` temperature lock protocol established in `llm_provider.py`.
* **Testing Cover:** All pull requests must match or exceed an **80% code coverage threshold** via `pytest`.

## Workflow Process
1. **Fork the Repository:** Create your own copy of `AnticipatedD/vane-enterprise.github.io`.
2. **Branch Naming Scheme:** Use `feature/my-railways-agent` or `bugfix/issue-id`.
3. **Commit Messages:** Prefix commits clearly (e.g., `Fix: update config schema anchor validation`).
4. **Pull Requests:** Describe how your modification guarantees compliance with the *Law of the Diamond* security boundaries.

For questions, reach out to the project maintainer at **harigov63@gmail.com**.
