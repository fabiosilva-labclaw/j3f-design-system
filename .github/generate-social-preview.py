"""
Gera o social-preview.png do repositório J3F Design System.

Dimensões: 1280x640 (proporção 2:1, recomendação GitHub).
Background: Verde Escuro #005263 (paleta institucional J3F 2026).
Logo: J3F_logo_primario_branco.png centralizado, com tagline em Manrope SemiBold.

Para regenerar:
  python3 .github/generate-social-preview.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parent.parent

# Canvas
W, H = 1280, 640
BG = "#005263"          # Verde Escuro institucional
ACCENT = "#00ACCA"      # Teal
SOFT = "#96C9D7"        # Verde Claro
WHITE = "#FFFFFF"

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# Logo branco — redimensionar mantendo proporção
logo = Image.open(REPO / "logos" / "png" / "J3F_logo_primario_branco.png").convert("RGBA")
target_logo_width = 520
aspect = logo.height / logo.width
new_size = (target_logo_width, int(target_logo_width * aspect))
logo = logo.resize(new_size, Image.LANCZOS)

# Posição logo: centralizado horizontalmente, um pouco acima do meio vertical
logo_x = (W - logo.width) // 2
logo_y = 150
img.paste(logo, (logo_x, logo_y), logo)

# Fontes Manrope
font_dir = REPO / "fonts" / "manrope"
font_tagline = ImageFont.truetype(str(font_dir / "Manrope-SemiBold.ttf"), 38)
font_descriptor = ImageFont.truetype(str(font_dir / "Manrope-Medium.ttf"), 16)

# Tagline principal
tagline = "Pagando o justo. Nem um centavo a mais."
tagline_bbox = draw.textbbox((0, 0), tagline, font=font_tagline)
tagline_w = tagline_bbox[2] - tagline_bbox[0]
tagline_h = tagline_bbox[3] - tagline_bbox[1]
tagline_x = (W - tagline_w) // 2
tagline_y = logo_y + logo.height + 70
draw.text((tagline_x, tagline_y), tagline, font=font_tagline, fill=WHITE)

# Linha decorativa em Teal — abaixo da tagline com folga para o descender
line_w = 80
line_x = (W - line_w) // 2
line_y = tagline_y + tagline_h + 50
draw.rectangle([line_x, line_y, line_x + line_w, line_y + 3], fill=ACCENT)

# Descritor — abaixo da linha
descriptor = "DESIGN  SYSTEM   ·   v2026.1   ·   MANROPE   ·   8  CORES  AUTORIZADAS"
descriptor_bbox = draw.textbbox((0, 0), descriptor, font=font_descriptor)
descriptor_w = descriptor_bbox[2] - descriptor_bbox[0]
descriptor_x = (W - descriptor_w) // 2
descriptor_y = line_y + 22
draw.text((descriptor_x, descriptor_y), descriptor, font=font_descriptor, fill=SOFT)

# Output
out = REPO / ".github" / "social-preview.png"
img.save(out, "PNG", optimize=True)
print(f"Saved: {out}")
print(f"Size: {out.stat().st_size:,} bytes")
print(f"Dimensions: {W}x{H}")
