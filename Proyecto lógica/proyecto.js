function generarTabla() {
    let expresion = document.getElementById("expresion").value;
    let variables = [...new Set(expresion.match(/[a-z]/g))].filter(v => v !== 'v').sort(); 

    if (variables.length === 0) {
        alert("Ingrese una expresión válida con proposiciones lógicas.");
        return;
    }

    let combinaciones = Math.pow(2, variables.length);
    let tablaHTML = "<table><tr>";

    // Crear encabezados de tabla
    variables.forEach(v => tablaHTML += `<th>${v}</th>`);
    tablaHTML += `<th>${expresion}</th></tr>`;

    // Generar filas de la tabla
    for (let i = 0; i < combinaciones; i++) {
        let valores = {};
        let binario = i.toString(2).padStart(variables.length, '0');

        variables.forEach((v, index) => valores[v] = binario[index] === '1');

        let evaluacion = evaluarExpresion(expresion, valores);
        tablaHTML += "<tr>";

        variables.forEach(v => tablaHTML += `<td>${valores[v] ? 'V' : 'F'}</td>`);
        tablaHTML += `<td>${evaluacion ? 'V' : 'F'}</td></tr>`;
    }

    tablaHTML += "</table>";
    document.getElementById("tabla").innerHTML = tablaHTML;
}