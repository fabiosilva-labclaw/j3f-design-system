/**
 * J3F Brand Tokens 2026 — TypeScript constants
 * Source: brand.json | Manual de marca J3F 2026.pdf
 */

export const COLORS = {
  // Primary
  verdeEscuro: '#005263',
  teal:        '#00ACCA',
  verdeClaro:  '#96C9D7',
  // Secondary
  cobre:       '#9E947E',
  begeClaro:   '#EEE7D7',
  cinza:       '#999999',
  preto:       '#000000',
  branco:      '#FFFFFF',
  // Semantic aliases
  textPrimary:   '#000000',
  textSecondary: '#999999',
  textOnDark:    '#FFFFFF',
  bg:            '#FFFFFF',
  bgAlt:         '#EEE7D7',
  bgDark:        '#005263',
  accent:        '#00ACCA',
  accentSoft:    '#96C9D7',
  border:        '#96C9D7',
  divider:       '#999999',
} as const;

export const FONTS = {
  primary:  'Manrope',
  fallback: "Manrope, -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif",
  weights: {
    extraLight: 200,
    light:      300,
    regular:    400,
    medium:     500,
    semiBold:   600,
    bold:       700,
    extraBold:  800,
  },
  scale: {
    display: '4.5rem',
    h1:      '3rem',
    h2:      '2.25rem',
    h3:      '1.5rem',
    lead:    '1.3125rem',
    body:    '1rem',
    small:   '0.8125rem',
  },
} as const;

export const TAGLINES = {
  principal: 'Pagando o justo. Nem um centavo a mais.',
  manifesto: 'Precisão técnica. Inteligência fiscal.',
  descritor: 'Tax Intelligence',
  fullName:  'J3F Consultoria | Tax Intelligence',
} as const;

export const WORDS_TO_USE = [
  'Inteligência Fiscal', 'Precisão', 'Conformidade', 'Fôlego Financeiro',
  'Estratégico', 'Segurança Jurídica', 'Tecnologia', 'Dados',
  'Oportunidade', 'Justiça Fiscal', 'Auditoria Consultiva', 'Tranquilidade',
] as const;

export const WORDS_TO_AVOID = [
  'Burocracia', 'Problema', 'Desespero', 'Gastos',
  'Talvez', 'Acho', 'Tradicional',
] as const;

export const COMPANY = {
  legalName:   'J3F Consultoria',
  displayName: 'J3F Consultoria | Tax Intelligence',
  domain:      'j3f.com.br',
  address:     'São Paulo, SP',
} as const;

export type J3FColor = keyof typeof COLORS;
