const nombre = document.getElementById("nombre")
const telefono = document.getElementById("telefono")
const cantidad = document.getElementById("cantidad")
const email = document.getElementById("email")
const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")

form.addEventListener("submit", e=>{
  e.preventDefault()

  let warnings = ""
  let entrar = false
  let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
  parrafo.innerHTML = ""

  if(nombre.value.length <2){
    warnings += `El nombre no es valido <br>`
    entrar = true
  }
  if(!regexEmail.test(email.value)){
    warnings += `El email no es valido <br>`
    entrar = true
  }
  if(telefono.value.length < 10){
    warnings += `El numero de telefono no es valido <br>`
    entrar = true
  }
  if(cantidad.value.length >2){
    warnings += `La cantidad de personas no es valida <br>`
    entrar = true
  }
  if(entrar){
    parrafo.innerHTML = warnings
  } else{
    parrafo.innerHTML = `Su reserva fue enviada, nos comunicaremos a la brevedad`

  }








})