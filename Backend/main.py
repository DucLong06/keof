from fastapi import FastAPI
from fastapi import FastAPI
from fastapi import HTTPException
import utils
from interface.api import DataList
import logic
import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Server is running"}


@app.get("/user")
async def get_user():
    return utils.read_data_json("db/User.json")


@app.post("/money")
async def money(data: DataList):
    total_money = sum(entry.gold for entry in data.items)
    if total_money == 0:
        try:
            current_date = datetime.date.today().strftime('%d/%m/%Y')
            new_data = {
                "date": current_date,
                "items": [{"id": item.id, "money": item.gold} for item in data.items]
            }
            utils.write_data_json("db/Money.json", [new_data])
            await logic.calculator(data.items, current_date)
            return HTTPException(status_code=200, detail={"send message successful"})
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    else:
        return HTTPException(status_code=400, detail={"Tổng tiền đang bị sai!"})
