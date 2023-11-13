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


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # Sample YouTube video link
# video_link = "https://www.youtube.com/watch?v=OAbsSapZY-I"



# @app.get("/api/video")
# async def get_video():
#     return {"url": video_link}

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

app = FastAPI()

class VideoRequest(BaseModel):
    url: str

def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        return ' '.join([item['text'] for item in transcript_list])
    except (TranscriptsDisabled, NoTranscriptFound):
        return "No transcript available"

@app.post("/api/video")
async def post_video(video_request: VideoRequest):
    video_id = video_request.url.split('v=')[1]
    transcript = get_transcript(video_id)
    return {
        'url': video_request.url,
        'transcript': transcript
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
