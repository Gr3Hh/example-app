from fastapi import FastAPI

from routers.users import router as user_router


app = FastAPI(
    title="Hello World"
)

app.include_router(
    router=user_router,
    prefix="/hello"
)
