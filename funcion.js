function consumo(){
    var endPoint = document.getElementById("endPoint").value;
    fetch(endPoint)
    .then(function(response){
        return response.json();
    })
  
    .then(function(data){
        var precios = [];
        var key =[];
        //cliclo for, va a ejecutar hasta que i sea igual al tamaño del arreglo, i++ (condicion de avance)
        for (var i=0; i<data.length; i++){
            //inserta un elemento en el arreglo
            key.push(data[i].id);
            precios.push(data[i].rating.count);
        }
        var grafica = [
            {
                x: key,
                y: precios,
                type: 'bar'
            }
        ];
        Plotly.newPlot('myDiv', grafica);
    })
    .catch(function(error){
        console.log(error);
    })
}

// {}
