import simplegui

num1 = 0;
num2 = 0;
result = 0;

def input1(inp):
    global num1;
    num1 = float(inp);
    output();

def input2(inp):
    global num2;
    num2 = float(inp);
    output();

def output():
    print "Num1 = ", num1;
    print "Num2 = ", num2;
    print "";
    
def swap():
    global num1, num2
    num1, num2 = num2, num1
    output()
    
def add():
    global num1, num2, result
    result = num1 + num2;
    output();
    print "Sum = ", result;
    print "";

def sub():
    global num1, num2, result
    result = num1 - num2;
    output();
    print "Diff = ", result
    print ;

def multi():
    global num1, num2, result
    result = num1 * num2;
    output();
    print "Product = ", result;
    print "";

def div():
    global num1, num2, result
    result = num1 / num2;
    output();
    print "Result = ", result;
    print "";

    
frame = simplegui.create_frame("Calculator", 200, 400);
frame.add_button("Print", output, 100);
frame.add_button("Swap", swap, 100);
frame.add_button("Add" ,add, 100);
frame.add_button("Sub", sub, 100);
frame.add_button("Multi", multi, 100);
frame.add_button("Divide", div, 100);
frame.add_input("Enter num1", input1,100);
frame.add_input("Enter num2", input2, 100);           
frame.start();
