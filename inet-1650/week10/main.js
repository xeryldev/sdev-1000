// main.js
// ---------------------------------
// Assignment 2
// ---------------------------------
// here i did essentially what was shown on slide 7, 
// and made each function log in the console 'entering'
// and 'exiting'; except for bar, which triggers baz.
function foo() {
  console.log('Entering foo().');
  console.log('Exiting foo().');
}
function bar() {
  console.log('Entering bar().');
  baz(); // once we put baz into the mix, it immediately skips to baz.
}
function baz() {
  console.log('Entering baz().');
  console.log('Exiting baz().');
}

foo(); // we have to call the functions in order for them to do what we want them to,
bar(); // otherwise nothing would happen. Can be an easy mistake!

// ---------------------------------
// Assignment 3
// ---------------------------------

function abc(words, length) {
  // here, i split the string 'words' into an arry of words
  let wordList = words.split(' ');
  
  // then i iterated through the wordList array
  for (let i = 0; i < wordList.length; i++) {
    // now i need it to check to see if the length of the current word
    // is greater than or equal to the specified length.
    if (wordList[i].length >= length) {
      // afterward, i simply output the words that meet this length
      // condition into the console.
      console.log(wordList[i]);
    }
  }
}

let quote = 'Creativity Is Intelligence Having Fun';
abc(quote, 5);

// ---------------------------------
// Assignment 4
// ---------------------------------

let puzzle = 'Gs!kPrAF5tEnA!uan57PtXikd!xThj!Zr';
let puzzleList = puzzle.split("");

// first, we want to loop through the characters provided in puzzleList
for (let i = 0; i < puzzleList.length; i++) {
// then, we check if the current position of i + 1 is evenly divisible by
// 5 with no remainder
  if ((i + 1) % 5 === 0) {
// after that, its as simple as just logging the output in the console
    console.log(puzzleList[i]);
  }
}
// ---------------------------------
// Assignment 5
// ---------------------------------

// here, we define our function with the name 'gP' that takes a single 
// parameter, 'length'
function gP(length) {
  // then we define a string that contains uppercase letters, lowercase 
  // letters, and numbers 0-9 which can be used to generate a password.
  let alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  // here, we initialize an empty string to store the generated password.
  let password = '';
  // next, we split the alphabet string into an array of characters and 
  // store it in 'alphabetList'
  let alphabetList = alphabet.split("");
  // afterward, we check to see if the specified length is greater than the 
  // length of the alphabet string.
  if (length > alphabet.length) {
    // if the length is greater, we set it to the length of the alphabet
    // string to avoid an out-of-bounds error
    length = alphabet.length;
  }
  // now, we use a for loop to generate a password of the specified length 
  // from earlier.
  for(i = 0; i < length; i++) {
    // here, we generate a random position within the length of the alphabet
    // and then store it in 'position'
    position = Math.floor(Math.random() * alphabet.length);
    // then we add the character at the randomly selected position of the 
    // alphabetList array to the password.
    password += alphabetList[position];
  }
  // in our last line for this function, we return the generated password
  return password;
}

// in order for our password to work, we call the gP function with an argument
// to generate 10 characters and store the result in the 'password' variable.
let password = gP(10);
// lastly, we output our generated password into the console.
console.log(password);