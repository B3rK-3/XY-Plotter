const fileButton = document.getElementById('file-button');
const h = document.getElementById('height');
const w = document.getElementById('width');
const uploadImg = document.getElementById('upload-img');
const exportImg = document.getElementById('export-img');

fileButton.onclick = async function () {
  let notSelected = await eel.selectFolder()();
  if (notSelected === 0) {
    await eel.writeImg();// Wait for trace_edge to complete processing

    // Force image refresh by adding a timestamp to bypass caching
    uploadImg.src = './upload_img/img.png?t=' + new Date().getTime();
    await eel.trace_edge();// Wait for trace_edge to complete processing

    // Force image refresh by adding a timestamp to bypass caching
    exportImg.src = './export_img/export.png?t=' + new Date().getTime();
    eel.jsPrint(img.src);
  }
}

h.addEventListener('input', (event) => {
  eel.setHeight(event.target.value);
});

w.addEventListener('input', (event) => {
  eel.setHeight(event.target.value);
});