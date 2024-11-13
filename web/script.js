const fileButton = document.getElementById('file-button');
const bH = document.getElementById('height');
const bW = document.getElementById('width');
const dH = document.getElementById('hSize');
const dW = document.getElementById('wSize');
const uploadImg = document.getElementById('upload-img');
const exportImg = document.getElementById('export-img');
const pathButton = document.getElementById('path-button');
const pathFound = document.getElementById('path-found');
let isTraced = 1;

fileButton.onclick = async function () {
  let notSelected = await eel.selectFile()();
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

bH.addEventListener('input', (event) => {
  eel.setHeight(event.target.value);
});

bW.addEventListener('input', (event) => {
  eel.setWidth(event.target.value);
});

/*dH.addEventListener('change', (event) => {
  eel.setDheight(event.target.value);
});*/

/*dW.addEventListener('change', (event) => {
  eel.setDwidth(event.target.value);
}); */
