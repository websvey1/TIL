// click on a door handle
// var a = 1;
$(".door-handle").on("click", function(){
    // stop a hash being appended to the url bar
    event.preventDefault();
    // assign "left" or "right" to var name
    var name = $(this).attr("data-name");
    console.log(name)
    // add the animation to either the left or right door
    $(".door."+name).addClass(name+"-DoorOpen");
});