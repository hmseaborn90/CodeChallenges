
//reverse the string and return true if reversed string equals initial str

function palindrome(str) {
  var reversed = str.split('').reverse().join('')
  if ( reversed === str) return true
  return false
}
console.log(palindrome('eye'))

//with reg ex to rid of symbols
function palindrome(str) {
  var reg = /[\W_]/g
  var smallStr = str.toLowerCase().replace(reg, '')
  var reversed = smallStr.split('').reverse().join('')
  if ( reversed === smallStr) return true
  return false
}
console.log(palindrome('_eye'))

