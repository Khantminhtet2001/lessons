let keypad = document.querySelector(".key");
let displayBox = document.querySelector(".display");

let showDisplay = (x) => displayBox.innerText += x

let calc = () => displayBox.innerText = eval(displayBox.innerText);

let clearAll = () => displayBox.innerText = '';

let clearLast = () => displayBox.innerText = displayBox.innerText.substring(0,displayBox.innerText.length - 1);