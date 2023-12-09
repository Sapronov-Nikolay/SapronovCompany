var colorArray= ["#60b47a", "#e5e351", "#d746af", "#6dcae7"];
var i =0;

function changeColor(){
    document.body.style.background = colorArray[i];
    i++;
    if( i > colorArray.length - 1){
        i = 0;
    }
}
