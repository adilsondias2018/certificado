from PIL import Image, ImageFilter, ImageDraw, ImageFont

convidados = ['Karla Santos', 'Erik Jose', 'Oliver Oliveira', 'Guido Mateiga']

image1= Image.open("./template.png")
new_image = image1.resize((100,100))


# image.rotate(45).filter(ImageFilter.GaussianBlur(radius= -5)).save("./novo_certificado.png")

font1 = ImageFont.truetype("./Phetsarath_OT.ttf",size=35)
font2 = ImageFont.truetype("./LiberationSerif-Regular.ttf",size=35)


for convidado in convidados:

    image = Image.open("./certificado.png").convert("RGBA")
    
    
    image.paste(new_image,(400,180))

    lapis = ImageDraw.Draw(image)

    
    lapis.text(
        (280,360),
        text= f' {convidado}',
        fill="#000",
        font=font2
    )

    lapis.text(
        (280,440),
        text="Mirtes Dias de Olivera",
        fill="#000",
        font=font1
    )

    lapis.text(
        (250,600),
        text="Jarmira Santos",
        fill="#000",
        font=font1
    )

    lapis.text(
        (600,600),
        text="Alexandra Gonçalves Oliveira",
        fill="#000",
        font=font1
    )

    image.save(f"./certificado_{convidado}.png")