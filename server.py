import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)

    def printUpperCase(self, s, current=None):
        print(s.upper())

    def printReverse(self, s, current=None):
        print(s[::-1])

class GreeterI(Demo.Greeter):
    def greet(self, name, current=None):
        print(f"Hello, {name}!")

    def farewell(self, name, current=None):
        print(f"Goodbye, {name}!")

communicator = Ice.initialize(sys.argv)

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
adapter.add(PrinterI(), communicator.stringToIdentity("SimplePrinter"))
adapter.add(GreeterI(), communicator.stringToIdentity("SimpleGreeter"))
adapter.activate()

communicator.waitForShutdown()