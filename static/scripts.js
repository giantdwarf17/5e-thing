import DiceBox from "@3d-dice/dice-box";

// Create an instance of DiceBox
const diceBox = new DiceBox();

// Generate a random roll of a six-sided die
const result = diceBox.roll();

console.log(result); // Output: A random number between 1 and 6
