$(function () {

	function changeClass() {
		$('header').toggleClass("red green");
	}

	$("#toggle_header").click(function () {
		changeClass();
	});
});

// function nextclass() {
// 	if ($('header').hasClass('green')) {
// 		$('header').removeClass('green').addClass('red');
// 	} else {
// 		$('header').removeClass('red').addClass('green');
// 	}
// }
