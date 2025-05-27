from fastapi import FastAPI, Request
from pydantic import BaseModel
from claim_processing_agent import create_workflow
from uuid import uuid4, UUID
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()
graph = create_workflow()

class ClaimRequest(BaseModel):
    patient_id: str
    treatment_code: str
    claim_details: str

class ClaimResponse(BaseModel):
    final_decision: str
    ai_feedback: str
    thread_id: UUID

@app.post("/process-claim", response_model=ClaimResponse)
async def process_claim(request_data: ClaimRequest, request: Request):
    # Optionally extract from headers or request context
    custom_thread_id = request.headers.get("X-Thread-ID")

    # Fallback to a new UUID if not provided
    thread_id = custom_thread_id or str(uuid4())

    input_state = {
        "patient_id": request_data.patient_id,
        "treatment_code": request_data.treatment_code,
        "claim_details": request_data.claim_details
    }

    result = graph.invoke(
        input_state,
        config={"configurable": {"thread_id": thread_id}}
    )

    return {
        "final_decision": result.get("final_decision"),
        "ai_feedback": result.get("ai_validation_feedback"),
        "thread_id": thread_id  # Optionally return for debugging
    }

