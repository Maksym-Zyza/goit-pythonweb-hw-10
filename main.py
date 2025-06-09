from fastapi import FastAPI, Depends, HTTPException, status
from src.database.db import get_db
from sqlalchemy import text
from src.routers import contacts

app = FastAPI()


@app.get("/", name="API root")
def get_index():
    return {"message": "Welcome to root API"}


@app.get("/health", name="Server availability")
def get_health(db=Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1+1")).fetchone()
        print(">>", result)
        if result is None:
            raise Exception

        return {"message": "API is up and ready for the requests"}
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="DB is not configured correctly",
        )


app.include_router(contacts.router)
