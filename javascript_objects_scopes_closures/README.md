# JavaScript - Objects, Scopes and Closures

This project introduces important JavaScript concepts related to **objects, scopes, closures, prototypes, and inheritance**.

## Learning Objectives

By completing this project, I should be able to explain:

- Why JavaScript programming is amazing
- How to create an object in JavaScript
- The difference between a class and an object
- How to use `this` in JavaScript
- What `undefined` means
- Why variables cannot be changed or modified
- What variable types and scopes exist in JavaScript
- What a closure is
- What a prototype is
- How to inherit an object from another object
- How to use `class` in JavaScript

## Requirements

- Ubuntu/Linux environment
- Node.js
- JavaScript files using the Node.js interpreter
- Semistandard for code style
- No `var` keyword

## General Instructions

Each JavaScript file should:

- Start with the Node.js shebang:

```javascript
#!/usr/bin/node
```

- Use `const` or `let` instead of `var`
- Follow Semistandard coding style
- Be executable when required

For example:

```bash
chmod +x filename.js
```

The script can then be executed with:

```bash
./filename.js
```

## Project Structure

The project contains JavaScript exercises covering objects, scopes, closures, prototypes, and classes.

| File | Topic |
|---|---|
| `0-rectangle.js` | Creating a class |
| `1-rectangle.js` | Class constructor |
| `2-rectangle.js` | Class methods |
| `3-rectangle.js` | Object properties and validation |
| `4-rectangle.js` | Additional class methods |
| `5-square.js` | Inheritance |
| `6-square.js` | Extending a class |
| `7-occurrences.js` | Working with objects |
| `8-esrever.js` | Closures |
| `9-logme.js` | Closures and function execution |
| `10-converter.js` | Closures and conversion |
| `100-map.js` | Array methods and callbacks |
| `101-sorted.js` | Sorting and objects |
| `102-concat.js` | Concatenating arguments |

> The exact files may vary depending on the exercises included in the project.

## Important Concepts

### Objects

An object stores data as **key-value pairs**.

```javascript
const student = {
  name: 'Sokka',
  age: 18,
  course: 'Computer Science'
};
```

Properties can be accessed using dot notation:

```javascript
console.log(student.name);
```

Or bracket notation:

```javascript
console.log(student['name']);
```

### `this`

The `this` keyword refers to the object associated with the current function call.

For example:

```javascript
const student = {
  name: 'Sokka',

  introduce () {
    console.log(`My name is ${this.name}`);
  }
};

student.introduce();
```

Output:

```text
My name is Sokka
```

### Scope

Scope determines where a variable can be accessed.

JavaScript has several important types of scope, including:

- Global scope
- Function scope
- Block scope

Variables declared with `let` and `const` are block-scoped.

```javascript
if (true) {
  const message = 'Hello';
  console.log(message);
}
```

The variable `message` cannot be accessed outside the block.

### Closures

A closure occurs when a function remembers and can access variables from its surrounding scope even after the outer function has finished executing.

Example:

```javascript
function createCounter () {
  let count = 0;

  return function () {
    count++;
    return count;
  };
}

const counter = createCounter();

console.log(counter());
console.log(counter());
```

Output:

```text
1
2
```

The inner function continues to access `count`.

### Prototypes

JavaScript objects can inherit properties and methods from another object through the **prototype chain**.

This allows objects to share behavior without every object needing its own copy of a method.

### Classes

A class provides a structure for creating objects.

```javascript
class Student {
  constructor (name, age) {
    this.name = name;
    this.age = age;
  }

  introduce () {
    console.log(`My name is ${this.name}`);
  }
}
```

An object can then be created from the class:

```javascript
const student = new Student('Sokka', 18);
student.introduce();
```

## Running the Code

Make a JavaScript file executable:

```bash
chmod +x filename.js
```

Run it:

```bash
./filename.js
```

You can also run it directly with Node.js:

```bash
node filename.js
```

## Checking Code Style

Semistandard can be used to check the JavaScript files:

```bash
npx semistandard
```

To check a specific file:

```bash
npx semistandard filename.js
```

If there are style errors, Semistandard will indicate the file, line, and problem.

## Example

A simple object:

```javascript
#!/usr/bin/node

const student = {
  name: 'Sokka',
  age: 18,
  course: 'Computer Science'
};

console.log(student);
console.log(student.name);
```

Output:

```text
{ name: 'Sokka', age: 18, course: 'Computer Science' }
Sokka
```

## Key Takeaways

The main concepts covered in this project are:

1. Objects store related data and behavior.
2. `this` refers to the relevant object depending on how a function is called.
3. Scope controls where variables can be accessed.
4. `const` prevents reassignment of a variable, but objects declared with `const` can still have their properties modified.
5. Closures allow functions to remember variables from their surrounding scope.
6. Prototypes allow objects to inherit properties and methods.
7. Classes provide a convenient way to create objects with shared behavior.
8. JavaScript uses a prototype-based inheritance system underneath its class syntax.
