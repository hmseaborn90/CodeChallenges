function digitize(n) {
  let reversedString = n.toString().split('').reverse().join('')
  return Array.from(reversedString).map(Number);
  
}