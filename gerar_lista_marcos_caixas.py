"""Gera 'MM_YYYY_Lista de Marcos e Caixas YYYYMMDD.pdf' a partir do relatorio
PontosAcessoMarcosCaixasRpt3_*.xls do IR, sem usar Excel/Word.

Uso:
    python gerar_lista_marcos_caixas.py PontosAcessoMarcosCaixasRpt3_2024_04_09.xls
    python gerar_lista_marcos_caixas.py <xls> --data-ref 2024-03-31 --out-dir <pasta> --max-rows 100

Dependencias: pip install xlrd reportlab
Os logotipos/imagens da capa sao lidos do template 'Listagem Global de Pontos de Acesso.dotm'.
"""
import argparse
import calendar
import datetime as dt
import io
import re
import shutil
import sys
import zipfile
from pathlib import Path

import xlrd
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit

PAGE_W, PAGE_H = 841.92, 595.32            # A4 horizontal
MARGIN_L = 28.35                           # 1 cm
BODY_TOP = 85.05                           # margem superior do Word (3 cm)
BODY_BOTTOM = PAGE_H - 56.7                # margem inferior (2 cm)
TABLE_COLS_CM = [1.9, 1.9, 2.61, 3.3, 1.15, 0.95, 2.6, 1.75, 1.55, 1.55, 1.75, 6.78]
COL_W = [c * 28.3465 for c in TABLE_COLS_CM]
COL_X = [MARGIN_L + sum(COL_W[:i]) for i in range(12)]
TABLE_R = MARGIN_L + sum(COL_W)
# alinhamento horizontal: l=esquerda, c=centro
ALIGN = "l l l l c c l c c c c l".split()
FONT, FONT_B, SIZE, LINE_H, PAD = "Calibri", "Calibri-Bold", 10, 12.2, 3.5
HEADER_H = 70.4
WRAP_SLACK = 0.0                           # ajuste fino da largura util face ao Word
RED = (0.875, 0.0, 0.141)
ASCENT = 0.82                              # baseline = topo do texto + ASCENT*tamanho


def register_fonts():
    fonts = Path(r"C:\Windows\Fonts")
    pdfmetrics.registerFont(TTFont(FONT, str(fonts / "calibri.ttf")))
    pdfmetrics.registerFont(TTFont(FONT_B, str(fonts / "calibrib.ttf")))


def read_report(path, max_rows=0):
    book = xlrd.open_workbook(path, logfile=open("nul", "w") if sys.platform == "win32" else None)
    sh = book.sheet_by_index(0)
    hdr = next(r for r in range(sh.nrows) if str(sh.cell_value(r, 1)).strip() == "Distrito")
    cols = [1, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]   # B,D,G..P (as outras sao celulas fundidas)

    def val(cell, ci):
        v = cell.value
        if cell.ctype == xlrd.XL_CELL_NUMBER:
            if ci == 4:
                return "%04d" % int(v)
            if ci == 5:
                return "%03d" % int(v)
            if 7 <= ci <= 10 and v < 1:                  # hora guardada como fracao do dia
                m = round(v * 1440)
                return "%d:%02d" % (m // 60, m % 60)
            return str(int(v)) if v == int(v) else str(v)
        return str(v).strip("\r") if v != "" else ""

    header = [str(sh.cell_value(hdr, c)) for c in cols]
    rows = []
    last = sh.nrows if not max_rows else min(sh.nrows, hdr + 1 + max_rows)
    for r in range(hdr + 1, last):
        row = [val(sh.cell(r, c), i) for i, c in enumerate(cols)]
        if any(row):
            rows.append(row)
    return header, rows


def _sw(s):
    return pdfmetrics.stringWidth(s, FONT, SIZE)


def _fragments(word, width):
    """Partes de uma palavra: quebra apos hifen; se ainda nao couber, quebra por caracteres."""
    out = []
    for frag in re.split(r"(?<=-)", word):
        while frag and _sw(frag) > width:
            k = len(frag) - 1
            while k > 1 and _sw(frag[:k]) > width:
                k -= 1
            out.append(frag[:k])
            frag = frag[k:]
        if frag:
            out.append(frag)
    return out


def wrap(text, width):
    """Quebra de linhas como o Word: por espacos, depois hifens, depois caracteres."""
    lines = []
    for para in text.replace("\r", "").split("\n"):
        cur = ""
        for word in para.split():
            cand = word if not cur else cur + " " + word
            if _sw(cand) <= width:
                cur = cand
                continue
            if cur:
                lines.append(cur)
                cur = ""
            if _sw(word) <= width:
                cur = word
                continue
            for frag in _fragments(word, width):
                cand = cur + frag
                if cur and _sw(cand) > width:
                    lines.append(cur)
                    cur = frag
                else:
                    cur = cand
        if cur or not para:
            lines.append(cur)
    return [l for l in lines] if text.strip() else []


def draw_text_lines(c, lines, x, top, h, width, align, color=(0, 0, 0)):
    c.setFillColorRGB(*color)
    c.setFont(FONT, SIZE)
    block = len(lines) * LINE_H
    y0 = top + (h - block) / 2
    for i, ln in enumerate(lines):
        base = PAGE_H - (y0 + i * LINE_H + 0.5 + ASCENT * SIZE + 1.5)
        if align == "c":
            c.drawCentredString(x + width / 2, base, ln.strip())
        else:
            c.drawString(x + PAD, base, ln.strip())


def draw_row(c, cells, top, h, header=False):
    if header:
        c.setFillColorRGB(*RED)
        c.rect(MARGIN_L, PAGE_H - top - h, TABLE_R - MARGIN_L, h, stroke=0, fill=1)
    for i, txt in enumerate(cells):
        w = COL_W[i]
        lines = wrap(txt, w - 2 * PAD - WRAP_SLACK)
        draw_text_lines(c, lines, COL_X[i], top, h, w, "c" if header else ALIGN[i],
                        (1, 1, 1) if header else (0, 0, 0))
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(0.5)
    c.rect(MARGIN_L, PAGE_H - top - h, TABLE_R - MARGIN_L, h, stroke=1, fill=0)
    for x in COL_X[1:]:
        c.line(x, PAGE_H - top, x, PAGE_H - top - h)


def page_frame(c, page_no, total, date_iso, logo):
    c.drawImage(logo, 0, PAGE_H - 74.25, width=97.5, height=74.25)
    c.setFillColorRGB(0, 0, 0)
    c.setFont(FONT, 18)
    c.drawCentredString(PAGE_W / 2, PAGE_H - (30.6 + ASCENT * 18),
                        "Listagem Global de Pontos de Acesso \u2013 Marcos e Caixas")
    c.setFont(FONT, 10)
    base = PAGE_H - (541.9 + ASCENT * 10)
    c.drawString(MARGIN_L, base, "P\u00e1g. %d/%d" % (page_no, total))
    c.drawRightString(815.9, base, "Data de atualiza\u00e7\u00e3o: " + date_iso)


def cover(c, date_iso, dotm):
    with zipfile.ZipFile(dotm) as z:
        logo = ImageReader(io.BytesIO(z.read("word/media/image1.jpeg")))
        horse = ImageReader(io.BytesIO(z.read("word/media/image2.jpeg")))
    c.drawImage(horse, 0, 0, width=610.55, height=PAGE_H - 283.32, preserveAspectRatio=False)
    c.drawImage(logo, 652.9, PAGE_H - 141.0, width=189.1, height=141.0)
    c.setFillColorRGB(0, 0, 0)
    c.setFont(FONT_B, 24)
    c.drawString(309.95, PAGE_H - 238.92, "Listagem Global de Pontos de Acesso")
    c.drawString(309.95, PAGE_H - 282.6, "Marcos e Caixas")
    c.setFont(FONT, 14.04)
    c.drawString(312.2, PAGE_H - 312.72, date_iso)
    c.showPage()


def paginate(rows):
    pages, cur, y = [], [], BODY_TOP + HEADER_H
    for row in rows:
        n = max(len(wrap(t, COL_W[i] - 2 * PAD - WRAP_SLACK)) for i, t in enumerate(row))
        h = n * LINE_H + 0.5
        if cur and y + h > BODY_BOTTOM:
            pages.append(cur)
            cur, y = [], BODY_TOP + HEADER_H
        cur.append((row, h))
        y += h
    if cur:
        pages.append(cur)
    return pages


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("xls")
    ap.add_argument("--data-ref", help="YYYY-MM-DD (por omissao: ultimo dia do mes anterior ao do ficheiro)")
    ap.add_argument("--out-dir")
    ap.add_argument("--base-dir", help="cria <base>\\Marcos e Caixas MM_YYYY, copia o xls para la e grava PDF+ZIP")
    ap.add_argument("--template-dir", default=str(Path(__file__).resolve().parent))
    ap.add_argument("--no-zip", action="store_true", help="nao gerar o ZIP com o PDF")
    ap.add_argument("--max-rows", type=int, default=0, help="apenas as primeiras N linhas (teste)")
    a = ap.parse_args()

    xls = Path(a.xls).resolve()
    if a.data_ref:
        ref = dt.date.fromisoformat(a.data_ref)
    else:
        m = re.search(r"(\d{4})_(\d{2})_(\d{2})", xls.name)
        if not m:
            sys.exit("Nao consegui deduzir a data do nome do ficheiro; use --data-ref.")
        first = dt.date(int(m[1]), int(m[2]), 1)
        ref = first - dt.timedelta(days=1)
    date_iso = ref.isoformat()
    out_dir = Path(a.out_dir) if a.out_dir else xls.parent
    if a.base_dir:
        gen = re.search(r"(\d{4})_(\d{2})_\d{2}", xls.name)
        month = "%s_%s" % (gen[2], gen[1]) if gen else (ref + dt.timedelta(days=1)).strftime("%m_%Y")
        out_dir = Path(a.base_dir) / ("Marcos e Caixas " + month)
    out_dir.mkdir(parents=True, exist_ok=True)
    if a.base_dir and xls.parent.resolve() != out_dir.resolve():
        shutil.copy2(xls, out_dir / xls.name)
    pdf = out_dir / ("%s_Lista de Marcos e Caixas %s.pdf" % (ref.strftime("%m_%Y"), ref.strftime("%Y%m%d")))
    dotm = Path(a.template_dir) / "Listagem Global de Pontos de Acesso.dotm"

    register_fonts()
    header, rows = read_report(str(xls), a.max_rows)
    print("Registos: %d | Data ref.: %s" % (len(rows), date_iso))
    pages = paginate(rows)
    total = len(pages) + 1
    with zipfile.ZipFile(dotm) as z:
        logo = ImageReader(io.BytesIO(z.read("word/media/image3.jpeg")))

    c = canvas.Canvas(str(pdf), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    c.setTitle(pdf.stem)
    c.setAuthor("")
    cover(c, date_iso, dotm)
    for pn, page in enumerate(pages, start=2):
        page_frame(c, pn, total, date_iso, logo)
        y = BODY_TOP
        draw_row(c, header, y, HEADER_H, header=True)
        y += HEADER_H
        for row, h in page:
            draw_row(c, row, y, h)
            y += h
        c.showPage()
    c.save()
    print("PDF gerado: %s (%d paginas)" % (pdf, total))
    if not a.no_zip:
        zp = pdf.with_suffix(".zip")
        with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            z.write(pdf, pdf.name)
        print("ZIP gerado: %s (%.1f MB)" % (zp, zp.stat().st_size / 1048576))


if __name__ == "__main__":
    main()
