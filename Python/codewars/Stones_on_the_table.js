function solve(stones) {
	let count = 0;
	for (let i = 0; i < stones.length - 1; i++) {
		console.log(stones[i], stones[i + 1]);
		if (stones[i] == stones[i + 1]) {
			count += 1;
		}
	}
	return count;
}
