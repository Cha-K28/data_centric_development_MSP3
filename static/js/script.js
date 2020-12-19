  $(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: "True"
    });

    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true,
        duration: 200
    });
        autoplay();
        function autoplay() {
        $('.carousel').carousel('next');
        setTimeout(autoplay, 4500);
    }
    

      $(document).ready(function(){
    $('.modal').modal();
    });

  });
