$("#help").on('mouseenter', function() {
	$('#title_quote').fadeOut(100);
	$('.help_enlarge_content').css({
			"opacity": "0.8",
			"transition": "1s"
  })
  $('#index_banner').css({
			"height": "250",
			"transition": "1s"
  })
  $('.help_enlarge_content').addClass("large")
})
$("#help").on('mouseleave', function() {
	$('.help_enlarge_content').css({
			"opacity": "1",
			"transition": "1s"
	  })
	  $('#title_quote').fadeIn(1000);
	  $('#index_banner').css({
			"height": "600",
			"transition": "1s"
	  })
	  $('.help_enlarge_content').removeClass("large")
})