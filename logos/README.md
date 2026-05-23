# Logotipos J3F

Três variantes oficiais. Cada uma em múltiplas combinações de cor para diferentes fundos.

## Variantes

| Variante | Quando usar |
|---|---|
| **Logo primário** | Aplicação institucional padrão: capas, headers, papelaria, assinaturas, propostas. |
| **Logo secundário** | Espaços compactos: rodapé, footer, redes sociais, contextos onde o primário não cabe. |
| **Isotipo** | Apenas o símbolo, sem texto. Favicon, app icon, marca d'água, repetições em padrão. |

## Catálogo completo

### SVG (vetorial — preferencial)

| Arquivo | Variante | Cor | Uso |
|---|---|---|---|
| [svg/J3F_logo_primario_verde.svg](svg/J3F_logo_primario_verde.svg) | Primário | Verde | Fundo claro (branco, bege, verde claro) |
| [svg/J3F_logo_primario_branco.svg](svg/J3F_logo_primario_branco.svg) | Primário | Branco | Fundo escuro (verde escuro, preto) |
| [svg/J3F_logo_primario_preto.svg](svg/J3F_logo_primario_preto.svg) | Primário | Preto | Fundo claro, mono/print |
| [svg/J3F_logo_secundario_verde.svg](svg/J3F_logo_secundario_verde.svg) | Secundário | Verde | Compacto, fundo claro |
| [svg/J3F_isotipo_verde.svg](svg/J3F_isotipo_verde.svg) | Isotipo | Verde | Fundo claro |
| [svg/J3F_isotipo_branco.svg](svg/J3F_isotipo_branco.svg) | Isotipo | Branco | Fundo escuro |
| [svg/J3F_isotipo_preto.svg](svg/J3F_isotipo_preto.svg) | Isotipo | Preto | Fundo claro, mono/print |

### PNG (raster)

Para apps que não suportam SVG (alguns clientes de e-mail, Office antigo, integrações legadas). Mesmas variantes em [png/](png/), incluindo combinações pré-renderizadas com fundo:

- `J3F_logo_primario_branco_fundo_verde_escuro.png` — primário branco já compositado sobre `#005263`
- `J3F_logo_primario_verde_fundo_branco.png` — primário verde sobre branco

### PDF CMYK

Para impressão profissional (gráficas, papelaria). Disponíveis em [pdf/](pdf/) nas variantes primário (verde, preto, branco) e isotipo (verde).

### Avatar / Favicon

Três variantes circulares para perfis sociais e favicon em [avatar/](avatar/).

## Regras de aplicação

### Posicionamento

**Permitido:**
- Superior esquerdo (padrão para documentos e slides)
- Inferior esquerdo (rodapé)
- Superior centralizado (capas)
- Inferior centralizado (encerramento)

**Proibido:** lado direito. Em nenhuma circunstância.

### Área de não-interferência

Manter no mínimo **1× a altura do símbolo** ao redor do logo, livre de qualquer outro elemento. Margem visual respiratória que protege a legibilidade.

### Proporção

- **Sempre** redimensionar proporcionalmente
- **Nunca** achatar, esticar, aplicar skew ou shear
- **Nunca** distorcer a geometria do símbolo
- A relação largura/altura original é inegociável

### Tamanho mínimo

- Logo primário: 80px de largura em digital, 25mm em impresso
- Isotipo: 24px (favicon) a 16px (limite absoluto)

### Fundos

- **Fundo claro** (branco, bege, verde claro): usar versão **verde** ou **preto**
- **Fundo escuro** (verde escuro, preto): usar versão **branco**
- Fundos fotográficos: usar versão branco com camada de proteção (overlay sutil)
- Nunca aplicar sobre fundos que comprometam contraste mínimo WCAG AA

## Não fazer

- Recriar, redesenhar ou redigitalizar o logo
- Alterar cor além das variantes oficiais
- Aplicar efeitos (sombra, contorno, gradiente, brilho)
- Rotacionar
- Recortar
- Inserir dentro de formas (círculos, quadrados — exceto avatares oficiais)
- Combinar com outros logos sem espaço de respiração adequado

## Decisão rápida — qual variante usar?

```
Fundo claro + espaço amplo  → Primário Verde
Fundo claro + espaço limitado → Secundário Verde
Fundo escuro/verde escuro     → Primário Branco
Print mono / fax / OCR        → Primário Preto
Favicon / app icon            → Isotipo (cor conforme fundo)
Avatar social (Instagram, LinkedIn) → Avatar circular oficial
```

Detalhes completos no Manual de marca J3F 2026 (PDF), seções "Logotipo" e "Aplicação", páginas 22–34.
