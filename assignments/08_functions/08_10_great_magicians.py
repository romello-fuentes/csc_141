# 8-10, sending messages, pg 184


def show_messages(messages):
    """Prints all messages in list"""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    '''Print all messages, then the sent ones'''
    print("Sending all messages:")
    while messages:
        current_messages = messages.pop()
        print(current_messages)
        sent_messages.append(current_messages)

messages = ["hello there", "how are you?", "hi"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)
print("Final list:")
print(messages)
print(sent_messages)
