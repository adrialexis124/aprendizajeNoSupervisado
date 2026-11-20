import html
import re
import time
import pandas as pd
from playwright.sync_api import sync_playwright

URL = "https://red.humana.med.ec/RedHumana"
registros = []


def limpiar_texto(valor: str | None) -> str:
    if not valor:
        return ""
    texto = html.unescape(valor).replace("\xa0", " ")
    texto = re.sub(r"\s+", " ", texto).strip()
    return "" if texto in {"-", "&nbsp;"} else texto


def parsear_tarjeta(card, pagina: int) -> dict:
    card_id = card.get_attribute("id") or ""
    # En DevExpress CardView, los campos se ubican en orden dentro del layout de la tarjeta
    statics = card.locator(".form-control-static").all()
    valores = [limpiar_texto(el.inner_text()) for el in statics]

    # Índices típicos según CardviewPrestadores_DXCardLayout:
    # 1: nombre, 2: producto, 3: direccion, 4: telefono, 5: tipo_atencion,
    # 6: ciudad, 8: servicio, 9: concepto_servicio, 10: especialidad
    def get_idx(idx: int) -> str:
        return valores[idx] if idx < len(valores) else ""

    return {
        "pagina": pagina,
        "card_id": card_id,
        "nombre": get_idx(1),
        "producto": get_idx(2),
        "direccion": get_idx(3),
        "telefono": get_idx(4),
        "tipo_atencion": get_idx(5),
        "ciudad": get_idx(6),
        "servicio": get_idx(8),
        "concepto_servicio": get_idx(9),
        "especialidad": get_idx(10),
    }


def obtener_total_paginas(page) -> int | None:
    texto_pager = page.locator("#CardviewPrestadores_DXPagerBottom").inner_text()
    match = re.search(r"Page\s+\d+\s+of\s+(\d+)", texto_pager, re.IGNORECASE)
    return int(match.group(1)) if match else None


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(URL, wait_until="networkidle")
    page.wait_for_selector("#CardviewPrestadores_DXMainTable")

    total_paginas = obtener_total_paginas(page)
    inicio = time.perf_counter()
    pagina_actual = 1

    while True:
        t_pag_inicio = time.perf_counter()
        primera_card = page.locator("[id^='CardviewPrestadores_DXDataCard']").first
        firma_anterior = primera_card.inner_text() if primera_card.count() > 0 else ""

        cards = page.locator("[id^='CardviewPrestadores_DXDataCard']").all()
        extraidos_pag = []
        for card in cards:
            fila = parsear_tarjeta(card, pagina_actual)
            extraidos_pag.append(fila)
            registros.append(fila)

        # Cálculo de avance y ETA
        elapsed = time.perf_counter() - inicio
        t_pag = time.perf_counter() - t_pag_inicio
        if total_paginas and total_paginas > 0:
            pct = (pagina_actual / total_paginas) * 100
            promedio_pag = elapsed / pagina_actual
            restantes = max(total_paginas - pagina_actual, 0)
            eta_seg = promedio_pag * restantes
            progreso_str = f"Página {pagina_actual}/{total_paginas} ({pct:5.1f}%)"
            eta_str = f"ETA: {eta_seg:5.1f}s"
        else:
            progreso_str = f"Página {pagina_actual}"
            eta_str = ""

        primer_nombre = extraidos_pag[0]["nombre"] if extraidos_pag else "N/A"
        print(
            f"[{progreso_str}] +{len(extraidos_pag)} items "
            f"(total: {len(registros)}) | {t_pag:.2f}s/pág | {eta_str} | "
            f"1º: {primer_nombre}",
            flush=True,
        )

        btn_siguiente = page.locator("#CardviewPrestadores_DXPagerBottom a[data-args='PBN']")
        parent_li = btn_siguiente.locator("..")

        if btn_siguiente.count() == 0 or "disabled" in (parent_li.get_attribute("class") or ""):
            break

        btn_siguiente.click()
        pagina_actual += 1

        page.wait_for_function(
            """([selector, prevText]) => {
                const el = document.querySelector(selector);
                return el && el.innerText.trim() !== prevText.trim();
            }""",
            arg=["[id^='CardviewPrestadores_DXDataCard']", firma_anterior],
            timeout=20000,
        )
        time.sleep(0.8)

    browser.close()

df = pd.DataFrame(registros)
df.to_csv("prestadores_humana_limpio.csv", index=False)
print(f"\nCompletado en {time.perf_counter() - inicio:.1f}s. Total filas: {len(df)}")
