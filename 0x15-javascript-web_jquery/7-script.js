$(document).ready(function () {

	function fetchData(data) {
		$('#character').append(data.name);
	}

	getValues();

	function getValues() {
		$.ajax({
			url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
			type: 'get',
			dataType: 'json',
			cache: false,
			success: fetchData,
			async: true,
		});
	};
})
