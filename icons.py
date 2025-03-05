import tkinter as tk
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Carregar o modelo e o tokenizer do GPT-2
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Função para gerar uma resposta
def gerar_resposta(input_text):
    # Codificar o texto de entrada
    inputs = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")
    
    # Gerar a resposta
    output = model.generate(
        inputs, 
        max_length=150,  # Limitar o comprimento da resposta
        num_return_sequences=1,  # Retornar apenas uma sequência
        no_repeat_ngram_size=2,  # Evitar repetições de n-grams
        top_k=50,  # Limitar o número de palavras mais prováveis para o modelo
        top_p=0.95,  # Controla a amostragem com base na probabilidade acumulada
        temperature=0.7,  # Controle de aleatoriedade, quanto menor mais determinístico
        pad_token_id=tokenizer.eos_token_id,  # Definir token de padding para evitar erros
    )
    
    # Decodificar e retornar a resposta gerada
    resposta = tokenizer.decode(output[0], skip_special_tokens=True)
    return resposta

# Função chamada quando o usuário enviar uma mensagem
def enviar_mensagem():
    usuario_input = entry.get()
    if usuario_input.lower() == "sair":
        root.quit()  # Fecha o aplicativo se o usuário digitar "sair"
    else:
        resposta = gerar_resposta(usuario_input)
        texto_chat.config(state=tk.NORMAL)  # Habilita o texto para atualização
        texto_chat.insert(tk.END, "Você: " + usuario_input + "\n")
        texto_chat.insert(tk.END, "ChatBot: " + resposta + "\n\n")
        texto_chat.config(state=tk.DISABLED)  # Desabilita o texto após a atualização
        entry.delete(0, tk.END)  # Limpa a caixa de entrada

# Criando a janela principal
root = tk.Tk()
root.title("ChatBot GPT-2")

# Criando a área de exibição do chat
texto_chat = tk.Text(root, height=15, width=50, wrap=tk.WORD, state=tk.DISABLED)
texto_chat.grid(row=0, column=0, padx=10, pady=10)

# Criando a caixa de entrada para o usuário digitar a mensagem
entry = tk.Entry(root, width=40)
entry.grid(row=1, column=0, padx=10, pady=10)

# Criando o botão para enviar a mensagem
botao_enviar = tk.Button(root, text="Enviar", width=10, command=enviar_mensagem)
botao_enviar.grid(row=1, column=1, padx=10, pady=10)

# Rodar a interface
root.mainloop()
