function specialReverse(s, c) {
  output = [];
  let splitString = s.split(" ");
  splitString.map((word) => {
    if (word[0] === c) {
      let dorw = word.split("").reverse().join("");
      return output.push(dorw);
    } else {
      return output.push(word);
    }
  });
  return output.join(" ");
}

console.log(specialReverse("the something went super quick on that thing", s));
