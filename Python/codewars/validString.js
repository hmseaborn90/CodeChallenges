var validWord = function (dictionary, word) {
	let sw = dictionary.sort();
	for (let i = 0; i < dictionary.length; i++) {
		while (word.includes(dictionary[i])) {
			word = word.replace(dictionary[i], "");
		}
	}
	return word.length === 0;
};
