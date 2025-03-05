import tkinter as tk
from tkinter import scrolledtext
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
