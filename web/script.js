const fileButton = document.getElementById('file-button');
const h = document.getElementById('height');
const w = document.getElementById('width');
const uploadImg = document.getElementById('upload-img');
const exportImg = document.getElementById('export-img');
const pathButton = document.getElementById('path-button');
const pathFound = document.getElementById('path-found');
let isTraced = 1;

fileButton.onclick = async function () {
  let notSelected = await eel.selectFolder()();
  if (notSelected === 0) {
    pathFound.innerHTML = 'Not Executed!';
    let imgUploaded = await eel.writeImg()();// Wait for trace_edge to complete processing
    if (imgUploaded === 0) {
      // Force image refresh by adding a timestamp to bypass caching
      uploadImg.src = './upload_img/img.jpg?t=' + new Date().getTime();
      isTraced = await eel.trace_edge()();// Wait for trace_edge to complete processing

      // Force image refresh by adding a timestamp to bypass caching
      exportImg.src = './export_img/export.jpg?t=' + new Date().getTime();
    }
  }
}

pathButton.onclick = async function () {
  if (pathFound.innerHTML !== 'Not Executed!' && pathFound.innerHTML === 'Path Found!') {
    return
  }
  if (isTraced === 0) {
    pathFound.innerHTML = 'Path Finding!';
    let isPathFound = await eel.findPath()();
    if (isPathFound === 0) {
      pathFound.innerHTML = 'Path Found!';
    }
    else {
      pathFound.innerHTML = 'Error Occured!';
    }
  }
  else {
    pathFound.innerHTML = 'Select an Image!';
  }
}

h.addEventListener('input', (event) => {
  eel.setHeight(event.target.value);
});

w.addEventListener('input', (event) => {
  eel.setHeight(event.target.value);
});