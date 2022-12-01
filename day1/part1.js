const fs = require('fs');
const path = require('path');

function getMaxDeerCalories(caloriesInput) {
  let maxCalories = 0;
  let actualCalories = 0;

  caloriesInput.forEach(el => {
    if (el === '') {
      actualCalories = 0;
      return;
    }

    actualCalories += Number(el);
    if (actualCalories > maxCalories) {
      maxCalories = actualCalories;
    }
  });

  return maxCalories;
}

fs.readFile(path.resolve(__dirname, 'input.txt'), 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  const dataSplitted = data.split('\n');
  const result = getMaxDeerCalories(dataSplitted);

  console.log(result);
});
