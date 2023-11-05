let firstName = 'Steven'
let lastName = 'Cooper'
let fullName = firstName + ' ' + lastName
console.log(fullName)
let answer = document.getElementById('answer');
let button = document.getElementById('showAnswer');
button.addEventListener("click", function() {
  answer.style.display = 'block';
  button.style.display = 'none';
});