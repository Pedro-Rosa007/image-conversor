# Image Conversor 🖼️

Um conversor automático de imagens com interface gráfica, desenvolvido em Python. Converte múltiplos formatos de imagem incluindo AVIF, HEIF, RAW e outros formatos populares.

## ✨ Características

- 🎨 **Interface Gráfica Intuitiva** - Desenvolvida com customtkinter
- 🔄 **Conversão em Batch** - Processa múltiplas imagens automaticamente
- 📁 **Organização Automática** - Salva imagens convertidas em pasta específica
- 🎞️ **Suporte Múltiplos Formatos** - AVIF, HEIF, RAW, JPG, PNG, BMP, WebP e mais
- ⚡ **Processamento Rápido** - Otimizado com Pillow

## 📋 Requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Pedro-Rosa007/image-conversor.git
cd image-conversor
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv .venv
```

3. Ative o ambiente virtual:

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

4. Instale as dependências:
```bash
pip install pillow customtkinter pillow-avif pillow-heif rawpy
```

## 📖 Como Usar

1. Inicie a aplicação:
```bash
python frontend.py
```

2. A interface gráfica abrirá
3. Coloque as imagens que deseja converter na pasta `image/a_converter/`
4. Clique no botão de conversão
5. As imagens convertidas estarão em `image/convertidas/`

## 📁 Estrutura do Projeto

```
image-conversor/
├── main.py              # Backend - lógica de conversão
├── frontend.py          # Frontend - interface gráfica
├── README.md            # Este arquivo
└── image/
    ├── a_converter/     # Imagens a converter (entrada)
    └── convertidas/     # Imagens convertidas (saída)
```

## 🔧 Dependências

| Pacote | Descrição |
|--------|-----------|
| `pillow` | Processamento de imagens |
| `customtkinter` | Interface gráfica moderna |
| `pillow-avif` | Suporte para formato AVIF |
| `pillow-heif` | Suporte para formatos HEIF/HEIC |
| `rawpy` | Suporte para arquivos RAW |

## 💡 Exemplos de Uso

### Adicione imagens à pasta de entrada
```
image/a_converter/
├── foto1.jpg
├── foto2.png
└── foto3.heic
```

### Execute o conversor
A aplicação processará todas as imagens e salvará em:
```
image/convertidas/
├── foto1.jpg
├── foto2.png
└── foto3.jpg
```

## 🐛 Solução de Problemas

### Erro ao abrir a GUI
- Verifique se o ambiente virtual está ativado
- Reinstale o customtkinter: `pip install --upgrade customtkinter`

### Imagens não encontradas
- Certifique-se de que estão na pasta `image/a_converter/`
- Verifique as permissões da pasta

### Erro ao converter formato específico
- Instale o plugin correspondente:
  - AVIF: `pip install pillow-avif`
  - HEIF: `pip install pillow-heif`
  - RAW: `pip install rawpy`

## 📝 Licença

Este projeto é de código aberto. Sinta-se livre para usar e modificar.

## 👤 Autor

**Pedro Rosa** - [@Pedro-Rosa007](https://github.com/Pedro-Rosa007)

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para:
1. Fazer um Fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

---

**Desenvolvido com ❤️ por Pedro Rosa**
