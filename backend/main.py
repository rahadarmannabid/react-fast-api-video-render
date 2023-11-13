# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# class Person(BaseModel):
#     name: str

# # In-memory database
# db = [
#     {"name": "Alice"},
#     {"name": "Bob"},
#     {"name": "Charlie"}
# ]

# @app.get("/api/")
# async def read_people():
#     return db

# @app.post("/api/add")
# async def add_person(person: Person):
#     db.append(person.dict())
#     return {"message": "Person added successfully"}

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Sample YouTube video link
video_link = "https://www.youtube.com/watch?v=OAbsSapZY-I"



@app.get("/api/video")
async def get_video():
    return {"url": video_link}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
