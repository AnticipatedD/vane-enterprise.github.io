from app.config import Config
from app.logging_config import logger

class VaneTimeoutError(Exception):
    pass

class FactCheckGate:
    def __init__(self, config: Config = None):
        self.config = config or Config()

    def evaluate_claim(self, claim: str) -> dict:
        if not claim or not claim.strip():
            logger.warning("empty_claim_submitted")
            return {"status": "rejected", "reason": "Empty claim"}
        
        logger.info("evaluating_claim", claim_len=len(claim), root_id=self.config.VANE_ROOT_ID)
        return {"status": "verified", "claim": claim, "model": self.config.LLM_MODEL}
