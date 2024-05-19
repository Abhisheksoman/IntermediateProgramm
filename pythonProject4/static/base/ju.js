const form=document.querySelector("#credit-card");

const nama=document.querySelector("#name");
const birth=document.querySelector("#birth-from");
const pinv=document.querySelector("#pincode");


const nameText=document.querySelector(".name-v1");
const birthText=document.querySelector(".birth-v1");
const pinText=document.querySelector(".pin-v1");



nama.addEventListener("keyup",(e)=>{
    if(!e.target.value){
        nameText.innerHTML='ceras jacob';
    }
    else{
        nameText.innerHTML=e.target.value.toUpperCase();
    }
});

birth.addEventListener("keyup",(e)=>{
    if(!e.target.value){
        birthText.innerHTML='12/2020';
    }
    else{
        const valuesOfInput=e.target.value.replaceAll(" ","");
        birthText.innerHTML=valuesOfInput.replace(/(\d{2})(\d{2})/,"$1/$2");
    }
});
pinv.addEventListener("keyup",(e)=>{
    if(!e.target.value){
        pinText.innerHTML='123';
    }
    else{
        const valuesOfInput=e.target.value.replaceAll(" ","");
        pinText.innerHTML=valuesOfInput.replace(/(\d{3})/,"$1");
    }
});

form.addEventListener("submit",(e)=>{
    e.preventDefault();
    alert("Thank you for your purchase");
});