function hide(){
    console.log('button clicked')
    var elem = document.getElementById('sidebar')
    if(elem.style.display === 'none'){
        elem.style.display = 'block'
    } else{
        elem.style.display = 'none'
    }
}