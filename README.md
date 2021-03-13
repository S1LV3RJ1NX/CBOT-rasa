# CBOT
A Chatbot made using the RASA Conversational AI to solve user queries related to C language.

The Chatbot is designed so that it can answer the Basic queries related to C through it's trained NLU Data.
It can answer queries related to:
* Programming
* Information of C Language
* The Data Types used in C: Integer, Float, Char and Void
* The Ranges of different Data Types
* Variables and their declaration
* Conditions in C
* Loops in C: for, while, do while
* Other Info related to Loops: break, continue
* The Errors in C and their classification: 
    * Runtime 
    * Syntax
    * Linker
    * Logical
    * Semantic
* Reserved Words in C
* Identifiers
* Switch Case
* Operators
* Types of Operators and their Information: 
    * Arithmetic
    * Logical
    * Bitwise
    * Relational
    * Assignment
    * Conditional
    * Special
* Features of C

Apart from this basic information, the Bot has the ability to search for necessary information out of it's scope.
The Bot uses Stackoverflow API to search for the User Queries whenever it has to give the User more information
on the subject or when, the Queries are out of scope of the training data.
Thus, ensures the scope of Queries being answered to a higher extent.
