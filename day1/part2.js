const fs = require('fs');
const path = require('path');

function getMaxOfBestThreeDeerCalories(caloriesInput) {
  const calories = [];
  let actualCalories = 0;

  caloriesInput.forEach(el => {
    if (el === '') {
      calories.push(actualCalories);
      actualCalories = 0;
      return;
    }

    actualCalories += Number(el);
  });

  return calories
    .sort((a, b) => b - a)
    .slice(0, 3)
    .reduce((sum, a) => sum + a, 0);
}

fs.readFile(path.resolve(__dirname, 'input2.txt'), 'utf8', (err, data) => {
  if (err) {
    console.error(err)
    return;
  }

  const dataSplitted = data.split('\n');
  const result = getMaxOfBestThreeDeerCalories(dataSplitted);

  console.log(result);
});
