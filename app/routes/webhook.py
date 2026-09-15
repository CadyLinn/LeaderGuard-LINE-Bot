from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from app.services.line_service import LineService

router = APIRouter()

@router.post("/callback")
async def line_callback(request: Request):
    try:
        body = await request.body()
        signature = request.headers.get("X-Line-Signature")
        events = LineService.parse_events(body, signature)
        for event in events:
            await LineService.handle_event(event)
        return JSONResponse(content={"status": "ok"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
