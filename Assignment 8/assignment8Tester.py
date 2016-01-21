##Daniel Lee
##CSCI 1101 Section 1

from assignment8 import*

myInbox = SMSstore()
myInbox.addNewArrival(5158495672,505,'This is a message.')
myInbox.addNewArrival(9856211235,1705,'Another message.')
myInbox.addNewArrival(4525847583,1905,'I love computer science.')
print(myInbox)
print(myInbox.message_count())
print(myInbox.get_unread_indexes())
print(myInbox.get_message(2))
print(myInbox)
print(myInbox.get_unread_indexes())
print(myInbox.get_message(9))
print(myInbox)
myInbox.delete(1)
print(myInbox)
myInbox.clear()
print(myInbox)
