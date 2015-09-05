import paramiko
import os


global_result = []

def make_Info(filename, title, description, tags):
    fn_new = filename.split("/")[-1]
    real_fn = fn_new.split(".")[0] + ".txt"
    with open("./tmp/" + real_fn, "w") as file:
         file.write(title + "\n")
         file.write(description + "\n")
         file.write(tags + "\n")
         file.close()



def printTotals(transferred, toBeTransferred):
    print "Transferred: {0}\tOut of: {1}".format(transferred, toBeTransferred) #"Transferred: {0}\tOut of: {1}".format(transferred, toBeTransferred)
    #giveStatus(transferredData = transferred, dataToBeTransferred = toBeTransferred)

"""def giveStatus(transferredData, dataToBeTransferred): #transferred_data, dataToTransfer
    result = []
    result.append(transferredData)
    result.append(dataToBeTransferred)
    global_result = result
    print global_result
    return result"""

def upload_Start(filename):

     paramiko.util.log_to_file(os.path.abspath(os.path.join(os.path.dirname(__file__))) + '/tmp/gyt.log')

     # Open a transport


     host = "127.0.0.1"
     port = 22
     transport = paramiko.Transport((host, port))

     # Auth


     password = "pass"
     username = "user"
     transport.connect(username = username, password = password)

     # Go!

     sftp = paramiko.SFTPClient.from_transport(transport)

     # Upload

     print "Uploading video"
     real_fn = filename.split("/")[-1]
     filepath_vid = "/home/" + real_fn
     localpath_vid = filename
     sftp.put(localpath_vid, filepath_vid, callback=printTotals)
     print "Uploading info"
     filepath_txt = "/home/" + real_fn.split(".")[0] + ".txt"
     localpath_txt = "./tmp/" + real_fn.split(".")[0] + ".txt"
     sftp.put(localpath_txt, filepath_txt)

    # Close


     sftp.close()
     transport.close()