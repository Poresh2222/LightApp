import firebase_admin

from firebase_admin import firestore
from firebase_admin import credentials
from dotenv import load_dotenv
from os import environ

from typing import Optional

from app.schemas import msg as msg_schemas
from app.schemas import users as user_schemas
from app.utils import msg as msg_utils
from app.utils import users as users_utils


load_dotenv()

ENV_KEYS = {
    "type": "service_account",
    "project_id": environ["PROJECT_ID"],
    "private_key_id": environ["PRIVATE_KEY_ID"],
    "private_key": environ["PRIVATE_KEY"],
    "client_email": environ["CLIENT_EMAIL"],
    "client_id": environ["CLIENT_ID"],
    "auth_uri": environ["AUTH_URI"],
    "token_uri": environ["TOKEN_URI"],
    "auth_provider_x509_cert_url": environ["AUTH_PROVIDER_X509_CERT_URL"],
    "client_x509_cert_url": environ["CLIENT_X509_CERT_URL"]
}

cred = credentials.Certificate(ENV_KEYS)
firebase_admin.initialize_app(cred)

db = firestore.client()

msg_ref = db.collection(u'messages')
user_ref = db.collection(u'users')
phone_ref = db.collection(u'phones')


async def add_msg(msg: msg_schemas.MessageMidle, uid_from: str, uid_for: str):
    msg_ref.document(uid_from).collection(uid_for).document().set({
        u'msg': msg.message,
        u'date': msg.date,
        u'uid_from': msg.uid_from,
        u'uid_for': msg.uid_for
    })

    return None


async def get_msg(uid_from, uid_for):
    uid_list = []
    
    if uid_for == None:

        doc_ref = msg_ref.document(uid_from).collections()
        for collection in doc_ref:

            for doc in collection.stream():
                uid_list.append(doc.to_dict())

        return await msg_utils.build_dict(uid_list=uid_list, uid_from=uid_from)

    else:
        
        doc_ref = msg_ref.document(uid_from).collection(uid_for).stream()
        for doc in doc_ref:
            uid_list.append(doc.to_dict())

        return await msg_utils.build_dict(uid_list=uid_list, uid_from=uid_from)


async def del_doc(uid_from: str, uid_for: str, date: Optional[str] = None, dell: Optional[bool] = False, new_msg: Optional[str] = None):

    if date == None:
        doc_ref = msg_ref.document(uid_from).collection(uid_for).stream()

    else:
        doc_ref = msg_ref.document(uid_from).collection(uid_for).where(u'date', u'==', date).stream()

    if dell == False:
        for doc in doc_ref:
            doc.reference.update({u'msg': new_msg})

    else:

        for doc in doc_ref:
            doc.reference.delete()


async def create_user(user: user_schemas.UserCreate):
    uid = await users_utils.get_random_string()

    hashedPassword = users_utils.get_password_hash(user.password)

    phone_ref.document(user.phone).set({
        u'us_phone': user.phone,
        u'uid': uid})

    user_ref.document(uid).collection(u'user_data').document().set({
        u'username': user.username,
        u'first_name': user.first_name,
        u'last_name': user.last_name, 
        u'hashed_password': hashedPassword,
        u'phone': user.phone,
        u'uid': uid
    })


async def check_phone(phone: str):
    num = phone_ref.document(phone).get({u'us_phone'}).to_dict()
    if num == None:
        return True
    else:
        return False


async def get_user(phone: str):
    user_uid = phone_ref.document(phone).get({u'uid'}).to_dict()
    if user_uid == None:
        return False

    uid = user_uid['uid']
    doc_ref = user_ref.document(uid).collection(u'user_data').where(u'uid', u'==', uid).stream()

    for doc in doc_ref:
        doc = doc.to_dict()
        hashed_password = doc['hashed_password'] 

    return user_schemas.UserOut(phone=phone, password=hashed_password, uid=uid)

