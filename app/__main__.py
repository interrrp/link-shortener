import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import links

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True))
app.include_router(links.router)


if __name__ == "__main__":
    uvicorn.run(app)
