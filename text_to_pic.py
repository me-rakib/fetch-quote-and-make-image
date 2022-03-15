from PIL import Image, ImageDraw, ImageFont

def make_pic_with_text(quote_text):
    # variable for image size
    height = 612
    width = 612

    img = Image.new('RGB', (height, width), color=(21, 23, 24))  # background 
    d = ImageDraw.Draw(img)

    # font
    fnt = ImageFont.truetype('./Ubuntu-Regular.ttf', 20)
    sum = 0
    for letter in quote_text:
        sum += d.textsize(letter, font=fnt)[0]

    avg_length_of_letter = sum / len(quote_text)

    num_of_letter_for_each_line = (height/1.618) / avg_length_of_letter
    increment = 0
    fresh_sentence = ""

    # add some line break
    for letter in quote_text:
        if letter == "-":
            fresh_sentence += '\n\n' + letter
        elif increment < num_of_letter_for_each_line:
            fresh_sentence += letter
        else:
            if letter == ' ':
                fresh_sentence += '\n'
                increment = 0
            else:
                fresh_sentence += letter
        increment += 1

    # render text in the center of the box
    dim = d.textsize(fresh_sentence, font=fnt)
    height2 = dim[0]
    width2 = dim[1]

    qx = (height/2 - height2/2)
    qy = (width/2 - width2/2)

    # create text at 0,0 location on the image
    d.text((qx,qy), fresh_sentence, align="center", font=fnt, fill=(251, 251, 255))
    # 220, 220, 170   223, 213, 137 

    # save image in current directory
    img.save('quote.png')


# code from - https://muthu.co/instagram-quotes-generator-using-python-pil/