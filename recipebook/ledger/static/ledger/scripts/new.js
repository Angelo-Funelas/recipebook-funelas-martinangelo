
var ingredientCount = 1;
var table = document.querySelector('table');
var addIngButton = document.querySelector('table button');
addIngButton.addEventListener('click', function(e) {
  e.preventDefault()
  var newRow = document.createElement('tr');
  var ingredientNameInput = document.createElement('input');
  var ingredientQuantityInput = document.createElement('input');
  var cell1 = document.createElement('td');
  var cell2 = document.createElement('td');

  ingredientCount++;
  document.querySelector("#ingredient-count").value = ingredientCount;

  ingredientNameInput.name = `ingredient-${ingredientCount}-name`;
  ingredientNameInput.required = true;
  ingredientNameInput.type = "text";
  ingredientNameInput.placeholder = "(e.g. milk, sugar)";
  ingredientNameInput.setAttribute('list', 'ingredients');
  ingredientNameInput.autocomplete = "off";

  ingredientQuantityInput.name = `ingredient-${ingredientCount}-qty`;
  ingredientQuantityInput.required = true;
  ingredientQuantityInput.type = "text";
  ingredientQuantityInput.placeholder = "(e.g. 1 cup, 3 teaspoons)";
  ingredientQuantityInput.autocomplete = "off";

  cell1.append(ingredientNameInput);
  cell2.append(ingredientQuantityInput);
  newRow.append(cell1, cell2);
  console.log(e.target.parentElement.parentElement);
  table.querySelector('tbody').insertBefore(newRow, e.target.parentElement.parentElement);
})