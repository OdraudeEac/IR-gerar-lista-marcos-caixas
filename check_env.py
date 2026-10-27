#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Verificação de ambiente para gerar_lista_marcos_caixas.py

Testa dependências, fontes e ficheiros necessários.
"""
import sys
import shutil
from pathlib import Path


def check_python():
    """Verifica versão do Python."""
    if sys.version_info < (3, 9):
        print(f"❌ Python 3.9+ necessário (actual: {sys.version})")
        return False
    print(f"✓ Python {sys.version.split()[0]}")
    return True


def check_package(name, import_name=None):
    """Verifica se um pacote está instalado."""
    if import_name is None:
        import_name = name
    try:
        __import__(import_name)
        print(f"✓ {name}")
        return True
    except ImportError:
        print(f"❌ {name} não instalado")
        print(f"   Instalar com: pip install {name}")
        return False


def check_font():
    """Verifica se Calibri está instalado."""
    fonts_path = Path(r"C:\Windows\Fonts\calibri.ttf")
    if fonts_path.exists():
        print("✓ Calibri instalado")
        return True
    print("❌ Calibri não encontrado")
    print("   Instalar via Windows Update ou Adobe Creative Suite")
    return False


def check_dotm():
    """Verifica se o template .dotm existe."""
    dotm_path = Path(__file__).parent / "Listagem Global de Pontos de Acesso.dotm"
    if dotm_path.exists():
        size_kb = dotm_path.stat().st_size / 1024
        print(f"✓ Template .dotm ({size_kb:.1f} KB)")
        return True
    print("❌ Template 'Listagem Global de Pontos de Acesso.dotm' não encontrado")
    return False


def main():
    print("=" * 50)
    print("Verificação de ambiente")
    print("=" * 50)
    
    results = [
        ("Python 3.9+", check_python()),
        ("xlrd", check_package("xlrd")),
        ("reportlab", check_package("reportlab")),
        ("Calibri font", check_font()),
        ("Template .dotm", check_dotm()),
    ]
    
    print("\n" + "=" * 50)
    passed = sum(1 for _, r in results if r)
    total = len(results)
    print(f"Resultado: {passed}/{total}")
    
    if passed == total:
        print("✓ Ambiente OK! Pronto para usar.")
        return 0
    else:
        print("❌ Corrigir os erros acima antes de continuar.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
