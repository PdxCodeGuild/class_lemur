//JS Lab 2 - Credit Card Validation
//Class Lemur
//Scott Cormack

//VERSION 1
// //Input and change to an integer array
// let intList = prompt(
//   "Input 16 digit credit card number to validate (ex 1234567890123456): "
// )
//   .split("")
//   .map((i) => {
//     return parseInt(i, 10);
//   });

// console.log(intList);

// //take the last digit for a check number
// const chkNum = intList.pop();
// console.log(chkNum);
// //reverse order of digits in array
// intList.reverse();
// console.log(intList);
// //double every other number in array
// for (let i = 0; i < intList.length; i++) {
//   if (i % 2 === 0) {
//     intList[i] = intList[i] * 2;
//   }
// }
// console.log(intList);
// //subtract 9 from all numbers over 9
// for (let i = 0; i < intList.length; i++) {
//   if (intList[i] > 9) {
//     intList[i] = intList[i] - 9;
//   }
// }
// console.log(intList);
// //sum all values
// total = intList.reduce(function (a, b) {
//   return a + b;
// }, 0);
// console.log(total);

// //check if last digit of sum and check number
// function isValid(a, b) {
//   if (a % 10 === b) {
//     return true;
//   } else return false;
// }

// let valid = isValid(total, chkNum);

// console.log(valid);
// if (valid == true) {
//   alert("Your credit card number is valid");
// } else alert("Your credit card number is not valid");

//VERSION 2
const form = document.querySelector("form");

//Gather information from user and turn into a list of numbers
form.addEventListener("submit", function (evt) {
  evt.preventDefault();
  const ccNum = document
    .getElementById("ccNum")
    .value.split("")
    .map((i) => {
      return parseInt(i, 10);
    });
  //Pull the last number off as the check number
  const chkNum = ccNum.pop();
  //Reverse the order of remaining CC numbers
  ccNum.reverse();
  //Double every other number
  for (let i = 0; i < ccNum.length; i++) {
    if (i % 2 === 0) {
      ccNum[i] = ccNum[i] * 2;
    }
  }
  //Subtract 9 from every number over 9
  for (let i = 0; i < ccNum.length; i++) {
    if (ccNum[i] > 9) {
      ccNum[i] = ccNum[i] - 9;
    }
  }
  //sum all values
  const total = ccNum.reduce(function (a, b) {
    return a + b;
  }, 0);
  //check if last digit of sum and check number
  function isValid(a, b) {
    if (a % 10 === b) {
      return true;
    } else return false;
  }
  //Post results
  const valid = isValid(total, chkNum);
  const result = document.getElementById("result");
  if (valid == true) {
    result.innerText = "Your credit card is valid";
  } else result.innerText = "Your credit card is NOT valid";
});
