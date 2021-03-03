import dropbox
import cv2
import time

frame_count = 1

class TransferData(object):
    def __init__(self, token):
        self.token = token

    def upload(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

token = "x73z4wKfvO8AAAAAAAAAAXdT-_pQBJxtwICpyX2AP83S95z2wR6So5LQWtT4XX_c"
transferData = TransferData(token)

def take_img():
    cap = cv2.VideoCapture(0)
    count=0

    while count!=30:
        ret, frame = cap.read()
        cv2.imwrite('frame' + str(frame_count) + '.jpg', frame)
        count+=1

    cap.release()
    cv2.destroyAllWindows()
    
    file_name = 'frame' + str(frame_count) + '.jpg'

    file_from = 'C:/Users/Saaheer/Desktop/Programming/Whitehatjr/1Python/' + file_name
    file_to = '/images/' + file_name
    
    transferData.upload(file_from, file_to)

while True:
    time.sleep(300)
    take_img()
    frame_count+=1

