/**
 * Created by obodov-vladimir on 06.11.16.
 */
$('.form').find('input, textarea').on('keyup blur focus', function (e) {

  var $this = $(this),
      label = $this.prev('label');

	  if (e.type === 'keyup') {
			if ($this.val() === '') {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
    	if( $this.val() === '' ) {
    		label.removeClass('active highlight');
			} else {
		    label.removeClass('highlight');
			}
    } else if (e.type === 'focus') {

      if( $this.val() === '' ) {
    		label.removeClass('highlight');
			}
      else if( $this.val() !== '' ) {
		    label.addClass('highlight');
			}
    }

});

$('.tab a').on('click', function (e) {

  e.preventDefault();

  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');

  target = $(this).attr('href');

  $('.tab-content > div').not(target).hide();

  $(target).fadeIn(600);

});
function signUp(){
    var first = document.getElementById('first_name');
    var last = document.getElementById('last_name');
    var email = document.getElementById('up_email');
    var pass = document.getElementById('up_pass');
    console.log(first.value);
    if(first.value!=''&& last.value!=''&&email.value!=''&&pass.value.length>5){
        fetch('POST','',{})
    }


}