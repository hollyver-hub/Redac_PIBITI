from PIL import Image
import json

with open("data.json", 'r') as d:
    dados = json.load(d)

imagem = Image.open('Division/Paragraph/Paragraph1.png')


def recortar_imagem(dados, imagem):
    for anotacao in range(len(dados['annotations'][0]['result'])):
        x = (dados['annotations'][0]['result'][anotacao]['value']['x'] / 100)  * dados['annotations'][0]['result'][anotacao]['original_width']
        y = (dados['annotations'][0]['result'][anotacao]['value']['y'] / 100) * dados['annotations'][0]['result'][anotacao]['original_height']
        width = x + (dados['annotations'][0]['result'][anotacao]['value']['width'] / 100) * dados['annotations'][0]['result'][anotacao]['original_width']
        height = y + (dados['annotations'][0]['result'][anotacao]['value']['height'] / 100) * dados['annotations'][0]['result'][anotacao]['original_height']

        imagem_recortada = imagem.crop((x, y, width, height))

        imagem_recortada.save(f'./Division/Lines/Line{anotacao + 1}.png')


if __name__ == '__main__':
    recortar_imagem(dados, imagem)