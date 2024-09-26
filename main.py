from fastapi import FastAPI
from routers.livros import router as livros_router
from config.database import conect,end
app = FastAPI()

app.add_event_handler("startup", func=conect)
app.add_event_handler(event_type='shutdown',func=end)


app.include_router(livros_router)