// it should return the places from the given routes
function findRoutes(routes) {
	//Your code here...
	let res = [];
	// map through routes
	routes.map((curr) => {
		//destructure first and second elem in arrays of array assing to a and b
		const [a, b] = curr;
		const first = routes.find((route) => {
			a === route[1];
		});
		if (!first) {
			res.splice(0, 0, a, b);
		}
		routes.map((matching) => {
			if (matching[0] === res[res.length - 1]) {
				res.push(matching[1]);
			}
		});
	});
	return res.join(", ");
}
/// the old

function findRoutes(routes) {
	const result = [];

	routes.map((current) => {
		const [routeA, routeB] = current;

		// checking to see if the FIRST value of one set, is the second value of another set
		const firstItem = routes.find((route) => routeA === route[1]);

		// if not the first item
		if (!firstItem) result.splice(0, 0, routeA, routeB);

		// else ->
		routes.map((matching) => {
			if (matching[0] === result[result.length - 1]) {
				result.push(matching[1]);
			}
		});
	});

	return result.join(", ");
}
