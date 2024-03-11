let operators = ["+","-","*","/","="];
let keyPad = document.querySelector('.keypad');
let displayBox = document.querySelector('.display-box');

for (let i=0;i<10;i++){
    keyPad.innerHTML += `<button class="key" onclick = 'showInDisplay(${i})'>${i}</button>`;
}

operators.forEach(x=>{
    if (x === "="){
        keyPad.innerHTML += `<button class="key" onclick = 'calc()'>${x}</button>`;
    }else{
        keyPad.innerHTML += `<button class="key" onclick = 'showInDisplay("${x}")'>${x}</button>`;
    }
});
let showInDisplay=(x)=> displayBox.innerText += x
let calc =()=> displayBox.innerText = eval(displayBox.innerText);
