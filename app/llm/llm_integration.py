import requests
from fastapi import HTTPException
import json
from app.config import settings
from loguru import logger

def get_llm_response(query: str, preferred_language: str) -> dict:
    # Log the received language for debugging
    logger.info(f"Received preferred language: {preferred_language}")
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.OPENAI_API_KEY}"
    }
    
    payload = {
        "model": settings.MODEL_ID,
        "messages": [
            {
                "role": "system",
                "content": "You're a Medical AI Assistant that translates the user's query into provided language while enhancing it with more precise medical terminology, including clinical terms, symptoms, diagnoses, treatments, and medical conditions where applicable."
            },
            {"role": "user", "content": f"Translate this into {preferred_language} with enhanced clinical terms and more precise medical terminology: {query}"}
        ],
        "temperature": 0.7
    }
    
    try:
        logger.info(f"Sending request to OpenAI API:\n{json.dumps(payload, indent=2)}")
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload
        )
        
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail=f"OpenAI API error: {response.text}")
        
        result = response.json()
        content = result['choices'][0]['message']['content']
        logger.info(f"LLM response: {content}")
        
        return {
            'translated_text': content
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM API request failed: {str(e)}")