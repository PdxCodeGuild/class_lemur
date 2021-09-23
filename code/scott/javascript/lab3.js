//JS Lab 2 - Credit Card Validation
//Class Lemur
//Scott Cormack

//Input and change to an integer array
let intList = prompt(
  "Input 16 digit credit card number to validate (ex 1234567890123456): "
)
  .split("")
  .map((i) => {
    return parseInt(i, 10);
  });

console.log(intList);

//take the last digit for a check number
chkNum = intList.pop();
console.log(chkNum);
//reverse order of digits in array
intList.reverse();
console.log(intList);
//double every other number in array
for (let i = 0; i < intList.length; i++) {
  if (i % 2 === 0) {
    intList[i] = intList[i] * 2;
  }
}
console.log(intList);
//subtract 9 from all numbers over 9
for (let i = 0; i < intList.length; i++) {
  if (intList[i] > 9) {
    intList[i] = intList[i] - 9;
  }
}
console.log(intList);
//sum all values
total = intList.reduce(function (a, b) {
  return a + b;
}, 0);
console.log(total);

//check if last digit of sum and check number
function isValid(a, b) {
  if (a % 10 === b) {
    return true;
  } else return false;
}

let valid = isValid(total, chkNum);

console.log(valid);
if (valid == true) {
  alert("Your credit card number is valid");
} else alert("Your credit card number is not valid");
