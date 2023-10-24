
# from firebase_admin import messaging
# import fcm_notification

# def send_to_firebase_cloud_messaging():
#     # This registration token comes from the client FCM SDKs.
#     registration_token = '클라이언트의 FCM 토큰'

#     # See documentation on defining a message payload.
#     message = messaging.Message(
#     notification=messaging.Notification(
#         title='안녕하세요 타이틀 입니다',
#         body='안녕하세요 메세지 입니다',
#     ),
#     token=registration_token,
#     )

#     response = messaging.send(message)
    
#     try:
#         response = messaging.send(message)
#         # Response is a message ID string.
#         print('Successfully sent message:', response)
#     except Exception as e:
#         print('예외가 발생했습니다.', e)
        
#     # Response is a message ID string.
#     print('Successfully sent message:', response)
    
# fcm_notification.send_push_when_new_family_question_registered(family_question)

# from pyfcm import FCMNotification
 
# APIKEY = "Your Server Key"
# TOKEN = "Your Token"
 
# # 파이어베이스 콘솔에서 얻어 온 서버 키를 넣어 줌
# push_service = FCMNotification(APIKEY)
 
# def sendMessage(body, title):
#     # 메시지 (data 타입)
#     data_message = {
#         "body": body,
#         "title": title
#     }
 
#     # 토큰값을 이용해 1명에게 푸시알림을 전송함
#     result = push_service.single_device_data_message(registration_id=TOKEN, data_message=data_message)
 
#     # 전송 결과 출력
#     print(result)
 
# sendMessage("배달의 민족", "치킨 8000원 쿠폰 도착!")

# This registration token comes from the client FCM SDKs.

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

json_path = "/home/dfx/naro/cap/smartfarmKey.json"
path = credentials.Certificate(json_path)
firebase_admin.initialize_app(path)

def send_push_notification(registration_token, message):
    registration_token = ''

    message = messaging.Message(
        notification = messaging.Notification(
            data = '물 높이 경고!',
            body = '스마트팜을 확인해주세요!'
        ),    
        token = registration_token,
    )

    response = messaging.send(message)
    print('successfully waterlevel message: ', response)
    
def send_push_notification2(registration_token, message):
    registration_token = ''

    message = messaging.Message(
        notification = messaging.Notification(
            data = '물 온도 경고!',
            body = '스마트팜을 확인해주세요!'
        ),    
        token = registration_token,
    )

    response = messaging.send(message)
    print('successfully watertemp message: ', response)

def send_push_notification3(registration_token, message):
    registration_token = ''

    message = messaging.Message(
        notification = messaging.Notification(
            data = '내부 온도 경고!',
            body = '스마트팜을 확인해주세요!'
        ),    
        token = registration_token,
    )

    response = messaging.send(message)
    print('successfully temp message: ', response)
    
def send_push_notification4(registration_token, message):
    registration_token = ''

    message = messaging.Message(
        notification = messaging.Notification(
            data = '습도 경고!',
            body = '스마트팜을 확인해주세요!'
        ),    
        token = registration_token,
    )

    response = messaging.send(message)
    print('successfully hum message: ', response)
    
def send_push_notification5(registration_token, message):
    registration_token = ''

    message = messaging.Message(
        notification = messaging.Notification(
            data = '수분 경고!',
            body = '스마트팜을 확인해주세요!'
        ),    
        token = registration_token,
    )

    response = messaging.send(message)
    print('successfully soil message: ', response)
    
# if __name__ == "__main__":
#     send_push_notification()