from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import classifica_router

app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(classifica_router.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="192.168.100.51", port=8000)
