Why is Redis so fast? There are 3 main reasons as shown in the diagram below.
![image](https://user-images.githubusercontent.com/22426280/229981527-316490d3-5540-4544-be81-e168d7f6c6bd.png)

1. Redis is a RAM-based database. RAM access is at least 1000 times faster than random disk access.

2. Redis leverages IO multiplexing and single-threaded execution loop for execution efficiency.

3. Redis leverages several efficient lower-level data structures.

