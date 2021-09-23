//JS Lab 2 - Make Change
//Class Lemur
//Scott Cormack

//VERSION 1
// let amt = parseFloat(
//   prompt("input a dollar amount that you wish to calculate:")
// );
// let ttlCents = parseInt(amt * 100);

// quarters = Math.floor(ttlCents / 25);
// dimes = Math.floor((ttlCents % 25) / 10);
// nickels = Math.floor(((ttlCents % 25) % 10) / 5);
// pennies = Math.floor(ttlCents % 5);

// alert(
//   `Change for ${amt} is: ${quarters} quarters, ${dimes} dimes, ${nickels} and ${pennies}.`
// );

//VERSION 2
form = document.querySelector("form");

form.addEventListener("submit", function (evt) {
  evt.preventDefault();
  const totalInput = parseFloat(document.getElementById("totalInput").value);
  const ttlCents = parseInt(totalInput * 100);

  quarters = Math.floor(ttlCents / 25);
  dimes = Math.floor((ttlCents % 25) / 10);
  nickels = Math.floor(((ttlCents % 25) % 10) / 5);
  pennies = Math.floor(ttlCents % 5);

  const result = document.getElementById('result')
  result.innerText = `The total amount of change for ${totalInput} is:\nQuarters: ${quarters}\nDimes: ${dimes}\nNickels: ${nickels}\nPennies: ${pennies}`
});
