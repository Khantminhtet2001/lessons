let keypad = document.querySelector(".key");
let displayBox = document.querySelector(".display");
let operators = ["+","-","*","/","%"];

let filter = x =>{
    let current = displayBox.innerText;
    let lastChar = current[current.length-1];
    if (current == '0'){
        if(x != "."){
            clearLast();
        }

        
    }
    if(operators.includes(x)){
        if(operators.includes(lastChar)){
            return false;
        }
    }
    return true;
}

// let calcFiler = x =>{
//     let current = displayBox.innerText;
//     let lastChar = current[current.length-1];
//     if(operators.includes(lastChar) == operators.includes()){
//         return false;
//     }
//     return true;
// }



let showDisplay = (x) => {
    if(filter(x)) {
        displayBox.innerText += x;
    }
}

let calc = () => {
    // if(calcFiler(x)){
        displayBox.innerText = eval(displayBox.innerText);
    // }
}

let clearAll = () => displayBox.innerText = '';

let clearLast = () => displayBox.innerText = displayBox.innerText.substring(0,displayBox.innerText.length - 1);