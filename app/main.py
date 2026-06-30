from fastapi import FastAPI
from pydantic import BaseModel
from habbitTracker import *


app = FastAPI()

class Habit(BaseModel):
    name: str

