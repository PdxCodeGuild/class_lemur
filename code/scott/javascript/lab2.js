//JS Lab 2 - Make Change
//Class Lemur
//Scott Cormack

let amt = parseFloat(
  prompt("input a dollar amount that you wish to calculate:")
);
let ttlCents = parseInt(amt * 100);

quarters = Math.floor(ttlCents / 25);
dimes = Math.floor((ttlCents % 25) / 10);
nickels = Math.floor(((ttlCents % 25) % 10) / 5);
pennies = Math.floor(ttlCents % 5);

alert(
  `Change for ${amt} is: ${quarters} quarters, ${dimes} dimes, ${nickels} and ${pennies}.`
);
