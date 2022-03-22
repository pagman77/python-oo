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

    def __init__(self, serial_start=0):
        """accepts starting serial number"""
        self.start = serial_start
        self.next = serial_start

    def __repr__(self):
        return f"<SerialGenerator start = {self.start} next = {self.next}>"

    def generate(self):
        """Increment running serial number"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset running serial number to starting serial number"""
        self.next = self.start
