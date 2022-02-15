$(function () {

	function addItem() {
		$('.my_list').append("<li>Item</li>");
	}

	$("#add_item").click(function () {
		addItem();
	});
});
