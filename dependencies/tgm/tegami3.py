from PIL import Image, ImageDraw, ImageFont
import textwrap
import re


def create_text_image(text, font_path, font_size=24, max_width=1800, bold=True):
    # 创建一个高度为1的临时透明图像，仅用于测量文本尺寸
    img = Image.new("RGBA", (1, 1), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(font_path, font_size)

    # 将文本分行
    lines = textwrap.wrap(text, width=int(max_width // font_size * wrap_index))

    # 计算文本大小
    max_line_width = 0
    total_height = 0
    line_heights = []

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        line_width = bbox[2] - bbox[0]
        line_height = bbox[3] - bbox[1]
        max_line_width = max(max_line_width, line_width)
        total_height += line_height
        line_heights.append(line_height)

    # 为了不截断最后一行文字，将总高度加上一定的行间距
    line_spacing = font_size // 4
    total_height += len(lines) * line_spacing + 15

    # 创建适当大小的图像
    img = Image.new("RGBA", (max_width, total_height), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # 在图像上绘制文本
    y_text = 10
    x_text = 10
    for idx, line in enumerate(lines):
        if bold:
            for dx in [-2, -1, 0, 1, 2]:
                for dy in [-2, -1, 0, 1, 2]:
                    if dx != 0 or dy != 0:
                        draw.text((x_text + dx, y_text + dy), line, font=font, fill='black')

        draw.text((x_text, y_text), line, font=font, fill='white')
        y_text += line_heights[idx] + line_spacing

    return [img, total_height]


def get_text(fn):
    fn1 = fn + "_pt.txt"
    fn2 = fn + "_names.txt"
    t = list()
    with open(fn1, "r", encoding="utf-8") as f2, open(fn2, "r", encoding="utf-8") as f1:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        lines1 = list(map(str.strip, lines1))
        lines2 = list(map(lambda x: " " * 3 + x.strip(), lines2))

    t = list(zip(lines1, lines2))
    return t


def pdraw(fn, font_path, font_size, max_width):
    f2 = open(f"{fn}_wg.txt", "w", encoding="utf-8")
    for title, text in get_text(fn):    
        pd = create_text_image(text, font_path, font_size, max_width)
        image = pd[0]
        image.save(f"./new/{title.replace('.png', '')}_pt.png")
        print(f"{title}_cn.png\t{pd[1]}", file=f2)
        print(f"Generated image for: {title.replace('.png', '')}_pt.png")
    f2.close()


p1 = [5, 5, 4, 4, 7, 6, 6, 6]
p1_s = [0, 5, 9, 13, 20, 26, 32, 38]

def trans_height(wg, p, s):
    lt = []
    res = []
    def sum_n(t1, n1):
        return sum(t1[i:i+n1]) 
    with open(wg, 'r') as f1, open(f'{wg}_hg.txt', 'w') as f2:
        for line in f1.readlines():
            title, height = line.split('\t')
            height = int(height)
            lt.append(height)
    for i, start in zip(p, s):
        for x in range(i):
            res.append(sum(lt[start:start+x], linespace * x) + firstline_space)
    return res

def edit_svg(fn, wg, p, s):
    ht = trans_height(wg, p, s)
    count = 0

    def check(t1, t2):
        for i in range(len(t1)):
            if t1[i] in t2:
                return t1[i]
        return False

    pattern1 = r"<image (id='[^']*') x='[^']*' (y='[^']*') width='[^']*' (height='[^']*') xlink:href='[^']*'/>"

    def replace_line(match, y, width, title, height):
        return f"<image {match.group(1)} x='150' y='{y}' width='{width}' height='{height}' xlink:href='./{title}'/>"

    for title, text in get_text(fn):
        title = title.replace(".png", "")
        f3 = open(f'./new/{title}.svg', "w", encoding="utf-8")

        with open(f'{fn}_wg.txt', "r", encoding="utf-8") as f1, open(f'{title}.svg', "r", encoding="utf-8") as f2:
            lines1 = f1.readlines()
            dic = {}
            for line in lines1:
                title, width = line.split('\t')
                dic[title.replace('_cn.png', '')] = width.strip()

            lines2 = f2.readlines()
            for i in range(len(lines2)):
                ck = check(list(map(lambda x: x.replace('.png', ''), dic.keys())), lines2[i])
                if ck:
                    title = ck + ".png"
                    height = dic[title].strip()
                    title = ck + '_pt.png'
                    res = re.sub(pattern1, lambda m: replace_line(m, y=ht[count], width=iw, title=title, height=height), lines2[i])
                    print(res, end='', file=f3)
                    count += 1
                else:
                    print(lines2[i], end='', file=f3)

        print(f"Edited SVG for: {title}")

fp = "Alenor.otf"
fs = 50
iw = 1620
ih = 980
linespace = 10
firstline_space = 150
wrap_index = 2.5
pdraw("tgm3", fp, fs, iw)
edit_svg("tgm3", p1, p1_s)
