from fastapi import FastAPI
from rest.test import test


# 라우터 설정
def includeRouter(app: FastAPI) -> None:
    app.include_router(test.router, prefix="/test")


# 앱 실행
def run() -> FastAPI:
    app = FastAPI()
    includeRouter(app)
    return app
