# 📑 Índice — Guia de navegação

Bem-vindo ao projeto **Gerador de Lista de Marcos e Caixas — PDF Automático**.

Use este índice para encontrar o que precisa.

---

## 🎯 Por onde começar?

### Se quer **usar o script agora**:
1. Ler: **[README.md](README.md)** (overview + uso rápido)
2. Ler: **[INSTALL.md](INSTALL.md)** (setup das dependências)
3. Executar: `pip install -r requirements.txt`
4. Testar: `python gerar_lista_marcos_caixas.py --help`

### Se quer **entender o projeto**:
1. Ler: **[SUMMARY.md](SUMMARY.md)** (resumo completo)
2. Ler: **[README.md](README.md)** (overview técnico)
3. Ver: `gerar_lista_marcos_caixas.py` (código-fonte comentado)

### Se quer **publicar no GitHub**:
1. Ler: **[PUBLICAR_GITHUB.md](PUBLICAR_GITHUB.md)** (instruções em português)
2. Ler: **[GITHUB_SETUP.md](GITHUB_SETUP.md)** (opções técnicas)
3. Executar: comandos Git conforme guia

### Se tiver **problemas**:
1. Ler: **[INSTALL.md](INSTALL.md)** → "Resolução de problemas"
2. Executar: `python check_env.py` (diagnóstico)
3. Contactar: Filipe — IR/CTT Portugal

---

## 📂 Estrutura dos ficheiros

```
.
├── 📄 FICHEIROS PRINCIPAIS
│   ├── gerar_lista_marcos_caixas.py    ← Script que gera o PDF
│   ├── check_env.py                     ← Verificador de ambiente
│   ├── requirements.txt                 ← Dependências Python
│   └── Listagem Global de...dotm        ← Template (não editar)
│
├── 📚 DOCUMENTAÇÃO (LEIA ISTO!)
│   ├── README.md                        ← Comece por aqui!
│   ├── INSTALL.md                       ← Setup detalhado
│   ├── PUBLICAR_GITHUB.md               ← Publicar no GitHub (português)
│   ├── GITHUB_SETUP.md                  ← Opções técnicas GitHub
│   ├── SUMMARY.md                       ← Resumo completo
│   ├── CHANGELOG.md                     ← Histórico de versões
│   └── INDEX.md                         ← Este ficheiro
│
└── 📌 CONTROLO DE VERSÃO
    ├── .git/                            ← Repositório Git (interno)
    └── .gitignore                       ← Ficheiros ignorados
```

---

## 📖 Descrição de cada ficheiro

### Ficheiros principais

| Ficheiro | Descrição | Tamanho | Editar? |
|----------|-----------|---------|---------|
| **gerar_lista_marcos_caixas.py** | Script Python que gera o PDF | 10 KB | ❌ Não (já funciona) |
| **check_env.py** | Verifica se o ambiente está pronto | 2 KB | ❌ Não |
| **requirements.txt** | Lista de dependências Python | <1 KB | ✓ Sim (se adicionar packages) |
| **Listagem Global...dotm** | Template Word com imagens da capa | 177 KB | ❌ Não (extrai só imagens) |

### Documentação

| Ficheiro | Leia se... | Tamanho | Prioridade |
|----------|-----------|---------|-----------|
| **README.md** | Quer visão geral do projecto | 4 KB | 🔴 ALTA |
| **INSTALL.md** | Quer instalar/usar o script | 3 KB | 🔴 ALTA |
| **PUBLICAR_GITHUB.md** | Quer publicar no GitHub (português) | 8 KB | 🟠 MÉDIA |
| **GITHUB_SETUP.md** | Quer detalhes técnicos GitHub | 4 KB | 🟡 BAIXA |
| **SUMMARY.md** | Quer conhecer todo o projecto | 6 KB | 🟡 BAIXA |
| **CHANGELOG.md** | Quer ver histórico de versões | 2 KB | ⚪ OPCIONAL |
| **INDEX.md** | Está agora (navegação) | 3 KB | ⚪ REFERÊNCIA |

### Controlo de versão

| Ficheiro | Descrição |
|----------|-----------|
| **.git/** | Repositório Git (não editar) |
| **.gitignore** | Ficheiros ignorados no Git (PDF, ZIP, logs, etc.) |

---

## 🚀 Fluxo de trabalho típico

### Fluxo 1: Usar o script

```
1. Ler README.md (visão geral)
   ↓
2. Ler INSTALL.md (setup)
   ↓
3. Instalar: pip install -r requirements.txt
   ↓
4. Testar: python check_env.py
   ↓
5. Executar: python gerar_lista_marcos_caixas.py <xls> --base-dir <pasta>
   ↓
6. Validar PDF gerado
```

### Fluxo 2: Publicar no GitHub

```
1. Ler PUBLICAR_GITHUB.md (português + passo a passo)
   ↓
2. Criar repositório no GitHub
   ↓
3. git remote add origin https://...
   ↓
4. git branch -M main
   ↓
5. git push -u origin main
   ↓
6. Verificar no GitHub
```

### Fluxo 3: Resolver problemas

```
1. Executar: python check_env.py
   ↓
2. Ver resultado (5/5 OK ou FALHA?)
   ↓
3. Se falha, ler INSTALL.md → Resolução de problemas
   ↓
4. Corrigir e testar de novo
```

---

## 🔍 Procurar por tópico

### Instalação e Setup
- 📄 **README.md** — Requisitos e instalação rápida
- 📄 **INSTALL.md** — Setup passo a passo + troubleshooting

### Como usar o script
- 📄 **README.md** — Exemplos de uso
- 💻 `python gerar_lista_marcos_caixas.py --help`

### Publicar no GitHub
- 📄 **PUBLICAR_GITHUB.md** — Instruções em português (RECOMENDADO!)
- 📄 **GITHUB_SETUP.md** — Opções técnicas avançadas

### Problemas
- 📄 **INSTALL.md** → "Resolução de problemas" — Soluções comuns
- 💻 `python check_env.py` — Diagnóstico automático

### Histórico
- 📄 **CHANGELOG.md** — Versões anteriores
- 💻 `git log --oneline` — Commits Git

### Resumo do projecto
- 📄 **SUMMARY.md** — Tudo junto (para compreensão global)

---

## ✅ Checklist de primeiro uso

- [ ] Li **README.md**
- [ ] Executei `python check_env.py` → 5/5 OK
- [ ] Instalei dependências: `pip install -r requirements.txt`
- [ ] Testei o script com um ficheiro XLS
- [ ] Validei o PDF gerado
- [ ] Estou pronto para usar em produção!

---

## ⚡ Comandos rápidos

```powershell
# Verificar ambiente
python check_env.py

# Ver ajuda do script
python gerar_lista_marcos_caixas.py --help

# Testar com 100 linhas (rápido)
python gerar_lista_marcos_caixas.py <xls> --max-rows 100 --out-dir .\test

# Gerar PDF mensal (recomendado)
python gerar_lista_marcos_caixas.py PontosAcessoMarcosCaixasRpt3_2026_10_09.xls `
  --base-dir C:\Users\atos91\Desktop\APPs\IR

# Ver histórico Git
git log --oneline

# Ver status Git
git status
```

---

## 📞 Suporte

### Dúvidas sobre:

| Tópico | Contacte | Recurso |
|--------|----------|---------|
| **Como usar** | INSTALL.md | 📄 INSTALL.md ou `--help` |
| **Problemas** | check_env.py | 💻 Executar diagnóstico |
| **GitHub** | PUBLICAR_GITHUB.md | 📄 PUBLICAR_GITHUB.md |
| **Código** | README.md | 📄 README.md ou code |
| **Geral** | Filipe | IR/CTT Portugal |

---

## 🎓 Recursos adicionais

- **Python docs**: https://docs.python.org/3/
- **Git docs**: https://git-scm.com/doc
- **GitHub docs**: https://docs.github.com/
- **ReportLab docs**: https://www.reportlab.com/docs/reportlab-userguide.pdf

---

## 📅 Versão

- **Versão atual**: 1.1
- **Data**: 27 de outubro de 2026
- **Status**: ✓ Pronto para produção

---

## 🎯 Resumo: O que fazer agora

### Opção A: Usar o script (para gerar PDF)
→ Ler **README.md**, depois **INSTALL.md**, depois usar!

### Opção B: Publicar no GitHub (para compartilhar)
→ Ler **PUBLICAR_GITHUB.md**, depois executar!

### Opção C: Aprender mais (para entender tudo)
→ Ler **SUMMARY.md**, depois explorar!

---

**Pronto? Escolha uma opção acima e comece! 🚀**
