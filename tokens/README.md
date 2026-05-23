# Design Tokens

Fonte de verdade técnica do brand kit J3F 2026. Cinco formatos sincronizados a partir do mesmo conteúdo. `brand.json` é o canônico — se houver divergência entre arquivos, ele vence.

## Arquivos

| Arquivo | Formato | Quando usar |
|---|---|---|
| [brand.json](brand.json) | W3C Design Tokens | Canônico. Consumo por LLMs, Figma, Style Dictionary, ferramentas de design. |
| [brand.css](brand.css) | CSS Custom Properties | Sites estáticos, HTML, componentes web sem build step. |
| [brand.scss](brand.scss) | SCSS Variables | Projetos com Sass/preprocessador. |
| [brand.ts](brand.ts) | TypeScript const | React, Vue, Svelte, qualquer projeto JS com tipagem. |
| [brand.py](brand.py) | Python module | Streamlit, scripts internos, geração de PPTX/DOCX/XLSX. |

## Schema

Estrutura do `brand.json` segue [W3C Design Tokens Community Group](https://design-tokens.github.io/community-group/format/):

```
brand.colors.primary.verdeEscuro.hex    → "#005263"
brand.colors.primary.teal.hex            → "#00ACCA"
brand.colors.semantic.accent             → "#00ACCA"
brand.typography.fontFamily.primary      → "Manrope"
brand.typography.weights.semiBold        → 600
brand.typography.scale.h1                → { size: "48pt", weight: 600, ... }
brand.logo.rules.forbiddenPositions      → ["lado-direito"]
brand.voice.taglines.principal           → "Pagando o justo. Nem um centavo a mais."
```

## Exemplos de consumo

### HTML estático

```html
<link rel="stylesheet" href="brand.css">
<style>
  body { font-family: var(--j3f-font-primary); }
  .header { background: var(--j3f-verde-escuro); color: var(--j3f-branco); }
  .cta { background: var(--j3f-teal); }
</style>
```

### React + TypeScript

```tsx
import brand from "./brand";

export const Card = () => (
  <div style={{
    background: brand.colors.secondary.begeClaro,
    fontFamily: brand.typography.fontFamily.primary,
  }}>
    Conteúdo
  </div>
);
```

### Streamlit + Python

```python
from brand import COLORS, TYPOGRAPHY

st.markdown(f"""
<style>
  .stApp {{ font-family: {TYPOGRAPHY['family']}; }}
  h1 {{ color: {COLORS['verde_escuro']}; }}
  .accent {{ color: {COLORS['teal']}; }}
</style>
""", unsafe_allow_html=True)
```

### Style Dictionary (gerar outros formatos)

`brand.json` é compatível com [Style Dictionary](https://amzn.github.io/style-dictionary/). Para gerar tokens em formatos adicionais (Android XML, iOS Swift, Flutter):

```bash
npx style-dictionary build --config sd.config.js
```

## Sincronização entre formatos

Quando alterar um token, atualizar **todos os arquivos**. Roteiro de PR descrito em [../CONTRIBUTING.md](../CONTRIBUTING.md).

Validação manual: rodar `diff` entre as cores hex nos cinco arquivos para garantir paridade.
