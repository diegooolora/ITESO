function generarTabla() {
    let expresion = document.getElementById("expresion").value.trim();

    // Extraer variables permitidas (todas las letras excepto "v")
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

        let evaluacion;
        try {
            evaluacion = evaluarExpresion(expresion, valores);
        } catch (error) {
            alert("Error al evaluar la expresión lógica. Verifique los operadores y la sintaxis.");
            return;
        }

        tablaHTML += "<tr>";
        variables.forEach(v => tablaHTML += `<td>${valores[v] ? 'V' : 'F'}</td>`);
        tablaHTML += `<td>${evaluacion ? 'V' : 'F'}</td></tr>`;
    }

    tablaHTML += "</table>";
    document.getElementById("tabla").innerHTML = tablaHTML;
}

function evaluarExpresion(expresion, valores) {
    try {
        let expresionModificada = expresion
            .replace(/¬/g, '!')
            .replace(/∧/g, '&&')
            .replace(/∨/g, '||')
            .replace(/→/g, '<=')  // Corregir si se requiere otro comportamiento
            .replace(/↔/g, '==')
            .replace(/⊕/g, '^');

        // Reemplazar variables con sus valores correspondientes
        Object.keys(valores).forEach(v => {
            expresionModificada = expresionModificada.replace(new RegExp(`\\b${v}\\b`, 'g'), valores[v]);
        });

        return eval(expresionModificada);
    } catch (error) {
        console.error("Error en la evaluación de la expresión:", error);
        throw error;  // Relanza el error para manejarlo en `generarTabla()`
    }
}
