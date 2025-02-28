from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import clubes_router
import classifica_router
import rodada_router

app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (NÃO RECOMENDADO EM PRODUÇÃO)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos os headers
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(classifica_router.router)
app.include_router(clubes_router.router)
app.include_router(rodada_router.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8585)
