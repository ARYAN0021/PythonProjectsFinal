from os import access
import dropbox

class TransferData(object):
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_files(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        with open(file_from,"rb") as f:
            dbx.files_upload(f.read(),file_to)


def main():
    access_token="sl.BE-JmRBE9uu2Qhtq5zFcv8d2it9kqeeqJfH5wC0cee8eB_b7Km0-gXbatxsUeCJkndy2FIPZEOfNoPjXu3WcUhMrt3xLkqnRUc0xwF5geIz8SEhp4mCy4YXdcu-_BowGzm4owkp5Tzk"
    transferdata=TransferData(access_token)
    file_from=input()
    file_to="/ary/class101.py"
    transferdata.upload_files(file_from,file_to)


if __name__== "__main__":
    main()