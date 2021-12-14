#!/usr/bin/node

function callMeMoby (x, theFunction) {
	return (theFunction * x);
}

module.exports = { callMeMoby: callMeMoby };
