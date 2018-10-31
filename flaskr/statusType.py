class statusType():

    def __init__(self):
        self.status = -1

    def setWaiting(self):
        #TODO: Put on Database
        self.status = 0

    def setProcessing(self):
        #TODO: Put on Database
        self.status = 1

    def setEnded(self):
        #TODO: Put on Database
        self.status = 2

    def __str__(self):
        if self.status == 0:
            return 'Not Processed'
        if self.status == 1:
            return 'Processing'
        if self.status == 2:
            return 'Processed'
        else:
            raise Exception('Status not available')
