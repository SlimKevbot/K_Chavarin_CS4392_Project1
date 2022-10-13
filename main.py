# Kevin Chavarin
# CS 4392 Project 1: Sockets

# import socket module and logging module
import socket
import logging
import argparse

debug = False
# initialize the variables for our commandline arguments
logLocation = ''
serverPort = 0
serverIP = ''

# create a socket object using SOCK_STREAM for TCP
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# generate an argument parser to separate the IP, PORT, and Logfile variables
helpMsg = "This script connects a client socket to a server, given the user provides a valid IP and Port number"
myParse = argparse.ArgumentParser(description=helpMsg)
# add the arguments
myParse.add_argument("-s", "--server", help="Server IP Address")
myParse.add_argument("-p", "--port", help="Port number")
myParse.add_argument("-l", "--logfile", help="The location of your logfile")
# read the arguments from the command line
# check that the log file location is valid
args = myParse.parse_args()
if args.logfile:
    logLocation = args.logfile
else:
    print("Invalid Logfile location")
    exit()
    #script aborts upon invalid input
# Set up the log file
logging.basicConfig(filename=logLocation + '.log',
                    level=logging.INFO,
                    format="%(asctime)s[%(levelname)-8s] %(message)s",
                    filemode='w')
# check that the IP and Port number are valid inputs
if args.server:
    serverIP = args.server
else:
    logging.error("Invalid server IP\n")
    exit()
    # script aborts upon invalid input
if args.port:
    serverPort = args.port
else:
    logging.error("Invalid port number\n")
    exit()
    # script aborts upon invalid input


# creating the logging object
logger = logging.getLogger()
logging.info('Command Line Arguments - IP:' + serverIP + ' port:' + serverPort + ' Log Location:' + logLocation + "\n")

try:
    logging.info("Connecting to server: " + serverIP + " at port:" + serverPort + "\n")
    # connect to the server on local computer
    mySock.connect((serverIP, int(serverPort)))
except ExceptionGroup:
    logging.error("Could not connect to socket\n")
    # error message for failed connection
    exit()

# send message to server
print("Send a message to the server:")
myMsg = str(input())
print("Your message to send is:" + myMsg)
logging.info("Sending: " + myMsg + '\n')

# sending message to the server through the socket
mySock.sendall(myMsg.encode())
logging.info("Waiting for server response. . .\n")

# receive data from the server and decoding to get the string
serverReply = mySock.recv(1024).decode()
print(serverReply)
logging.info("Server replied with: " + serverReply + '\n')

# close the connection
logging.info("Closing socket connection.\n")
mySock.close()
