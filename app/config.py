import os
from pydantic_settings 
import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator

class Config(BaseModel):
    LLM_MODEL: str = Field(default_factory=lambda: os.getenv("LLM_MODEL", "gpt-4-turbo"))
    VANE_ROOT_ID: str = Field(default_factory=lambda: os.getenv("VANE_ROOT_ID", "vane_default_root"))
    API_TIMEOUT: int = Field(default=30) 

class SovereignConfig(BaseSettings):
    # Anchor System Secrets to your VANE Root ID
    vane_root_id: str = Field(default="VANE_ROOT_STABLE_001", alias="VANE_ROOT_ID")
    repository_deploy_key: str = Field(..., alias="REPOSITORY_DEPLOY_KEY")
    
    # Environment configs
    environment: str = Field(default="production", alias="ENVIRONMENT")
    host: str = Field(default="0.0.0.0", alias="HOST")
    port: int = Field(default=8000, alias="PORT")

    # Read from local .env file if available
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8", 
        extra="ignore"
    )

    @field_validator("vane_root_id")
    @classmethod
    def validate_root_identity(cls, v: str) -> str:
        if v != "VANE_ROOT_STABLE_001":
            raise ValueError(f"Sovereignty violation: ID '{v}' does not match official anchor 'VANE_ROOT_STABLE_001'.")
        return v

# Instantiate configuration object
try:
    config = SovereignConfig()
except Exception as e:
    print(f"[FATAL GATE 1 CRASH] Configuration Validation Failed: {e}")
    raise SystemExit(1)
