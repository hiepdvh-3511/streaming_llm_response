import asyncio

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from vertexai.generative_models import GenerativeModel

model = GenerativeModel("gemini-1.5-flash-002")

app = FastAPI()


async def generate_response():
    response = model.generate_content("Tell me a romance story.", stream=True)
    for chunk in response:
        yield f"{chunk.text}"  # Định dạng SSE chuẩn
        await asyncio.sleep(0)  # Giúp tránh block event loop


@app.get("/stream")
async def stream():
    return StreamingResponse(generate_response(), media_type="text/event-stream")
