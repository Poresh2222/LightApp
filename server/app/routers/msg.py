from fastapi import APIRouter

from typing import Optional

from app.schemas import msg as msg_schemas
from app.utils import msg as msg_utils
from app.utils import firebase as firebase_utils


msg_router = APIRouter()


@msg_router.post('/messages/send_message')
async def create_msg(msg: msg_schemas.MessageIn):
    await msg_utils.add_time(msg=msg)
    return await firebase_utils.get_msg(uid_from=msg.uid_from, uid_for=msg.uid_for)


@msg_router.get('/messages/get_messages')
async def get_all_msg(uid_from: str, uid_for: Optional[str] = None):
    return await firebase_utils.get_msg(uid_from=uid_from, uid_for=uid_for)


@msg_router.delete('/messages/dell_messages') 
async def dell_msg(msg: msg_schemas.MessageInputDell):
    return await msg_utils.del_msg(msg=msg)


@msg_router.put('/messages/update_messages')
async def update_msg(msg: msg_schemas.MessageUp):
    return await msg_utils.update_msg(msg=msg)