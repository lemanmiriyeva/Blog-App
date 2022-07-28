function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}
let item=document.querySelector('.carousel-item')
let item2=document.querySelector('.carousel2')
item.classList.add("active")
item2.classList.add("active")