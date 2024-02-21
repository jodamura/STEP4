from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str


@app.post("/ultra")
def ultra(item: Item):
    for keyword in ["おだむら", "オダムラ","小田村","odamura"]:
        if keyword in item.name:
            return {"result": f"ウルトラ{keyword}"}
    else:
            return {"result": "人違いでした"}
