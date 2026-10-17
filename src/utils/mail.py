from fastapi import FastAPI
# from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List 

# class EmailSchema(BaseModel):
#     email: List[EmailStr]


conf = ConnectionConfig(
    MAIL_USERNAME = "abdul.eoxysit@gmail.com",
    MAIL_PASSWORD = "uuxk daxg jsve oiwu",
    MAIL_FROM = "abdul.eoxysit@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="Abdul Khalid ",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)



async def send_email(emails: List[str]):
    html = """<p>Hi thanks for ragistartion our team connect you</p> """

    message = MessageSchema(
        subject="Ragistraion Confirmation",
        recipients=emails,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    print("mail sent successfull....")
    return {"message": "email has been sent"}