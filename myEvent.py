# myEvent.py
# by DFT 2023-09-06
from datetime import datetime


class MyEvent:

    # MyEvent Constructor
    def __init__(self, event = None):

        # Event Model
        self.event = {
            "agora": datetime.now(),
            "sender": "sender-name",
            "message": "description",
            "source": "origin",
        } if event is None else event

        print("init", self.event)




class LogEvent(MyEvent):

    # LogEvent Constructor
    def __init__(self, event = None):
        self.log_file = "myEventLogFile.txt"
        super().__init__(event)

    def direct(self):
        # Log the event direct in a file
        retorno = False
        try:
            with open(self.log_file, 'a') as fp:
                fp.write(str("\n" + "-"*80 + "\n"))
                fp.write(str(self.event))

            retorno = "Direct log"
        except Exception as e:
            print("Exception direct(): ", e)
        return retorno

    def remote(self):
        # Log the event by requests
        print("Log requests", self.event)

e = LogEvent({'agora':str(datetime.now()),'sender':'logtest','message':'first message', 'source': '__main__'})
print(e.direct())



