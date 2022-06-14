import os
import sys
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        #f = open(file_from, 'rb')
        #dbx.files_upload(f.read(), file_to)
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                # construct the full local path
                local_path = os.path.join(root, filename)

                # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    access_token = 'sl.BJhnoZqOHkw_lnIlHmJcMUsyzNoBDw8f03fC6tSIZ5uXQDVw4M3EXoWEBDA6yKLURYf6yJXc6ipxPdyb1nwPczwUn9Ja3nBiVePbpT2xd55kCSDWhK_MIy2DB-bAWhaVbUaBtG7o1iYH '
    transferData = TransferData(access_token)
    file_from = str(input("Enter the folder path to transfer : -"))
    file_to = '/test_dropbox' + '/' + file_from
    try:
        transferData.upload_file(file_from, file_to)
        print("File Uploaded")
    except:
        print("Something Wrong Happened")

main()