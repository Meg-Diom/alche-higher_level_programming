#!/usr/bin/node

const myVar = process.argv[2];
if (!myVar) {
  console.log('Missing size');
} else {
  const number = parseInt(myVar);
  for (let i = 1; i <= number; i++) {
    let row = '';
    for (let j = 0; j < number; j++) {
      row += 'x';
    }
    console.log(row);
  }
}
