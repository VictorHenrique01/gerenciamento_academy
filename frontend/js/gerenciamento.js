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
