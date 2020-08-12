$(document).on("click",".chat-button", function(){
  $(".chatbox").fadeToggle()
  var icon = $(this).children()
  icon.toggleClass('fa-comments')
  icon.toggleClass('fa-times')
})

$(document).on("click",".head",function(){
 $(this).toggleClass("barra");
 $(".hora").toggle();
 $(".medico").toggle();
 if ($(this).hasClass('barra')) {
   $(".chatlogs").css("height","calc(100% - 113px)")
 } else {
   $(".chatlogs").css("height","calc(100% - 133px)")
 }
})
