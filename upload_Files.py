from os import access
import os
import dropbox


class TransferData(object):
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_files(self,file_from,file_to,local_path,WriteMode):
        dbx=dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            relative_path = os.path.realpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relative_path)
        with open(local_path,"rb") as f:
            dbx.files_upload(f.read(), dropbox.path, mode= WriteMode('overwrite'))



    

def main():
    access_token="sl.BFHPCFaF6CyZjMJcrV0vEIzaWOi2FEBLXROe-Fr2b-pwvxMdydtr5eFHyQKOQuOYuuzNQf3tLgrzr4p2Hbtg0vfMZlCkQu_O3MqQZ02T37pGCWxNB2T_a4y4J9h2kKqjS_bVDPZMUK8"
    transferdata=TransferData(access_token)
    file_from=input()
    file_to="/ary/class101.py"
    transferdata.upload_files(file_from,file_to)


if __name__== "__main__":
    main()


