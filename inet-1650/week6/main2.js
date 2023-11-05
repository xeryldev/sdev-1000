let userNumber = prompt('Enter a number:')
let remainder = userNumber % 2;

if (remainder == 0) {
  console.log(userNumber + ' is even.');
}
else {
  console.log(userNumber+ ' is odd.');
}