function on() {
    document.getElementById("overlay").style.display = "flex";
  }

function off() {
    document.getElementById("overlay").style.display = "none";
}

$(document).ready(function () {
	$("#convert").on("click", function (e) {
		on();
		e.preventDefault();
		let from = $("#from").val();
		let from_curr = $("#from_currency").val();
		let to_curr = $("#to_currency").val();
		let url = $("#url").data('url');
		let getData = {
			from_curr: from_curr,
			to_curr: to_curr,
			curr_val: from,
		};

		$.get(url, getData, function (data, status) {
		$("#error").html('');
		if (status == "success") {
				$("#to").val(data["converted_value"]);
				$("#error").html(data['msg']);
		} else {
			console.log("Not able to reach to the server.");
		}
		off();
		});
	});

	$(".numberonly").keypress(function (e) {
		var charCode = e.which ? e.which : event.keyCode;
		if (String.fromCharCode(charCode).match(/[^0-9]/g)) return false;
	});
});