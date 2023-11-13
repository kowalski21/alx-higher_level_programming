#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing x');
} else {
  for (let r = 0; r < x; r++) {
    let raid = '';
    for (let c = 0; c < x; c++) raid += 'X';
    console.log(raid);
  }
}
