#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  let biggest = -Infinity;
  let secondBiggest = -Infinity;

  for (const number of args) {
    if (number > biggest) {
      secondBiggest = biggest;
      biggest = number;
    } else if (number > secondBiggest && number < biggest) {
      secondBiggest = number;
    }
  }

  console.log(secondBiggest);
}
