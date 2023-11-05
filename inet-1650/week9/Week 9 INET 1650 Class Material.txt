// Excercises
// #1: Create an array that contains the numbers 8, 3, 9, 5, 6 called numbers.

// #2: Write to the console the value at index 2 in numbers.


// #3: What would the console.log statement be if we wanted to display the value 5 from
//     the numbers array?


// #4: Add the numbers 19 and 11 to the array.


// #5: Create an array called words that contains the following words:
//     (hint: these are strings so use quotes)
// Shenanigans, Bamboozle, Bodacious, Brouhaha, Canoodle, Gnarly, 
// Goggle, Gubbins, Malarkey, Nincompoop


// #6: Using a for loop, write each word to the console.  The only statement
//     in the for loop body will be your console.log statement


// #7: Change the following code to add each word from the array sports to the web page.  Each
//     word should be contained in an H3 element.
let sports = ['Football', 'Tennis', 'Basketball', 'Biking', 'Baseball', 'Running'];
for (let i = 0; i<sports.length; i++) {
  let element = document.createElement('p');
  element.innerHTML = sports[i];
  document.getElementById('list1').append(element);
}

// #8: Change the color of the list items in sports2 to blue that have more
//     than 6 characters. Strings have a property called length too.
let sports2 = ['Swimming', 'Hockey', 'Volleyball', 'Skiing'];
let element = document.createElement('ul');
for (let i = 0; i<sports2.length; i++) {
  let listItem = document.createElement('li');
  listItem.innerHTML = sports2[i];
  listItem.style = 'color: red';
  element.append(listItem);
}
document.getElementById('list2').append(element);

// #9: Create an ordered list (<ol>) of grades and then write 
//     the total of all the grades after the list. Ordered doesn't mean 
//     list them in order, it means you are using an HTML ordered list.
//     Grades are: 89, 72, 95, 77, 88, 90, 99, 89, 86
//     Display these in the div element with id value list3.
