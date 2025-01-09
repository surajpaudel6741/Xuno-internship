# Day-1 XUNO - Internship
 
## Understanding programming basics


### Software Programming

- WEB:
Web basics starts with HTML, CSS and JAVASCRIPT, keeping the base foundation of these technologies. Many frameworks and libraries are created to make web development more efficient and optimized.There are two major parts in web i.e front end and back end. Frontend relies on design, UI/UX and visual components while backend handles server side, database, APIs (JAVA, Python,  NodeJS, PHP).

- APP:
App programming can be for IOS and android. Swift is the language used in making IOS apps natively while in android java and kotlin are used natively. Flutter, based on dart programming language and React Native is used as a hybrid (suitable for both android and ios).

- Server:
Server programming runs on a server dealing with the contents on the web, like updating data, automations etc. Some of the server side languages are.
JAVA: Due to its multithreading functionality it can load huge and complex data. It supports cross platform. Frameworks:Spring Boot, Java EE.
Usecases: Enterprise level, Large scale.


- PHP: As it was formed for server side programming and is very traditional and old, its community is very large. And the best thing about PHP is it is open source, you can modify it on your own, as per your needs. Frameworks: Laravel. Usecases: Large scale projects


- Python: Quick and easy to learn and implement. Has vast libraries and tools for AI and automation. Frameworks: Django, Flask. Usecases: Automation and AI integrated sites


- Javascript (Node-js): As being a client side scripting language with the help of node. It is considered as one of the popular languages for server side programming with trending tech stack like MERN. It is easier to learn as the JAVASCRIPT is used and is better for small scale and faster projects.


### Data Types:
Represents the type and properties of value the variable has.
- INT:Integer [2/4 Bytes]
- Char: Characters [1 Byte ]
- Float: decimal [8 Byte]
- Short: short integer [2 Byte]
- String: Array of char

### Unsigned data types:
Positive and large numbers than signed data types. Used where the whole numbers or non negative numbers are needed like iterations, data counting etc’

### Signed data types:
Negative and positive numbers and quite smaller in range than unsigned data types. Used where the values can be represented in both negative and positive. Eg Debt tracker, Balance tracer

### Mutable and Immutable
Mutable refers to changeable data type and Immutable refers to unchangeable data types.

| Mutable       | Immutable |
| --------      | -------   |
| Dictionary    | Integer   |
| List          | String    |
| Set           | Char      |
| Arraylist     | Short     |
| StringBuilder |           |

Similarly many more are there as per different programming languages. But the question arises how they are immutable. As when we assign a value lets say,
`int a = 10;`
Here 10 is kept in heap memory and a is kept in stack memory and a points towards 10. When we assign value to 11 then the object is not changed just the variable points towards the 11 in heap memory.

### ASCII and UTF encoding
For every character the number is assigned which was introduced by ASCII which stands for American Standard Code for Information Interchange, which enables a common language for data exchange. Firstly it ranged from 0-128 but later it was extended to 128-255. Making it suitable for punctuations, space and characters.

Whereas UTF-8 is ascii updated version, as ascii store 1 character in 1 byte, same UTF-8 also follows but if it need 2 bytes then it can store it in 2 bytes also, it works as per needed and overshadowing ASCII it is used world wide now a days. There is UTF- 16 and UTF 32 also which represent 16 and 32 bits, UTF-16 is used by JAVA as its character encoding which uses 2 bytes. 


### Errors in programming
There is two types of error majorly

Compile time error:
This type of error is generated during compile time, indicating what we need to fix before compiling. It represents a Syntax error and Semantic Error. 

Run time error:
This type of error is given after the compiled file is run for an output. This type of error include:
Arithmetic Error
Uninitialized Variable
Stack overflow and Array out of bound
Null pointer dereference

### Compiler and Interpreter
They both convert the high level code into binary or machine level code. But their way of converting is very different. Compiler first converts the code into object and runs it for the output, So in this compiling steps it analyzes the code at once unlike interpreter it checks the code line by line, during analyzing it gives error if any. But in the case of an interpreter it does not need to convert the code to object code as it runs the code line by line and if any error is found it stops there. With these findings we can say that interpreters are memory efficient and analyzing is faster. But the compiler executes the code faster.

- Interpreter: Python, Javascript
- Compiler: Java, C, C++ 

### Memory Management:
Computer memory works as two parts Heap and Stack, and they store program’s Objects and References. 
When we use 
`int a = 4;`
a is a reference for a memory address where 4 is stored. And 4 is stored in the head while a is stored in the stack. In c and c++ there is manual memory management where we on our own have to assign memory and free it, it is done with the help of pointers and functions like malloc, realloc etc.

While in Java and Python the memory management is done automatically with the help of Garbage collector. Which use reference count and reference mark technique to automatically free the space.



