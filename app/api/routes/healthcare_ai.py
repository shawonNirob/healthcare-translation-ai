from fastapi import APIRouter, HTTPException
from app.schemas.text_schema import AskRequest
from app.llm.llm_integration import get_llm_response

router = APIRouter()

@router.post("/translate", response_model=dict, status_code=200)
def translate(request: AskRequest):
    try:
        return get_llm_response(request.query, request.preferred_language)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
