import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base = communicator.stringToProxy("SimplePrinter:default -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

printer.printString("Hello World!")
printer.printUpperCase("Hello World!")
printer.printReverse("Hello World!")

base2 = communicator.stringToProxy("SimpleGreeter:default -p 11000")
greeter = Demo.GreeterPrx.checkedCast(base2)
if not greeter:
    raise RuntimeError("Invalid proxy")

greeter.greet("Kelvin")
greeter.farewell("Kelvin")
