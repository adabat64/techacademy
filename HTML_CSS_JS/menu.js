$(document).ready (function(){
  $(".navigation li").hover(
    function() {$("ul", this).fadeIn();},
    function() {$("ul", this).fadeOut();}
);
});
