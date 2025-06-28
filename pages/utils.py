import re

def parse_description(desc: str) -> str:
    # 1. Заменить *жирный текст* на <b>жирный текст</b>
    desc = re.sub(r'\*(.*?)\*', r'<b>\1</b>', desc)

    # 2. Обработка специальных ссылок вида >[текст](ссылка)
    def custom_link_block(match):
        text = match.group(1)
        url = match.group(2)
        return (
            f'<a href="{url}" class="custom-link-block">'
            f'<img src="{{% static \'assets/link_arrow.png\' %}}" alt="link arrow">'
            f'<span>{text}</span>'
            f'</a>'
        )
    desc = re.sub(r'>\[(.*?)\]\((.*?)\)', custom_link_block, desc)

    # 3. Заменить [текст](ссылка) на <a href="ссылка">текст</a>
    desc = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', desc)

    # 4. Обработка кастомного блока [[ текст1 ]]-[[ текст2 ]]
    def double_span_block(match):
        text1 = match.group(1).strip()
        text2 = match.group(2).strip()
        return (
            f'<div class="double-span-block">'
            f'<span>{text1}</span>'
            f'<span>{text2}</span>'
            f'</div>'
        )
    desc = re.sub(r'\[\[\s*(.*?)\s*\]\]-\[\[\s*(.*?)\s*\]\]', double_span_block, desc)

    # 5. Заменить {подпись}<ссылка>|позиция на блок с изображением
    def image_block(match):
        caption = match.group(1).strip()
        url = match.group(2).strip()
        position = match.group(3).strip().lower()

        if position == 'center':
            float_class = 'image-block-center'
        elif position == 'right':
            float_class = 'image-block-right'
        else:
            float_class = 'image-block-left'

        return (
            f'<div class="image-block {float_class}">'
            f'<img src="{url}" alt="{caption}">'
            f'<p>{caption}</p>'
            f'</div>'
        )
    desc = re.sub(r'\{(.*?)\}<([^>]+)>\|(\w+)', image_block, desc)

    # 6. Заменить #Текст# на <h1 class="generic-inner-title">Текст</h1>
    desc = re.sub(r'#(.*?)#', r'<h1 class="generic-inner-title">\1</h1>', desc)

    # 7. Обработка списков: строки с "- текст"
    lines = desc.splitlines()
    in_list = False
    new_lines = []

    for line in lines:
        if line.strip().startswith("- "):
            if not in_list:
                new_lines.append("<ul>")
                in_list = True
            new_lines.append(f"<li>{line.strip()[2:].strip()}</li>")
        else:
            if in_list:
                new_lines.append("</ul>")
                in_list = False
            new_lines.append(line)

    if in_list:
        new_lines.append("</ul>")

    return "\n".join(new_lines)

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90,  50, 40,
        10, 9,   5, 4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    roman = ""
    for i in range(len(val)):
        count = num // val[i]
        roman += syms[i] * count
        num %= val[i]
    return roman