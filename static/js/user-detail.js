const menuBtn = document.querySelector("#bars");
const navbar = document.querySelector("#asideBar");

menuBtn.addEventListener("click", () => {
    navbar.style.left === "0px" || navbar.style.left === "" 
        ? navbar.style.left = "-100%" 
            : navbar.style.left = "0px";
})