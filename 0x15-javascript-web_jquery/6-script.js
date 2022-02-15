$(function () {

	function updateH() {
		$('header').empty().append('New Header!!!');
	}

	$("#update_header").click(function () {
		updateH();
	});
});
