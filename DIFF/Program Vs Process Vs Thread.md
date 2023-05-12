## PROGRAM VS PROCESS VS THREAD

#### PROGRAM
A __program__ is an executable file which consists of a set of instructions to perform some task and is usually stored on the disk of your computer.

#### PROCESS
A __process__ is what we call a program that has been loaded into memory along with all the resources it needs to operate. It has its __own memory space__.

#### THREAD
A __thread__ is the unit of execution within a process. A process can have __multiple threads__ running as a part of it, where each thread uses the __process’s memory space__ and shares it with other threads.


## Multithreading
It is a technique where multiple threads are spawned by a process to do different tasks, at about the same time, just one after the other. This gives you the illusion that the threads are running in parallel, but they are actually run in a concurrent manner. In Python, the Global Interpreter Lock (GIL) prevents the threads from running simultaneously.

## Multiprocessing -:
It is a technique where parallelism in its truest form is achieved. Multiple processes are run across multiple CPU cores, which do not share the resources among them. Each process can have many threads running in its own memory space. In Python, each process has its own instance of Python interpreter doing the job of executing the instructions.
