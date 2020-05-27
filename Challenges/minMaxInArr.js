function minMax(arr) {
  console.log(arr);
  max = arr[0];
  min = arr[1];
  for (var i = 0; i < arr.length; i++) {
    console.log(arr[i]);
    if (arr[i] < min) {
      min = arr[i];
    } else if (arr[i] > max) {
      max = arr[i];
    }
  }
  return [min, max];
}

console.log(minMax([14, 35, 6, 1, 34, 54]));
console.log(minMax([1.346, 1.6532, 1.8734, 1.8723]));
