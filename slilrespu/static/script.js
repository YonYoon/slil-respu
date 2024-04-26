document.addEventListener('DOMContentLoaded', addBackground);

async function addBackground() {
    let image_response = await fetch('/image');
    let image_name = await image_response.json();
    var bgDiv = document.createElement("div");
    bgDiv.classList.add('bg')

    // Apply necessary styles to the div
    bgDiv.style.position = "fixed";
    bgDiv.style.top = "0";
    bgDiv.style.left = "0";
    bgDiv.style.width = "100%";
    bgDiv.style.height = "100%";
    bgDiv.style.zIndex = "-1";
    bgDiv.style.backgroundImage = `url('../static/images/${image_name}')`;
    bgDiv.style.backgroundSize = "cover";
    bgDiv.style.filter = "brightness(60%)";

    // Append the div to the body
    document.body.appendChild(bgDiv);
    bgDiv.classList.add('fadeIn');
    bgDiv.addEventListener('animationend', function() {
        bgDiv.classList.remove('fadeIn');
    });
}