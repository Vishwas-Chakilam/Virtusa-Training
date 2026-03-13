# Day 13: Java 8 Features

Java 8 brought major paradigm shifts to the Java ecosystem, notably introducing functional programming paradigms.

## 1. Lambda Expressions
Lambda expressions basically express instances of functional interfaces. They provide a clear and concise way to represent one method interface using an expression.
Syntax: `(argument-list) -> {body}`

## 2. Functional Interfaces
An interface with exactly one abstract method. Examples: `Runnable`, `Callable`, `Comparator`.
Annotated with `@FunctionalInterface`.

## 3. Stream API
Streams act as a wrapper around a data source, allowing us to operate with that data source and making bulk processing convenient and fast.
Operations:
- **Intermediate**: `filter`, `map`, `sorted` (Returns stream)
- **Terminal**: `forEach`, `collect`, `reduce` (Returns definite result)

## 4. Optional Class
Introduced to prevent `NullPointerException`s gracefully.
