# Manrope — Fonte oficial J3F

**Manrope** é a única fonte da marca J3F. Sans-serif moderna, geométrica, com altura reduzida, linhas retas estruturadas e pingo quadrado. Transmite tecnologia, precisão e clareza executiva.

## Arquivos

### Pesos estáticos

| Peso | Valor | Arquivo |
|---|---|---|
| ExtraLight | 200 | [manrope/Manrope-ExtraLight.ttf](manrope/Manrope-ExtraLight.ttf) |
| Light | 300 | [manrope/Manrope-Light.ttf](manrope/Manrope-Light.ttf) |
| Regular | 400 | [manrope/Manrope-Regular.ttf](manrope/Manrope-Regular.ttf) |
| Medium | 500 | [manrope/Manrope-Medium.ttf](manrope/Manrope-Medium.ttf) |
| SemiBold | 600 | [manrope/Manrope-SemiBold.ttf](manrope/Manrope-SemiBold.ttf) |
| Bold | 700 | [manrope/Manrope-Bold.ttf](manrope/Manrope-Bold.ttf) |
| ExtraBold | 800 | [manrope/Manrope-ExtraBold.ttf](manrope/Manrope-ExtraBold.ttf) |

### Variable Font

[manrope/Manrope-VariableFont_wght.ttf](manrope/Manrope-VariableFont_wght.ttf) — único arquivo cobrindo todo o range de peso 200–800. Preferencial para web e apps modernos.

## Instalação

### macOS

1. Abrir os arquivos `.ttf` no Font Book
2. Clicar em "Instalar fonte"
3. Confirmar instalação para todos os usuários

### Windows

1. Selecionar todos os `.ttf`
2. Clicar com botão direito → "Instalar para todos os usuários"

### Web (CSS)

```css
@font-face {
  font-family: "Manrope";
  src: url("fonts/manrope/Manrope-VariableFont_wght.ttf") format("truetype-variations");
  font-weight: 200 800;
  font-display: swap;
}

body {
  font-family: "Manrope", -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
}
```

### Google Fonts (alternativa rápida)

```html
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&display=swap" rel="stylesheet">
```

A versão do Google Fonts é idêntica à local. Os arquivos no repo garantem disponibilidade offline e em apps nativos.

## Aplicação no brand

Escala completa documentada em [../docs/typography.md](../docs/typography.md) e codificada em [../tokens/brand.json](../tokens/brand.json) → `typography.scale`.

Resumo:

| Estilo | Tamanho | Peso |
|---|---|---|
| Display | 72pt | 600 SemiBold |
| H1 | 48pt | 600 SemiBold |
| H2 | 36pt | 600 SemiBold |
| H3 | 24pt | 600 SemiBold |
| Lead | 21pt | 400 Regular |
| Body | 12pt | 400 Regular |
| Body Doc (pareceres) | 11pt | 400 Regular |
| Small | 9pt | 400 Regular |

## Fontes descontinuadas

Em 2025, as seguintes fontes foram **removidas** do brand kit:

- Georgia
- Calibri
- Playfair Display
- DM Sans

Qualquer template, app ou documento ainda usando essas fontes deve ser **migrado para Manrope**.

## Licença

Manrope é distribuída sob a [SIL Open Font License 1.1](manrope/OFL.txt). Permite uso comercial, redistribuição, modificação e embed em produtos, desde que a licença seja preservada e a fonte modificada não use o nome "Manrope".

Copyright 2018 The Manrope Project Authors. Projeto original: https://github.com/sharanda/manrope
