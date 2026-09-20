import os
import pytest

@pytest.fixture(autouse=True)
def mock_env():
    os.environ["LLM_MODEL"] = "mock-llm-v1"
    os.environ["VANE_ROOT_ID"] = "mock-root-123"
