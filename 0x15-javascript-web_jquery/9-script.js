$(document).ready(function () {

	function fetchHello(data) {
		console.log(data.hello);
		$('#hello').append(data.hello);
	}

	getValues();

	function getValues() {
		$.ajax({
			url: 'https://fourtonfish.com/hellosalut/?lang=fr',
			type: 'get',
			dataType: 'json',
			cache: false,
			success: fetchHello,
			async: true,
		});
	};
})
