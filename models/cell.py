from models.board import Board
from models.status import Status
from models.models import *

class Cell(BaseModel):
    text = CharField(default="")
    name = CharField()
    order = IntegerField()
    status = ForeignKeyField(Status)
    board = ForeignKeyField(Board)
