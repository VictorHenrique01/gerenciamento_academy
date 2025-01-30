const formEquipamento = document.getElementById("formEquipamento");
const formConsultarEquipamento = document.getElementById("formConsultarEquipamento");

function exibirFormulario(formularioId) {
    const formularios = document.querySelectorAll(".formulario");
    formularios.forEach((formulario) => {
        formulario.classList.remove("ativo");
    });
    document.getElementById(formularioId).classList.add("ativo");
 }