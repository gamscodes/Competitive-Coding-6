class Logger:

    def __init__(self):
        # Initialize a dictionary to track the last printed timestamp of each message
        self.hashMap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # If message hasn't been seen before, print it and store the timestamp
        if message not in self.hashMap:
            self.hashMap[message] = timestamp
            return True

        # If the message was last printed >= 10 seconds ago, print and update timestamp
        if timestamp - self.hashMap[message] >= 10:
            self.hashMap[message] = timestamp
            return True

        # Otherwise, don't print
        return False


if __name__ == "__main__":
    logger = Logger()
    print(logger.shouldPrintMessage(1, "foo"))  # True
    print(logger.shouldPrintMessage(2, "bar"))  # True
    print(logger.shouldPrintMessage(3, "foo"))  # False
    print(logger.shouldPrintMessage(8, "bar"))  # False
    print(logger.shouldPrintMessage(10, "foo"))  # False
    print(logger.shouldPrintMessage(11, "foo"))  # True
