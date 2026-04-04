from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path("/Users/brunonattino/Desktop/PAGINA TUTORIAS")
OUTPUT_DIR = ROOT / "clases" / "suma-resta"


CSS = """
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@600;800;900&display=swap');
:root {
    --base: #1C4A82;
    --bg: #f5f6f8;
    --tx: #333;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    font-family: 'Nunito', sans-serif;
    background: var(--bg);
    overflow: hidden;
    height: 100vh;
    width: 100vw;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: var(--tx);
}
.dk { position: relative; width: 100%; height: 100%; max-width: 1000px; display: flex; }
.sl {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    padding: 36px 40px 82px;
    opacity: 0;
    transform: scale(.96);
    transition: opacity .4s, transform .4s;
    pointer-events: none;
    z-index: 1;
}
.sl.on { opacity: 1; transform: scale(1); pointer-events: auto; z-index: 10; }
.sl.pv { opacity: 0; transform: translateX(-50px) scale(.95); }
.sl.nx { opacity: 0; transform: translateX(50px) scale(.95); }
.head-title {
    background: var(--base);
    color: white;
    padding: 10px 40px;
    font-size: 32px;
    font-weight: 900;
    margin-bottom: 24px;
    display: inline-block;
    border-radius: 12px;
    text-align: center;
}
.sub-text {
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 22px;
    text-align: center;
    line-height: 1.4;
}
.pb { position: fixed; top: 0; left: 0; height: 6px; background: var(--base); transition: width .4s; z-index: 100; }
.nv {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 60px;
    background: white;
    border-top: 1px solid #ddd;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 40px;
    z-index: 100;
}
.nb {
    background: #eee;
    color: var(--base);
    border: none;
    padding: 10px 20px;
    border-radius: 8px;
    font-family: 'Nunito', sans-serif;
    font-size: 16px;
    font-weight: 900;
    cursor: pointer;
    transition: all .2s;
}
.nb:hover { background: #ddd; }
.nb:disabled { opacity: 0.3; cursor: not-allowed; }
.sc { color: #888; font-size: 16px; font-weight: 900; }
.stp {
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    pointer-events: none;
}
.stp.shwn { opacity: 1; transform: translateY(0); pointer-events: auto; }
.pnl {
    background: #fff;
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    border: 3px solid #eaeaea;
    width: 100%;
}
.pnl-border {
    background: #fff;
    border: 4px solid var(--base);
    border-radius: 20px;
    padding: 24px;
    width: 100%;
}
.hl { color: var(--base); font-weight: 900; }
.btn {
    background: var(--base);
    color: white;
    border: none;
    padding: 14px 24px;
    border-radius: 12px;
    font-size: 20px;
    font-weight: 900;
    cursor: pointer;
    transition: transform .2s;
    font-family: 'Nunito', sans-serif;
}
.btn:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(28,74,130,0.3); }
.math-eq {
    font-size: 52px;
    font-weight: 900;
    color: var(--base);
    background: #fff;
    padding: 12px 30px;
    border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    border: 3px dashed #bbdefb;
    margin: 12px;
    text-align: center;
}
.chip-row, .card-row, .base-row, .quiz-row {
    display: flex;
    justify-content: center;
    gap: 18px;
    width: 100%;
    flex-wrap: wrap;
}
.mini-chip {
    background: #eef5ff;
    border: 2px solid #b6d4f3;
    border-radius: 999px;
    padding: 12px 18px;
    font-size: 20px;
    font-weight: 800;
}
.idea-card {
    flex: 1 1 220px;
    background: linear-gradient(180deg, #ffffff 0%, #f7fbff 100%);
    border-radius: 18px;
    padding: 18px;
    border: 3px solid #d7e7f7;
    min-height: 220px;
}
.idea-card h3 {
    font-size: 28px;
    color: var(--base);
    margin-bottom: 10px;
}
.idea-card p {
    font-size: 21px;
    line-height: 1.45;
}
.base-card {
    flex: 1 1 320px;
    background: #fff;
    border-radius: 20px;
    padding: 18px;
    border: 4px solid #d9e7f6;
    box-shadow: 0 10px 26px rgba(0,0,0,0.06);
}
.base-card h3 {
    font-size: 28px;
    color: var(--base);
    text-align: center;
    margin-bottom: 14px;
}
.place-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
}
.place-box {
    background: #f8fbff;
    border: 2px dashed #c6d9ef;
    border-radius: 16px;
    padding: 12px;
    min-height: 184px;
}
.place-title {
    text-align: center;
    font-size: 19px;
    font-weight: 900;
    color: #315c8d;
    margin-bottom: 10px;
}
.block-stack {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    align-items: flex-start;
    justify-content: center;
    min-height: 88px;
}
.unit {
    width: 28px;
    height: 28px;
    border-radius: 6px;
    background: var(--fill, #9DDEFF);
    border: 2px solid rgba(0,0,0,0.18);
}
.rod {
    width: 30px;
    height: 108px;
    border-radius: 8px;
    background: var(--fill, #9DE3BD);
    border: 2px solid rgba(0,0,0,0.18);
}
.flat {
    width: 94px;
    height: 94px;
    border-radius: 12px;
    background:
        linear-gradient(rgba(255,255,255,0.42), rgba(255,255,255,0.42)),
        repeating-linear-gradient(0deg, transparent, transparent 18px, rgba(0,0,0,0.08) 18px, rgba(0,0,0,0.08) 20px),
        repeating-linear-gradient(90deg, transparent, transparent 18px, rgba(0,0,0,0.08) 18px, rgba(0,0,0,0.08) 20px),
        var(--fill, #FFE082);
    border: 2px solid rgba(0,0,0,0.18);
}
.number-tag {
    margin-top: 10px;
    text-align: center;
    font-size: 20px;
    font-weight: 900;
}
.two-col {
    display: grid;
    grid-template-columns: 1.15fr .85fr;
    gap: 18px;
    width: 100%;
    align-items: stretch;
}
.step-list {
    display: flex;
    flex-direction: column;
    gap: 14px;
}
.step-box {
    background: #f7fbff;
    border-left: 8px solid var(--base);
    padding: 14px 16px;
    border-radius: 14px;
    font-size: 20px;
    line-height: 1.4;
    font-weight: 700;
}
.column-wrap {
    display: grid;
    grid-template-columns: 1fr 300px;
    gap: 18px;
    width: 100%;
    align-items: start;
}
.alg-board {
    background: #fff;
    border: 4px solid var(--base);
    border-radius: 20px;
    padding: 22px 26px;
}
.alg-grid {
    display: grid;
    grid-template-columns: 68px repeat(3, 76px);
    grid-auto-rows: 58px;
    align-items: center;
    justify-items: center;
    margin: 0 auto;
    width: max-content;
}
.alg-grid.long {
    grid-template-columns: 68px repeat(3, 76px);
}
.alg-label {
    font-size: 20px;
    font-weight: 900;
    color: #57779d;
}
.alg-digit {
    width: 60px;
    height: 46px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
    background: #f7fbff;
    font-size: 34px;
    font-weight: 900;
    color: #173b67;
    border: 2px solid #d4e5f8;
}
.alg-digit.dim { color: #b6c6d8; }
.alg-digit.reserve {
    height: 38px;
    background: #fff7df;
    border-color: #f0cf67;
    color: #9f6200;
    font-size: 24px;
}
.alg-line {
    grid-column: 2 / span 3;
    width: 100%;
    height: 4px;
    background: #395f90;
    border-radius: 999px;
}
.alg-sign {
    font-size: 30px;
    font-weight: 900;
    color: #c94d2a;
}
.side-panel {
    background: linear-gradient(180deg, #fefefe 0%, #f4f9ff 100%);
    border: 3px solid #d5e4f5;
    border-radius: 18px;
    padding: 18px;
    min-height: 290px;
}
.side-panel h3 {
    font-size: 24px;
    color: var(--base);
    margin-bottom: 12px;
}
.side-panel p {
    font-size: 20px;
    line-height: 1.45;
}
.story-card {
    width: 100%;
    border-radius: 28px;
    padding: 28px;
    display: grid;
    grid-template-columns: 120px 1fr;
    gap: 24px;
    align-items: center;
}
.story-emoji {
    font-size: 114px;
    text-align: center;
    animation: bob 2.8s infinite;
}
.story-card h2 {
    font-size: 30px;
    margin-bottom: 12px;
}
.story-card p {
    font-size: 24px;
    line-height: 1.45;
}
.summary-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
    width: 100%;
}
.summary-item {
    background: #fff;
    border-radius: 16px;
    padding: 16px 18px;
    border: 3px solid #dbe7f4;
    font-size: 23px;
    line-height: 1.45;
}
.count-board {
    display: flex;
    justify-content: center;
    gap: 20px;
    width: 100%;
    flex-wrap: wrap;
}
.count-card {
    flex: 1 1 260px;
    background: linear-gradient(180deg, #ffffff 0%, #f6fbff 100%);
    border-radius: 22px;
    padding: 20px;
    border: 4px solid #d6e8f8;
    box-shadow: 0 12px 24px rgba(0,0,0,0.06);
    text-align: center;
}
.count-card h3 {
    font-size: 28px;
    margin-bottom: 12px;
    color: var(--base);
}
.emoji-pack {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    min-height: 86px;
    margin-bottom: 12px;
}
.fact-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
    width: 100%;
}
.fact-box {
    background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%);
    border-radius: 18px;
    padding: 16px;
    border: 3px solid #d8e7f6;
    min-height: 170px;
}
.fact-box h4 {
    font-size: 24px;
    color: var(--base);
    margin-bottom: 10px;
    text-align: center;
}
.fact-box p {
    font-size: 21px;
    line-height: 1.45;
    text-align: center;
}
.msg-area {
    font-size: 24px;
    font-weight: 900;
    height: 40px;
    text-align: center;
    margin-top: 20px;
}
.hero-title {
    font-size: 68px;
    color: var(--base);
    margin-bottom: 18px;
    text-align: center;
    line-height: 1;
}
.hero-sub {
    font-size: 28px;
    font-weight: 700;
    text-align: center;
    max-width: 720px;
}
.hero-emoji {
    font-size: 108px;
    margin-top: 28px;
    animation: bounce 2s infinite;
}
.formula-row {
    display: flex;
    justify-content: center;
    gap: 18px;
    align-items: center;
    flex-wrap: wrap;
    width: 100%;
}
.label-pill {
    background: #eef5ff;
    border: 2px solid #c5dcf5;
    border-radius: 14px;
    padding: 10px 16px;
    font-size: 22px;
    font-weight: 900;
    color: var(--base);
}
.warn-card {
    background: #fff8e5;
    border: 4px solid #f0ca59;
    border-radius: 20px;
    padding: 20px;
    font-size: 22px;
    line-height: 1.45;
    width: 100%;
}
.decomp-flow {
    display: flex;
    justify-content: center;
    gap: 14px;
    flex-wrap: wrap;
    width: 100%;
    align-items: center;
}
.decomp-box {
    background: #fff;
    border: 3px solid #d4e6f7;
    border-radius: 18px;
    padding: 14px 18px;
    font-size: 28px;
    font-weight: 900;
    color: var(--base);
}
.arrow {
    font-size: 34px;
    font-weight: 900;
    color: #4d6d94;
}
@keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-16px); } }
@keyframes bob { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
"""


JS = """
const S=document.querySelectorAll('.sl'); let c=0; const T=S.length;
function ui() {
    S.forEach((s,i)=>{
        s.classList.remove('on','pv','nx');
        if(i===c) s.classList.add('on');
        else if(i<c) s.classList.add('pv');
        else s.classList.add('nx');
    });
    document.getElementById('pb').style.width=((c+1)/T*100)+'%';
    document.getElementById('sc').textContent=`${c+1} / ${T}`;
    document.getElementById('pv').disabled=c===0;
    document.getElementById('nx').disabled=c===T-1;
}
function go(d) {
    if(d>0) {
        const hid = S[c].querySelectorAll('.stp:not(.shwn)');
        if(hid.length > 0) { hid[0].classList.add('shwn'); return; }
    } else {
        const shw = S[c].querySelectorAll('.stp.shwn');
        if(shw.length > 0) { shw[shw.length-1].classList.remove('shwn'); return; }
    }
    const n=c+d;
    if(n>=0 && n<T) { c=n; ui(); }
}
document.addEventListener('keydown', e => {
    if(e.key==='ArrowRight' || e.key===' ') go(1);
    if(e.key==='ArrowLeft') go(-1);
});
function chkAns(btn, correct, exp) {
    const wrap = btn.closest('.sl');
    const buttons = btn.parentElement.querySelectorAll('.btn');
    const msg = wrap.querySelector('.msg-area');
    buttons.forEach(b => {
        b.disabled = false;
        b.style.background = 'var(--base)';
        b.style.transform = 'scale(1)';
    });
    if (correct) {
        btn.style.background = '#047857';
        btn.style.transform = 'scale(1.06)';
        msg.textContent = `¡Muy bien! ${exp}`;
        msg.style.color = '#047857';
    } else {
        btn.style.background = '#b91c1c';
        msg.textContent = 'Revisa las unidades primero y vuelve a intentarlo.';
        msg.style.color = '#b91c1c';
    }
}
ui();
"""


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def slide(content: str) -> str:
    return f'<div class="sl">{content}</div>'


def intro_slide(title: str, subtitle: str, emoji: str) -> str:
    return slide(
        f"""
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center;">
            <h1 class="hero-title">{esc(title)}</h1>
            <p class="hero-sub">{subtitle}</p>
            <div class="hero-emoji">{emoji}</div>
        </div>
        """
    )


def unit_blocks(count: int, color: str = "#9DDEFF") -> str:
    return "".join(f'<span class="unit" style="--fill:{color};"></span>' for _ in range(count))


def rods(count: int, color: str = "#9DE3BD") -> str:
    return "".join(f'<span class="rod" style="--fill:{color};"></span>' for _ in range(count))


def flats(count: int, color: str = "#FFE082") -> str:
    return "".join(f'<span class="flat" style="--fill:{color};"></span>' for _ in range(count))


def base_ten_card(number: int, title: str, colors: tuple[str, str, str] = ("#FFE082", "#9DE3BD", "#9DDEFF")) -> str:
    hundreds = number // 100
    tens = (number % 100) // 10
    units = number % 10
    return f"""
    <div class="base-card">
        <h3>{esc(title)}</h3>
        <div class="place-grid">
            <div class="place-box">
                <div class="place-title">Centenas</div>
                <div class="block-stack">{flats(hundreds, colors[0])}</div>
                <div class="number-tag">{hundreds}</div>
            </div>
            <div class="place-box">
                <div class="place-title">Decenas</div>
                <div class="block-stack">{rods(tens, colors[1])}</div>
                <div class="number-tag">{tens}</div>
            </div>
            <div class="place-box">
                <div class="place-title">Unidades</div>
                <div class="block-stack">{unit_blocks(units, colors[2])}</div>
                <div class="number-tag">{units}</div>
            </div>
        </div>
        <div class="math-eq" style="font-size:34px;">{number}</div>
    </div>
    """


def notebook_slide(prompt: str, hidden_steps: list[str], visual: str = "") -> str:
    steps = "".join(f'<div class="stp decomp-box">{step}</div>' for step in hidden_steps)
    return slide(
        f"""
        <div class="head-title" style="background:#F57C00;">Abre tu cuaderno</div>
        <p class="sub-text">{prompt}</p>
        {visual}
        <div class="decomp-flow" style="margin-top:20px;">{steps}</div>
        """
    )


def emoji_pack(emoji: str, count: int, size: int = 52) -> str:
    return "".join(f'<span style="font-size:{size}px; line-height:1;">{emoji}</span>' for _ in range(count))


def picture_operation_slide(
    title: str,
    subtitle: str,
    left_title: str,
    left_visual: str,
    right_title: str,
    right_visual: str,
    operator: str,
    result_text: str,
    note: str,
    left_border: str = "#FFE082",
    right_border: str = "#9DE3BD",
    result_border: str = "#E1BEE7",
) -> str:
    return slide(
        f"""
        <div class="head-title">{esc(title)}</div>
        <p class="sub-text">{subtitle}</p>
        <div class="count-board">
            <div class="count-card" style="border-color:{left_border}; background:linear-gradient(180deg,#fffdf1 0%,#ffffff 100%);">
                <h3>{left_title}</h3>
                <div class="emoji-pack">{left_visual}</div>
            </div>
            <div class="math-eq" style="font-size:60px;">{operator}</div>
            <div class="count-card" style="border-color:{right_border}; background:linear-gradient(180deg,#f4fff7 0%,#ffffff 100%);">
                <h3>{right_title}</h3>
                <div class="emoji-pack">{right_visual}</div>
            </div>
        </div>
        <div class="stp math-eq" style="border-color:{result_border}; background:#faf4ff;">{result_text}</div>
        <div class="stp mini-chip">{note}</div>
        """
    )


def exercise_cards_slide(title: str, subtitle: str, items: list[tuple[str, str, str, str]]) -> str:
    cards = []
    for emoji, expr, ans, border in items:
        cards.append(
            f"""
            <div class="idea-card" style="border-color:{border}; background:linear-gradient(180deg,#ffffff 0%,#fbfcff 100%);">
                <div style="font-size:60px; text-align:center; margin-bottom:10px;">{emoji}</div>
                <div style="font-size:34px; font-weight:900; text-align:center; color:#234c7c; margin-bottom:10px;">{expr}</div>
                <div class="stp math-eq" style="font-size:38px; border-color:{border}; margin:0;">{ans}</div>
            </div>
            """
        )
    return slide(
        f"""
        <div class="head-title">{esc(title)}</div>
        <p class="sub-text">{subtitle}</p>
        <div class="card-row">{''.join(cards)}</div>
        """
    )


def fact_boxes_slide(title: str, subtitle: str, items: list[tuple[str, str, str]]) -> str:
    boxes = []
    for heading, text, border in items:
        boxes.append(
            f"""
            <div class="fact-box" style="border-color:{border};">
                <h4>{heading}</h4>
                <p>{text}</p>
            </div>
            """
        )
    return slide(
        f"""
        <div class="head-title">{esc(title)}</div>
        <p class="sub-text">{subtitle}</p>
        <div class="fact-grid">{''.join(boxes)}</div>
        """
    )


def quiz_slide(title: str, question: str, options: list[str], ok: int, exp: str) -> str:
    buttons = []
    exp_attr = esc(json.dumps(exp))
    for idx, opt in enumerate(options):
        buttons.append(
            f"<button class=\"btn\" onclick=\"chkAns(this, {str(idx == ok).lower()}, {exp_attr})\">{esc(opt)}</button>"
        )
    return slide(
        f"""
        <div class="head-title">{esc(title)}</div>
        <div class="pnl-border" style="border-color:#d63384; background:#fff7fb;">
            <p style="font-size:32px; font-weight:800; text-align:center; margin-bottom:24px;">{question}</p>
            <div class="quiz-row">{''.join(buttons)}</div>
            <div class="msg-area"></div>
        </div>
        """
    )


def problem_slide(title: str, emoji: str, body: str, answer: str, bg: str, border: str) -> str:
    return slide(
        f"""
        <div class="head-title">Problemas Situacionales</div>
        <div class="story-card" style="background:{bg}; border:5px solid {border};">
            <div class="story-emoji">{emoji}</div>
            <div>
                <h2 style="color:{border};">{esc(title)}</h2>
                <p>{body}</p>
                <div class="stp" style="margin-top:18px; background:#fff; border-left:10px solid {border}; border-radius:18px; padding:18px 20px;">
                    <p style="font-size:20px; font-weight:800; color:#555; margin-bottom:8px;">Respuesta guiada:</p>
                    <div style="font-size:28px; font-weight:900; line-height:1.4;">{answer}</div>
                </div>
            </div>
        </div>
        """
    )


def summary_slide(items: list[str]) -> str:
    body = "".join(f'<div class="stp summary-item">{item}</div>' for item in items)
    return slide(
        f"""
        <div class="head-title">Resumen</div>
        <div class="summary-list">{body}</div>
        """
    )


def finish_slide(message: str, emoji: str) -> str:
    return slide(
        f"""
        <div class="head-title" style="background:#047857;">Cierre</div>
        <div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">
            <p style="font-size:38px; font-weight:800; line-height:1.45; max-width:780px;">{message}</p>
            <div style="font-size:120px; margin-top:30px; animation:bounce 2s infinite;">{emoji}</div>
        </div>
        """
    )


def alg_board(rows: list[list[str]], side_title: str, side_notes: list[str], long: bool = False) -> str:
    grid_rows = []
    for row in rows:
        label, *cells = row
        grid_rows.append(f'<div class="alg-label">{label}</div>')
        for cell in cells:
            classes = ["alg-digit"]
            text = cell
            if cell.startswith("r:"):
                classes.append("reserve")
                text = cell[2:]
            elif cell == "_":
                classes.append("dim")
                text = ""
            grid_rows.append(f'<div class="{" ".join(classes)}">{esc(text)}</div>')
    lines_html = '<div class="alg-line"></div>'
    notes_html = "".join(f'<p class="stp" style="margin-bottom:12px;">{note}</p>' for note in side_notes)
    return f"""
    <div class="column-wrap">
        <div class="alg-board">
            <div class="alg-grid{' long' if long else ''}">
                {''.join(grid_rows)}
                {lines_html}
            </div>
        </div>
        <div class="side-panel">
            <h3>{esc(side_title)}</h3>
            {notes_html}
        </div>
    </div>
    """


def html_doc(title: str, slides: list[str]) -> str:
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>{esc(title)}</title>
    <style>{CSS}</style>
</head>
<body>
    <div class="pb" id="pb"></div>
    <div class="dk">
        {''.join(slides)}
    </div>
    <div class="nv">
        <button class="nb" id="pv" onclick="go(-1)">⬅ Anterior</button>
        <div class="sc" id="sc">1 / {len(slides)}</div>
        <button class="nb" id="nx" onclick="go(1)">Siguiente ➡</button>
    </div>
    <script>{JS}</script>
</body>
</html>
"""


def module_one() -> str:
    slides: list[str] = []
    slides.append(intro_slide("¡Suma y resta 1!", "Bloques, sumandos y primeras estrategias para sumar sin usar los dedos.", "🧱"))
    slides.append(
        picture_operation_slide(
            "¿Qué es sumar?",
            "Sumar es <b class=\"hl\">juntar</b> dos cantidades para formar una cantidad mayor.",
            "Primero tengo 6",
            emoji_pack("🟨", 6, 54),
            "Luego agrego 3",
            emoji_pack("🟩", 3, 54),
            "+",
            "6 + 3 = 9",
            "Primero miro lo que ya tengo y después agrego lo nuevo.",
            "#FFE082",
            "#9DE3BD",
            "#E1BEE7",
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Elementos de la suma</div>
            <div class="pnl-border" style="background:#f8fbff;">
                <div class="formula-row" style="margin-bottom:16px;">
                    <div class="label-pill stp">Sumando</div>
                    <div class="label-pill stp">Sumando</div>
                    <div class="label-pill stp">Suma total</div>
                </div>
                <div class="math-eq" style="font-size:64px;">7 + 2 = 9</div>
                <div class="stp chip-row">
                    <div class="mini-chip">7 es un <b>sumando</b>.</div>
                    <div class="mini-chip">2 es otro <b>sumando</b>.</div>
                    <div class="mini-chip">9 es la <b>suma</b>.</div>
                </div>
            </div>
            """
        )
    )
    slides.append(
        fact_boxes_slide(
            "Miramos bloques, no dedos",
            "Queremos <b class=\"hl\">ver las cantidades</b>, no solo contarlas de memoria.",
            [
                ("🟨 Unidades", "Cada cubito vale <b>1</b>. Los cubitos muestran la cantidad exacta.", "#FFE082"),
                ("🟩 Decenas", "Una barra vale <b>10</b>. Así vemos más rápido números grandes.", "#9DE3BD"),
                ("🟪 Idea clave", "Los bloques ayudan a pensar sin depender de los dedos.", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Bloques grandes y claros</div>
            <p class="sub-text">Con bloques grandes distinguimos mejor <b class="hl">cuánto tenemos</b> y <b class="hl">qué agregamos</b>.</p>
            <div class="card-row">
                <div class="idea-card" style="border-color:#9DDEFF;">
                    <h3>7</h3>
                    <div class="block-stack">""" + unit_blocks(7) + """</div>
                    <p style="margin-top:12px;">Siete unidades son siete cubitos.</p>
                </div>
                <div class="idea-card stp" style="border-color:#9DE3BD;">
                    <h3>12</h3>
                    <div class="block-stack">""" + rods(1) + unit_blocks(2) + """</div>
                    <p style="margin-top:12px;">Doce es <b>1 decena y 2 unidades</b>.</p>
                </div>
                <div class="idea-card stp" style="border-color:#FFB74D;">
                    <h3>15</h3>
                    <div class="block-stack">""" + rods(1, "#FFB74D") + unit_blocks(5, "#E1BEE7") + """</div>
                    <p style="margin-top:12px;">Ver los bloques hace más fácil sumar.</p>
                </div>
            </div>
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Propiedad conmutativa</div>
            <p class="sub-text">Si cambiamos el orden de los sumandos, la suma <b class="hl">no cambia</b>.</p>
            <div class="formula-row">
                <div class="math-eq stp" style="background:#fff7e8; border-color:#FFB74D;">4 + 2 = 6</div>
                <div class="math-eq stp" style="background:#f2fff5; border-color:#9DE3BD;">2 + 4 = 6</div>
            </div>
            <div class="stp pnl-border" style="background:linear-gradient(135deg,#fff7e8 0%,#f4fff8 50%,#f8f2ff 100%); text-align:center;">
                <div style="font-size:30px; font-weight:900;">El total sigue siendo <span class="hl">6</span>.</div>
                <p style="font-size:22px; margin-top:10px;">Mover los sumandos no cambia la cantidad final.</p>
            </div>
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Elemento neutro</div>
            <div class="pnl-border">
                <div class="math-eq">8 + 0 = 8</div>
                <div class="stp warn-card">
                    Si sumo <b>0</b>, no agrego ningún bloque nuevo. Por eso el número queda igual.
                </div>
                <div class="stp formula-row">
                    <div class="pnl" style="max-width:300px; text-align:center;">""" + unit_blocks(8, "#FFE082") + """</div>
                    <div class="math-eq" style="font-size:54px;">+</div>
                    <div class="pnl" style="max-width:220px; text-align:center; font-size:34px; font-weight:900;">0 bloques</div>
                </div>
            </div>
            """
        )
    )
    slides.append(
        picture_operation_slide(
            "Suma de 1 dígito con 1 dígito",
            "Primero miramos el número grande y después agregamos el otro sumando.",
            "Tengo 5 globos",
            emoji_pack("🎈", 5, 56),
            "Agrego 3 más",
            emoji_pack("🟣", 3, 54),
            "+",
            "5 + 3 = 8",
            "Parto en 5 y agrego 1, 2, 3.",
            "#FFB74D",
            "#E1BEE7",
            "#9DDEFF",
        )
    )
    slides.append(
        exercise_cards_slide(
            "Practiquemos con sumas pequeñas",
            "Resuelve estas sumas mirando las cantidades.",
            [
                ("🍎", "4 + 3", "= 7", "#FFE082"),
                ("⚽", "6 + 2", "= 8", "#9DE3BD"),
                ("🟣", "5 + 4", "= 9", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        notebook_slide(
            "Escribe la suma y resuélvela con bloques: <b class=\"hl\">7 + 2</b>.",
            ["7 + 2", "7, 8, 9", "Resultado: 9"],
            '<div class="pnl" style="max-width:760px; text-align:center;"><div class="block-stack">' +
            unit_blocks(7, "#FFE082") + '<span class="math-eq" style="font-size:46px;">+</span>' + unit_blocks(2, "#9DE3BD") +
            "</div></div>",
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Cruzar la decena</div>
            <p class="sub-text">Cuando estamos cerca del 10, conviene <b class="hl">descomponer</b> para llegar primero a una decena completa.</p>
            <div class="decomp-flow" style="margin-bottom:18px;">
                <div class="decomp-box">8 + 5</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">8 + 2 + 3</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">10 + 3</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">13</div>
            </div>
            <div class="stp warn-card">Partimos el <b>5</b> en <b>2 y 3</b> porque a 8 le faltan 2 para llegar a 10.</div>
            """
        )
    )
    slides.append(
        picture_operation_slide(
            "Llegar a 10 primero",
            "Esta estrategia hace la suma más rápida y más ordenada.",
            "Tengo 9 estrellas",
            emoji_pack("⭐", 9, 52),
            "Agrego 4",
            emoji_pack("🟢", 4, 50),
            "+",
            "9 + 4 = 13",
            "Primero hago 9 + 1 = 10 y después sumo 3.",
            "#FFE082",
            "#9DE3BD",
            "#FFB74D",
        )
    )
    slides.append(
        exercise_cards_slide(
            "Cruzando la decena",
            "Descompón el segundo sumando para llegar a 10.",
            [
                ("🌟", "9 + 4", "= 13", "#FFB74D"),
                ("🍊", "8 + 5", "= 13", "#9DE3BD"),
                ("🧩", "7 + 6", "= 13", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Números de 2 dígitos</div>
            <p class="sub-text">Un número de 2 dígitos se puede pensar como <b class="hl">decenas y unidades</b>.</p>
            <div class="base-row">
                """ + base_ten_card(23, "23 = 2 decenas y 3 unidades", ("#FFE082", "#9DE3BD", "#E1BEE7")) + """
            </div>
            <div class="stp mini-chip">23 es lo mismo que 20 + 3.</div>
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Descomponer para sumar</div>
            <p class="sub-text">Si sumamos un número de 2 dígitos con uno de 1 dígito, miramos primero sus unidades.</p>
            <div class="decomp-flow">
                <div class="decomp-box">23 + 5</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">(20 + 3) + 5</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">20 + 8</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">28</div>
            </div>
            <div class="stp base-row" style="margin-top:20px;">
                """ + base_ten_card(23, "Partimos de 23", ("#FFE082", "#9DE3BD", "#E1BEE7")) + base_ten_card(28, "Agregamos 5 unidades", ("#FFB74D", "#9DE3BD", "#9DDEFF")) + """
            </div>
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Otro ejemplo con descomposición</div>
            <p class="sub-text">A veces conviene partir el sumando pequeño para llegar a 10 y seguir.</p>
            <div class="decomp-flow">
                <div class="decomp-box">18 + 6</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">18 + 2 + 4</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">20 + 4</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">24</div>
            </div>
            <div class="stp warn-card" style="margin-top:18px;">Al 18 le faltan <b>2</b> para llegar a 20. Por eso partimos el 6 en <b>2 y 4</b>.</div>
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Un ejemplo más</div>
            <p class="sub-text">Mira cómo se ve esta suma cuando pensamos en llegar a la siguiente decena.</p>
            <div class="decomp-flow">
                <div class="decomp-box">27 + 4</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">27 + 3 + 1</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">30 + 1</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">31</div>
            </div>
            <div class="stp mini-chip">A 27 le faltan 3 para llegar a 30.</div>
            """
        )
    )
    slides.append(
        exercise_cards_slide(
            "Práctica con 2 dígitos",
            "Ahora resuelve sumas de 2 dígitos con 1 dígito.",
            [
                ("🚗", "24 + 3", "= 27", "#FFE082"),
                ("🐠", "36 + 2", "= 38", "#9DE3BD"),
                ("🟣", "41 + 5", "= 46", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        notebook_slide(
            "Resuelve descomponiendo: <b class=\"hl\">29 + 4</b>.",
            ["29 + 4", "29 + 1 + 3", "30 + 3", "Resultado: 33"],
        )
    )
    slides.append(
        picture_operation_slide(
            "Suma visual con decenas",
            "Las barras y los cubitos también nos ayudan a sumar números más grandes.",
            "26",
            rods(2, "#9DE3BD") + unit_blocks(6, "#FFE082"),
            "7 unidades más",
            unit_blocks(7, "#FFB74D"),
            "+",
            "26 + 7 = 33",
            "Primero 26 + 4 = 30 y luego + 3.",
            "#9DE3BD",
            "#FFB74D",
            "#E1BEE7",
        )
    )
    slides.append(
        exercise_cards_slide(
            "Ejercicios relámpago",
            "Tres sumas más para practicar sin usar los dedos.",
            [
                ("🎨", "34 + 5", "= 39", "#FFB74D"),
                ("🌈", "18 + 7", "= 25", "#9DE3BD"),
                ("🧸", "45 + 4", "= 49", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        picture_operation_slide(
            "¿Qué suma representa?",
            "Observa las dos colecciones y escribe la suma correcta.",
            "Colección A",
            emoji_pack("🍓", 6, 52),
            "Colección B",
            emoji_pack("🍇", 5, 52),
            "+",
            "6 + 5 = 11",
            "Seis frutas más cinco frutas forman once.",
            "#FFB74D",
            "#9DE3BD",
            "#FFE082",
        )
    )
    slides.append(
        quiz_slide(
            "Desafío rápido",
            "¿Cuál descomposición ayuda mejor a resolver <b>8 + 5</b>?",
            ["8 + 4 + 1", "8 + 2 + 3", "8 + 5 + 5"],
            1,
            "8 necesita 2 para llegar a 10.",
        )
    )
    slides.append(
        problem_slide(
            "Lápices de colores",
            "✏️",
            "Sofía tenía <b>23 lápices</b> y su tía le regaló <b>5 más</b>. ¿Cuántos lápices tiene ahora?",
            "23 + 5 = 28<br><span style='color:var(--base);'>Sofía tiene 28 lápices.</span>",
            "#E3F2FD",
            "#1976D2",
        )
    )
    slides.append(
        problem_slide(
            "Entradas al zoológico",
            "🦁",
            "Un curso compró <b>8 entradas</b> y después compró <b>5 más</b>. ¿Cuántas entradas tienen en total?",
            "8 + 5 = 13<br><span style='color:var(--base);'>En total tienen 13 entradas.</span>",
            "#FFF3E0",
            "#EF6C00",
        )
    )
    slides.append(
        problem_slide(
            "Libros prestados",
            "📚",
            "En una mesa había <b>34 libros</b>. La bibliotecaria llevó <b>7 libros más</b>. ¿Cuántos libros hay ahora?",
            "34 + 7 = 41<br><span style='color:var(--base);'>Ahora hay 41 libros.</span>",
            "#F3E5F5",
            "#8E44AD",
        )
    )
    slides.append(
        problem_slide(
            "Globos en la fiesta",
            "🎈",
            "Había <b>27 globos</b> decorando una fiesta y colgaron <b>4 globos más</b>. ¿Cuántos globos hay ahora?",
            "27 + 4 = 31<br><span style='color:var(--base);'>Ahora hay 31 globos.</span>",
            "#FFF8E1",
            "#F9A825",
        )
    )
    slides.append(
        problem_slide(
            "Peces del acuario",
            "🐟",
            "Un acuario tenía <b>18 peces</b> y llegaron <b>6 peces más</b>. ¿Cuántos peces hay en total?",
            "18 + 6 = 24<br><span style='color:var(--base);'>En total hay 24 peces.</span>",
            "#E8F5E9",
            "#2E7D32",
        )
    )
    slides.append(
        summary_slide(
            [
                "<b>Sumando + sumando = suma.</b> Los números que juntamos se llaman sumandos.",
                "<b>Propiedad conmutativa:</b> 4 + 2 y 2 + 4 dan el mismo resultado.",
                "<b>Elemento neutro:</b> si sumo 0, el número no cambia.",
                "<b>Bloques y descomposición:</b> ayudan a sumar sin usar los dedos.",
            ]
        )
    )
    slides.append(finish_slide("Ya puedes sumar con bloques, reconocer los sumandos y descomponer para avanzar con seguridad.", "🌟"))
    assert len(slides) == 30, len(slides)
    return html_doc("Suma y resta 1", slides)


def module_two() -> str:
    slides: list[str] = []
    slides.append(intro_slide("¡Suma y resta 2!", "Centenas, decenas, suma de 3 dígitos y una primera entrada al mundo de la resta.", "🏗️"))
    slides.append(
        slide(
            """
            <div class="head-title">Centenas, decenas y unidades</div>
            <p class="sub-text">Con bloques grandes podemos representar números de <b class="hl">3 dígitos</b>.</p>
            <div class="base-row">
                """ + base_ten_card(248, "248 = 2 centenas, 4 decenas y 8 unidades", ("#FFE082", "#9DE3BD", "#E1BEE7")) + """
            </div>
            <div class="stp mini-chip">Una centena vale 100. Una decena vale 10. Una unidad vale 1.</div>
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Otro ejemplo visual</div>
            <p class="sub-text">Miremos cómo se ve un número grande cuando lo separamos por valor posicional.</p>
            <div class="base-row">
                """ + base_ten_card(356, "356 = 3 centenas, 5 decenas y 6 unidades", ("#FFB74D", "#9DE3BD", "#9DDEFF")) + """
            </div>
            <div class="stp mini-chip">356 = 300 + 50 + 6.</div>
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Sumar 3 dígitos con bloques</div>
            <p class="sub-text">Primero juntamos unidades, después decenas y finalmente centenas.</p>
            <div class="base-row">
                """ + base_ten_card(125, "Primer número", ("#FFE082", "#9DE3BD", "#9DDEFF")) +
            base_ten_card(243, "Segundo número", ("#FFB74D", "#B39DDB", "#FF9D9D")) + """
            </div>
            <div class="stp decomp-flow" style="margin-top:18px;">
                <div class="decomp-box">125 + 243</div>
                <div class="arrow">→</div>
                <div class="decomp-box">300 + 60 + 8</div>
                <div class="arrow">→</div>
                <div class="decomp-box">368</div>
            </div>
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Cuando hay reserva</div>
            <p class="sub-text">Si junto 10 unidades, las cambio por 1 decena. Si junto 10 decenas, las cambio por 1 centena.</p>
            <div class="two-col">
                <div class="pnl-border">
                    <div class="math-eq">138 + 274</div>
                    <div class="stp step-box">Unidades: 8 + 4 = 12. Escribo 2 y <b>reservo 1 decena</b>.</div>
                    <div class="stp step-box">Decenas: 3 + 7 + 1 = 11. Escribo 1 y <b>reservo 1 centena</b>.</div>
                    <div class="stp step-box">Centenas: 1 + 2 + 1 = 4.</div>
                    <div class="stp math-eq">412</div>
                </div>
                <div class="warn-card stp">
                    La reserva aparece porque estamos cambiando <b>10 unidades por 1 decena</b> o <b>10 decenas por 1 centena</b>.
                </div>
            </div>
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Suma en columna</div>
            <p class="sub-text">Seguimos el orden correcto: <b class="hl">unidades, decenas y centenas</b>.</p>
            """ +
            alg_board(
                [
                    ["", "r:1", "r:1", "_"],
                    ["C D U", "1", "3", "8"],
                    ["+", "2", "7", "4"],
                    ["", "4", "1", "2"],
                ],
                "Paso a paso",
                [
                    "Unidades: 8 + 4 = 12. El <b>2</b> queda abajo y la <b>1 decena</b> sube.",
                    "Decenas: 3 + 7 + 1 = 11. El <b>1</b> queda abajo y la <b>1 centena</b> sube.",
                    "Centenas: 1 + 2 + 1 = 4. Resultado final: <b>412</b>.",
                ],
            ) +
            """
            """
        )
    )
    slides.append(
        notebook_slide(
            "Resuelve en columna: <b class=\"hl\">326 + 157</b>.",
            ["Unidades: 6 + 7 = 13", "Decenas: 2 + 5 + 1 = 8", "Centenas: 3 + 1 = 4", "Resultado: 483"],
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Sumar 3 números en columna</div>
            <p class="sub-text">El orden sigue siendo el mismo, pero ahora juntamos <b class="hl">tres números</b> en cada columna.</p>
            """ +
            alg_board(
                [
                    ["", "_", "r:1", "_"],
                    ["C D U", "1", "0", "8"],
                    ["+", "5", "4", "9"],
                    ["+", "1", "3", "7"],
                    ["", "7", "9", "4"],
                ],
                "Cómo pensar",
                [
                    "Unidades: 8 + 9 + 7 = 24. Escribo 4 y reservo 2 decenas.",
                    "Decenas: 0 + 4 + 3 + 2 = 9. Escribo 9.",
                    "Centenas: 1 + 5 + 1 = 7. Resultado: <b>794</b>.",
                ],
            ) +
            """
            """
        )
    )
    slides.append(
        notebook_slide(
            "Suma estos tres números: <b class=\"hl\">370 + 48 + 64</b>.",
            ["Unidades: 0 + 8 + 4 = 12", "Decenas: 7 + 4 + 6 + 1 = 18", "Centenas: 3 + 1 = 4", "Resultado: 482"],
        )
    )
    slides.append(
        picture_operation_slide(
            "Suma visual de centenas",
            "Los bloques grandes también se pueden juntar mentalmente.",
            "240",
            flats(2, "#FFE082") + rods(4, "#9DE3BD"),
            "130",
            flats(1, "#FFB74D") + rods(3, "#E1BEE7"),
            "+",
            "240 + 130 = 370",
            "2 centenas + 1 centena = 3 centenas. 4 decenas + 3 decenas = 7 decenas.",
            "#FFE082",
            "#E1BEE7",
            "#9DE3BD",
        )
    )
    slides.append(
        exercise_cards_slide(
            "Sumas de 3 dígitos sin reserva",
            "Primero practica casos donde no necesitamos cambiar 10 unidades por 1 decena.",
            [
                ("📦", "241 + 126", "= 367", "#FFE082"),
                ("🚲", "352 + 214", "= 566", "#9DE3BD"),
                ("🌈", "430 + 125", "= 555", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        exercise_cards_slide(
            "Sumas de 3 dígitos con reserva",
            "Ahora sí aparece la reserva en unidades o decenas.",
            [
                ("🎯", "138 + 274", "= 412", "#FFB74D"),
                ("🧩", "247 + 168", "= 415", "#9DE3BD"),
                ("🪁", "359 + 186", "= 545", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        notebook_slide(
            "Resuelve en columna: <b class=\"hl\">451 + 239</b>.",
            ["Unidades: 1 + 9 = 10", "Decenas: 5 + 3 + 1 = 9", "Centenas: 4 + 2 = 6", "Resultado: 690"],
        )
    )
    slides.append(
        fact_boxes_slide(
            "Cómo ordenar los números",
            "En columna, cada cifra va con su lugar correcto.",
            [
                ("🟡 Unidades", "Las unidades van <b>debajo de unidades</b>.", "#FFE082"),
                ("🟢 Decenas", "Las decenas van <b>debajo de decenas</b>.", "#9DE3BD"),
                ("🟣 Centenas", "Las centenas van <b>debajo de centenas</b>.", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        picture_operation_slide(
            "Tres sumandos visuales",
            "También podemos pensar una suma de tres números por partes.",
            "108",
            flats(1, "#FFE082") + unit_blocks(8, "#9DDEFF"),
            "549 y 137",
            flats(5, "#FFB74D") + rods(4, "#9DE3BD") + unit_blocks(9, "#E1BEE7"),
            "+",
            "108 + 549 + 137 = 794",
            "Aunque hay tres números, seguimos sumando unidades, decenas y centenas.",
            "#FFE082",
            "#FFB74D",
            "#9DE3BD",
        )
    )
    slides.append(
        exercise_cards_slide(
            "Práctica con tres números",
            "Resuelve estas sumas en columna.",
            [
                ("🏁", "108 + 549 + 137", "= 794", "#9DE3BD"),
                ("🎨", "126 + 417 + 203", "= 746", "#FFE082"),
                ("🪄", "233 + 508 + 111", "= 852", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        quiz_slide(
            "Desafío rápido",
            "¿Cuál es el resultado de <b>138 + 274</b>?",
            ["302", "412", "422"],
            1,
            "La suma correcta es 412.",
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">¿Qué es restar?</div>
            <p class="sub-text">Restar es <b class="hl">quitar</b>, <b class="hl">separar</b> o saber cuánto falta.</p>
            <div class="formula-row">
                <div class="pnl" style="max-width:320px; text-align:center; border-color:#9DDEFF;">
                    <div class="block-stack">""" + unit_blocks(9, "#FFE082") + """</div>
                    <div class="number-tag">Tengo 9</div>
                </div>
                <div class="math-eq" style="font-size:58px;">−</div>
                <div class="pnl" style="max-width:260px; text-align:center; border-color:#FF9D9D;">
                    <div class="block-stack">""" + unit_blocks(4, "#FF9D9D") + """</div>
                    <div class="number-tag">Quito 4</div>
                </div>
            </div>
            <div class="stp math-eq">9 − 4 = 5</div>
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Elementos de la resta</div>
            <div class="pnl-border" style="background:#f8fbff;">
                <div class="formula-row" style="margin-bottom:16px;">
                    <div class="label-pill stp">Minuendo</div>
                    <div class="label-pill stp">Sustraendo</div>
                    <div class="label-pill stp">Diferencia</div>
                </div>
                <div class="math-eq" style="font-size:62px;">15 − 6 = 9</div>
                <div class="stp chip-row">
                    <div class="mini-chip">15 es el <b>minuendo</b>: la cantidad inicial.</div>
                    <div class="mini-chip">6 es el <b>sustraendo</b>: lo que quito.</div>
                    <div class="mini-chip">9 es la <b>diferencia</b>: lo que queda.</div>
                </div>
            </div>
            """
        )
    )
    slides.append(
        fact_boxes_slide(
            "Ideas importantes de la resta",
            "Estas reglas ayudan a entender mejor lo que hacemos al restar.",
            [
                ("0 no cambia", "Si resto <b>0</b>, el número queda igual.", "#FFE082"),
                ("El orden importa", "<b>9 − 4</b> no es lo mismo que <b>4 − 9</b>.", "#FFB74D"),
                ("Comprobación", "Si sumo <b>diferencia + sustraendo</b>, vuelvo al minuendo.", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Primera resta en columna</div>
            <p class="sub-text">Si las unidades alcanzan, restamos primero ahí y luego seguimos con las decenas.</p>
            <div class="two-col">
                <div class="pnl-border">
                    <div class="math-eq">58 − 3</div>
                    <div class="stp step-box">Unidades: 8 − 3 = 5.</div>
                    <div class="stp step-box">Decenas: 5 − 0 = 5.</div>
                    <div class="stp math-eq">55</div>
                </div>
                <div class="warn-card stp">El sustraendo tiene 0 decenas. Por eso solo quitamos unidades.</div>
            </div>
            """
        )
    )
    slides.append(
        picture_operation_slide(
            "Resta visual",
            "También podemos ver una resta con dibujos grandes.",
            "Tengo 7 globos",
            emoji_pack("🎈", 7, 56),
            "Se van 5",
            emoji_pack("⬜", 5, 50),
            "−",
            "7 − 5 = 2",
            "Primero miro lo que tengo y después cuento cuánto queda.",
            "#FFB74D",
            "#E1BEE7",
            "#9DE3BD",
        )
    )
    slides.append(
        notebook_slide(
            "Resuelve: <b class=\"hl\">89 − 5</b>.",
            ["Unidades: 9 − 5 = 4", "Decenas: 8 − 0 = 8", "Resultado: 84"],
        )
    )
    slides.append(
        exercise_cards_slide(
            "Restas simples para practicar",
            "Aquí todavía no necesitamos desagrupar.",
            [
                ("🍪", "67 − 5", "= 62", "#FFE082"),
                ("🧸", "74 − 2", "= 72", "#9DE3BD"),
                ("⚽", "93 − 4", "= 89", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        quiz_slide(
            "Desafío de resta",
            "En <b>15 − 6 = 9</b>, ¿qué nombre recibe el 9?",
            ["Minuendo", "Sustraendo", "Diferencia"],
            2,
            "9 es la diferencia.",
        )
    )
    slides.append(
        problem_slide(
            "Cajas en la bodega",
            "📦",
            "En una bodega había <b>138 cajas</b> y llegaron <b>274 cajas más</b>. ¿Cuántas cajas hay en total?",
            "138 + 274 = 412<br><span style='color:var(--base);'>Ahora hay 412 cajas.</span>",
            "#E8F5E9",
            "#2E7D32",
        )
    )
    slides.append(
        problem_slide(
            "Puntos del campeonato",
            "🏅",
            "Un equipo logró <b>108 puntos</b> en la mañana, <b>549</b> en la tarde y <b>137</b> al final. ¿Cuántos puntos juntó?",
            "108 + 549 + 137 = 794<br><span style='color:var(--base);'>Juntó 794 puntos.</span>",
            "#E3F2FD",
            "#1565C0",
        )
    )
    slides.append(
        problem_slide(
            "Galletas que quedaron",
            "🍪",
            "Había <b>58 galletas</b> y se comieron <b>3</b>. ¿Cuántas quedaron?",
            "58 − 3 = 55<br><span style='color:var(--base);'>Quedaron 55 galletas.</span>",
            "#FFF8E1",
            "#F9A825",
        )
    )
    slides.append(
        summary_slide(
            [
                "<b>En 3 dígitos</b> pensamos en centenas, decenas y unidades.",
                "<b>Suma en columna:</b> empezamos por las unidades y reservamos cuando se juntan 10.",
                "<b>Resta:</b> minuendo, sustraendo y diferencia.",
                "<b>Comprobar una resta:</b> diferencia + sustraendo = minuendo.",
            ]
        )
    )
    slides.append(finish_slide("Ya puedes sumar números grandes en columna y reconocer cómo funciona una resta antes de desagrupar.", "🚀"))
    assert len(slides) == 30, len(slides)
    return html_doc("Suma y resta 2", slides)


def module_three() -> str:
    slides: list[str] = []
    slides.append(intro_slide("¡Suma y resta 3!", "Restas de 1, 2 y 3 dígitos con desagrupación en unidades, decenas y centenas.", "➖"))
    slides.append(
        picture_operation_slide(
            "Resta de 1 dígito",
            "Cuando restamos números pequeños, vemos cuántos bloques quitamos.",
            "Tengo 9 cubitos",
            unit_blocks(9, "#FFE082"),
            "Quito 5",
            unit_blocks(5, "#FF9D9D"),
            "−",
            "9 − 5 = 4",
            "Quitamos cinco y observamos cuántos quedan.",
            "#FFE082",
            "#FF9D9D",
            "#9DE3BD",
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Resta de 2 dígitos sin desagrupar</div>
            <p class="sub-text">Si las unidades alcanzan, restamos normal.</p>
            <div class="two-col">
                <div class="pnl-border">
                    <div class="math-eq">67 − 4</div>
                    <div class="stp step-box">Unidades: 7 − 4 = 3.</div>
                    <div class="stp step-box">Decenas: 6 − 0 = 6.</div>
                    <div class="stp math-eq">63</div>
                </div>
                <div class="base-card stp" style="border-color:#9DE3BD;">
                    <h3>67</h3>
                    <div class="block-stack">""" + rods(6, "#9DE3BD") + unit_blocks(7, "#FFE082") + """</div>
                    <p style="font-size:22px; margin-top:14px; text-align:center;">Quitamos 4 unidades y quedan 3 unidades.</p>
                </div>
            </div>
            """
        )
    )
    slides.append(
        exercise_cards_slide(
            "Restas sin desagrupar",
            "Primero practicamos casos donde las unidades alcanzan.",
            [
                ("🍎", "74 − 2", "= 72", "#FFE082"),
                ("⚽", "86 − 5", "= 81", "#9DE3BD"),
                ("🧸", "93 − 1", "= 92", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Cuando no alcanza en unidades</div>
            <p class="sub-text">Si no puedo restar en las unidades, <b class="hl">desagrupo</b> una decena.</p>
            <div class="decomp-flow">
                <div class="decomp-box">42 − 19</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">4D 2U</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">3D 12U</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">23</div>
            </div>
            <div class="stp warn-card" style="margin-top:18px;">Una decena vale <b>10 unidades</b>. Por eso 42 puede transformarse en <b>3 decenas y 12 unidades</b>.</div>
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Resta en columna con desagrupación</div>
            <p class="sub-text">Primero resolvemos las unidades, luego las decenas.</p>
            """ +
            alg_board(
                [
                    ["", "_", "3", "12"],
                    ["D U", "4", "2", "_"],
                    ["−", "1", "9", "_"],
                    ["", "2", "3", "_"],
                ],
                "Paso a paso",
                [
                    "Como <b>2 − 9</b> no se puede, desagrupo una decena. Ahora tengo <b>12 unidades</b> y <b>3 decenas</b>.",
                    "Unidades: <b>12 − 9 = 3</b>.",
                    "Decenas: <b>3 − 1 = 2</b>. Resultado: <b>23</b>.",
                ],
                long=True,
            ) +
            """
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Otro caso: una decena completa</div>
            <p class="sub-text">Si el número termina en 0, la decena se convierte en 10 unidades.</p>
            <div class="decomp-flow">
                <div class="decomp-box">50 − 23</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">4D 10U</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">10 − 3 = 7</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">4 − 2 = 2</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">27</div>
            </div>
            """
        )
    )
    slides.append(
        notebook_slide(
            "Resuelve en tu cuaderno: <b class=\"hl\">81 − 37</b>.",
            ["No alcanza en unidades: 1 − 7", "Desagrupo: 8D 1U = 7D 11U", "11 − 7 = 4", "7 − 3 = 4", "Resultado: 44"],
        )
    )
    slides.append(
        exercise_cards_slide(
            "Práctica con desagrupación",
            "Ahora sí necesitamos pedir prestada una decena.",
            [
                ("🌟", "72 − 38", "= 34", "#FFB74D"),
                ("🚲", "61 − 27", "= 34", "#9DE3BD"),
                ("🪁", "90 − 46", "= 44", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Miremos otro ejemplo</div>
            <p class="sub-text">Observa cómo cambia el número cuando desagrupamos una decena.</p>
            <div class="decomp-flow">
                <div class="decomp-box">72 − 38</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">6D 12U</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">12 − 8 = 4</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">6 − 3 = 3</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">34</div>
            </div>
            """
        )
    )
    slides.append(
        quiz_slide(
            "Desafío rápido",
            "¿Cuál es el resultado de <b>42 − 19</b>?",
            ["21", "23", "33"],
            1,
            "Después de desagrupar, queda 23.",
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Resta de 3 dígitos</div>
            <p class="sub-text">En 3 dígitos seguimos el mismo orden: <b class="hl">unidades, decenas y centenas</b>.</p>
            <div class="two-col">
                <div class="pnl-border">
                    <div class="math-eq">521 − 143</div>
                    <div class="stp step-box">Unidades: 1 − 3 no alcanza. Desagrupo 1 decena y quedan 11 − 3 = 8.</div>
                    <div class="stp step-box">Decenas: ahora quedó 1 − 4. Desagrupo 1 centena y quedan 11 − 4 = 7.</div>
                    <div class="stp step-box">Centenas: 4 − 1 = 3.</div>
                    <div class="stp math-eq">378</div>
                </div>
                <div class="warn-card stp">A veces necesitamos desagrupar dos veces: primero una decena y luego una centena.</div>
            </div>
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Resta de 3 dígitos en columna</div>
            """ +
            alg_board(
                [
                    ["", "4", "11", "11"],
                    ["C D U", "5", "2", "1"],
                    ["−", "1", "4", "3"],
                    ["", "3", "7", "8"],
                ],
                "Qué ocurrió",
                [
                    "Primero, 1 unidad no alcanza para quitar 3. Desagrupo y quedan <b>11 unidades</b>.",
                    "Luego, 1 decena no alcanza para quitar 4. Desagrupo una centena y quedan <b>11 decenas</b>.",
                    "Finalmente obtengo <b>378</b>.",
                ],
            ) +
            """
            """
        )
    )
    slides.append(
        picture_operation_slide(
            "Resta de 3 dígitos sin desagrupar",
            "No siempre hace falta pedir prestado: a veces cada columna alcanza.",
            "864",
            flats(8, "#FFE082") + rods(6, "#9DE3BD") + unit_blocks(4, "#E1BEE7"),
            "321",
            flats(3, "#FFB74D") + rods(2, "#9DE3BD") + unit_blocks(1, "#FF9D9D"),
            "−",
            "864 − 321 = 543",
            "Como 4−1, 6−2 y 8−3 sí se pueden, no necesitamos desagrupar.",
            "#FFE082",
            "#FFB74D",
            "#9DE3BD",
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Desagrupación desde centenas</div>
            <p class="sub-text">Si las decenas son 0, primero desagrupo una centena y después una decena.</p>
            <div class="decomp-flow">
                <div class="decomp-box">400 − 175</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">3C 10D 0U</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">3C 9D 10U</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">225</div>
            </div>
            <div class="stp warn-card" style="margin-top:18px;">Primero una centena se transforma en 10 decenas. Luego una de esas decenas se transforma en 10 unidades.</div>
            """
        )
    )
    slides.append(
        notebook_slide(
            "Ahora intenta: <b class=\"hl\">600 − 248</b>.",
            ["6C 0D 0U", "5C 10D 0U", "5C 9D 10U", "10 − 8 = 2", "9 − 4 = 5", "5 − 2 = 3", "Resultado: 352"],
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Otro caso con ceros</div>
            <p class="sub-text">Cuando una columna tiene 0, debemos mirar a la izquierda para desagrupar.</p>
            <div class="decomp-flow">
                <div class="decomp-box">902 − 458</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">8C 9D 12U</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">12 − 8 = 4</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">9 − 5 = 4</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">8 − 4 = 4</div>
            </div>
            """
        )
    )
    slides.append(
        exercise_cards_slide(
            "Restas de 3 dígitos con desagrupación",
            "Ahora practica varios casos más.",
            [
                ("🎯", "521 − 143", "= 378", "#FFE082"),
                ("📘", "731 − 208", "= 523", "#9DE3BD"),
                ("🧩", "642 − 327", "= 315", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        exercise_cards_slide(
            "Restas con ceros",
            "Aquí la desagrupación viene desde las centenas.",
            [
                ("🟠", "400 − 175", "= 225", "#FFB74D"),
                ("🔵", "600 − 248", "= 352", "#9DE3BD"),
                ("🟣", "902 − 458", "= 444", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        fact_boxes_slide(
            "Qué revisar antes de restar",
            "Haz estas preguntas antes de empezar.",
            [
                ("1. Unidades", "¿La unidad del minuendo alcanza para restar la del sustraendo?", "#FFE082"),
                ("2. Decenas", "Si no alcanza, ¿debo desagrupar una decena?", "#9DE3BD"),
                ("3. Centenas", "Si las decenas son 0, ¿debo desagrupar una centena primero?", "#E1BEE7"),
            ],
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Restar descomponiendo</div>
            <p class="sub-text">También puedo restar por partes: primero decenas y luego unidades.</p>
            <div class="decomp-flow">
                <div class="decomp-box">94 − 72</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">94 − 70 = 24</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">24 − 2 = 22</div>
            </div>
            <div class="stp mini-chip">Descomponer también ayuda a pensar y comprobar resultados.</div>
            """
        )
    )
    slides.append(
        slide(
            """
            <div class="head-title">Estimar una resta</div>
            <p class="sub-text">Para estimar, redondeamos y obtenemos un resultado cercano.</p>
            <div class="decomp-flow">
                <div class="decomp-box">447 − 182</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">400 − 200</div>
                <div class="arrow stp">→</div>
                <div class="decomp-box stp">≈ 200</div>
            </div>
            <div class="stp warn-card" style="margin-top:18px;">La estimación no reemplaza el cálculo exacto, pero nos ayuda a revisar si la respuesta tiene sentido.</div>
            """
        )
    )
    slides.append(
        notebook_slide(
            "Resuelve en tu cuaderno: <b class=\"hl\">450 − 319</b>.",
            ["450 = 4C 5D 0U", "4C 4D 10U", "10 − 9 = 1", "4 − 1 = 3", "4 − 3 = 1", "Resultado: 131"],
        )
    )
    slides.append(
        quiz_slide(
            "Desafío de 3 dígitos",
            "¿Cuál es el resultado de <b>521 − 143</b>?",
            ["368", "378", "388"],
            1,
            "La resta correcta es 378.",
        )
    )
    slides.append(
        problem_slide(
            "Canicas del recreo",
            "🔵",
            "Tomás tenía <b>42 canicas</b> y perdió <b>19</b>. ¿Cuántas le quedaron?",
            "42 − 19 = 23<br><span style='color:var(--base);'>Le quedaron 23 canicas.</span>",
            "#E3F2FD",
            "#1976D2",
        )
    )
    slides.append(
        problem_slide(
            "Álbum de láminas",
            "🎴",
            "Martina tenía <b>521 láminas</b> y regaló <b>143</b>. ¿Con cuántas se quedó?",
            "521 − 143 = 378<br><span style='color:var(--base);'>Se quedó con 378 láminas.</span>",
            "#FCE4EC",
            "#C2185B",
        )
    )
    slides.append(
        problem_slide(
            "Cuadernos en la sala",
            "📘",
            "Había <b>400 cuadernos</b> y se repartieron <b>175</b>. ¿Cuántos cuadernos quedaron?",
            "400 − 175 = 225<br><span style='color:var(--base);'>Quedaron 225 cuadernos.</span>",
            "#E8F5E9",
            "#2E7D32",
        )
    )
    slides.append(
        problem_slide(
            "Pegatinas ordenadas",
            "🌈",
            "Una caja tenía <b>902 pegatinas</b> y se usaron <b>458</b>. ¿Cuántas quedaron?",
            "902 − 458 = 444<br><span style='color:var(--base);'>Quedaron 444 pegatinas.</span>",
            "#FFF8E1",
            "#F9A825",
        )
    )
    slides.append(
        summary_slide(
            [
                "<b>Si las unidades alcanzan</b>, resto normal de derecha a izquierda.",
                "<b>Si no alcanzan</b>, desagrupo: 1 decena = 10 unidades.",
                "<b>En 3 dígitos</b>, también puedo desagrupar una centena en 10 decenas.",
                "<b>Descomponer y estimar</b> ayudan a pensar y comprobar la resta.",
            ]
        )
    )
    slides.append(finish_slide("Ya puedes resolver restas con desagrupación en unidades, decenas y centenas siguiendo un orden claro.", "🏁"))
    assert len(slides) == 30, len(slides)
    return html_doc("Suma y resta 3", slides)


def generate_all() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    files = {
        "suma-resta-1.html": module_one(),
        "suma-resta-2.html": module_two(),
        "suma-resta-3.html": module_three(),
    }
    for name, content in files.items():
        (OUTPUT_DIR / name).write_text(content, encoding="utf-8")
        print(f"Generado: {OUTPUT_DIR / name}")


if __name__ == "__main__":
    generate_all()
