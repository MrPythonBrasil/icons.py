import discord
import requests
import random

client = discord.Client()

# Função para pegar ícones e postar no Discord
def pegar_icone_aleatorio():
    API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ZDEzOGViMi1hMDE5LTRhYzEtYWJmNy0wYTMxMDYyZTQ2NzgiLCJleHAiOjE1MDg4NDM3MjIsImlkIjoiNDQ2OTE4NCJ9.FlexrpEdISo-Pfpx5dS3znUVPU229p6SlncT2AJZzN8'  # Substitua pela sua chave da API do Flaticon
    BASE_URL = 'https://api.flaticon.com/v3/search/iconsdiscord'

    params = {
        'apikey': API_KEY,
        'query': 'icon discord',  # Palavra-chave para pesquisa
        'limit': 10,  # Quantidade de ícones a buscar
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and len(data['data']) > 0:
            icone = random.choice(data['data'])
            return icone['images']['128']  # Retorna a URL do ícone
        else:
            return None
    else:
        print(f"Erro ao buscar ícones: {response.status_code}")
        return None

# Evento que ocorre quando o bot está pronto
@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

    # Pega um ícone aleatório
    url_icone = pegar_icone_aleatorio()

    if url_icone:
        # Envia o ícone no canal padrão (substitua 'canal_id' com o ID do canal desejado)
        canal = client.get_channel('canal_id')  # Troque 'canal_id' pelo ID do canal
        await canal.send(url_icone)

# Evento que ocorre quando uma mensagem é recebida
@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignora as mensagens do bot

    if message.content.startswith('!icon'):
        # Quando alguém enviar "!icon", o bot envia um ícone aleatório
        url_icone = pegar_icone_aleatorio()
        if url_icone:
            await message.channel.send(url_icone)

# Token do seu bot
TOKEN = 'MTM0Mjk5NzMyODE2ODIyNjkwOA.G4dPi4.Y3dTjWJsiX9x2tjVKZhAfEun3Lzw7bhlu8V6cQ'  # Substitua pelo token do seu bot

# Inicia o bot
client.run(TOKEN)
