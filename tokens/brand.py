"""
J3F Brand Tokens 2026 — Python constants
Source: brand.json | Manual de marca J3F 2026.pdf
Use: from brand import COLORS, FONTS, TAGLINES
"""

from typing import Final

# === COLORS — HEX ===
COLORS: Final = {
    # Primary
    "verde_escuro":  "#005263",
    "teal":          "#00ACCA",
    "verde_claro":   "#96C9D7",
    # Secondary
    "cobre":         "#9E947E",
    "bege_claro":    "#EEE7D7",
    "cinza":         "#999999",
    "preto":         "#000000",
    "branco":        "#FFFFFF",
    # Semantic
    "text_primary":   "#000000",
    "text_secondary": "#999999",
    "text_on_dark":   "#FFFFFF",
    "bg":             "#FFFFFF",
    "bg_alt":         "#EEE7D7",
    "bg_dark":        "#005263",
    "accent":         "#00ACCA",
    "accent_soft":    "#96C9D7",
    "border":         "#96C9D7",
    "divider":        "#999999",
}

# === COLORS — RGB tuples (0-255), úteis para python-pptx, openpyxl, reportlab ===
RGB: Final = {
    "verde_escuro": (0, 82, 99),
    "teal":         (0, 172, 202),
    "verde_claro":  (150, 201, 215),
    "cobre":        (158, 148, 126),
    "bege_claro":   (238, 231, 215),
    "cinza":        (153, 153, 153),
    "preto":        (0, 0, 0),
    "branco":       (255, 255, 255),
}

# === TYPOGRAPHY ===
FONTS: Final = {
    "primary": "Manrope",
    "fallback": "Manrope, -apple-system, Segoe UI, system-ui, sans-serif",
    "weights": {
        "extra_light": 200,
        "light":       300,
        "regular":     400,
        "medium":      500,
        "semi_bold":   600,
        "bold":        700,
        "extra_bold":  800,
    },
    "scale_pt": {
        "display": 72,
        "h1":      48,
        "h2":      36,
        "h3":      24,
        "lead":    21,
        "body":    12,
        "body_doc": 11,
        "small":   9,
    },
}

# === VOICE / TAGLINES ===
TAGLINES: Final = {
    "principal":  "Pagando o justo. Nem um centavo a mais.",
    "manifesto":  "Precisão técnica. Inteligência fiscal.",
    "descritor":  "Tax Intelligence",
    "full_name":  "J3F Consultoria | Tax Intelligence",
}

WORDS_TO_USE: Final = (
    "Inteligência Fiscal", "Precisão", "Conformidade", "Fôlego Financeiro",
    "Estratégico", "Segurança Jurídica", "Tecnologia", "Dados",
    "Oportunidade", "Justiça Fiscal", "Auditoria Consultiva", "Tranquilidade",
)

WORDS_TO_AVOID: Final = (
    "Burocracia", "Problema", "Desespero", "Gastos",
    "Talvez", "Acho", "Tradicional",
)

# === COMPANY ===
COMPANY: Final = {
    "legal_name":   "J3F Consultoria",
    "display_name": "J3F Consultoria | Tax Intelligence",
    "domain":       "j3f.com.br",
    "address":      "São Paulo, SP",
}


def hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
    """#005263 -> (0, 82, 99)"""
    h = hex_str.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))  # type: ignore
