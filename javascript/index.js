//variables

//Var
 var hw="Hello World";
 console.log(hw);

 //Let
 let aungaungName="Aung Aung";
console.log(aungaungName);
aungaungName="Zaw Zaw";
console.log(aungaungName);


//const
const pi=3.14;
console.log(pi);        //no overwrite


//type of corecion(+)

// var number= 12;
// var number2=14;
var number="12";
var number2="14";


console.log(number+number2);

let name ="Khant Min Htet";
let age = 19;

console.log(name+" age is "+age);


//operators

//+ - * / %


let a=10;
let b=20;

console.log(a+b);
console.log(a-b);
console.log(a*b);
console.log(a/b);
console.log(a%b);


let x=20-7*2/3  
console.log(x);


a+=1;       //11
a++;        //12
a-=1;       //11
a--;        //10
console.log(a);

//if else

var name1="khant min htet";
// console.log(name1=="khant min htet");
if(name1=="kyaw kyaw"){
    console.log("your name is khant min htet");}
else{
    console.log("your name is not khant min htet");}

//truthy and falsy

//falsy 6
//false
//0(zero)
//' ' or "" (empty string)
//null
//undefined
//not a number(nan)

let t=0;
if(t){
    console.log(true)}
else{
    console.log(false);
}