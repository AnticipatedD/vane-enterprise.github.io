import pytest
from app.orchestrator import FactCheckGate, VaneValidationError

def test_evaluate_claim_edge_cases():
    gate = FactCheckGate()
    
    # Whitespace-only claim triggers validation error
    with pytest.raises(VaneValidationError):
        gate.evaluate_claim("   ")
        
    # Very long claim handling
    long_claim = "A" * 10000
    result = gate.evaluate_claim(long_claim)
    assert result is not None
