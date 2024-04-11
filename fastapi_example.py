import requests
import pandas as pd
import time

## API - Application Programming interface
## two pirces of software can communicate with each other
## Request and response are the two main components of an API
## usually only one app requests and the other responds

## REST API - instead of html, it uses JSON
## JSON - JavaScript Object Notation
## XML is old fashioned

##  Endpoints - where the request or response is sent
## REST is the means of communication. It's how we're communicating
## RESTful API - REST API that follows the REST principles
## REST stands for representational state transfer
## to the constraints of REST architectural style and allows for interaction with RESTful web services
## Useful because you don't need to know the internal workings of the server, it can be  built in any language

##GET - retrieve data, get all of the data by making a request to the endpoint. Returns a JSON object.
##POST - create data, send data to the server. write information to the server. Only for new data
##DELETE - delete data, delete data from the server.
##PUT - update data, update data on the server. Update existing data
##CRUD - Create, Read, Update, Delete

## using fastapi
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Category(Enum):
    food = "food"
    electronics = "electronics"
    clothing = "clothing"
    tools = "tools"


class Item(BaseModel):
    name: str
    category: str
    price: float
    id: int
    count: int

@app.get('/')
def read_root() -> Item:
    return Item(name="cake", category="food", price=1.99, id=1, count=100)
    


