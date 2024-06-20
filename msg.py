import pywhatkit as kit

Phone_Number = "+919322794805"  # Use international format (with country code)
message = "Hello, this is a auto generated message..!"

# Define the time to send the message (24-hour format)
hour = 22  # 3 PM
minute = 23  # 30 minutes past the hour

# Send the message
try:
    kit.sendwhatmsg(Phone_Number, message, hour, minute)
    print("Message scheduled successfully!")
except Exception as eobj:
    print("An error occurred: ",eobj)
