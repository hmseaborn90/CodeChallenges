function maxTotal(nums) {
  console.log(nums);
  var fiveLargest = nums.sort().splice(5, 10);
  return fiveLargest.reduce(function (a, b) {
    return a + b;
  });
}
