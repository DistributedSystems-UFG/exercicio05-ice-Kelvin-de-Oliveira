module Demo
{
    interface Printer
    {
        void printString(string s);
        void printUpperCase(string s);
        void printReverse(string s);
    }

    interface Greeter
    {
        void greet(string name);
        void farewell(string name);
    }
}
