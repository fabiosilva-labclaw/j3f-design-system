# Tipografia J3F

## Família única — Manrope

**Manrope** é a única fonte da marca. Sem fontes secundárias, sem serifadas, sem fontes de sistema como fallback principal (apenas em emergência via cascata CSS).

Sans-serif geométrica moderna. Altura reduzida, linhas retas estruturadas, pingo quadrado. Transmite tecnologia, precisão e clareza executiva.

## Pesos

| Peso | Valor numérico | Quando usar |
|---|---|---|
| ExtraLight | 200 | Ornamental, números grandes em dashboards |
| Light | 300 | Citações longas, texto editorial |
| Regular | 400 | **Corpo de texto padrão** |
| Medium | 500 | Texto enfatizado leve, captions importantes |
| SemiBold | 600 | **Títulos H1–H3, display, labels de KPI** |
| Bold | 700 | Negrito dentro do corpo, destaque crítico |
| ExtraBold | 800 | Hero numérico, headlines de impacto |

Padrão da marca: **400 Regular** para corpo, **600 SemiBold** para títulos. Bold (700) e ExtraBold (800) usados com parcimônia, apenas para destaque genuíno.

## Escala tipográfica

| Estilo | Tamanho | Peso | Line-height | Uso |
|---|---|---|---|---|
| Display | 72pt | SemiBold 600 | 1.05 | Capas, hero de apresentação |
| H1 | 48pt | SemiBold 600 | 1.1 | Títulos de capítulo |
| H2 | 36pt | SemiBold 600 | 1.15 | Títulos de seção |
| H3 | 24pt | SemiBold 600 | 1.2 | Subtítulos |
| Lead | 21pt | Regular 400 | 1.4 | Texto introdutório, abertura de seção |
| Body | 12pt | Regular 400 | 1.5 | Corpo de texto em Word/parecer |
| Body Doc | 11pt | Regular 400 | 1.5 | **Corpo padrão de pareceres tributários** |
| Small | 9pt | Regular 400 | 1.4 | Notas de rodapé, captions, metadados |

## Aplicação por suporte

### Documento Word (pareceres, relatórios)

- Corpo: Body Doc (11pt, Regular, line-height 1.5)
- Títulos H1: 18pt SemiBold (escala reduzida para Word)
- Títulos H2: 14pt SemiBold
- Margens: topo 2,5cm, base 2,5cm, esquerda 3cm, direita 2cm

### Slide PPTX

- Hero/Display: 72pt SemiBold
- Título de slide (H1): 32pt SemiBold
- Subtítulo: 20pt Regular
- Body: 18pt Regular
- Caption: 12pt Regular

### Planilha XLSX

- Header de coluna: 11pt SemiBold
- Corpo: 10pt Regular
- Totalizador: 11pt Bold

### Web / app

- Hero (landing): clamp(48px, 8vw, 96px) SemiBold
- H1: 36–48px SemiBold
- H2: 24–32px SemiBold
- H3: 20px SemiBold
- Body: 16px Regular, line-height 1.6
- Small: 14px Regular

### E-mail

- Assinatura: 13–14px Regular
- Nome: 14px SemiBold
- Cargo/OAB: 12px Regular Cinza

## Regras gerais

- **Hierarquia clara.** Cada nível visual deve ser distinguível à primeira vista. Não usar tamanhos próximos (ex: 13pt e 14pt) na mesma página.
- **Line-height generoso.** Corpo de texto sempre ≥ 1.5. Títulos podem cair para 1.05–1.2.
- **Tracking padrão.** Não comprimir nem expandir letter-spacing por estética. Caso queira ênfase, mudar peso, não tracking.
- **Capitalização.** Títulos em **sentence case** (apenas primeira letra maiúscula), nunca CAPS LOCK exceto em badges/labels curtos (máx. 3 palavras).
- **Alinhamento.** Esquerda por padrão. Centralizar apenas em capas, citações e CTAs isolados. Nunca justificado em web. Em DOCX, evitar justificado em pareceres exceto se solicitado por convenção do cliente.

## Cascata CSS recomendada

```css
font-family: "Manrope", -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
```

A cascata só entra em ação se Manrope falhar ao carregar (offline, bloqueio de CDN). Em ambiente controlado (apps internos, PDFs gerados), embed do TTF garante 100%.

## Fontes descontinuadas em 2025

As seguintes fontes foram **removidas** do brand kit:

- **Georgia** — substituir por Manrope SemiBold
- **Calibri** — substituir por Manrope Regular
- **Playfair Display** — substituir por Manrope SemiBold ou ExtraBold
- **DM Sans** — substituir por Manrope Regular

Qualquer template, app ou documento ainda usando essas fontes deve ser **migrado para Manrope**.

## Token canônico

A escala completa está codificada em [../tokens/brand.json](../tokens/brand.json) sob `typography.scale`. Arquivos da fonte em [../fonts/manrope/](../fonts/manrope/).
