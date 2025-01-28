// Seleciona os formulários
const formAluno = document.getElementById("formAluno");
const formPlano = document.getElementById("formPlano");
const formConsultarAluno = document.getElementById("formConsultarAluno");
const formConsultarPlano = document.getElementById("formConsultarPlano");
// Função para exibir o formulário correto
function exibirFormulario(formularioId) {
   const formularios = document.querySelectorAll(".formulario");
   formularios.forEach((formulario) => {
       formulario.classList.remove("ativo");
   });
   document.getElementById(formularioId).classList.add("ativo");
}
// Cadastro de Aluno
formAluno.addEventListener("submit", async (event) => {
   event.preventDefault();
   const aluno = {

    nome: document.getElementById("nome").value,
    idade: parseInt(document.getElementById("idade").value),
    plano_id: parseInt(document.getElementById("plano").value),

   };
   try {
       const response = await fetch("http://127.0.0.1:8000/alunos/", {
           method: "POST",
           headers: { "Content-Type": "application/json" },
           body: JSON.stringify(aluno),
       });
       alert(response.ok ? "Aluno cadastrado com sucesso!" : "Erro ao cadastrar aluno.");
       formAluno.reset();
   } catch (error) {
       alert("Erro ao cadastrar aluno.");
   }
});
// Consulta de Aluno
// Evento para o formulário de consulta
document.getElementById("formConsultarAluno").addEventListener("submit", async function (event) {
    event.preventDefault(); // Impede o comportamento padrão do formulário
    // Captura o valor do campo de entrada do ID
    const alunoId = document.getElementById("consultaIdAluno").value;
    // Verifica se o ID foi preenchido
    if (!alunoId) {
        alert("Por favor, insira o ID do aluno.");
        return;
    }
    try {
        // Faz a requisição para o backend
        const response = await fetch(`http://127.0.0.1:8000/alunos/${alunoId}`);
        // Verifica se a resposta é válida
        if (!response.ok) {
            throw new Error("Aluno não encontrado ou erro na consulta.");
        }
        // Converte a resposta para JSON
        const aluno = await response.json();
        // Exibe o resultado no HTML
        const resultadoDiv = document.getElementById("resultadoConsulta");
        resultadoDiv.innerHTML = `
        <h3>Aluno Encontrado</h3>
        <p><strong>ID:</strong> ${aluno.id}</p>
        <p><strong>Nome:</strong> ${aluno.nome}</p>
        <p><strong>Idade:</strong> ${aluno.idade}</p>
        <p><strong>Plano:</strong> ${aluno.plano_id}</p>
        `;
    } catch (error) {
        // Trata erros e exibe uma mensagem para o usuário
        console.error(error.message);
        alert("Erro ao consultar aluno. Verifique o ID e tente novamente.");
    }
 });

// Mapeia os valores dos planos
const valoresPlanos = {
    mensal: 60.00,
    trimestral: 200.00,
    semestral: 320.00,
    anual: 630.00
 };
 // Atualiza o valor do plano ao selecionar no menu suspenso
 document.getElementById("nomePlano").addEventListener("change", function () {
    const valorPlano = valoresPlanos[this.value]; // Obtém o valor do plano selecionado
    document.getElementById("valorPlano").value = `R$ ${valorPlano.toFixed(2)}`; // Atualiza o campo de valor
 });
 // Define o valor inicial ao carregar a página
 document.addEventListener("DOMContentLoaded", function () {
    const planoInicial = document.getElementById("nomePlano").value;
    document.getElementById("valorPlano").value = `R$ ${valoresPlanos[planoInicial].toFixed(2)}`;
 });
 // Cadastro de Plano atualizado para enviar o valor correto
 formPlano.addEventListener("submit", async (event) => {
    event.preventDefault();
    const nomePlano = document.getElementById("nomePlano").value;
    const valorPlano = valoresPlanos[nomePlano]; // Obtém o valor numérico correto
    const plano = { nome: nomePlano, valor: valorPlano };
    try {
        const response = await fetch("http://127.0.0.1:8000/planos/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(plano),
        });
        alert(response.ok ? "Plano cadastrado com sucesso!" : "Erro ao cadastrar plano.");
        formPlano.reset();
    } catch (error) {
        alert("Erro ao cadastrar plano.");
    }
 });
 
 // Consulta de Plano
 formConsultarPlano.addEventListener("submit", async (event) => {
    event.preventDefault();
    const planoId = document.getElementById("consultaIdPlano").value;
    try {
        const response = await fetch(`http://127.0.0.1:8000/planos/${planoId}`);
        if (!response.ok) throw new Error("Plano não encontrado.");
        const plano = await response.json();
        document.getElementById("resultadoConsultaPlano").innerHTML = `
        <h3>Plano Encontrado</h3>
        <p><strong>ID:</strong> ${plano.id}</p>
        <p><strong>Nome:</strong> ${plano.nome}</p>
        <p><strong>Valor:</strong> R$ ${plano.valor.toFixed(2)}</p>
        `;
    } catch (error) {
        alert("Erro ao consultar plano.");
    }
 });

