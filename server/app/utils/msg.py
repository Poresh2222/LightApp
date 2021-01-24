from datetime import datetime

from app.schemas import msg as msg_schemas
from app.utils import firebase as firebase_utils


async def add_time(msg: msg_schemas.MessageIn):
    msg_midlle = msg_schemas.MessageMidle(uid_from=msg.uid_from, uid_for=msg.uid_for, message=msg.message, date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    await firebase_utils.add_msg(msg=msg_midlle, uid_from=msg.uid_from, uid_for=msg.uid_for)

    return await firebase_utils.add_msg(msg=msg_midlle, uid_from=msg.uid_for, uid_for=msg.uid_from)


async def build_dict(uid_list, uid_from):
    msg = { uid_from : {} }
    msg_dict = {}

    for item in uid_list:

        if uid_from != item['uid_from']:
            uid = item.pop('uid_from')
            
        else:
            uid = item.pop('uid_for')           

        if uid in msg_dict.keys():
            msg_dict[uid].append(item)
            
        elif uid not in msg_dict.keys():
            msg_dict[uid] = [item]

        else:
            break

    msg[uid_from] = msg_dict    

    return msg


async def del_msg(msg: msg_schemas.MessageInputDell):
    if msg.all_msg == True:

        if msg.all_in_all == True:
            await firebase_utils.del_doc(uid_from=msg.uid_from, uid_for=msg.uid_for)
            await firebase_utils.del_doc(uid_from=msg.uid_for, uid_for=msg.uid_from)

        else:
            await firebase_utils.del_doc(uid_from=msg.uid_from, uid_for=msg.uid_for)

    else:

        if msg.all_in_all == True:
            await firebase_utils.del_doc(uid_from=msg.uid_from, uid_for=msg.uid_for, date=msg.date)
            await firebase_utils.del_doc(uid_from=msg.uid_for, uid_for=msg.uid_from, date=msg.date)

        else:
            await firebase_utils.del_doc(uid_from=msg.uid_from, uid_for=msg.uid_for, date=msg.date)


async def update_msg(msg: msg_schemas.MessageUp):
    await firebase_utils.del_doc(uid_from=msg.uid_from, uid_for=msg.uid_for, date=msg.date, new_msg=msg.message, dell=msg.dell)
    await firebase_utils.del_doc(uid_from=msg.uid_for, uid_for=msg.uid_from, date=msg.date, new_msg=msg.message, dell=msg.dell)