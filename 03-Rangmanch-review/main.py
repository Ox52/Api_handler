from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("Database tables created")
    yield
    # shutdown:cleanup here
    print ("shutting down the app")



app = FastAPI(

    title =" Rangmanch Reviews Api",
    description ="Theatre reviews API for pune Rangmanch",
    lifespan =lifespan
)

@app.get("/")
def root():
    return{"message ": "Welcome to rangmanch reviews API"}
