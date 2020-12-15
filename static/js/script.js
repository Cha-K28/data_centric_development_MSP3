  $(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3
    });
  });