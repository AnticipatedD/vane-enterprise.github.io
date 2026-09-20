from app.orchestrator import FactCheckGate, Config

def test_fact_check_gate_success():
    gate = FactCheckGate()
    res = gate.evaluate_claim("Data science is essential.")
    assert res["status"] == "verified"

def test_fact_check_gate_empty():
    gate = FactCheckGate()
    res = gate.evaluate_claim("")
    assert res["status"] == "rejected"
