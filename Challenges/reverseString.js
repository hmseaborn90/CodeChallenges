// do it from scratch no methods
function reverseStr(str) {
  var final = '';
  for (var i= str.length - 1; i >= 0; i--){
    final += str[i];
  }
  return final
}
console.log(reverseStr('hello'))


/// makes use of methods as dry as i can
function reverseString(str) {
  return str.split('').reverse().join('');
}

reverseString('workywork')


// multiple line brute force method
function reverseString(str){
  var strArr = str.split('')
  var reverseStrArr = strArr.reverse()
  var reversedString = reverseStrArr.join('')
  return reversedString
}

reverseString('workywork')
