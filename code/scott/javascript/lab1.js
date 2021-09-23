//JS Lab 1 - Average Numbers
//Class Lemur
//Scott Cormack

//VERSION 1
// let nums = [];
// let avg = 0;
// let totalNums = prompt("How many numbers do you want averaged? ");
// // Loop to get user input
// i = 1;
// while (i < totalNums) {
//   let input = prompt("Enter a number to continue: ");
//   nums.push(input);
//   i++;
// }

// let total = 0;
// for (let i = 0; i < nums.length; i++) {
//   total += nums[i];
// }
// avg = total / totalNums;

// alert(`The average is ${avg}`);

//VERSION 2
const form = document.querySelector("form");
const totalOut = document.getElementById("result");
form.addEventListener("submit", function (evt) {
  evt.preventDefault();
  let total = 0;
  let numInput = document.getElementById("numInput").value;
  const numArr = numInput.split(",");
  for (let i = 0; i < numArr.length; i++) {
    total += +numArr[i];
  }
  console.log(total);
  let avg = total / numArr.length;
  totalOut.innerText = `The average value of your numbers is ${avg}.`;
});