function isValidPick(pick) {
    if (pick == 'rock' || pick == 'paper' || pick == 'scissors') {
    return true;
  }
  else {
    return false;
  }
}

function winner(computerPick, userPick) {
  let result = 'unknown';

  if (!isValidPick(computerPick) || !isValidPick(userPick)) {
    return result;
  } 

  if (computerPick == userPick) {
    result = 'tie';
  }

  if ((computerPick == 'rock' && userPick == 'scissors')
     || (computerPick == 'scissors' && userPick == 'paper')
     || (computerPick == 'paper' && userPick == 'rock')) {
    result = 'computer, you lose! :(';
  }
  else {
    result = 'user, you win! :)';
  }
  
  if (computerPick == userPick) {
    result = 'tie!!!';
  }
  
  return result;
}

function rps() {
  console.log('In the function rps.');
  let userChoice = prompt("Enter rock, paper, or scissors");

  let randomNumber = Math.floor(Math.random() * 3) + 1;
  let computerChoice = 'scissors';
  if (randomNumber == 1) {
    computerChoice = 'rock';
  }
  else if (randomNumber == 2) {
    computerChoice = 'paper';
  }
  
  console.log('User picked ' + userChoice + ', Computer picked ' + computerChoice);
  theWinner = winner(computerChoice,userChoice);
  console.log('Winner is: ' + theWinner)
}

rps();