"use strict";
// get styles for sells
const r1c1 = document.getElementById("r1c1");
const r2c1 = document.getElementById("r2c1");
const r3c1 = document.getElementById("r3c1");
const r1c2 = document.getElementById("r1c2");
const r2c2 = document.getElementById("r2c2");
const r3c2 = document.getElementById("r3c2");

const score_value = document.querySelector(".score");
let score = 0;
let currentLetterIndex = 0;

const ham = document.querySelector(".ham");
const menu = document.querySelector(".menu");

const opt_1 = document.querySelector(".opt-1");
const opt_2 = document.querySelector(".opt-2");
const opt_3 = document.querySelector(".opt-3");

const letters = [
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G",
  "H",
  "I",
  "J",
  "K",
  "L",
  "M",
  "N",
  "O",
  "P",
  "Q",
  "R",
  "S",
  "T",
  "U",
  "V",
  "W",
  "X",
  "Y",
  "Z",
];

// braile patterns
const braillePatterns = {
  A: [1, 0, 0, 0, 0, 0], // ⠁
  B: [1, 1, 0, 0, 0, 0], // ⠃
  C: [1, 0, 0, 1, 0, 0], // ⠉
  D: [1, 0, 0, 1, 1, 0], // ⠙
  E: [1, 0, 0, 0, 1, 0], // ⠑
  F: [1, 1, 0, 1, 0, 0], // ⠋
  G: [1, 1, 0, 1, 1, 0], // ⠛
  H: [1, 1, 0, 0, 1, 0], // ⠓
  I: [0, 1, 0, 1, 0, 0], // ⠊
  J: [0, 1, 0, 1, 1, 0], // ⠚
  K: [1, 0, 1, 0, 0, 0], // ⠅
  L: [1, 1, 1, 0, 0, 0], // ⠇
  M: [1, 0, 1, 1, 0, 0], // ⠍
  N: [1, 0, 1, 1, 1, 0], // ⠝
  O: [1, 0, 1, 0, 1, 0], // ⠕
  P: [1, 1, 1, 1, 0, 0], // ⠏
  Q: [1, 1, 1, 1, 1, 0], // ⠟
  R: [1, 1, 1, 0, 1, 0], // ⠗
  S: [0, 1, 1, 1, 0, 0], // ⠎
  T: [0, 1, 1, 1, 1, 0], // ⠞
  U: [1, 0, 1, 0, 0, 1], // ⠥
  V: [1, 1, 1, 0, 0, 1], // ⠧
  W: [0, 1, 0, 1, 1, 1], // ⠺
  X: [1, 0, 1, 1, 0, 1], // ⠭
  Y: [1, 0, 1, 1, 1, 1], // ⠽
  Z: [1, 0, 1, 0, 1, 1], // ⠵
};

ham.addEventListener("click", function () {
  if (menu.classList.contains("hide")) {
    menu.classList.remove("hide");
  } else {
    menu.classList.add("hide");
  }
});

opt_1.addEventListener("click", function () {
  // run the normal code
  startGame();
  console.log("option 1 selected");
});

function displayBrailleLetter(pattern) {
  const cells = [r1c1, r2c1, r3c1, r1c2, r2c2, r3c2];
  cells.forEach((cell, index) => {
    cell.style.backgroundColor = pattern[index] === 1 ? "#000" : "#FFF";
  });
}

// Add a function to speak the current letter
function speakLetter(letter) {
  // Create a new speech synthesis utterance
  const utterance = new SpeechSynthesisUtterance(letter);

  // Optional: You can customize the speech
  // utterance.rate = 1; // Speed of speech
  // utterance.pitch = 1; // Pitch of speech

  // Speak the letter
  window.speechSynthesis.speak(utterance);
}

function checkLetter() {
  const entryInput = document.querySelector(".entry");
  entryInput.focus();
  const entry = entryInput.value.trim().toUpperCase();
  const currentLetter = letters[currentLetterIndex];

  if (entry === currentLetter) {
    score++;
    score_value.textContent = score;
    console.log(`Correct! Score: ${score}`);

    // Speak the correct letter
    speakLetter(currentLetter);

    // Move to the next letter
    currentLetterIndex++;

    // Check if all letters have been traversed
    if (currentLetterIndex < letters.length) {
      // Display the next letter
      const nextLetter = letters[currentLetterIndex];
      displayBrailleLetter(braillePatterns[nextLetter]);

      // Speak the next letter
      speakLetter(nextLetter);
    } else {
      console.log("All letters completed!");
      speakLetter("All letters completed!");
      displayBrailleLetter(braillePatterns["A"]);
      currentLetterIndex = 0;
      score = 0;
      score_value.textContent = score;
    }
  } else {
    console.log("Try again!");
  }

  // Clear the input
  entryInput.value = "";
}

function startGame() {
  currentLetterIndex = 0;
  score = 0;
  score_value.textContent = score;
  const firstLetter = letters[currentLetterIndex];
  displayBrailleLetter(braillePatterns[firstLetter]);

  // Speak the first letter when the game starts
  speakLetter(firstLetter);

  // Add event listener for checking entry on "input"
  const entryCheck = document.querySelector(".entry");
  entryCheck.addEventListener("input", checkLetter);
}
// Start game when DOM is loaded
// speakLetter("A");
document.addEventListener("DOMContentLoaded", startGame);
