import requests
import discord
from discord.ext import commands
from discord.ui import Button, View
import youtube_dl

class MyClient(discord.Client):
    prefix = '!carlito' #Ex: !carlito matue gorila roxo 
    voice_channels = { }
    
    async def on_ready(client):
        print(f'Bot online: {client.user} ✅')

    async def on_message(client, message):
        if message.author == client.user:
            return  

        if message.content.startswith(MyClient.prefix):
            await MyClient.process_command(client, message)

    @staticmethod
    async def process_command(client, message):
        # pesquisa do user
        
        pesquisa = message.content[len(client.prefix):].strip()
        pesquisa_url = f'https://server1.mtabrasil.com.br/youtube/search?q={pesquisa}'
        resposta = requests.get(pesquisa_url)
        
        if resposta.status_code == 200:
            resultados = resposta.json()
            if resultados['items']:
                embed = discord.Embed(
                    title='Resultados da Pesquisa',
                    color=discord.Color.random(),
                )
                for i, index in enumerate(resultados['items'], start=1):
                    if 'title' in index:
                        
                        embed.add_field(
                            name=f'{i} - {index['title']}',
                            value='',
                            inline=False
                        )
                    else:
                        print('Erro: Nenhuma informação foi encontrada')
                embed.add_field(name='Desenvolvido por Andrey', value='', inline=False) 
                await message.channel.send(embed=embed)
                await message.channel.send('**:arrow_forward: Digite o número da música que você deseja escolher:**')
                
                
                def checkpimba(ksksks):
                    # Verifica se a msg é do user original e contem um número
                    return ksksks.author == message.author and ksksks.channel == message.channel and ksksks.content.isdigit()
                try:
                    # Espera a resposta do user para escolher a musica
                    resposta_user = await client.wait_for('message', check=checkpimba, timeout=30)
                    number = int(resposta_user.content)
                    guild_id = message.guild.id

                    if message.author.voice and message.author.voice.channel:
                        user_conect = message.author.voice.channel
                        if guild_id in MyClient.voice_channels and MyClient.voice_channels[guild_id].is_connected():
                            await MyClient.voice_channels[guild_id].disconnect()
                
                        voice_channel = await user_conect.connect()
                        MyClient.voice_channels[guild_id] = voice_channel
                        
                        LinkMusica = resultados['items'][number - 1].get('url', 'Url não encontrada')
                        TituloMusica = resultados['items'][number - 1]['title']
                        thumbnail_url = resultados['items'][number - 1].get('bestThumbnail', {}).get('url')
                        if not thumbnail_url:
                            thumbnail_url = 'https://cdn.discordapp.com/attachments/1198050047544266762/1199787060903542976/32.jpg?ex=65c3cfc6&is=65b15ac6&hm=5f50cd9192b2b9f604dd424eb5495a7eac299d274b48f53242ff5118296a3d28&'
                        embed_escolhida = discord.Embed(
                            title='Música escolhida:',
                            color=discord.Color.random(),
                        )
                        embed_escolhida.add_field(
                            name=f'{number} - {TituloMusica}',
                            value=f'Link da música [aqui]({LinkMusica}).',
                            inline=False
                        )
                        embed_escolhida.add_field(name='Desenvolvido por Andrey', value='', inline=False) 
                            
                        button_downloadMP3 = discord.ui.Button(label='Download MP3', custom_id='play_buttonmp3')
                        button_downloadMP4 = discord.ui.Button(label='Download MP4', custom_id='play_buttonmp4')
                        view = discord.ui.View()
                        view.add_item(button_downloadMP3)
                        view.add_item(button_downloadMP4)
                        embed_escolhida.set_image(url=thumbnail_url)
                        await message.channel.send(embed=embed_escolhida, view=view)
                        
                        try:
                            selected_item = resultados['items'][number - 1]
                            if 'id' in selected_item:
                                musica_id = resultados['items'][number - 1]['id']
                                await MyClient.play_music(guild_id, musica_id)
                            else:
                                await message.channel.send(':warning: **A música selecionada não possui um ID válido.**')
                        except IndexError:
                            await message.channel.send(':warning: **ID de música inválido. Escolha um número de música válido.**')
                    else:
                        await message.channel.send(':warning: **Você não está conectado a um canal de voz.**')
                except TimeoutError:
                    await message.channel.send(':warning: **Tempo esgotado. Operação cancelada.**')
            else:
                print('Nenhum resultado encontrado.')
        else:
            print(f'Erro na requisição. Código de status: {resposta.status_code}')
            await message.channel.send(f':warning: **Erro na requisição. Código de status: {resposta.status_code}**')
    

## Obrigado stack overflow
    @staticmethod
    async def play_music(guild_id, musica_id):
        play_url = f'https://server1.mtabrasil.com.br/youtube/play?id={musica_id}' #Usei API de play, que utilizei em projeto spotify para MTA San Andreas

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '126',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(play_url, download=False)
            url = info['formats'][0]['url']

            # Verifica se o servidor está no dicionário de canais de voz
            if guild_id in MyClient.voice_channels and MyClient.voice_channels[guild_id].is_connected():
                if MyClient.voice_channels[guild_id].is_playing():
                    MyClient.voice_channels[guild_id].stop()
                MyClient.voice_channels[guild_id].play(discord.FFmpegPCMAudio(url), after=lambda e: print(f'Error: {e}') if e else None)
            else:
                print(f':warning: **O bot não está conectado a um canal de voz no servidor {guild_id}.**')


intents = discord.Intents.default()
intents.message_content = True
        
client = MyClient(intents=intents)
client.run('')

