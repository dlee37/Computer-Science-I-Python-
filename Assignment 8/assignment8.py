##Daniel Lee
##CSCI 1101 Section 1

class SMSstore(object):

    def __init__(self):

        self.messages = []

    def addNewArrival(self,from_number,time_arrived,text_of_SMS):
        ##please write the time in interger military time without colons, or as a string
        
        has_been_viewed = False
        return self.messages.append((has_been_viewed,from_number,time_arrived,text_of_SMS))

    def message_count(self):

        return len(self.messages)

    def get_unread_indexes(self):
        ##returns a list of indexes of all non-read messages

        count = 0
        for item in self.messages:
            if item[0] == False:
                count += 1
        return count
        

    def get_message(self,i):
        ##returns the tuple for that particular message, changes has_been_viewed to true

        try:
            message = list(self.messages[i])
            message[0] = True
            self.messages[i] = tuple(message)
            return self.messages[i]
        except IndexError:
            return None

    def delete(self,i):

        self.messages.pop(i)
##        return self.messages

    def clear(self):

        self.messages[:] = []
##        return self.messages

    def __str__(self):
        ##returns a list representation of your inbox

        return str(self.messages)
