/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction();};

// Get the header
var container = document.getElementById("menu");

// Get the offset position of the navbar
var sticky = container.offsetTop;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset > sticky) {
    container.classList.add("sticky");
  } else {
    container.classList.remove("sticky");
  }
}

