from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}
import uvicorn
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# Import structural logic gates
from app.config import config
from app.llm_provider import llm_provider
from app.rag_pipeline import rag_pipeline

# Initialize FastAPI with native Vane Enterprise LLC Branding
app = FastAPI(
    title="Vane Enterprise Orchestrator Service",
    description="Deterministic Truth-AI Architecture with Immutable Output Guardrails.",
    version="1.0.0",
    docs_url="/api/docs"
)

class QueryRequest(BaseModel):
    prompt: str

@app.get("/api/health", status_code=status.HTTP_200_OK)
def health_check():
    """
    Returns system health and marketplace validation metrics. Zero external telemetry is authorized.
    """
    return {
        "status": "ONLINE",
        "identity_anchor": config.vane_root_id,
        "environment": config.environment,
        "security_boundary": "LOCALIZED_INFRASTRUCTURE_ONLY",
        "compliance": "100% TELEMETRY FREE SLA"
    }

@app.post("/api/orchestrate", status_code=status.HTTP_200_OK)
def process_sovereign_inference(request: QueryRequest):
    """
    Sequentially processes workflows across all deterministic verification gates.
    """
    try:
        # Gate 1 check happens automatically at boot (app.config import validation)
        
        # Gate 3: Pull data from the vector pipeline with a transparent audit trail
        rag_data = rag_pipeline.retrieve_with_audit_trail(user_query=request.prompt)
        
        # Gate 2: Pass validated context into the locked inference provider
        inference_result = llm_provider.execute_inference(
            prompt=request.prompt, 
            context=rag_data["context_payload"]
        )
        
        # Gate 4: Package and return verified payload over the secure API boundary
        return {
            "branding": "Vane Enterprise LLC Official Output",
            "audit_trail": rag_data["audit_trail"],
            "inference": inference_result
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Deterministic Architecture Guardrail Violation: {str(e)}"
        )

if __name__ == "__main__":
    # Launch execution engine using variables defined from Gate 1 configuration schema
    uvicorn.run(
        "app.app:app",
        host=config.host,
        port=config.port,
        reload=(config.environment == "development")
    )
