from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Carregar o modelo e o tokenizer do GPT-2 (você pode trocar por GPT-3 se tiver acesso via API)
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Função para gerar uma resposta
def gerar_resposta(input_text):
    # Codificar o texto de entrada
    inputs = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")
    
    # Gerar a resposta
    output = model.generate(inputs, max_length=1000, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)
    
    # Decodificar e retornar a resposta gerada
    resposta = tokenizer.decode(output[0], skip_special_tokens=True)
    return resposta

# Loop para simular um chat
print("ChatBot (escreva 'sair' para encerrar)")
while True:
    usuario_input = input("Você: ")
    if usuario_input.lower() == "sair":
        break
    resposta = gerar_resposta(usuario_input)
    print(f"ChatBot: {resposta}")
