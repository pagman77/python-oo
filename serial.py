class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(serial_start= 100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, serial_start):
        """accepts starting serial number"""
        self.serial_start = serial_start
        self.running_serial = 0
        self.counter = 0


    def __repr__(self):
        return f"<SerialGenerator serial_start = {self.serial_start}>"

    def generate(self):
        """Increment running serial number"""
        self.running_serial = self.serial_start + self.counter
        self.counter += 1
        return self.running_serial

    def reset(self):
        """Reset running serial number to starting serial number"""
        self.running_serial = self.serial_start
        self.counter = 0
