# Gerador de Lista de Marcos e Caixas — Instruções de Setup

## Instalação rápida

### 1. Clonar/descarregar o projeto

```powershell
cd C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas
```

### 2. Criar ambiente virtual (recomendado)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Instalar dependências

```powershell
pip install -r requirements.txt
```

### 4. Verificar instalação

```powershell
python -c "import xlrd, reportlab; print('✓ Dependências OK')"
```

### 5. Testar o script

```powershell
# Teste com primeiras 100 linhas
python gerar_lista_marcos_caixas.py PontosAcessoMarcosCaixasRpt3_2026_10_09.xls --max-rows 100 --out-dir .\test_output

# Ver ajuda
python gerar_lista_marcos_caixas.py --help
```

## Resolução de problemas

### ❌ "Calibri.ttf não encontrado"

Se não tiver Calibri instalado:

1. Instalar fontes (Windows Update ou Adobe)
2. OU editar `register_fonts()` em `gerar_lista_marcos_caixas.py`:

```python
# Usar Carlito (similar ao Calibri)
pdfmetrics.registerFont(TTFont(FONT, str(fonts / "carlito.ttf")))
pdfmetrics.registerFont(TTFont(FONT_B, str(fonts / "carlitobd.ttf")))
```

### ❌ "Ficheiro XLS não encontrado"

```powershell
# Confirmar que o ficheiro existe
Get-Item "PontosAcessoMarcosCaixasRpt3_2026_10_09.xls"

# Se não, copiar da pasta do IR
Copy-Item "C:\Users\atos91\Desktop\APPs\IR\Marcos e Caixas 10_2026\*.xls" .
```

### ❌ "Dotm não encontrado"

```powershell
# Template deve estar na mesma pasta que o script OU especificar:
python gerar_lista_marcos_caixas.py <xls> --template-dir "C:\caminho\para\template"
```

## Workflow mensal recomendado

```powershell
# 1. Gerar relatório no IR (UI web)
# 2. Descarregar XLS para a pasta do projeto

# 3. Executar gerador
cd C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas
python gerar_lista_marcos_caixas.py PontosAcessoMarcosCaixasRpt3_2026_10_09.xls `
  --base-dir C:\Users\atos91\Desktop\APPs\IR

# 4. Validar PDF gerado em:
# C:\Users\atos91\Desktop\APPs\IR\Marcos e Caixas 10_2026\10_2026_Lista de Marcos e Caixas 20260930.pdf

# 5. Arquivar ZIP
```

## Integração com agendador (Windows Task Scheduler)

```powershell
# Script: run_monthly.ps1
$ErrorActionPreference = "Stop"
$scriptPath = "C:\Users\atos91\Desktop\APPs\IR\gerar-lista-marcos-caixas"
Set-Location $scriptPath
& python gerar_lista_marcos_caixas.py "PontosAcessoMarcosCaixasRpt3_*.xls" `
  --base-dir "C:\Users\atos91\Desktop\APPs\IR" `
  | Tee-Object -FilePath "log_$(Get-Date -Format 'yyyyMM').txt"
```

Agendar em Task Scheduler para executar mensalmente.

---

**Data**: 27 de outubro de 2026
