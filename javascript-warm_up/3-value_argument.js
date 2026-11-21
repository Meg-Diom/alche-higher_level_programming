#!/usr/bin/node

const numberOfArguments = process.argv.length - 2;

if (numberOfArguments === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
