# CS117-lab3
All material regarding lab 04 of Applications of ICT is here.


Assembly Reflections:
1. Registers are small, high-speed storage locations within the CPU essential for quick data access, while instructions are the commands that operate on data, often stored in these registers.
2. Assembly is a low level computer language whereas Python is a high level language. Coding is much easier in python as it is understable to humans as compared with assembly language.



Python Reflections:
1. Python utilizes a more human-readable syntax with keywords, functions, and object-oriented features, that is why python is easier and faster than assembly language.
2. Assembly requires developers to manage each and every detail whereas Python , being a high level language handles most of these details automatically.


Comparison Table
  | Feature | Assembly Example | Python Example | Notes |
  |---------|------------------|----------------|-------|
  |Variable storage|mov eax| x=5 | Assembly stores directly into registers(low-level), while python uses variables in memory(high-level) |
  |Printing Output|int 0x80 mov eax, 1| print()| assembly requires system calls, python has built in features|
  |Arithmetic|add ax, bx | x+y | Assembly operates on registers directly. Python handles expressions symbolically|
