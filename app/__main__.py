import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import links

app = FastAPI()
app.include_router(links.router)
app.mount("/", StaticFiles(directory="static", html=True))


if __name__ == "__main__":
    uvicorn.run(app)
