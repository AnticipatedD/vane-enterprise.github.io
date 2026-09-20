import os
from pydantic import BaseModel, Field

class Config(BaseModel):
    LLM_MODEL: str = Field(default_factory=lambda: os.getenv("LLM_MODEL", "gpt-4-turbo"))
    VANE_ROOT_ID: str = Field(default_factory=lambda: os.getenv("VANE_ROOT_ID", "vane_default_root"))
    API_TIMEOUT: int = Field(default=30)
