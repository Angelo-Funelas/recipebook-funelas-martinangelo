
var recipe_gallery = document.querySelector('#recipe-gallery');
var focused_image = recipe_gallery.querySelector('div:nth-child(1) > img');
recipe_gallery.querySelectorAll('div:nth-child(2) > img:not(#add-image)').forEach((image) => {
  image.addEventListener('click', (e) => {
      focused_image.src = e.target.src;
      focused_image.alt = e.target.alt;
      recipe_gallery.querySelectorAll('div:nth-child(2) > img').forEach((image) => {
          image.style.border = "none";
          image.style.filter = "brightness(.9)";
      })
      e.target.style.border = "2px solid black";
      e.target.style.filter = "brightness(1)";
  })
})

var imageForm = document.querySelector('form');
var imageModal = document.querySelector('#new-image-modal');
var imageInput = imageForm.querySelector('#new-img');
document.querySelector('#add-image').addEventListener('click', () => {
  imageInput.click();
})
imageInput.addEventListener('change', (e) => {
  imageModal.style.display = 'block';
  var files = e.target.files;
  var done = function (url) {
      imageForm.querySelector('img').src = url;
  }
  if (files && files.length > 0) {
      file = files[0];
  }
  if (URL) {
      done(URL.createObjectURL(file));
  } else if (FileReader) {
      reader = new FileReader();
      reader.onload = function (e) {
          done(reader.result);
      };
      reader.readAsDataURL(file);
  }
})
imageForm.querySelector("button").addEventListener('click', (e) => {
  e.preventDefault();
  imageInput.value = null;
  imageModal.style.display = 'none';
})