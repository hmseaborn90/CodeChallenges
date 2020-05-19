function FindIntersection(input) {

  const [firstList, secondList] = input.map(s => s.split(", "));

  const resultMap = {};
  const result = [];

  for (const number of firstList) {
    resultMap[number] = true;
  }

  for (const number of secondList) {
    if (resultMap[number]) {
      result.push(number);
    }
  }

  return result.length ? result.join(",") : false;
}

test = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
// keep this function call here 
console.log(FindIntersection(test))

