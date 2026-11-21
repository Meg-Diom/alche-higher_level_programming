#!/usr/bin/node

/* The process.argv.length - 2 is because the first two elements of
process.argv are used by Node.js */

const numberOfArguments = process.argv.length - 2;

if (numberOfArguments === 0) {
  console.log('No argument');
} else if (numberOfArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
