$(document).ready(function () {

	function fetchMovies(data) {
		for (let item of data.results) {
			$('#list_movies').append(`<li>${item.title}</li>`);
		}
	}

	getValues();

	function getValues() {
		$.ajax({
			url: 'https://swapi-api.hbtn.io/api/films/?format=json',
			type: 'get',
			dataType: 'json',
			cache: false,
			success: fetchMovies,
			async: true,
		});
	};
})
