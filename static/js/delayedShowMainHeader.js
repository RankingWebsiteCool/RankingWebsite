function showMainHeaderAndButton() {
    $('#main_header').show()
}
$("#scroll_down").on('click', function() {
    window.scrollTo(0, (document.body.scrollHeight || document.documentElement.scrollHeight) - 1000);
})
setTimeout(showMainHeaderAndButton, 750);
var smallNavVisible = false;
$("#showSmallNavigation").on('click', function() {
    if (smallNavVisible) {
           $('#small-navigation').hide();
    } else {
           $('#small-navigation').show()
    }
    smallNavVisible = !smallNavVisible;
})