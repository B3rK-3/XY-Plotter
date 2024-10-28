document.getElementById('file-button').onclick = function() {
  eel.selectFolder();
}
const h = document.getElementById('height');
const w = document.getElementById('width');

h.addEventListener('input', (event) => {
  eel.setHeight(event.target.value);
});

w.addEventListener('input', (event) => {
  eel.setWidth(event.target.value);
});