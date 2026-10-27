# Gerador de Lista de Marcos e Caixas — PDF Automático

Geração automática do PDF `MM_YYYY_Lista de Marcos e Caixas YYYYMMDD.pdf` a partir do relatório do IR
`PontosAcessoMarcosCaixasRpt3_YYYY_MM_DD.xls`, sem necessidade de Excel, Word ou PDFCreator.

## 🎯 Objetivo

Substituir o processo manual:
1. Relatório do IR → Excel (manual)
2. Copiar dados para template Excel
3. Macro de formatação
4. Copiar para template Word
5. Impressão para PDF (PDFCreator)

**Solução**: script Python que gera o PDF final em ~1 minuto, mantendo o layout oficial.

## 📋 Requisitos

- **Python 3.9+** (Windows)
- **Dependências**: `pip install xlrd reportlab`
- **Fonts**: Calibri instalado em `C:\Windows\Fonts\`
- Relatório do IR em formato `.xls`

## 🚀 Uso rápido

```powershell
# Mensal (recomendado)
python gerar_lista_marcos_caixas.py PontosAcessoMarcosCaixasRpt3_2026_10_09.xls `
  --base-dir C:\Users\atos91\Desktop\APPs\IR

# Output: C:\Users\atos91\Desktop\APPs\IR\Marcos e Caixas 10_2026\*_Lista_de_Marcos_e_Caixas_*.pdf
```

## 📖 Opções avançadas

```powershell
# Pasta de saída específica
python gerar_lista_marcos_caixas.py <xls> --out-dir <pasta>

# Data de referência manual (YYYY-MM-DD)
python gerar_lista_marcos_caixas.py <xls> --data-ref 2026-09-30

# Teste rápido (primeiras 100 linhas)
python gerar_lista_marcos_caixas.py <xls> --max-rows 100

# Sem ZIP
python gerar_lista_marcos_caixas.py <xls> --no-zip
```

| Opção | Descrição |
|-------|-----------|
| `--data-ref YYYY-MM-DD` | Data de referência (default: último dia do mês anterior) |
| `--base-dir <path>` | Cria `Marcos e Caixas MM_YYYY` dentro desta pasta |
| `--out-dir <path>` | Pasta de saída (default: pasta do `.xls`) |
| `--template-dir <path>` | Pasta do `.dotm` (default: pasta do script) |
| `--no-zip` | Não gera o ZIP |
| `--max-rows N` | Apenas primeiras N linhas (teste) |

## 📦 Ficheiros

| Ficheiro | Descrição |
|----------|-----------|
| `gerar_lista_marcos_caixas.py` | Script principal Python |
| `Listagem Global de Pontos de Acesso.dotm` | Template Word (imagens extraídas para capa/cabeçalho) |
| `README.md` | Este ficheiro |
| `requirements.txt` | Dependências Python |

## 🔧 Funcionamento

1. **Leitura** — Localiza cabeçalho ("Distrito") no relatório e extrai colunas B, D, G–P
2. **Capa** — Imagens do template, título e data de referência
3. **Quebra de texto** — Por espaços, após hífens, depois por caracteres (como Word)
4. **Paginação** — Linhas não partem entre páginas; cabeçalho repetido em cada página
5. **Página** — Logótipo, título, numeração e data de atualização
6. **ZIP** — Compressão deflate do PDF final

**Geometria**: A4 horizontal, margens conforme template (esq./dir. 1 cm, topo 3 cm, fundo 2 cm)

## 📊 Validação

Checklist mensal:
- [ ] Nº de registos impresso = linhas do relatório
- [ ] Capa com data correta (último dia do mês anterior)
- [ ] Rodapé com "Pág. N/Total" e data corretos
- [ ] Amostra de páginas (início, meio, fim) sem texto cortado

**Performance**: ~1 minuto de geração, PDF ~20 MB, ZIP ~13 MB

## ⚠️ Limitações

- Script assume estrutura atual do relatório do IR (cabeçalho em B, colunas em B, D, G–P)
- Depende de Calibri instalado (alternativa: Carlito, com ajuste em `register_fonts()`)
- Data deduzida do nome do ficheiro; confirmar ou forçar com `--data-ref`
- Geração do relatório no IR continua manual

## 🔄 Histórico de versões

| Versão | Data | Notas |
|--------|------|-------|
| 1.0 | 2024-04 | Substituição do processo manual com Word/Excel |
| 1.1 | 2026-10 | Documentação completa e publicação no repositório |

## 👥 Contacto / Suporte

Filipe — IR/CTT Portugal

---

**Última atualização**: 27 de outubro de 2026
