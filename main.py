from fastapi import FastAPI
from fastapi.responses import JSONResponse
from courses import course_router
import uvicorn

class UTF8JSONResponse(JSONResponse):
    media_type = "application/json; charset=utf-8"

app = FastAPI(default_response_class=UTF8JSONResponse)
app.include_router(course_router) 

@app.get("/")
async def welcome() -> dict:
    return {
        "msg": "Welcome to Hello World API!"
        }   
app.include_router(course_router)

if __name__ =='__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)