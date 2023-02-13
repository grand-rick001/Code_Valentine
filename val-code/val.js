const yesButton = document.getElementById('yesButton');
const noButton = document.getElementById('noButton');

yesButton.addEventListener('click', () => {
    alert('Thanks, See you soon <3');
});

noButton.addEventListener('mouseover', change);

function change() {
    var x = Math.floor(Math.random() * window.innerWidth);
    var y = Math.floor(Math.random() * window.innerHeight);
    noButton.style.left = x + "px";
    noButton.style.top = y + "px";
};