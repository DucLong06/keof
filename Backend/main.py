from fastapi import FastAPI
from fastapi import FastAPI
from fastapi import HTTPException
import utils
from interface.api import DataList
import logic
import datetime

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Server is running"}


@app.get("/user")
async def get_user():
    return utils.read_data_json("db/User.json")


@app.post("/money")
async def money(data: DataList):
    total_money = sum(entry.money for entry in data.items)
    if total_money == 0:
        try:
            current_date = datetime.date.today().strftime('%d/%m/%Y')
            new_data = {
                "date": current_date,
                "items": [{"id": item.id, "money": item.money} for item in data.items]
            }
            utils.write_data_json("db/Money.json", [new_data])
            await logic.calculator(data.items)
            return HTTPException(status_code=200, detail={"send message successful"})
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    else:
        return HTTPException(status_code=400, detail={"Tổng tiền đang bị sai!"})
