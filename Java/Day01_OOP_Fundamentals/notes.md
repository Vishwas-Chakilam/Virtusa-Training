# Day 1: OOP Fundamentals

## Introduction to Object-Oriented Programming (OOP)
Object-Oriented Programming is a paradigm that organizes software design around data, or objects, rather than functions and logic. It focuses on the objects that developers want to manipulate rather than the logic required to manipulate them.

### Core Concepts:
1. **Class**: A blueprint or prototype from which objects are created. It dictates what methods and variables an object will have.
2. **Object**: A runtime instance of a class. It contains state (fields) and behavior (methods).
3. **Encapsulation**: Hiding the internal state and requiring all interaction to be performed through an object's methods. Keep fields `private` and provide `public` getters/setters.
4. **Inheritance**: A mechanism by which one object acquires all the properties and behaviors of a parent object. Used for code reusability.
5. **Polymorphism**: The ability of an object to take on many forms. Most commonly used when a parent class reference is used to refer to a child class object.
6. **Abstraction**: Hiding complex implementation details and showing only the essential features of the object.

## Best Practices
- Always favor composition over inheritance where possible.
- Use meaningful class names (PascalCase).
- Keep classes focused on a single responsibility (Single Responsibility Principle).
