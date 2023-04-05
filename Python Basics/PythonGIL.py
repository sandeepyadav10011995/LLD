"""
* GIL ( Global Interpreter Lock) -: The GIL is an interpreter-level lock.
This lock prevents execution of multiple threads at once in the Python interpreter.
Each thread that wants to run must wait for the GIL to be released by the other thread, which means your multi-threaded
Python application is actually single threaded. The GIL prevents simultaneous access to Python objects by multiple
threads.


* "if we have the GIL, and a thread must own it to execute within the interpreter, who decides if the GIL should be
released and when?" -: The answer is byte code instructions.

When a Python application is executed, it is compiled to byte code, the actual instructions that the interpreter uses
for execution of the application. Normally, byte code files end with a name like "pyc" or "pyo".
A given line of a Python application might be a single byte code, while others, such as an import statement, may
ultimately expand into many byte code instructions for the interpreter.
The Python interpreter (for pure Python code) will force the GIL to be released every hundred byte code instructions.


* multiprocessing not multithreading will allow you to achieve true concurrency
Coming back to main discussion, the fact is, the GIL does prevent you as a programmer from using multiple CPUs
simultaneously. Python as a language, however, does not. To be noted that the GIL does not prevent a process from
running on a different processor of a machine. It simply only allows one thread to run at once within the interpreter.
So multiprocessing not multithreading will allow you to achieve true concurrency.
"""
