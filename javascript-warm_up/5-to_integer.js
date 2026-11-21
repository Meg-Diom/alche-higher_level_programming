#!/usr/bin/node

if (!Number.isNaN(Number(process.argv[2]))) {
  const myNumber = parseInt(process.argv[2]);
  console.log(`My number: ${myNumber}`);
} else {
  console.log('Not a number');
}
