# Day 21: JVM Internals

## JVM Architecture
JVM (Java Virtual Machine) is an abstract machine. It is a specification that provides a runtime environment in which Java bytecode can be executed.

### Core Components
1. **Classloader**: A subsystem of JVM that loads class files. It verifies, prepares, and resolves classes. (Bootstrap, Extension, System/Application ClassLoaders).
2. **Runtime Data Areas**:
   - **Method Area**: Stores class level data (methods, variables).
   - **Heap Area**: Objects and their instance variables are stored here.
   - **Stack Area**: Stores frames (local variables and method calls). Thread-safe.
   - **PC Register**: Holds the JVM instruction currently being executed.
   - **Native Method Stack**: Stores native methods used in the application.
3. **Execution Engine**:
   - **Interpreter**: Reads bytecode stream and executes instructions.
   - **JIT Compiler**: Just-In-Time compiler improves performance by compiling bytecode into native machine code at runtime.
   - **Garbage Collector**: Clears unreferenced objects.
