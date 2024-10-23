let personas = JSON.parse(localStorage.getItem('personas')) || [];
let editIndex = null;

document.getElementById('personForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const index = document.getElementById('index').value;
    const nombre = document.getElementById('nombre').value;
    const telefono = document.getElementById('telefono').value;
    const documento = document.getElementById('documento').value;

    const persona = { nombre, telefono, documento };

    if (editIndex !== null) {
        personas[editIndex] = persona;
        editIndex = null;
    } else {
        personas.push(persona);
    }

    localStorage.setItem('personas', JSON.stringify(personas));
    displayData();
    this.reset();
});

function displayData() {
    const personGrid = document.getElementById('personGrid');
    personGrid.innerHTML = '';
    personas.forEach((persona, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${persona.nombre}</td>
            <td>${persona.telefono}</td>
            <td>${persona.documento}</td>
            <td>
                <button onclick="editData(${index})">Editar</button>
                <button onclick="deleteData(${index})">Eliminar</button>
            </td>
        `;
        personGrid.appendChild(row);
    });
}

function editData(index) {
    const persona = personas[index];
    document.getElementById('index').value = index;
    document.getElementById('nombre').value = persona.nombre;
    document.getElementById('telefono').value = persona.telefono;
    document.getElementById('documento').value = persona.documento;
    editIndex = index;
}

function deleteData(index) {
    personas.splice(index, 1);
    localStorage.setItem('personas', JSON.stringify(personas));
    displayData();
}

displayData();
