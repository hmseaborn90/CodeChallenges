function isValid(str) {
	// WRITE YOUR CODE HERE!
	let stack = [];
	let openPar = {
		"(": ")",
	};
	if (str === null) {
		return false;
	}

	for (let i = 0; i < str.length; i++) {
		let par = str[i];
		if (str[i] == "(") {
			stack.push(par);
		} else if ([par]) {
			let lastInStack = stack.pop();
			if (openPar[lastInStack] !== par) return false;
		}
	}
	return stack.length === 0;
}

console.log(isValid("((()))"));
//comment to push
