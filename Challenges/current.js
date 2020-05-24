// version 1 was the way to go

function maxTotal(nums) {
  console.log(nums);
  var fiveLargest = nums.sort().splice(5, 10);
  return fiveLargest.reduce(function (a, b) {
    return a + b;
  });
}
//v2 fail

function maxTotal(nums) {
  largest = [];
  notLargest = [];
  nums.map((num) => {
    if (num < 0 && notLargest.length < 5) {
      notLargest.push(num);
    } else if (largest.length < 5) {
      largest.push(num);
    } else {
      notLargest.push(num);
    }
  });
  console.log("l", largest);
  console.log("nl", notLargest);
  return notLargest.reduce(function (a, b) {
    return a + b;
  });
}

//v3 fail
function maxTotal(nums) {
  console.log(nums);
  var fiveL = nums.sort();
  for (i = fiveL.length - 1; i >= 5; i--) {
    if (fiveL[i] < 0) {
      fiveL.pop(fiveL[i]);
    }
  }
  console.log(fiveL.sort());
  return fiveL
    .sort()
    .splice(5, 10)
    .reduce(function (a, b) {
      return a + b;
    });
}
