## 📝 Descrição

Adicionar ferramenta de geração automática de PDF — **Marcos e Caixas**.

Substitui o processo manual com Word/Excel/PDFCreator por um script Python que:
- Lê relatório do IR em formato XLS
- Gera PDF profissional em ~1 minuto
- Embala tudo num ZIP para arquivo

## 🎯 Objetivo

Automação mensal da geração do PDF `MM_YYYY_Lista de Marcos e Caixas YYYYMMDD.pdf` baseado no relatório `PontosAcessoMarcosCaixasRpt3_YYYY_MM_DD.xls`.

## 📂 Mudanças

- **Novo diretório**: `tools/gerar-lista-marcos-caixas/`
- **Ficheiros principais**:
  - `gerar_lista_marcos_caixas.py` — Script Python (10.4 KB)
  - `check_env.py` — Verificador de ambiente
  - `requirements.txt` — Dependências (xlrd, reportlab)
  - `Listagem Global de Pontos de Acesso.dotm` — Template (177.5 KB)

- **Documentação** (6 ficheiros):
  - `README.md` — Overview e uso
  - `INSTALL.md` — Setup detalhado
  - `PUBLICAR_GITHUB.md` — Guia de publicação
  - `INDEX.md` — Mapa de documentação
  - `SUMMARY.md` — Resumo completo
  - `CHANGELOG.md` — Histórico

## ✅ Verificações efetuadas

- [x] Python 3.9+ funciona
- [x] Dependências instaladas (xlrd, reportlab)
- [x] Calibri font disponível
- [x] Template .dotm com imagens OK
- [x] Script testado com relatório real (100 linhas → PDF 101 páginas)
- [x] Documentação completa
- [x] Git versionado (5 commits)
- [x] Sem dados sensíveis ou credenciais

## 🚀 Como usar

```powershell
# Instalar dependências
pip install -r tools/gerar-lista-marcos-caixas/requirements.txt

# Gerar PDF mensal
python tools/gerar-lista-marcos-caixas/gerar_lista_marcos_caixas.py `
  PontosAcessoMarcosCaixasRpt3_2026_10_09.xls `
  --base-dir C:\dados\IR

# Ver ajuda
python tools/gerar-lista-marcos-caixas/gerar_lista_marcos_caixas.py --help
```

## 📊 Benefícios

| Antes | Depois |
|-------|--------|
| ⏱️ Processo manual: 2-3 horas | ⚡ Automático: ~1 minuto |
| 📝 Excel + Word + PDFCreator | 🐍 Apenas Python |
| ❌ Sem versionamento | ✓ Git versionado |
| 📚 Sem documentação | ✓ Documentação profissional |
| 🔄 Difícil manter | ✓ Fácil de manter/expandir |

## 📚 Documentação

Ler primeiro: `tools/gerar-lista-marcos-caixas/INDEX.md`

Depois:
- `README.md` — Overview técnico
- `INSTALL.md` — Setup e troubleshooting
- `PUBLICAR_GITHUB.md` — Publicação futura

## 🔗 Referências

- Relatório do IR: `PontosAcessoMarcosCaixasRpt3_YYYY_MM_DD.xls`
- Output: `MM_YYYY_Lista de Marcos e Caixas YYYYMMDD.pdf` + `.zip`
- Template: Imagens extraídas de `Listagem Global de Pontos de Acesso.dotm`

## 👤 Autor

Filipe — IR/CTT Portugal

## 📌 Notas adicionais

- Script assume estrutura atual do relatório do IR (cabeçalho em B, colunas em B, D, G–P)
- Depende de Calibri instalado (alternativa: editar `register_fonts()` para Carlito)
- Ideal para agendamento mensal com Windows Task Scheduler
- PDF ~20 MB, ZIP ~13 MB (compressão deflate)

---

**Versão**: 1.1  
**Data**: 27 de outubro de 2026  
**Status**: Pronto para produção
