# Paleta J3F 2026

Paleta única e fechada. Apenas estas oito cores são autorizadas. Cores fora desta lista são proibidas em qualquer aplicação J3F.

## Primárias

### Verde Escuro
**`#005263`** · `rgb(0, 82, 99)` · `cmyk(98, 45, 42, 33)`

Cor institucional principal. Headers, capas, fundos escuros, encerramentos.

### Teal
**`#00ACCA`** · `rgb(0, 172, 202)` · `cmyk(83, 0, 19, 0)`

Cor de destaque. Acentos, CTAs, links, gráficos analíticos, dataviz primária.

### Verde Claro
**`#96C9D7`** · `rgb(150, 201, 215)` · `cmyk(50, 2, 16, 0)`

Apoio. Backgrounds suaves, divisores, dataviz secundária, hover states.

## Secundárias

### Cobre
**`#9E947E`** · `rgb(158, 148, 126)` · `cmyk(36, 32, 47, 15)`

Acento neutro quente. Detalhes premium, separadores, ícones secundários.

### Bege Claro
**`#EEE7D7`** · `rgb(238, 231, 215)` · `cmyk(7, 9, 19, 0)`

Background quente. Cards, blocos de citação, callouts de destaque.

### Cinza
**`#999999`** · `rgb(153, 153, 153)` · `cmyk(41, 32, 32, 11)`

Texto secundário, captions, metadados, estados desabilitados.

### Preto
**`#000000`** · `rgb(0, 0, 0)` · `cmyk(0, 0, 0, 100)`

Texto corrido em fundos claros. Bordas técnicas, ícones funcionais.

### Branco
**`#FFFFFF`** · `rgb(255, 255, 255)` · `cmyk(0, 0, 0, 0)`

Background principal de documentos e slides. Tipografia sobre fundo escuro.

## Combinações recomendadas

| Fundo | Texto primário | Texto secundário | Acento |
|---|---|---|---|
| Branco | Preto | Cinza | Teal |
| Bege Claro | Preto | Cinza | Verde Escuro |
| Verde Claro | Verde Escuro | Cinza | Teal |
| Verde Escuro | Branco | Verde Claro | Teal |
| Preto | Branco | Cinza | Teal |

## Tokens semânticos

| Token | Valor | Aplicação |
|---|---|---|
| `--j3f-text-primary` | `#000000` | Texto corrido |
| `--j3f-text-secondary` | `#999999` | Metadados |
| `--j3f-text-on-dark` | `#FFFFFF` | Texto sobre fundo escuro |
| `--j3f-bg` | `#FFFFFF` | Background padrão |
| `--j3f-bg-alt` | `#EEE7D7` | Background secundário |
| `--j3f-bg-dark` | `#005263` | Background escuro |
| `--j3f-accent` | `#00ACCA` | Destaque, CTA |
| `--j3f-accent-soft` | `#96C9D7` | Hover, divisores |
| `--j3f-border` | `#96C9D7` | Bordas suaves |
| `--j3f-divider` | `#999999` | Separadores |

## Acessibilidade

Combinações testadas contra **WCAG 2.1 AA** (contraste mínimo 4.5:1 para texto normal, 3:1 para texto grande):

- ✅ Preto sobre Branco: 21:1
- ✅ Branco sobre Verde Escuro: 8.6:1
- ✅ Branco sobre Preto: 21:1
- ✅ Verde Escuro sobre Branco: 8.6:1
- ✅ Verde Escuro sobre Bege Claro: 7.9:1
- ✅ Verde Escuro sobre Verde Claro: 3.2:1 (apenas texto grande/h2+)
- ⚠️ Teal sobre Branco: 2.9:1 — evitar para corpo de texto, ok para títulos
- ⚠️ Cobre sobre Branco: 2.8:1 — evitar para corpo de texto

Quando em dúvida, preferir Verde Escuro ou Preto para texto principal sobre fundo claro, Branco sobre fundo escuro.

## Cores descontinuadas em 2025

As seguintes cores foram **removidas** do brand kit e não podem ser usadas em nenhum material J3F:

| HEX | Nome legado | Substituir por |
|---|---|---|
| `#505459` | Cinza antigo | `#999999` (Cinza) |
| `#54BFC3` | Teal antigo | `#00ACCA` (Teal) |
| `#3A9EA2` | Teal escuro antigo | `#005263` (Verde Escuro) |
| `#7DD4D7` | Teal claro antigo | `#96C9D7` (Verde Claro) |
| `#D4F0F1` | Teal pálido antigo | `#EEE7D7` (Bege Claro) ou `#96C9D7` |
| `#F7F8F9` | Off-white antigo | `#FFFFFF` (Branco) |
| `#2C3E50` | Navy antigo | `#005263` (Verde Escuro) ou `#000000` |
| `#D4A853` | Gold antigo | `#9E947E` (Cobre) |

Qualquer template, app ou documento ainda usando essas cores deve ser **migrado**.
