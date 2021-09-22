//JS Lab 1 - Average Numbers
//Class Lemur
//Scott Cormack

let nums = [];
let avg = 0;
let totalNums = prompt("How many numbers do you want averaged? ");
// Loop to get user input
i = 1;
while (i < totalNums) {
  let input = prompt("Enter a number to continue: ");
  nums.push(input);
  i++;
}

let total = 0;
for (let i = 0; i < nums.length; i++) {
  total += nums[i];
}
avg = total / totalNums;

alert(`The average is ${avg}`);
