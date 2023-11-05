// #1: Create an array that contains the numbers 8, 3, 9, 5, 6 called numbers.
let numbers = [8, 3, 9, 5, 6];
console.log('My array called numbers:', numbers);

// #2: Write to the console the value at index 2 in numbers.
console.log('Value at index 2:', numbers[2]);

// #3: What would the console.log statement be if we wanted to display the value 5 from
// the numbers array?
console.log('Value 5 from the array:', numbers[3]);

// #4: Add the numbers 19 and 11 to the array.
numbers.push(19, 11);
console.log('Updated numbers array:', numbers);

// #5: Create an array called words that contains the following words:
//     (hint: these are strings so use quotes)
// Shenanigans, Bamboozle, Bodacious, Brouhaha, Canoodle, Gnarly, 
// Goggle, Gubbins, Malarkey, Nincompoop:
let words = ['Shenanigans', 'Bamboozle', 'Bodacious', 'Brouhaha', 'Canoodle', 'Gnarly', 'Goggle', 'Gubbins', 'Malarkey', 'Nincompoop'];

// #6: Using a for loop, write each word to the console.  The only statement
//     in the for loop body will be your console.log statement
for (let i = 0; i < words.length; i++) {
  console.log(words[i]);
}

// #7: Change the following code to add each word from the array sports to the web page.  Each
//     word should be contained in an H3 element.
let sports = ['Football', 'Tennis', 'Basketball', 'Biking', 'Baseball', 'Running'];
for (let i = 0; i < sports.length; i++) {
  let element = document.createElement('h3'); // Change 'p' to 'h3' to create H3 elements.
  element.innerHTML = sports[i];
  document.getElementById('list1').appendChild(element);
}

// #8: Change the color of the list items in sports2 to blue that have more
//     than 6 characters. Strings have a property called length too.
let sports2 = ['Swimming', 'Hockey', 'Volleyball', 'Skiing'];
let list2 = document.getElementById('list2');
let ul = document.createElement('ul');
for (let i = 0; i < sports2.length; i++) {
  let listItem = document.createElement('li');
  listItem.innerHTML = sports2[i];
  if (sports2[i].length > 6) {
    listItem.style.color = 'blue';
  }
  ul.appendChild(listItem);
}
list2.appendChild(ul);

// #9: Create an ordered list (<ol>) of grades and then write 
//     the total of all the grades after the list. Ordered doesn't mean 
//     list them in order, it means you are using an HTML ordered list.
//     Grades are: 89, 72, 95, 77, 88, 90, 99, 89, 86
//     Display these in the div element with id value list3.
let grades = [89, 72, 95, 77, 88, 90, 99, 89, 86];
let list3 = document.getElementById('list3');
let ol = document.createElement('ol');
let total = 0;
for (let i = 0; i < grades.length; i++) {
  let li = document.createElement('li');
  li.innerHTML = grades[i];
  ol.appendChild(li);
  total += grades[i];
}
list3.appendChild(ol);
let totalElement = document.createElement('p');
totalElement.innerHTML = 'Total: ' + total;
list3.appendChild(totalElement);