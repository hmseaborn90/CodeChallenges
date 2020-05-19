

// using for var of loop
function findLongestString(str) {
  var words = str.split(" ")
  var longest = ''
  for (var word of words){
    if(word.length > longest.length) {
      longest = word
    }
  }
  return longest +' length of '+ longest.length
}

console.log(findLongestString("the something went super quick on that thing"))

function findLongestString(str) {
  return str.split(' ').sort(function(a, b) {
    return b.length - a.length
  })[0]
}

console.log(findLongestString("the something went super quick on that thing"))

