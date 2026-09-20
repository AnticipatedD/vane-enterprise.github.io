from app.config import Config

def test_config_defaults():
    cfg = Config()
    assert cfg.LLM_MODEL is not None
    assert cfg.VANE_ROOT_ID is not None
