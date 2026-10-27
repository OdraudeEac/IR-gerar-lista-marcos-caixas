# Publicar no GitHub — Instruções

Este projecto está pronto para ser publicado no repositório **CorreiosPortugal/pt.ctt.ir**.

## 🚀 Opções de publicação

### Opção 1: Push para repositório remoto existente

Se **pt.ctt.ir** é um repositório existente (e já tem acesso):

```powershell
cd C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas

# Adicionar repositório remoto
git remote add origin https://github.com/CorreiosPortugal/pt.ctt.ir.git

# Criar branch para este subprojecto
git checkout -b feature/gerar-lista-marcos-caixas

# Fazer push
git push -u origin feature/gerar-lista-marcos-caixas
```

Depois fazer um **Pull Request** no GitHub para integração na `main`.

### Opção 2: Criar novo repositório público

Se preferir um repositório dedicado para este script:

```powershell
# 1. Criar novo repositório no GitHub
#    https://github.com/new
#    Nome: IR-gerar-lista-marcos-caixas
#    Descrição: Gerador automático de PDF — Marcos e Caixas

# 2. Adicionar como remoto
cd C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas
git remote add origin https://github.com/CorreiosPortugal/IR-gerar-lista-marcos-caixas.git
git branch -M main
git push -u origin main
```

### Opção 3: Estrutura de subpasta no pt.ctt.ir

Se quer integrar no repositório **pt.ctt.ir** como subpasta:

```powershell
# 1. No repositório pt.ctt.ir, criar pasta
mkdir tools/gerar-lista-marcos-caixas

# 2. Copiar ficheiros (exceto .git)
Copy-Item "gerar_lista_marcos_caixas.py" -Destination "tools/gerar-lista-marcos-caixas/"
Copy-Item "check_env.py" -Destination "tools/gerar-lista-marcos-caixas/"
Copy-Item "requirements.txt" -Destination "tools/gerar-lista-marcos-caixas/"
Copy-Item "Listagem Global de Pontos de Acesso.dotm" -Destination "tools/gerar-lista-marcos-caixas/"
Copy-Item "README.md" -Destination "tools/gerar-lista-marcos-caixas/"
Copy-Item "INSTALL.md" -Destination "tools/gerar-lista-marcos-caixas/"
Copy-Item ".gitignore" -Destination "tools/gerar-lista-marcos-caixas/"

# 3. Fazer commit no pt.ctt.ir
cd <pt.ctt.ir-repo>
git add tools/gerar-lista-marcos-caixas/
git commit -m "Add: Ferramenta de geração automática de PDF — Marcos e Caixas"
git push origin main
```

## 📋 Verificação pré-publicação

Antes de fazer push, confirme:

- [ ] Repositório Git local está limpo: `git status`
- [ ] Histórico de commits está correto: `git log --oneline`
- [ ] Ambiente testado: `python check_env.py` retorna **[OK]**
- [ ] Script funciona: Testado com `--max-rows 100`
- [ ] `.gitignore` não incluir ficheiros sensíveis
- [ ] `README.md` está atualizado com instruções claras
- [ ] `requirements.txt` tem versões pinned (ou pelo menos mínimas)

## 🔐 Ficheiros sensíveis

O projecto **NÃO** contém:
- Credenciais ou tokens
- Dados confidenciais
- Ficheiros grandes de dados (relatórios reais)
- Chaves privadas

Pode publicar com segurança! ✓

## 🏷️ Tags recomendadas (GitHub)

```powershell
# Criar tag de versão 1.0
git tag -a v1.0 -m "Versão 1.0 — Publicação inicial"
git push origin v1.0

# Criar tag de versão 1.1
git tag -a v1.1 -m "Versão 1.1 — Documentação completa"
git push origin v1.1
```

## 📦 Informação do repositório

```
Owner: CorreiosPortugal
Repo: pt.ctt.ir (ou novo: IR-gerar-lista-marcos-caixas)
Branch: main (ou feature/gerar-lista-marcos-caixas)
Tamanho: ~0.2 MB
Linguagem: Python 3.9+
Licença: (A definir — sugerir: CC0 1.0 Universal ou similar)
```

## 🔗 Próximos passos

1. **Decidir opção** (1, 2, ou 3 acima)
2. **Executar comandos Git** para publicar
3. **Configurar CI/CD** (opcional):
   - GitHub Actions para validar `requirements.txt`
   - Teste com `--max-rows 10` em cada commit
4. **Adicionar Issues** para melhorias futuras
5. **Documentação Wiki** (opcional)

## 📞 Suporte

Para dúvidas sobre integração no GitHub:
- Verificar `/readme` do repositório pt.ctt.ir
- Contactar administrador de repositório
- Rever documentação GitHub: https://docs.github.com/en

---

**Data**: 27 de outubro de 2026
**Versão do projecto**: 1.1 (pronto para publicar)
