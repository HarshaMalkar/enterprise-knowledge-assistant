import logging
from datetime import datetime
from typing import Any, Dict, List

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from workflow.graph import run

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Smart AI Workspace API",
    version="2.0.0"
)


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    question: str
    answer: str
    citations: List[Dict[str, Any]]
    timestamp: str


@app.get("/")
def home():
    return {
        "status": "online",
        "application": "Smart AI Workspace",
        "version": "2.0.0"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/query", response_model=QueryResponse)
def query(req: QueryRequest):

    question = req.question.strip()

    if not question:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Question cannot be empty."
        )

    try:
        result = run(question)

        return QueryResponse(
            question=result.get("question", question),
            answer=result.get("answer", ""),
            citations=result.get("citations", []),
            timestamp=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    except Exception as e:
        logger.exception("Unexpected error")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "api:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )