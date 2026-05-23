# Como contribuir

Este é o brand kit oficial da J3F Consultoria. Alterações em tokens, logos ou regras de uso impactam todos os produtos digitais da empresa, então passam por revisão obrigatória.

## Quem pode propor mudanças

- **Colaboradores J3F:** abrir issue ou PR direto.
- **Designers externos contratados:** abrir issue com justificativa técnica antes do PR.
- **Comunidade:** abrir issue. PRs em código de tokens/exemplos são bem-vindos, alterações de assets visuais não são aceitas externamente.

## Tipos de contribuição

### 1. Token novo ou alterado (cor, espaçamento, fonte)

1. Abrir issue usando o template **brand-update**
2. Justificar a mudança (uso real, problema observado, decisão de design)
3. Atualizar **todos os formatos** consistentemente:
   - `tokens/brand.json` (canônico)
   - `tokens/brand.css`
   - `tokens/brand.scss`
   - `tokens/brand.ts`
   - `tokens/brand.py`
4. Atualizar [docs/color-palette.md](docs/color-palette.md) ou [docs/typography.md](docs/typography.md) conforme aplicável
5. Bump na versão em `manifest.json` e `package.json`
6. Entrada no [CHANGELOG.md](CHANGELOG.md)

### 2. Novo asset (logo, ícone)

Não aceitos via PR externo. Falar com [fabio@j3f.com.br](mailto:fabio@j3f.com.br).

### 3. Documentação ou exemplos

PR direto. Manter tom J3F (autoritário acessível, sem juridiquês, sem advérbios vazios). Validar contra [docs/tom-de-voz.md](docs/tom-de-voz.md).

### 4. Correção de bug em código de exemplo

PR direto.

## Padrões de commit

Formato em português, prefixado por tipo:

- `feat:` — funcionalidade nova (token, exemplo, doc)
- `fix:` — correção
- `docs:` — documentação
- `refactor:` — reorganização sem mudança funcional
- `chore:` — manutenção, deps, configs

Exemplo: `feat: adiciona token de spacing para grids 24px`

## Antes de abrir o PR

- [ ] Mudança consistente em **todos os formatos** de token
- [ ] Documentação atualizada se aplicável
- [ ] Sem cores fora da paleta J3F 2026
- [ ] Sem fontes fora de Manrope
- [ ] Exemplos HTML validados visualmente
- [ ] CHANGELOG atualizado

## Versionamento

`AAAA.X`:
- **AAAA** = ano da revisão maior da marca (2026 atual)
- **X** = incremento dentro do ano (2026.1, 2026.2…)

Revisão maior de marca (novo manual, paleta nova) avança o ano.

## Contato

- Questões técnicas: abrir issue
- Uso comercial / autorização: [fabio@j3f.com.br](mailto:fabio@j3f.com.br)
