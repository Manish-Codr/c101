import dropbox


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)


def main():
    access_token = 'sl.BJhnoZqOHkw_lnIlHmJcMUsyzNoBDw8f03fC6tSIZ5uXQDVw4M3EXoWEBDA6yKLURYf6yJXc6ipxPdyb1nwPczwUn9Ja3nBiVePbpT2xd55kCSDWhK_MIy2DB-bAWhaVbUaBtG7o1iYH'
    transferData = TransferData(access_token)
    fromFile = input("Enter The File You Want To Upload: ")
    file_from = fromFile
    file_to = '/test_dropbox' + '/' + fromFile
    try:
        transferData.upload_file(file_from, file_to)
        print("File Uploaded")
    except:
        print("Something Wrong Happened")


main()
