// Alterna entre as seções
function mostrarSecao(secaoId) {
    const secoes = document.querySelectorAll('.secao-gerenciamento');
    secoes.forEach(secao => secao.classList.remove('ativa'));
    const secaoSelecionada = document.getElementById(secaoId);
    secaoSelecionada.classList.add('ativa');
 }
 // Exemplo de envio de dados (substitua pelos endpoints reais)
 document.getElementById("formCadastroInstrutor").addEventListener("submit", function (e) {
    e.preventDefault();
    const nome = document.getElementById("nomeInstrutor").value;
    const especialidade = document.getElementById("especialidade").value;
    // Faça a requisição para o backend
    fetch("http://127.0.0.1:8000/instrutores", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nome, especialidade })
    })
    .then(response => response.json())
    .then(data => {
        alert("Instrutor cadastrado com sucesso!");
        console.log(data);
    })
    .catch(error => console.error("Erro ao cadastrar instrutor:", error));
 });
