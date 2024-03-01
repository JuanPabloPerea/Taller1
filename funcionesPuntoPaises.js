// funcion para recolectar la informacion de asia
function consumoAsia(){
    var endPont = document.getElementById("EndPoint").value;
    fetch(endPont)
        .then(response => response.json())
        .then(data => {
            var categorias1 = [];
            var key1 = [];
            for (let i = 0; i < data.length; i++) {
                // ir donde se pregunta en que continente se encuentra la region
                if (data[i].continents == 'Asia') {
                    key1.push(data[i].region);
                    categorias1.push(data[i].subregion);    
                }
            }
            var graficaAsia = [
                {
                    x: key1,
                    y: categorias1,
                    type: 'bar'
                }
            ]
            // Creacion de la grafica
            var graficaEuropa = [
                {
                    x: key2,
                    y: categorias2,
                    type: 'bar'
                }
            ]
            Plotly.newPlot('myDiv1', graficaAsia);
        })
    .catch(error => console.log(error));
}

// funcion para recolectar la informacion de europa
function consumoEuropa(){
    var endPont = document.getElementById("EndPoint").value;
    fetch(endPont)
        .then(response => response.json())
        .then(data => {
            var categorias1 = [];
            var key1 = [];
            for (let i = 0; i < data.length; i++) {
                // ir donde se pregunta en que continente se encuentra la region
                if(data[i].continents == 'Europe') {
                    key1.push(data[i].region);
                    categorias1.push(data[i].subregion);
                }
            }
            // Creacion de la grafica
            var graficaAsia = [
                {
                    x: key1[1],
                    y: categorias1,
                    type: 'bar'
                }
            ]
        Plotly.newPlot('myDiv2', graficaEuropa);
    })
    .catch(error => console.log(error));
}
