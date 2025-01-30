const fileButton = document.getElementById("file-submit-button");
const bH = document.getElementById("display-height-input");
const bW = document.getElementById("display-width-input");
const dH = document.getElementById("image-heigth-input");
const dW = document.getElementById("image-width-input");
const uploadImg = document.getElementById("upload-img-display");
const exportImg = document.getElementById("export-img-display");
const pathButton = document.getElementById("path-button");
const pathFound = document.getElementById("path-found");
let isTraced = 1;

fileButton.onclick = async function () {
    const fileInput = document.getElementById("image-upload-button");
    let image = null;
    if (fileInput.files.length === 0) {
        alert("Please select an image first!");
        return;
    }

    const reader = new FileReader();

    // Use `onload` to set the image **after** it has been read
    reader.onload = async function (event) {
        uploadImg.src = event.target.result; // Set image preview correctly
        image = event.target.result;
        pathFound.innerHTML = "Edge Tracing!";

        exportImg.src = await eel.trace_edge(image)(); // Wait for trace_edge to complete processing
        pathFound.innerHTML = "Edge Traced!";
    };

    reader.readAsDataURL(fileInput.files[0]); // Start reading file
};

pathButton.onclick = async function () {
    if (
        pathFound.innerHTML !== "Not Executed!" &&
        pathFound.innerHTML === "Path Found!"
    ) {
        return;
    }
    if (isTraced === 0) {
        pathFound.innerHTML = "Path Finding!";
        let isPathFound = await eel.findPath()();
        if (isPathFound === 0) {
            pathFound.innerHTML = "Path Found!";
        } else {
            pathFound.innerHTML = "Error Occured!";
        }
    } else {
        pathFound.innerHTML = "Select an Image!";
    }
};

bH.addEventListener("input", (event) => {
    eel.setHeight(event.target.value);
});

bW.addEventListener("input", (event) => {
    eel.setWidth(event.target.value);
});

/*dH.addEventListener('change', (event) => {
  eel.setDheight(event.target.value);
});*/

/*dW.addEventListener('change', (event) => {
  eel.setDwidth(event.target.value);
}); */
