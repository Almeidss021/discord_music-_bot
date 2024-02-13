# Bot de música para Discord feito em Python. 🎵

🎵 Bom, fiz esse bot de música para estudo. Ele é bem simples e pode ser utilizado em vários servidores ao mesmo tempo. Basta você hospedá-lo.

# 📚 Dependencias:

```bash
pip install discord.py
```
```bash
pip install discord.py[voice]
```
```bash
pip install python-dotenv
```

```bash
pip install PyNaCl
```
```bash
pip install youtube_dl
```

```bash
pip install ffmpeg
```

# 🤓 Como baixar ffmpeg:

## Passo 1: Baixar o FFmpeg

Vá para o site oficial do FFmpeg (https://ffmpeg.org/download.html) e faça o download da versão adequada para o seu sistema operacional Windows.

## Passo 2: Extrair os arquivos

Após o download, extraia os arquivos do FFmpeg para uma pasta em seu computador. Por exemplo, você pode criar uma pasta chamada "ffmpeg" no diretório C:\ e extrair os arquivos lá.

## Passo 3: Adicionar ao Path do Sistema

- Agora, precisamos adicionar o caminho dos arquivos executáveis do FFmpeg ao Path do sistema.
- No Windows 10, clique com o botão direito do mouse no ícone do Windows na barra de tarefas e selecione "Sistema".
- No painel esquerdo, clique em "Configurações avançadas do sistema", se não tiver essa opção basta procurar na lupa de pesquisa do windows.
- Na janela "Propriedades do sistema", clique no botão "Variáveis de ambiente...".
- Na seção "Variáveis de ambiente", encontre a variável chamada "Path" e clique em "Editar...".
- Na nova janela, clique em "Novo" e adicione o caminho para a pasta "bin" dentro da pasta onde você extraiu os arquivos do FFmpeg (por exemplo, C:\ffmpeg\bin).
- Clique em "OK" em todas as janelas para fechar as configurações.

## Passo 4: Verificar a instalação

Para verificar se a instalação foi bem-sucedida, abra o CMD e digite o seguinte comando:

```ffmpeg -version```

Se tudo estiver funcionandoo corretamente, você deve ver a versão do FFmpeg instalada.

# 🎶 Prefix

 ```!carlito [nome da música]```
