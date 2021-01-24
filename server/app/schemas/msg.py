from pydantic import BaseModel
from typing import Optional


class MessageIn(BaseModel):
    uid_from: str
    uid_for: str
    message: str

class MessageMidle(MessageIn):
    date: str

class MessageUp(MessageMidle):
    dell: bool    

class MessageInputDell(BaseModel):
    uid_from: str
    uid_for: str
    all_in_all: Optional[bool] = False
    all_msg: Optional[bool] = False
    date: Optional[str] = None

class MessagesInOpt(BaseModel):
    uid_from: str
    uid_for: Optional[str] = None    