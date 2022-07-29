 

// document.addEventListener("DOMContentLoaded", function(event) {
//   document.documentElement.setAttribute("data-theme", "dark");
// });

  // Wait for document to load
document.addEventListener("DOMContentLoaded", function(event) {
    document.documentElement.setAttribute("data-theme", "light");
    
      // Get our button switcher
    var themeSwitcher = document.getElementById("theme-switcher");
    
    
     
      // When our button gets clicked
    themeSwitcher.onclick = function() {
        // Get the current selected theme, on the first run
        // it should be `light`
      var currentTheme = document.documentElement.getAttribute("data-theme");
  
        // Switch between `dark` and `light`
        var switchToTheme = currentTheme === "dark" ? "light" : "dark"
  
        // Set our current theme to the new one
        document.documentElement.setAttribute("data-theme", switchToTheme);
        if(themeSwitcher.classList.contains("bi-sun")){
          themeSwitcher.classList.add("bi-moon-stars-fill")
          themeSwitcher.classList.remove("bi-sun");
          }
         else{
          themeSwitcher.classList.add("bi-sun")
          themeSwitcher.classList.remove("bi-moon-stars-fill");
         }
  
      }
}); 

$(document).ready(function(){
	$(window).scroll(function () {
			if ($(this).scrollTop() > 50) {
				$('#back-to-top').fadeIn();
			} else {
				$('#back-to-top').fadeOut();
			}
		});
		// scroll body to 0px on click
		$('#back-to-top').click(function () {
			$('body,html').animate({
				scrollTop: 0
			}, 400);
			return false;
		});
});
