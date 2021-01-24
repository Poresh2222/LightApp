from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import msg as msg_router
from app.routers import users as user_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(msg_router.msg_router)
app.include_router(user_router.user_router)


if __name__ == 'main':
    uvicorn.run(app, host='localhost', port=8000)