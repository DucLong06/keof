from fastapi import FastAPI
from fastapi import FastAPI
from fastapi import HTTPException
import utils
from interface.api import DataList
app = FastAPI()

data = [
    {"id": 1, "money": 4},
    {"id": 2, "money": -4},
    {"id": 3, "money": 5},
    {"id": 4, "money": -3},
    {"id": 5, "money": -2}
]



@app.get("/user")
async def root():
    return {"message": "Hello World"}


@app.post("/money")
async def money(data: DataList):
    try:
        result = {"message": utils.calculator(data.items)}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
