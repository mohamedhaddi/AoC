const elves = require('fs')
    .readFileSync('./input')
    .toString()
    .split("\n\n")
    .map(elf => {
        const listOfCalories = elf
           .split("\n")
           .map(
                calories => parseInt(calories)
           );
        return {
            listOfCalories: listOfCalories,
            totalCalories: listOfCalories.reduce(
                (a, b) => a + b, 0
            )
        }
    })
    .sort(
        (a, b) => b.totalCalories - a.totalCalories
    );

const topElfTotalCalories = elves[0].totalCalories;

const topThreeElves = elves.slice(0, 3);
const topThreeElvesTotalCalories = topThreeElves
    .reduce(
        (a, b) => a + b.totalCalories, 0
    );

console.log(topThreeElves, "\n");
console.log("Answer 1:", topElfTotalCalories);
console.log("Answer 2:", topThreeElvesTotalCalories);