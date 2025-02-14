// Alterna entre as seções
function mostrarSecao(secaoId) {
    const secoes = document.querySelectorAll('.secao-gerenciamento');
    secoes.forEach(secao => secao.classList.remove('ativa'));
    const secaoSelecionada = document.getElementById(secaoId);
    secaoSelecionada.classList.add('ativa');
 }
 

 document.addEventListener("DOMContentLoaded", function () {
    const equipamentosPorTreino = {
        "Membros Inferiores": ["Leg Press", "Cadeira Extensora", "Cadeira Flexora"],
        "Membros Superiores": ["Supino", "Pulley", "Máquina de Peito"],
        "Costas e Bíceps": ["Remada Baixa", "Halteres", "Pulley"],
        "Peito e Tríceps": ["Supino", "Polia", "Barras"],
        "Quadríceps": ["Cadeira Extensora", "Barra Guiada Smith", "Halteres", "Bancos para Musculação"],
        "Pernas Completo": ["Leg Press", "Cadeira Flexora", "Cadeira Abdutora"],
        "Ombros e Abdômen": ["Abdominal Máquina", "Halteres", "Máquina Ombro"],
        "Corpo Inteiro": ["Anilhas", "Halteres", "Mesa Posterior", "Leg Press 45 graus", "Bancos para Musculação"],
        "Cardio": ["Esteira", "Bicicleta Ergométrica"],
        "Flexibilidade": ["Colchonetes para Alongamento", "Bola de Pilates", "Elásticos de Resistência"]
    };

    const tipoTreinoSelect = document.getElementById("tipoTreino");
    const equipamentosSugeridosDiv = document.getElementById("equipamentosSugeridos");

    tipoTreinoSelect.addEventListener("change", function () {
        const tipoSelecionado = tipoTreinoSelect.value;
        const equipamentos = equipamentosPorTreino[tipoSelecionado] || [];

        if (equipamentos.length > 0) {
            equipamentosSugeridosDiv.innerHTML = `
                <label>Equipamentos Sugeridos ao Treino escolhido:</label>
                <ul>${equipamentos.map(equip => `<li>${equip}</li>`).join("")}</ul>
            `;
            equipamentosSugeridosDiv.style.display = "block"; // Mostra a seção
        } else {
            equipamentosSugeridosDiv.style.display = "none"; // Esconde se não houver equipamentos
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    carregarInstrutores();

    document.getElementById("formCadastroInstrutor").addEventListener("submit", function (event) {
        event.preventDefault();
        cadastrarInstrutor();
    });

    document.getElementById("formCadastroTurma").addEventListener("submit", function (event) {
        event.preventDefault();
        cadastrarTurma();
    });

    document.getElementById("formCadastroTreino").addEventListener("submit", function (event) {
        event.preventDefault();
        registrarTreino();
    });
});

function carregarInstrutores() {
    fetch("/instrutores/")
        .then(response => response.json())
        .then(data => {
            const instrutorSelect = document.getElementById("instrutorTurma");
            instrutorSelect.innerHTML = "";
            data.forEach(instrutor => {
                let option = document.createElement("option");
                option.value = instrutor.id;
                option.textContent = instrutor.nome;
                instrutorSelect.appendChild(option);
            });
        })
        .catch(error => console.error("Erro ao carregar instrutores:", error));
}

function cadastrarInstrutor() {
    const nome = document.getElementById("nomeInstrutor").value;
    const especialidade = document.getElementById("especialidade").value;
    const horario_trabalho = document.getElementById("periodo").value;

    fetch("/instrutores/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nome, especialidade, horario_trabalho })
    })
    .then(response => response.text()) // Usa text() ao invés de json()
    .then(text => {
        try {
            return JSON.parse(text); // Tenta converter para JSON
        } catch (error) {
            return { mensagem: text || "Resposta vazia do servidor" }; // Se falhar, assume que é uma string vazia
        }
    })
    .then(data => {
        alert(data.mensagem);
        carregarInstrutores();
    })
    .catch(error => console.error("Erro ao cadastrar instrutor:", error));
}    

function cadastrarTurma() {
    const nome = document.getElementById("nomeTurma").value;
    const horario = document.getElementById("horario").value;
    const instrutor_id = document.getElementById("instrutorTurma").value;

    fetch("/turmas/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nome, horario, instrutor_id })
    })
        .then(response => response.json())
        .then(data => {
            alert(data.mensagem);
        })
        .catch(error => console.error("Erro ao cadastrar turma:", error));
}

function registrarTreino() {
    const tipo = document.getElementById("tipoTreino").value;
    const aluno_id = document.getElementById("idAluno").value;
    const instrutor_id = document.getElementById("idInstrutorTreino").value;

    fetch("/treinos/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ tipo, aluno_id, instrutor_id })
    })
        .then(response => response.json())
        .then(data => {
            alert(data.mensagem);
        })
        .catch(error => console.error("Erro ao registrar treino:", error));
}

