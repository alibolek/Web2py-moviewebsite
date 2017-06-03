$(document).ready(function(){

	
	$('.add-watchlist-button')
  		.popup();
  	

  	$('.ui.rating')
  		.rating();

    $('textarea').val(
      $('textarea').attr('value')
    );

    $('#apply-changes-button').click(function(){

      $('.ui.modal').modal('show');
      first_name = $('#form1 input[name="first_name"]').val()
      $('#form2 input[name="first_name"]').val(first_name)
      last_name = $('#form1 input[name="last_name"]').val()
      $('#form2 input[name="last_name"]').val(last_name)
      email = $('#form1 input[name="email"]').val()
      $('#form2 input[name="email"]').val(email)
    })

    $('#multi-submit-button').click(function(){
      $('#form2').submit();
  
    });


    $('#search-area').keydown(function(e) {
      if(e.which == 13) {
          query = $(this).val()
          window.location.href = "http://127.0.0.1:8000/movies/default/films?s=" + query;
      }
    });

});