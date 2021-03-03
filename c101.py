import dropbox

class TransferData(object):
    def __init__(self, token):
        self.token = token

    def upload(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    token = "sl.AloRfve8VEGbDIAxhfgvpDo_X028n-4i1ksje8ClkXGLHt2VghhAeDIeIx4aOB2ZV_7P3sHzjeyzNzW9Jf6v2QWCvt1cmLhKBquDVUp7KPne0oXv-VmFN3l653tV88KijBe47D8u5tg"
    transferData = TransferData(token)
    #file_from = input("Enter file directory: ")
    #file_to = input("Enter the full path to transfer: ")
    file_from = 'C:/Users/Saaheer/Desktop/Programming/Whitehatjr/1Python/test.txt'
    file_to = '/test/test.txt'
    
    transferData.upload(file_from, file_to)

main()
