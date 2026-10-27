# 🚀 Guia Final — Fazer a Pull Request (PR)

Seu projeto está **100% pronto** para fazer PR no repositório `pt.ctt.ir`.

---

## 📋 Pré-requisitos

Certifique-se que tem:

- [ ] Conta GitHub (https://github.com)
- [ ] Acesso ao repositório `CorreiosPortugal/pt.ctt.ir`
- [ ] Git instalado e configurado
- [ ] Personal Access Token (PAT) se usar HTTPS

---

## ✅ Passo a passo para fazer a PR

### Passo 1: Clonar pt.ctt.ir (se ainda não tiver)

```powershell
cd C:\temp
git clone https://github.com/CorreiosPortugal/pt.ctt.ir.git
cd pt.ctt.ir
```

### Passo 2: Criar branch feature (no pt.ctt.ir)

```powershell
git checkout -b feature/add-marcos-caixas-pdf-generator
```

### Passo 3: Copiar ficheiros para a subpasta

```powershell
# Criar pasta
mkdir tools\gerar-lista-marcos-caixas

# Copiar ficheiros (EXCETO .git)
Copy-Item "C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas\*" `
  -Destination "tools\gerar-lista-marcos-caixas\" `
  -Exclude ".git", ".gitignore"

# Copiar .gitignore também
Copy-Item "C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas\.gitignore" `
  -Destination "tools\gerar-lista-marcos-caixas\"
```

### Passo 4: Verificar ficheiros copiados

```powershell
ls tools\gerar-lista-marcos-caixas\
```

Deve ter (12 ficheiros):
- `.gitignore`
- `CHANGELOG.md`
- `check_env.py`
- `gerar_lista_marcos_caixas.py`
- `GITHUB_SETUP.md`
- `INDEX.md`
- `INSTALL.md`
- `Listagem Global de Pontos de Acesso.dotm`
- `PUBLICAR_GITHUB.md`
- `PULL_REQUEST_TEMPLATE.md`
- `README.md`
- `requirements.txt`
- `SUMMARY.md`

### Passo 5: Fazer commit

```powershell
cd C:\temp\pt.ctt.ir

git add tools/gerar-lista-marcos-caixas/

git commit -m "Feat: Adicionar ferramenta de geração automática de PDF — Marcos e Caixas

- Script Python para gerar PDF a partir de relatório do IR
- Substitui processo manual com Word/Excel/PDFCreator
- Automação mensal: ~1 minuto de geração
- Documentação completa incluída
- Testado com dados reais

Ver tools/gerar-lista-marcos-caixas/README.md para detalhes."
```

### Passo 6: Fazer push para o seu fork (se necessário)

Se não tem acesso de push direto, faça fork e push para o seu fork:

```powershell
git remote add origin https://github.com/SEU_USERNAME/pt.ctt.ir.git
git push -u origin feature/add-marcos-caixas-pdf-generator
```

Se tem acesso direto:

```powershell
git push -u origin feature/add-marcos-caixas-pdf-generator
```

### Passo 7: Criar PR no GitHub

1. Ir para: https://github.com/CorreiosPortugal/pt.ctt.ir/pulls
2. Clicar: **"New Pull Request"** (ou GitHub avisa automaticamente)
3. Selecionar:
   - **base**: `main` (ou `master`)
   - **compare**: `feature/add-marcos-caixas-pdf-generator`
4. Preencher PR:
   - **Título**: "Feat: Adicionar ferramenta de geração automática de PDF — Marcos e Caixas"
   - **Descrição**: Copiar conteúdo do ficheiro **PULL_REQUEST_TEMPLATE.md**
5. Clicar: **"Create Pull Request"**

---

## 📄 Conteúdo para colar na descrição da PR

Copiar tudo isto para a caixa de descrição da PR:

```markdown
## 📝 Descrição

Adicionar ferramenta de geração automática de PDF — **Marcos e Caixas**.

Substitui o processo manual com Word/Excel/PDFCreator por um script Python que:
- Lê relatório do IR em formato XLS
- Gera PDF profissional em ~1 minuto
- Embala tudo num ZIP para arquivo

## 🎯 Objetivo

Automação mensal da geração do PDF `MM_YYYY_Lista de Marcos e Caixas YYYYMMDD.pdf`.

## 📂 Mudanças

- Novo diretório: `tools/gerar-lista-marcos-caixas/`
- 12 ficheiros (script, dependências, documentação)
- Sem breaking changes

## ✅ Verificações

- [x] Python 3.9+ funciona
- [x] Dependências testadas
- [x] Script testado com dados reais
- [x] Documentação completa
- [x] Sem credenciais ou dados sensíveis

## 🚀 Como usar

```powershell
pip install -r tools/gerar-lista-marcos-caixas/requirements.txt
python tools/gerar-lista-marcos-caixas/gerar_lista_marcos_caixas.py <xls> --base-dir <pasta>
```

## 📚 Documentação

Ver `tools/gerar-lista-marcos-caixas/INDEX.md` para mapa completo.

**Versão**: 1.1 | **Data**: 27 de outubro de 2026
```

---

## 🆘 Resolução de problemas

### ❌ "Erro: acesso negado"

Se receber erro de permissão ao fazer push:

1. **Verificar remote**:
   ```powershell
   git remote -v
   ```

2. **Se for HTTPS**, usar Personal Access Token:
   - Ir para: https://github.com/settings/tokens
   - Criar novo token com permissões: `repo`, `workflow`
   - Usar como password ao fazer push

3. **Se for SSH**, verificar chave:
   ```powershell
   ssh -T git@github.com
   ```

### ❌ "Erro: ficheiro grande"

Se o ficheiro `.dotm` (177 MB) for rejeitado:

```powershell
# Verificar tamanho
(Get-Item "tools\gerar-lista-marcos-caixas\Listagem Global de Pontos de Acesso.dotm").Length / 1MB
# Deve ser 177.5 KB, não 177 MB — OK para GitHub
```

### ❌ "Erro: branch já existe"

Se a branch já existe:

```powershell
git branch -D feature/add-marcos-caixas-pdf-generator
git checkout -b feature/add-marcos-caixas-pdf-generator
```

---

## ✨ O que vai acontecer depois

1. **PR revisada** pela equipa do pt.ctt.ir
2. **Comentários/sugestões** (se houver)
3. **Aprovação** e merge na `main`
4. **Publicado** no repositório público
5. **Disponível** para toda a comunidade CTT

---

## 📊 Checklist final

- [ ] Ficheiros copiados para `tools/gerar-lista-marcos-caixas/`
- [ ] Commit feito: `git log --oneline` mostra novo commit
- [ ] Push efetuado: `git push origin feature/...`
- [ ] PR criada no GitHub
- [ ] Descrição preenchida com template
- [ ] Verificar no GitHub se tudo ficou correto
- [ ] ✓ PRONTO!

---

## 🎉 Pronto!

Quando a PR for aprovada e merged, o projeto estará **publicamente disponível** no repositório CorreiosPortugal/pt.ctt.ir!

---

**Dúvidas?** Consultar:
- `INDEX.md` — Mapa de documentação
- `PUBLICAR_GITHUB.md` — Guia completo (português)
- `GITHUB_SETUP.md` — Opções técnicas

**Data**: 27 de outubro de 2026  
**Status**: ✓ Pronto para PR
