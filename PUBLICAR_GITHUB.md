# 🎯 Como publicar no GitHub — Instruções em Português

## Resumo

Tem um projeto Python pronto em:  
📁 `C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas`

Quer publicar no repositório **CorreiosPortugal/pt.ctt.ir** (ou criar um novo).

---

## ✅ Opção 1: Criar repositório dedicado (RECOMENDADO)

### Passo 1: Criar repositório no GitHub

1. Ir para https://github.com/CorreiosPortugal (ou seu perfil)
2. Clicar em **"New"** (novo repositório)
3. Preencher:
   - **Repository name**: `IR-gerar-lista-marcos-caixas`
   - **Description**: "Gerador automático de PDF — Marcos e Caixas"
   - **Visibility**: Public (ou Private se preferir)
   - **Clicar "Create repository"**

### Passo 2: Fazer push do projeto local

```powershell
cd C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas

# Adicionar repositório remoto
git remote add origin https://github.com/CorreiosPortugal/IR-gerar-lista-marcos-caixas.git

# Renomear branch (GitHub usa 'main' por default)
git branch -M main

# Fazer push
git push -u origin main
```

**Pronto!** 🎉 Repositório criado em GitHub.

---

## 🔄 Opção 2: Integrar no pt.ctt.ir (subpasta)

Se quer adicionar como subpasta do repositório existente **pt.ctt.ir**:

### Passo 1: Clonar pt.ctt.ir

```powershell
cd C:\temp
git clone https://github.com/CorreiosPortugal/pt.ctt.ir.git
cd pt.ctt.ir
```

### Passo 2: Criar subpasta e copiar ficheiros

```powershell
# Criar pasta
mkdir tools\gerar-lista-marcos-caixas

# Copiar ficheiros (EXCETO .git)
Copy-Item "C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas\gerar_lista_marcos_caixas.py" `
  -Destination "tools\gerar-lista-marcos-caixas\"
Copy-Item "C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas\check_env.py" `
  -Destination "tools\gerar-lista-marcos-caixas\"
Copy-Item "C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas\requirements.txt" `
  -Destination "tools\gerar-lista-marcos-caixas\"
Copy-Item "C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas\Listagem Global de Pontos de Acesso.dotm" `
  -Destination "tools\gerar-lista-marcos-caixas\"
Copy-Item "C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas\*.md" `
  -Destination "tools\gerar-lista-marcos-caixas\" -Exclude README.md
Copy-Item "C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas\README.md" `
  -Destination "tools\gerar-lista-marcos-caixas\"
```

### Passo 3: Fazer commit

```powershell
cd C:\temp\pt.ctt.ir

git add tools/gerar-lista-marcos-caixas/

git commit -m "Feat: Adicionar ferramenta de geração automática de PDF — Marcos e Caixas

- Script Python para gerar PDF a partir de relatório do IR
- Substitui processo manual com Word/Excel/PDFCreator
- Documentação completa incluída
- Ver tools/gerar-lista-marcos-caixas/README.md para detalhes"

git push origin main
```

---

## 📱 Opção 3: Branch feature (para pull request)

Se quer fazer um **Pull Request** no pt.ctt.ir:

### Passo 1: Clonar pt.ctt.ir

```powershell
git clone https://github.com/CorreiosPortugal/pt.ctt.ir.git
cd pt.ctt.ir
```

### Passo 2: Criar branch

```powershell
git checkout -b feature/gerar-lista-marcos-caixas
```

### Passo 3: Copiar ficheiros (como Opção 2)

```powershell
mkdir tools\gerar-lista-marcos-caixas
# ... copiar ficheiros ...
```

### Passo 4: Commit e push

```powershell
git add tools/gerar-lista-marcos-caixas/
git commit -m "Feat: Adicionar ferramenta de geração automática de PDF"
git push origin feature/gerar-lista-marcos-caixas
```

### Passo 5: Fazer Pull Request no GitHub

1. Ir para https://github.com/CorreiosPortugal/pt.ctt.ir/pulls
2. Clicar **"New Pull Request"**
3. Selecionar:
   - **base**: main
   - **compare**: feature/gerar-lista-marcos-caixas
4. Preencher título e descrição
5. Clicar **"Create Pull Request"**

Depois membros da equipa podem revisar e fazer merge.

---

## 🧪 Verificar antes de publicar

Antes de fazer push, execute:

```powershell
cd C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas

# Verificar ambiente
python check_env.py

# Ver status Git
git status

# Ver histórico
git log --oneline

# Testar script (rápido)
python gerar_lista_marcos_caixas.py <seu_arquivo.xls> --max-rows 50 --out-dir .\test
```

Se tudo está OK, faça o push! ✓

---

## 📖 Ficheiros principais

Dentro do repositório você terá:

```
gerar-lista-marcos-caixas/
├── README.md                      ← LER ISTO PRIMEIRO!
├── gerar_lista_marcos_caixas.py   ← Script principal
├── check_env.py                   ← Verificar ambiente
├── requirements.txt               ← Dependências (pip install)
├── INSTALL.md                     ← Setup e troubleshooting
├── GITHUB_SETUP.md                ← Instruções publicação
└── Listagem Global...dotm         ← Template (não editar)
```

---

## 🆘 Problemas comuns

### "Erro: não tem permissão"

Confirmar que tem acesso ao repositório CorreiosPortugal:

```powershell
git remote -v
# Deve mostrar:
# origin  https://github.com/CorreiosPortugal/IR-gerar-lista-marcos-caixas.git (fetch)
# origin  https://github.com/CorreiosPortugal/IR-gerar-lista-marcos-caixas.git (push)
```

Se tiver acesso, executar `git push origin main` de novo.

### "Erro: nome de utilizador/password"

GitHub deixou de aceitar passwords HTTP. Usar **Personal Access Token (PAT)**:

1. Ir para https://github.com/settings/tokens
2. Clicar **"Generate new token"** → **"Generate new token (classic)"**
3. Selecionar: `repo`, `workflow`
4. Clicar **"Generate token"**
5. **Copiar token** e guardar num local seguro
6. Usar como password:

```powershell
# Usar token como password (será pedido)
git push origin main
# Username: seu_utilizador_github
# Password: <colar token aqui>
```

Ou configurar permanentemente com:

```powershell
git config --global credential.helper wincred
```

### "Erro: ficheiros grandes"

Se tiver ficheiros > 100 MB, GitHub vai rejeitar. Solução:

```powershell
# Adicionar ao .gitignore
echo "*.pdf" >> .gitignore
echo "*.zip" >> .gitignore

# Ou usar Git LFS para ficheiros grandes
git lfs install
git lfs track "*.pdf" "*.zip"
```

---

## 🎓 Depois de publicar

### Adicionar tags (versões)

```powershell
# Criar tag
git tag -a v1.0 -m "Versão 1.0 — Publicação inicial"
git push origin v1.0

# Criar nova tag
git tag -a v1.1 -m "Versão 1.1 — Documentação completa"
git push origin v1.1
```

### Atualizar projeto localmente

Se fizer mudanças, fazer novo commit e push:

```powershell
cd C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas

# Fazer alterações...
# ...

git add .
git commit -m "Descrição das alterações"
git push origin main
```

### Adicionar CI/CD (GitHub Actions)

Criar `.github/workflows/test.yml`:

```yaml
name: Test
on: [push]
jobs:
  test:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r requirements.txt
      - run: python check_env.py
```

---

## ✅ Checklist final

- [ ] GitHub repositório criado (dedicado ou fork pt.ctt.ir)
- [ ] Ficheiros locais em: `C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas`
- [ ] `python check_env.py` retorna 5/5 OK
- [ ] `git status` mostra working tree clean
- [ ] `git log --oneline` mostra 3 commits
- [ ] Push efetuado com sucesso
- [ ] Verificar no GitHub se ficheiros estão lá
- [ ] README.md visível no GitHub (homepage do repo)

---

## 🎉 Pronto!

Projeto publicado e versionado. Agora pode:

- ✓ Partilhar link do GitHub com a equipa
- ✓ Receber contribuições via Pull Requests
- ✓ Manter histórico de versões com Git
- ✓ Adicionar melhorias facilmente
- ✓ Usar para automação na empresa

---

**Data**: 27 de outubro de 2026  
**Versão**: 1.1  
**Status**: Pronto para GitHub

Qualquer dúvida, contacte: **Filipe — IR/CTT Portugal**
