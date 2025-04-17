# Programming for Everybody (Getting Started with Python)

## Chapter 1

```
[Grafik: Einfaches Python-Logo mit blauem und gelbem Python-Symbol]
```

### Module 1

Wednesday, April 2nd, 09:17 -- 11:15, 15:45 -- 18:30 = 5h

##### 1.2 -- Hardware Overview

**INPUT AND OUTPUT DEVICES**

- Input: Mouse, Keyboard, Touchscreen etc.
- Output: Screen, Speakers, Printer
- Interaction with Software

**CENTRAL PROCESSING UNIT = CPU**

- Highly sophisticated Circuit (Chip)
- With millions of transistors
  - Transistors make yes/no decisions
- Runs the Program
  - Billions of instructions
    - = set of electrical pulses
    - 3 billion times per second
- It is always wondering "what to do next?"
- Not the brains exactly -- very dumb but very very fast

**MAIN MEMORY**

- Fast small temporary storage -- lost on reboot -- aka RAM
- File that is created by writing code in Secondary Memory is loaded and translated (in machine language) in Main Memory
- Program from Main Memory feeds instructions to CPU
- After Execution by CPU it feeds further instructions etc. "fetch-execute-cycle"

**SECONDARY MEMORY/STORAGE**

- Slower large permanent storage -- lasts until deleted
  - When the Computer turns off, the written program is erased from the Main Memory
  - Secondary Memory is permanent
- Writing of code and creating of file is being done here
- E.g. disk drive, memory stick

### Module 2

- Visual Studio Code: Text editor, with which I'll write Python Code
  - To show Text in the Terminal enter "print('xxxxx')
- Terminal: Program with which I can see if my code works
  - To show where I am + see what is listed there enter "ls"
  - To change directory enter "cd" and the name of the folder you want to be in -> you'll switch folders (if the folder has more than one word use "...")
  - When you are in a folder with python in it, enter "python3" and the name of the .py document -> it will run the document

### Module 3

**SYNONYMS WHILE LEARNING "THE LANGUAGE" PYTHON**

- Vocabulary/Words -> Variables and Reserved words (Chapter 2)
- Sentences -> Lines
- Sentence structure -> valid syntax patterns (Chapters 3-5)
- Story structure -> constructing a program for a purpose

**VOCABULARY**

- Variable = any given name, that is stored and can be retrieved later again, can also be changed later
- Operator = symbols (math signs) that represent computations like +, -, *, /, **
  - Comparison operators: compare variables but don't change the variables (<, >, <=, >=, ==)
- Constant = fixed value such as numbers, letters, strings
- Statement = unit of code that python can execute
  - Assignement statement: x = 2
  - Expression statement: print(x)
  - Conditional statement: if, if-else, if-elif, try-except
    - Nested decision: condition within condition
- Boolean expressions = means there is only True or False
- Function = stored code that we can use, takes input to create an output. There are built-in functions (e.g. def(), print(), max() etc.), one can also create functions (e.g. def *variable()* )
  - Function name: the variable name you give the function
  - Parameter: variable we put in the parantheses of the function as the *definition*, can be more than one variable, divided by comma
    - Argument: a value we enter in the place, where we put the argument when we defined the function, it's called parameter when we (re)call the function, then we can use different *values* to do the same work of the function
  - Return statement: ends the function execution and "sends back" the result of the function
- Iteration variables (iteration = wiederholend): a variable that changes the value each time python goes through a loop

**RESERVED WORDS**

```
[Liste von Python-Schlüsselwörtern: 
and, as, assert, break, class, continue, def, del, elif, else, except, 
False, finally, for, from, global, if, import, in, is, lambda, None, 
nonlocal, not, or, pass, raise, return, True, try, while, with, yield]
```

- If we use these words, we must use them to mean the thing that python expects them to be
  - We can't use them elsewhere
- You cannot use reserved words as variable names/identifiers

**LINES**

- Sentences are lines, so we can construct a paragraph out of several lines.

```
[Beispielcode mit mehreren Zeilen Python-Code]
```

**PYTHON SCRIPTS**

- Interactive Python is good for experiments and programs of 3-4 lines long
- Most programs are much longer, so we type them into a file and tell Python to run the commands in the file
- In a sense, we are "giving Python a script"
- As a convention, we add ".py" as the suffix on the end of these files to indicate they contain Python

Interactive
- You type directly to Python one line at a time and it responds

Script
- You enter a sequence of statements (lines) into a file using a text editor and tell Python to execute the statements in the file

**PROGRAM STEPS OR PROGRAM FLOW**

- Sequential
  - Like a recipe or installation instructions, a program is a sequence of steps to be done in order
- Conditional
  - Some steps are conditional -- they may be skipped
- Repetitional
  - Sometimes a step or group of steps is to be repeated
- Store and retreat
  - Sometimes we store a set of steps to be used over and over as needed several places throughout the program (Chapter 4)

## Chapter 2

Tuesday, April 3rd, 9:00-12, 13:15 -- 14:30, 16:15-18:00

### Module 4

**CONSTANTS**

- Fixed values such as
  - Numbers
  - Letters
  - Strings

```
[Bild zeigt Beispiele für Konstanten: 123, 98.6, "Hello World"]
```

are called "constants" because their value doesn't change

- Numeric constants are as you expect
- String constants use single quotes (') or double quotes ("")

**VARIABLES**

```
[Bild zeigt x = 12.2 mit einem Pfeil, der auf einen Speicherbereich zeigt]
```

- A variable is a named place in the memory where a programmer can store data and later retrieve the data using the variable "name"
- Programmers get to choose the names of the variables
- You can change the contents of a variable in a later statement
  - E.g. after y = 14 you can write x = 100 in the next line, which will change the value of x from 12.2 to 100
- Python Variable Name Rules
  - Must start with a letter or underscore _
  - Don't start with numbers, # or use a dot.
  - Should consist of letters, numbers, and underscores
  - Case sensitive (e.g. spam, Spam and SPAM are three different variables)

```
[Beispiel für Python-Code]
```

**STATEMENTS**

- A statement is a unit of code that the Python interpreter can execute
- We have seen two kinds of statements: print being an expression statement and assignment statement

**Assignment Statements**

- We assign a value to a variable using the assignment statement (=), e.g. x = 0,5
- An assignment statement consists of an expression on the right-hand side and a variable to store the result
- A variable is a memory location used to store a value
- Once the expression is evaluated, the result is placed in (assigned to) x
- The value stored in a variable can be updated by replacing the old value (e.g. 2) with a new value (e.g. 0,975)

```
[Bild zeigt Variablenzuweisung: x = 0.975]
```

**OPERATORS AND OPERATIONS**

- Operators are special symbols that represent computations like addition and multiplication
- The values the operator is applied to are called operands
- The operators +, -, *, /, and ** perform addition, subtraction, multiplication, division, and exponentiation
- The remainder (Restbetrag) ist %
- Operator precedence (Vorrang) rules
  - Parantheses
  - Exponentiation (raise to a power)
  - Multiplication, Division, Remainder
  - Addition and Subtraction
  - Left to right
- You can also add two constants, e.g.
  - >>> eee = "hello " + "there"
  - >>> print(eee)
  - Hello there

**TYPE**

- Python differs between types of variables and constants
- -> type(xx)
- Constants = string (Buchstabenfolge)
- (Full) Numbers = integer
- Kommazahlen = float (floating point)
- Type Conversions
  - >>> print(float(99))
  - 99.0
- String Conversions
  - You can use int() and float() to convert between strings and integers
  
```python
>>> x = "123"
>>> type (x)
<class 'str'>
>>> y = int(x)
>>> type (y)
<class 'int'>
>>> print(y + 1)
124
```

  - You will get an error if the string does not contain numeric characters
    - A = 'hello bob'
    - B = int(a)
    - Traceback (most recent call last): File "<stdin>", line 1, in <module>
    - ValueError: invalid literal for int() with base 10: 'x'

**USER INPUT**

```
[Bild zeigt: nam = input('Who are you? ')]
```

- We can instruct Python to pause and read data from the user using the input() function
- The input() function **returns a string**

```
[Bild zeigt ein Flussdiagramm für ein Begrüßungsprogramm]
```

## Chapter 3

Friday, April 4th, 11 -- 12, 13 - 16

### Module 5

**CONDITIONAL STATEMENTS**

- Comparison Operators
  - Boolean expressions
    - Ask a question and produce a Yes or No result
    - We use this to control program flow
    - Using comparison operators evaluate to True/False or Yes/No
  - Comparison operators look at variables but do not change the variables
- If-statements
  - End with colon (Doppelpunkt)
  - Next line is indented (eingezogen) by 4 Spaces
  - If the conditional statement has only one line, it can stand behind the colon
  - If the conditional statement has more than one line, they are indented with the same distance below each other
    - -> multi-line blocks of conditional code
  - S. Entscheidungsbaum als Gedankenstütze

```
[Grafik: Flussdiagramm zur Darstellung einer if-Anweisung]
```

```
[Grafik: Beispielcode für if-Anweisung und Entscheidungsbaum]
```

- Nested Decisions
  - Condition within condition

```
[Grafik: Beispiel für verschachtelte if-Anweisungen]
```

```
[Grafik: Flussdiagramm für verschachtelte Entscheidungen]
```

- If-else-statements (Two-way-Decisions)
  - Sometimes we want to do one thing if a logical expression is true and something else if the expression is false
  - It is like a fork in the road -- we must choose one or the other path, not both

```
[Grafik: Flussdiagramm für if-else-Anweisung]
```

```
[Grafik: Beispielcode für if-else-Anweisung]
```

- Elif-statements (= else + if)
  - Doesn't have to have an "else"
  - There can be more than one "elif"
    - But as soon as one elif is "True" and being executed, the other "elifs" and the "else" will be skipped

```
[Grafik: Flussdiagramm für elif-Anweisung]
```

```
[Grafik: Beispielcode für elif-Anweisung]
```

- The try/except structure
  - You surround a dangerous section of code with *try* and *except*
  - If the code in the *try* works -- the *except* is skipped
  - If the code in the *try* fails -- It jumps to the *except* section
  - To eliminate or catch a traceback
  - If you put a few lines in the "try" block and one line is not working, it will skip to the "except" block, so nothing in the "try" block will be executed

```
[Grafik: Beispiel für try/except-Struktur]
```

```
[Grafik: Weiteres Beispiel für try/except-Struktur]
```

```
[Grafik: Beispiel mit Fehler in try/except-Block]
```

```
[Grafik: Ausführliches Beispiel für try/except mit Fehlermeldung]
```

## Chapter 4

Monday, April 7th, 9:30 -- 11:15, 15-18

### Module 6

**FUNCTIONS**

- A function is some stored code that we use
- A function takes some input and produces an output
- Storing (and reusing)
  - "def" means start the definition of a function
  - This function helps to reuse several lines of code without rewriting them again
  - E.g.
    - Def = testest():
      - print ("Hello")
      - print ("Nice")
    - testest ()
    - print ("Beach")
    - testest ()
  - This will print in the end:
    - Hello
    - Nice
    - Beach
    - Hello
    - Nice
- Max and Min function
  - Gives us the largest and smallest values in a list
- Type conversions
  - Float conversions
    - When you put an integer and floating point in an expression, the integer is implicitly converted to a float
    - You can control this with the built-in functions int() and float()
  - String conversions
    - You can also use int() and float() to convert between strings and integers
    - You will get an error if the string does not contain numeric characters
    - S. chapter 3

**BUILDING FUNCTIONS**

- We create a new function using the def keyword followed by optional parameters in parentheses
- We indent the body of the function
- This defines the function but does *not execute* the body of the function
- We have to invoke (aufrufen) the body of the function seperately

```
[Grafik: Beispiel einer Funktionsdefinition mit def big():...]
```

```
[Grafik: Beispiel für Funktionsaufruf]
```

PARAMETERS

- A parameter is a variable which we use in the function *definition*
- It is a "handle" that allows the code in the function to access the arguments for a particular function invocation

ARGUMENTS

- An argument is a value we pass into the function as its input when we *call* the function
- We use arguments so we can direct the function to do different kinds of work when we call it at different times
- We put the arguments in parentheses after the name of the function

```
[Grafik: Beispiel für Parameter und Argumente]
```

RESULT/ RETURN VALUES

- Often a function will take its arguments, do some computation and return a value to be used as the value of the function call in the calling expression
- The return keyword is used for this
- A "fruitful" function is one that produces a result (or return value)
- The return statement ends the function execution and "sends back" the result of the function

```
[Grafik: Beispiel einer Funktion mit return-Anweisung]
```

```
[Grafik: Beispiel für Funktionsaufruf mit Rückgabewert]
```

**MULTIPLE PARAMETERS AND ARGUMENTS**

- We can define more than one parameter in the function definition
- When we call the function later on, we enter the argument

## Chapter 5

Tuesday, April 8th

### Module 7: Loops and Iteration

**INDEFINITE LOOPS: „WHILE-STATEMENTS"**

- Indefinite = unbestimmt
- Loops (repeated steps) have *iteration variables* (iteration = wiederholend)
  - A variable that changes the value each time python goes through the loop
  - Often these iteration variables go through a series of numbers

```
[Grafik: Beispiel für while-Schleife]
```

```
[Grafik: Flussdiagramm für while-Schleife]
```

Infinite Loops

- When there is no iteration variable (when the variable never changes, here n)
- The code won't stop running and locks up the computer until the battery of the computer dies

```
[Grafik: Beispiel für eine Endlosschleife]
```

```
[Grafik: Darstellung einer Endlosschleife]
```

- A "zero trip loop" would have a variable so that the code never runs (e.g. n = 0)
  - The loop would be skipped (behaves like an "if-statement")
- **Break statement**
  - Ends the current loop
  - Jumps to the statement immediately following the loop
  - Like a loop test that can happen anywhere in the body of the loop

```
[Grafik: Beispiel für break-Anweisung]
```

```
[Grafik: Weiteres Beispiel für break-Anweisung]
```

```
[Grafik: Flussdiagramm für break-Anweisung]
```

- **Continue statement**
  - Ends the current iteration
  - Jumps to *the top* of the loop and starts the next iteration

```
[Grafik: Beispiel für continue-Anweisung]
```

```
[Grafik: Flussdiagramm für continue-Anweisung]
```

**DEFINITE LOOPS: „FOR-STATEMENTS"**

*"for each of the values in [] have I take on the successive (aufeinanderfolgenden) values and run that loop one time"*

- Have explicit iteration variables that change each time through a loop
  - These iteration variables move through the sequence or set
- List = several values of the same type that are assigned to one variable, the values are in square brackets, e.g. friends (variable) = ["Joseph", "Glenn", "Sally"]
- If there are a few values for one variable (list) the "for" statement runs them one after another
- The *iteration variable* "iterates" through the *sequence* (ordered set)
- The *block (body)* of code is executed once for each value in the *sequence*
- The iteration variable moves through all the values *in* the sequence

```
[Grafik: Beispiel für for-Schleife]
```

```
[Grafik: Flussdiagramm für for-Schleife]
```

```
[Grafik: Weiteres Flussdiagramm für for-Schleife]
```

```
[Grafik: Beispielcode einer for-Schleife]
```

```
[Grafik: Ausführlicher Beispielcode für for-Schleife]
```

- E.g.:
  - "friends" is a list of three strings
  - "friend" is the iteration variable
  - It would be the same outcome if the code was:
- for friend in ["Joseph", "Glenn", "Sally"]:
- print("Happy New Year", friend)
- print("Done!")

**MAKING "SMART" LOOPS**

1. Set some variables to initial values
2. Look for something or do something to each entry separately, updating a variable
3. Look at the variables

- The trick is "knowing" something about the whole loop when you are stuck writing code that only sees one entry at a time
- Finding the largest value
  - We make a variable that contains the largest value we have seen so far
  - If the current number we are looking at is larger, it is the new largest value we have seen so far

```
[Grafik: Flussdiagramm zur Findung des größten Werts]
```

```
[Grafik: Beispielcode zur Findung des größten Werts]
```

**LOOP IDIOMS**

- Countings
  - To count how many times we execute a loop, we introduce a counter variable that starts at 0 and we add one to it each time through the loop

```
[Grafik: Beispielcode für Zählschleife]
```

counter = 0
print("Before: ", counter)
for i in [9, 41, 12, 3, 74, 15]:
    counter = counter + 1
    print(counter, i)
print("After: ", counter)

- Summing
  - To add up a value we encounter in a loop, we introduce a sum variable that starts at 0 and we add the value to the sum each time through the loop

```
[Grafik: Beispielcode für Summenbildung]
```

summing = 0
print("Before: ", summing)
for i in [9, 41, 12, 3, 74, 15]:
    summing = summing + i
    print(summing, i)
print("After: ", summing)

- Finding the Average
  - An average just combines the counting and sum patterns and divides when the loop is done

counter = 0
summing = 0
print("Before: Count: ", counter, ", Sum: ", summing)
for i in [9, 41, 12, 3, 74, 15]:
    counter = counter + 1
    summing = summing + i
    print("Count: ", counter, ", Sum: ", summing, ", Value: ", i)
print("After: Count: ", counter, ", Sum: ", summing, ", Average: ", summing/counter)

```
[Grafik: Ausgabe des Durchschnittsberechnungsprogramms]
```

- Filtering
  - We use an if statement in the loop to catch/filter the values we are looking for

```
[Grafik: Beispielcode für Filterung]
```

print("Before")
for i in [9, 41, 12, 3, 74, 15]:
    if i > 20:
        print ("Large number", i)
print("After")

- Search using a Boolean Variable
  - Boolean Variable: True or False
  - If we just want to search and know if a value was found, we use a variable that starts at False and is set to True as soon as we find what we are looking for

```
[Grafik: Beispielcode für Suche mit Boolean-Variable]
```

found = False
print("Before", found)
for i in [9, 41, 12, 3, 74, 15]:
    if i == 3:
        found = True
    print(found, i)
print("After", found)

- Finding the smallest value
  - We can't define smallest as e.g. -1 or any number so we use "None" do define "smallest" before we run the loope -> "Priming"
  - The first time through the loop, smallest is None, so we take the first value to be the smallest

```
[Grafik: Beispielcode für Suche des kleinsten Werts]
```

smallest = None
print("Before")
for i in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
    print(smallest, i)
print("After: ", smallest)

The „is" and „is not" Operators

- Python has an *is* Operator that can be used in logical expressions
- It implies "is the same as"
- Similar to, but stronger than "=="
- *Is not* also is a logical operator
- We use them for "True", "False" or "None"
- Don't overuse it! Use == instead if possible