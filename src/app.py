from fastapi import FastAPI

from .routers.chat_route import router as chat_router

app = FastAPI()

app.include_router(chat_router, prefix="/chat")

@app.get("/")
def hello_message():
    return {"Hello": "FastAPI"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)