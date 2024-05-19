import pywhatkit as pwk

# using Exception Handling to avoid unexpected errors
try:
    # sending message in Whatsapp in India so using Indian dial code (+91)
    pwk.sendwhatmsg("+918848534983", "Hi, how are you?", 14, 43)

    print("Message Sent!")  # Prints success message in console

    # error message
except:
    print("Error in sending the message")