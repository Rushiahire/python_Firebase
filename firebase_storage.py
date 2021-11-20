import credentials

storage = credentials.firebase.storage()

filename = input("Enter the name of file u want to upload ")
cloudfilename = input("Enter the name of file on the cloud ")
storage.child(cloudfilename).put(filename)