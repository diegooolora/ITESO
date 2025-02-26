function insertarSimbolo(simbolo) {
   document.getElementById("expresion").value += simbolo;
}

function generarTabla() {
   let expresion = document.getElementById("expresion").value;
   let variables = [...new Set(expresion.match(/[a-uw-z]/g))].sort(); // Permite cualquier letra excepto "v"

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

       // Asignar valores de verdad
       variables.forEach((v, index) => valores[v] = binario[index] === '1');

       let evaluacion = evaluarExpresion(expresion, valores);
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
           .replace(/¬/g, '!')  // Negación
           .replace(/∧/g, '&&') // Conjunción (AND)
           .replace(/∨/g, '||') // Disyunción (OR)
           .replace(/→/g, '<=') // Implicación
           .replace(/↔/g, '==') // Bicondicional
           .replace(/⊕/g, '^');  // XOR

       // Reemplazar variables con sus valores de verdad
       Object.keys(valores).forEach(v => {
           let regex = new RegExp(`\\b${v}\\b`, 'g'); // Evita reemplazos parciales
           expresionModificada = expresionModificada.replace(regex, valores[v]);
       });

       return eval(expresionModificada);
   } catch {
       alert("Expresión inválida. Use operadores lógicos como ¬, ∧, ∨, →, ↔, ⊕.");
       return false;
   }
}
