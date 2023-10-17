const imagenes = document.querySelectorAll('.imag-galeria')
const imageneslight = document.querySelector('.agregar-imagen')
const contenedorlight = document.querySelector('.imagen-ligth')
const hamburguesa1 = document.querySelector('.hamburguesa');

imagenes.forEach(imagen =>{
    imagen.addEventListener('click', ()=>{
        aparecerImagen(imagen.getAttribute('src'))
    } )
})

const aparecerImagen = (imagen)=>{
    imageneslight.src = imagen;
    contenedorlight.classList.toggle('show')
    imageneslight.classList.toggle('showImagen')
    hamburguesa1.style.opacity = '0'
}

contenedorlight.addEventListener('click', (e)=>{
    if(e.target !==imageneslight){
        contenedorlight.classList.toggle('show')
        imageneslight.classList.toggle('showImagen')
        hamburguesa1.style.opacity = '1'
}

})