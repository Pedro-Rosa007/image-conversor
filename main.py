import os
from PIL import Image
from tkinter import messagebox

# Importar plugins Pillow opcionalmente
try:
    import pillow_avif
    if hasattr(pillow_avif, "register_avif_opener"):
        pillow_avif.register_avif_opener()
except ImportError:
    pass

try:
    import pillow_heif
    if hasattr(pillow_heif, "register_heif_opener"):
        pillow_heif.register_heif_opener()
    if hasattr(pillow_heif, "register_avif_opener"):
        pillow_heif.register_avif_opener()
except ImportError:
    pass

try:
    import rawpy
except ImportError:
    pass



class Backend:
    ENTRADA_DIR = os.path.join("image", "a_converter")
    SAIDA_DIR = os.path.join("image", "convertidas")

    def _mostrar_mensagem(self, tipo, titulo, texto, parent=None):
        try:
            if tipo == "erro":
                messagebox.showerror(titulo, texto, parent=parent)
            else:
                messagebox.showinfo(titulo, texto, parent=parent)
        except Exception:
            print(f"{titulo}: {texto}")

    def _garantir_pastas(self):
        os.makedirs(self.ENTRADA_DIR, exist_ok=True)
        os.makedirs(self.SAIDA_DIR, exist_ok=True)
    
    def converter_e_limpar(self, parent=None):
        self._garantir_pastas()

        arquivos = [
            f
            for f in os.listdir(self.ENTRADA_DIR)
            if f.lower().endswith(('.avif', '.heic', '.heif', '.webp', '.raw', '.jpg', '.jpeg'))
        ]

        if not arquivos:
            self._mostrar_mensagem(
                "info",
                "Aviso",
                "Nenhum arquivo encontrado em image/a_converter!",
                parent=parent,
            )
            return

        self._mostrar_mensagem(
            "info",
            "Aviso",
            f"Encontradas {len(arquivos)} imagens. Iniciando processo...",
            parent=parent,
        )

        convertidas = 0
        erros = []
    
        for nome_arquivo in arquivos:
            caminho_entrada = os.path.join(self.ENTRADA_DIR, nome_arquivo)
            novo_nome = os.path.splitext(nome_arquivo)[0] + ".png"
            caminho_saida = os.path.join(self.SAIDA_DIR, novo_nome)

            try:
                if nome_arquivo.lower().endswith(".raw"):
                    if 'rawpy' not in globals():
                        raise ImportError("rawpy não está instalado para arquivos RAW")

                    raw = rawpy.imread(caminho_entrada)
                    try:
                        rgb = raw.postprocess()
                    finally:
                        raw.close()

                    img = Image.fromarray(rgb)
                else:
                    img = Image.open(caminho_entrada)

                img.save(caminho_saida, "PNG")
                os.remove(caminho_entrada)
                convertidas += 1
            except Exception as e:
                erros.append(f"{nome_arquivo}: {e}")

        if erros:
            self._mostrar_mensagem(
                "erro",
                "Concluido com erros",
                f"{convertidas} arquivo(s) convertido(s). {len(erros)} erro(s).",
                parent=parent,
            )
            return

        self._mostrar_mensagem(
            "info",
            "Sucesso",
            f"Processo concluido! {convertidas} arquivo(s) convertido(s) para image/convertidas.",
            parent=parent,
        )
        return
    
if __name__ == "__main__":
    app = Backend()
    app.converter_e_limpar()