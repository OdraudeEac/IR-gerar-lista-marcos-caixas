# Gerador de Lista de Marcos e Caixas

## 📂 Estrutura do projeto

```
gerar-lista-marcos-caixas/
├── gerar_lista_marcos_caixas.py          # Script principal
├── check_env.py                           # Verificação de ambiente
├── Listagem Global de Pontos de Acesso.dotm # Template Word (imagens)
├── README.md                              # Documentação principal
├── INSTALL.md                             # Instruções de setup
├── requirements.txt                       # Dependências Python
└── .gitignore                             # Ficheiros ignorados no Git
```

## 🚀 Começar

1. **Ler `README.md`** — Overview e uso
2. **Executar `check_env.py`** — Verificar ambiente
3. **Seguir `INSTALL.md`** — Setup das dependências
4. **Usar `gerar_lista_marcos_caixas.py`** — Gerar PDF

## 📝 Comandos rápidos

```powershell
# Verificar ambiente
python check_env.py

# Ver ajuda
python gerar_lista_marcos_caixas.py --help

# Gerar PDF mensal
python gerar_lista_marcos_caixas.py PontosAcessoMarcosCaixasRpt3_2026_10_09.xls `
  --base-dir C:\Users\atos91\Desktop\APPs\IR
```

## 📦 Histórico de desenvolvimento

- **Versão 1.0** (2024-04): Script original criado para substituir processo manual Word/Excel/PDFCreator
- **Versão 1.1** (2026-10): Documentação e estrutura de projeto profissional

## 🔗 Referências

- Relatório do IR: `PontosAcessoMarcosCaixasRpt3_YYYY_MM_DD.xls`
- Output: `MM_YYYY_Lista de Marcos e Caixas YYYYMMDD.pdf` + `.zip`
- Template: Imagens extraídas de `Listagem Global de Pontos de Acesso.dotm`

---

**Data**: 27 de outubro de 2026 | **Python**: 3.9+ | **Maintainer**: Filipe
