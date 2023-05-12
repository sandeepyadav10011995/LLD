## PROGRAM VS PROCESS VS THREAD

#### PROGRAM
A __program__ is an executable file which consists of a set of instructions to perform some task and is usually stored on the disk of your computer.

#### PROCESS
A __process__ is what we call a program that has been loaded into memory along with all the resources it needs to operate. It has its __own memory space__.

#### THREAD
A __thread__ is the unit of execution within a process. A process can have __multiple threads__ running as a part of it, where each thread uses the __process’s memory space__ and shares it with other threads.


#### Analogy
* __Program__: Imagine a program as a set of instructions written by a person. It's like a recipe for making a cake. The program tells the computer what tasks to perform and how to do them. It's a bunch of code that can be saved on a computer's storage, like a file. However, a program by itself doesn't do anything. It's just a set of instructions waiting to be executed.

* __Process__: A process is like a running instance of a program. Going back to the cake analogy, if a program is the recipe, a process is like actually making the cake according to that recipe. When you run a program, it creates a process in the computer's memory. The process has its own space to work and carries out the instructions of the program. Each process is separate from others, just like baking two cakes in two separate kitchens.

* __Thread__: Now, think of a thread as a small unit of work within a process. If a process is making a cake, a thread is like one person doing a specific task in the process. For example, one person might be mixing the ingredients, another person might be decorating the cake, and so on. Threads allow different parts of a process to work concurrently, which means they can perform tasks at the same time. It's like teamwork within a process, where each thread handles a specific job.

* To summarize, a program is a set of instructions, a process is an instance of a running program, and a thread is a unit of work within a process that helps accomplish tasks concurrently. Programs are like recipes, processes are like executing those recipes, and threads are like individual workers performing specific tasks within the execution process.

## Multithreading
It is a technique where multiple threads are spawned by a process to do different tasks, at about the same time, just one after the other. This gives you the illusion that the threads are running in parallel, but they are actually run in a concurrent manner. In Python, the Global Interpreter Lock (GIL) prevents the threads from running simultaneously.

## Multiprocessing -:
It is a technique where parallelism in its truest form is achieved. Multiple processes are run across multiple CPU cores, which do not share the resources among them. Each process can have many threads running in its own memory space. In Python, each process has its own instance of Python interpreter doing the job of executing the instructions.

#### Analogy
* Imagine you have a big homework assignment, and you want to finish it as quickly as possible. You have two options: either you can work on the assignment by yourself, or you can ask some friends to help you.

* __Multithreading__: Multithreading is like you working on the assignment with the help of your friends. Each friend takes a different part of the assignment and works on it simultaneously. For example, one friend might focus on math questions, another friend might handle the science questions, and so on. You divide the work among your friends, and everyone works together at the same time. This way, you can make progress faster since multiple tasks are being done concurrently.

* __Multiprocessing__: On the other hand, multiprocessing is like you and your friends each working on separate copies of the same assignment. Instead of dividing the tasks, you make multiple copies of the assignment, and you and your friends work on them independently. Each person has their own set of questions to solve. Once everyone finishes their respective assignments, you come together to combine the results. This way, you can finish the assignment faster because each person is working on a separate task independently.

* To summarize, multithreading is like working on different parts of a task simultaneously with the help of others, while multiprocessing is like working on separate copies of the same task independently and combining the results later. In multithreading, everyone cooperates and works together on the same assignment, while in multiprocessing, everyone works on separate assignments and combines the outcomes afterward.
