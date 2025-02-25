function generarTabla() {
   let expresion = document.getElementById("expresion").value;
   let tablaHTML = "<table><tr><th>A</th><th>B</th><th>Resultado</th></tr>";
   
   let valores = [false, true];
   for (let A of valores) {
       for (let B of valores) {
           let resultado;
           try {
               resultado = eval(expresion.replace(/A/g, A).replace(/B/g, B));
           } catch (e) {
               alert("Expresión no válida. Use A y B con operadores &&, || y !");
               return;
           }
           tablaHTML += `<tr><td>${A}</td><td>${B}</td><td>${resultado}</td></tr>`;
       }
   }
   tablaHTML += "</table>";
   document.getElementById("tabla").innerHTML = tablaHTML;
}
