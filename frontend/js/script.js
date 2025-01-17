const formAluno = document.getElementById("formAluno");
formAluno.addEventListener("submit", async (event) => {
   event.preventDefault(); // Evita o reload da página

   const nome = document.getElementById("nome").value;
   const idade = document.getElementById("idade").value;
   const planoId = document.getElementById("plano").value;

   const aluno = {
       nome: nome,
       idade: parseInt(idade),
       plano_id: parseInt(planoId)
   };

   try {
       //requisição POST
       const response = await fetch("http://127.0.0.1:8000/alunos/", {
           method: "POST",
           headers: {
               "Content-Type": "application/json"
           },
           body: JSON.stringify(aluno)
       });
       if (response.ok) {
           alert("Aluno cadastrado com sucesso!");
           formAluno.reset(); // Limpa o form
       } else {
           const error = await response.json();
           alert(`Erro: ${error.detail}`);
           console.log("Dados:", aluno);
       }
   } catch (error) {
       console.error("Erro ao cadastrar aluno:", error);
       alert("Erro ao cadastrar aluno. Verifique o console para mais detalhes.");
   }
});