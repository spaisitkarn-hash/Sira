"""Components 01-05, summary and close — slides 15-45."""
from dms_lib import *  # noqa: F401,F403
from dms_lib import _set_adj


def meta(accent=NAVY, dark=False):
    def wrap(fn):
        fn.accent, fn.dark = accent, dark
        return fn
    return wrap


def divider(sl, k, title, sub, tags, loop_tag, note):
    c = COMP[k]
    rect(sl, 0, 0, W, H, grad=(c["d"], c["c"]), angle=315)
    for i, a in enumerate((0.05, 0.035, 0.025)):
        b = rect(sl, 6.6 + i * 1.7, -1.5, 0.9, 10.5, fill=WHITE, alpha=a)
        b.rotation = 28
    txt(sl, 8.2, 1.55, 4.6, 2.9, f"0{k}", size=170, color=WHITE, bold=True, align="c", anchor="m", alpha=0.2)
    rect(sl, 9.25, 4.35, 2.5, 0.48, fill=WHITE, r=0.24, text=loop_tag, size=13, color=c["d"], font=FSB,
         align="c", anchor="m", margin=0)
    nl = title.count("\n")
    ty = 2.45 - nl * 0.42
    txt(sl, ML, ty - 0.5, 7.5, 0.34, f"COMPONENT 0{k}", size=13, color="E8EEFA", font=FSB, spc=3)
    txt(sl, ML, ty - 0.12, 7.6, 1.0 + nl * 0.85, title, size=50, color=WHITE, bold=True, ls=0.95)
    yy = ty + 1.0 + nl * 0.85
    txt(sl, ML, yy, 7.6, 0.45, sub, size=16, color=WHITE)
    cx, cy = ML, yy + 0.6
    for t in tags:
        w = text_w(t, 12) + 0.32
        if cx + w > 8.3:
            cx, cy = ML, cy + 0.48
        rect(sl, cx, cy, w, 0.38, fill=WHITE, alpha=0.12, line=WHITE, lw=0.75, r=0.19, text=t, size=12,
             color=WHITE, align="c", anchor="m", margin=0)
        cx += w + 0.1
    # section progress
    for i in range(5):
        x = ML + i * 0.42
        if i + 1 == k:
            rect(sl, x, 6.45, 0.32, 0.08, fill=WHITE, r=0.04)
        else:
            rect(sl, x, 6.45, 0.32, 0.08, fill=WHITE, alpha=0.3, r=0.04)
    txt(sl, ML + 2.2, 6.32, 4, 0.32, f"Component {k} of 5", size=11, color=WHITE, alpha=0.8, anchor="m")
    notes(sl, note)


# ======================================================================= 01 KPI CASCADE
K1 = "01 · KPI Cascade"


@meta(GREEN, True)
def s15(sl, n, T):
    divider(sl, 1, "KPI Cascade", "เป้าหมายที่เชื่อมกันทุกระดับ — จากโรงงานถึงเครื่องจักร",
            ["Cascade Levels", "Leading & Lagging", "5 Build Steps", "Visual Management"], "Stabilize Loop · S2",
            "องค์ประกอบที่ 1: ทำให้ทุกคนรู้ว่าเป้าหมายของตัวเองเชื่อมกับเป้าหมายโรงงานอย่างไร")


@meta(GREEN)
def s16(sl, n, T):
    background(sl)
    header(sl, K1, "KPI Cascade Levels", "ระดับบนมองผลรวม · ระดับล่างมองสิ่งที่ควบคุมได้", kc=GREEN)
    lv = [("PLANT", "OEE · Yield · Cost · Safety · Quality · Delivery", "0A4A39"),
          ("DEPARTMENT", "ผลลัพธ์เฉพาะหน้าที่ของแผนก", "0B5A45"),
          ("LINE / AREA", "Downtime · Waste · Output · Defect", "0B6B52"),
          ("SHIFT / TEAM", "ความสูญเสียและความผิดปกติประจำกะ", "0D7C5F"),
          ("OPERATOR / MACHINE", "ค่าควบคุมและมาตรฐานที่ทำได้จริง", GREEN)]
    cxm, h, g = ML + 3.5, 0.84, 0.12
    for i, (t, d, col) in enumerate(lv):
        w = 4.1 + i * 0.55
        y = 1.95 + i * (h + g)
        rect(sl, cxm - w / 2, y, w, h, fill=col, r=0.1, sh=(i == 0),
             text=[[(t, {"font": FSB, "size": 13, "spc": 1.5})], [(d, {"size": 12, "color": "D7F2E8"})]],
             color=WHITE, anchor="m", margin=0.2)
    # side scale
    line(sl, ML + 0.1, 2.05, ML + 0.1, 6.6, "9AA8C7", 1.5, arrow=True, head=True)
    txt(sl, ML - 0.05, 1.72, 0.9, 0.3, "ผลรวม", size=10, color=SLATE, font=FSB)
    txt(sl, ML - 0.05, 6.66, 1.2, 0.3, "ควบคุมได้", size=10, color=SLATE, font=FSB)
    rx, rw = 7.35, MR - 7.35
    txt(sl, rx, 1.95, rw, 0.35, "Every KPI Needs", size=16, color=NAVY, font=FSB)
    tiles = [("ads_click", "Target", "เป้าหมายชัด ตัวเลขเดียว"), ("person", "Owner", "ผู้รับผิดชอบหนึ่งคน"),
             ("update", "Frequency", "รอบการติดตาม"), ("emergency_home", "Reaction Plan", "วิธีตอบสนองเมื่อหลุดเป้า")]
    tw, th = (rw - 0.18) / 2, 1.42
    for i, (ic, t, d) in enumerate(tiles):
        x = rx + (i % 2) * (tw + 0.18)
        y = 2.45 + (i // 2) * (th + 0.18)
        rect(sl, x, y, tw, th, fill=GREEN_L, r=0.14)
        icon(sl, ic, x + 0.25, y + 0.22, 0.36, GREEN)
        txt(sl, x + 0.25, y + 0.66, tw - 0.4, 0.34, t, size=15, color=NAVY, font=FSB)
        txt(sl, x + 0.25, y + 1.0, tw - 0.4, 0.34, d, size=12, color=SLATE)
    rect(sl, rx, 5.82, rw, 1.0, fill=WHITE, line=LINE, r=0.12)
    icon(sl, "lightbulb", rx + 0.22, 6.1, 0.42, AMBER)
    txt(sl, rx + 0.8, 5.82, rw - 1.0, 1.0, "พนักงานควบคุม OEE ทั้งโรงงานไม่ได้ แต่ควบคุม เวลาหยุดเครื่อง การตรวจสภาพ และค่าตั้งเครื่อง ได้",
        size=12.5, color=INK, anchor="m")
    notes(sl, "ระดับบนดูผลรวม (Lagging) ระดับล่างดูสิ่งที่ควบคุมได้ในมือ (Leading)\n"
              "KPI ที่ขาด Target, Owner, Frequency หรือ Reaction Plan ข้อใดข้อหนึ่ง ยังไม่ถือว่าพร้อมใช้บนบอร์ด")


@meta(GREEN)
def s17(sl, n, T):
    background(sl)
    header(sl, K1, "Leading and Lagging KPIs", "ใช้ร่วมกัน เพื่อไม่ให้เห็นผลเสียเมื่อสายเกินไป", kc=GREEN)
    y, h, w = 1.95, 3.95, 5.35
    rect(sl, ML, y, w, h, fill=GREEN_L, r=0.18)
    icon(sl, "speed", ML + 0.3, y + 0.32, 0.46, GREEN)
    txt(sl, ML + 0.9, y + 0.25, 4, 0.4, "Leading KPI", size=20, color=NAVY, font=FSB)
    txt(sl, ML + 0.9, y + 0.65, 4, 0.3, "= Process KPI", size=12.5, color=GREEN, font=FSB)
    txt(sl, ML + 0.3, y + 1.1, w - 0.6, 0.62, "ติดตามปัจจัยก่อนเกิดผล และต้องควบคุมได้ในระดับนั้น", size=14, color=INK)
    rect(sl, ML + 0.3, y + 1.78, w - 0.6, 0.9, fill=WHITE, r=0.1,
         text=[[("Timing     ", {"font": FSB, "color": NAVY}), ("ก่อนเกิดผล — ยังป้องกันได้", {})],
               [("Question  ", {"font": FSB, "color": NAVY}), ("เรากำลังควบคุมสิ่งที่ถูกต้องอยู่หรือไม่?", {})]],
         size=12.5, color=INK, anchor="m", margin=0.18, after=4)
    chips(sl, ML + 0.3, y + 2.9, ["Centerline Adherence", "CIL Completion", "PM on Plan", "Abnormality Closed"], WHITE,
          NAVY, size=11.5, h=0.36, max_x=ML + w - 0.2, row_h=0.44)
    x2 = MR - w
    rect(sl, x2, y, w, h, fill=NAVY, r=0.18, sh=True)
    icon(sl, "flag", x2 + 0.3, y + 0.32, 0.46, MINT)
    txt(sl, x2 + 0.9, y + 0.25, 4, 0.4, "Lagging KPI", size=20, color=WHITE, font=FSB)
    txt(sl, x2 + 0.9, y + 0.65, 4, 0.3, "= Result KPI", size=12.5, color="AFC0E8", font=FSB)
    txt(sl, x2 + 0.3, y + 1.1, w - 0.6, 0.62, "วัดผลที่เกิดขึ้นแล้ว เป็นหลักฐานว่าบรรลุเป้าหรือไม่", size=14, color=WHITE)
    rect(sl, x2 + 0.3, y + 1.78, w - 0.6, 0.9, fill="2A3F78", r=0.1,
         text=[[("Timing     ", {"font": FSB}), ("หลังเกิดผล — ยืนยันผลลัพธ์", {"color": "DCE4F7"})],
               [("Question  ", {"font": FSB}), ("เราได้ผลตามเป้าหมายหรือไม่?", {"color": "DCE4F7"})]],
         size=12.5, color=WHITE, anchor="m", margin=0.18, after=4)
    chips(sl, x2 + 0.3, y + 2.9, ["OEE", "Defect Rate", "OTIF"], "2A3F78", WHITE, size=11.5, h=0.36)
    mx = ML + w + (x2 - ML - w) / 2
    txt(sl, mx - 0.6, y + 1.55, 1.2, 0.3, "drives", size=12, color=GREEN, font=FSB, align="c")
    icon_c(sl, "arrow_forward", mx, y + 2.08, 0.5, GREEN)
    y2 = 6.1
    rect(sl, ML, y2, CW, 0.72, fill="FDF3DE", r=0.12)
    icon(sl, "lightbulb", ML + 0.25, y2 + 0.16, 0.4, ORANGE)
    txt(sl, ML + 0.8, y2, CW - 1, 0.72, [[("CIL ครบ 100% แต่ OEE ยังต่ำ → ", {"font": FSB}),
                                          ("ตรวจว่า CIL ครอบคลุมความเสี่ยงจริงหรือไม่ — Leading ที่ไม่ขับ Lagging คือ KPI ที่วัดผิดจุด", {})]],
        size=13.5, color=INK, anchor="m")
    notes(sl, "Leading บอกว่าเรากำลังทำสิ่งที่ถูกต้องหรือไม่ Lagging บอกว่าได้ผลหรือไม่\n"
              "ถ้า Leading เขียวตลอดแต่ Lagging แดง แปลว่าเลือก Leading ผิด ต้องทบทวนความสัมพันธ์")


@meta(GREEN)
def s18(sl, n, T):
    background(sl)
    header(sl, K1, "Building a KPI Cascade in 5 Steps", "ทำตามลำดับ ทุกขั้นมี Output ที่ตรวจสอบได้", kc=GREEN)
    steps = [("Start from Plant KPI", "เลือกตัวที่ชัดและเชื่อมกับธุรกิจ", "list_alt", "Plant KPI List"),
             ("Map Contributors", "ระบุหน่วยงานและกระบวนการที่ส่งผล", "account_tree", "Contribution Map"),
             ("Split Lagging & Leading", "เช่น OEE → Downtime · Speed · Waste", "device_hub", "KPI Tree"),
             ("Set Target · Frequency · Owner · Reaction", "ทุก KPI ต้องมีครบสี่อย่าง", "table_chart", "KPI Matrix"),
             ("Pilot & Refine", "ทดลองใช้รายวัน แล้วปรับให้เหมาะ", "dashboard", "Board in Daily Use")]
    cols = ["0A4A39", "0B5A45", "0B6B52", "0D7C5F", "16A37E"]
    cw = CW / 5
    yc = 2.35
    line(sl, ML + cw / 2, yc, MR - cw / 2, yc, "9ED9C5", 3)
    for i, (t, d, ic, out) in enumerate(steps):
        x = ML + i * cw
        circle(sl, x + cw / 2, yc, 0.62, fill=cols[i], line=WHITE, lw=3, sh=True, text=str(i + 1), size=20,
               color=WHITE, font=FSB, align="c", anchor="m", margin=0)
        txt(sl, x + 0.1, yc + 0.48, cw - 0.2, 0.7, t, size=14.5, color=NAVY, font=FSB, align="c")
        txt(sl, x + 0.12, yc + 1.2, cw - 0.24, 0.7, d, size=12, color=SLATE, align="c")
        y = 4.5
        rect(sl, x + 0.08, y, cw - 0.16, 1.25, fill=GREEN_L, r=0.12)
        icon_c(sl, ic, x + cw / 2, y + 0.33, 0.34, GREEN)
        txt(sl, x + 0.1, y + 0.55, cw - 0.2, 0.28, "Output", size=10.5, color=SLATE, align="c")
        txt(sl, x + 0.1, y + 0.82, cw - 0.2, 0.32, out, size=12.5, color=NAVY, font=FSB, align="c")
    y = 6.05
    rect(sl, ML, y, CW, 0.75, fill=NAVY, r=0.14, sh=True)
    icon(sl, "filter_alt", ML + 0.28, y + 0.2, 0.36, MINT)
    txt(sl, ML + 0.85, y, CW - 1, 0.75, "Test: ถ้า KPI ไม่ทำให้เกิดการตัดสินใจ ก็ไม่ควรอยู่บนบอร์ดประจำวัน", size=15,
        color=WHITE, font=FSB, anchor="m")
    notes(sl, "สร้าง Cascade จากบนลงล่าง เริ่มจาก KPI โรงงานที่มีน้อยตัวและชัด\n"
              "ขั้นที่ 5 สำคัญที่สุด: ใช้จริงบนบอร์ด 2–4 สัปดาห์ แล้วตัด KPI ที่ไม่มีใครใช้ตัดสินใจออก")


@meta(GREEN)
def s19(sl, n, T):
    background(sl)
    header(sl, K1, "Example: Beverage OEE Cascade", "เชื่อมผลรวมระดับโรงงานกับจุดควบคุมจริงที่เครื่องจักร", kc=GREEN)
    cols = [("PLANT · WEEKLY", [("Beverage OEE", "d"), ("Top Loss", "l")]),
            ("SECTION · DAILY", [("OEE", "m"), ("Unplanned Downtime", "l"), ("Planned Downtime", "l")]),
            ("SHIFT", [("Output vs Plan", "c"), ("Speed Loss", "l"), ("Stop Minutes", "l")]),
            ("LINE / OPERATOR", [("Centerline", "o"), ("CIL", "o"), ("Abnormality", "o"), ("Machine Status", "o")])]
    styles = {"d": ("0A4A39", WHITE, None), "m": ("0B6B52", WHITE, None), "c": (GREEN, WHITE, None),
              "l": (GREEN_L, NAVY, None), "o": (WHITE, NAVY, GREEN)}
    cw, gx, bh, bg = 2.72, 0.4, 0.62, 0.14
    ymid = 4.1
    for i, (lab, items) in enumerate(cols):
        x = ML + i * (cw + gx)
        tot = len(items) * bh + (len(items) - 1) * bg
        y0 = ymid - tot / 2
        txt(sl, x, y0 - 0.42, cw, 0.3, lab, size=12, color=GREEN_D, font=FSB, spc=1.5)
        for j, (t, st) in enumerate(items):
            f, fg, ln = styles[st]
            rect(sl, x, y0 + j * (bh + bg), cw, bh, fill=f, line=ln, lw=1.5, r=0.1, sh=(j == 0 and st != "o"),
                 text=t, size=13.5 if st in "dmc" else 12.5, color=fg, font=FSB, anchor="m", margin=0.18)
        if i < 3:
            icon_c(sl, "chevron_right", x + cw + gx / 2, ymid, 0.32, "9AA8C7")
    y = 6.3
    txt(sl, ML, y, 2.2, 0.36, "ผลรวม · แนวโน้ม", size=12.5, color=SLATE, font=FSB, anchor="m")
    rect(sl, ML + 2.0, y + 0.16, CW - 4.1, 0.05, grad=("0A4A39", "7FDBC0"), angle=0)
    txt(sl, MR - 2.0, y, 2.0, 0.36, "สิ่งที่ควบคุมได้จริง", size=12.5, color=SLATE, font=FSB, anchor="m", align="r")
    txt(sl, ML, 5.85, 6, 0.3, "Lagging  ←", size=11, color=MUTED, font=FSB)
    txt(sl, MR - 6, 5.85, 6, 0.3, "→  Leading", size=11, color=MUTED, font=FSB, align="r")
    notes(sl, "อ่านจากซ้ายไปขวา: OEE โรงงานรายสัปดาห์ แตกเป็น Downtime รายวัน, Speed/Stop รายกะ และจุดควบคุมที่เครื่อง\n"
              "คนหน้างานรับผิดชอบคอลัมน์ขวาสุด ซึ่งเป็นสิ่งที่ควบคุมได้จริงในกะ")


@meta(GREEN)
def s20(sl, n, T):
    background(sl)
    header(sl, K1, "Visual Management Board", "ทำให้ KPI ใช้ตัดสินใจได้ทุกวัน ไม่ใช่แค่กราฟบนผนัง", kc=GREEN)
    x, y, w, h = ML, 1.95, 6.7, 4.9
    card(sl, x, y, w, h)
    txt(sl, x + 0.25, y + 0.18, 4, 0.32, "Line A · Shift Board", size=14, color=NAVY, font=FSB)
    chip(sl, x + w - 1.55, y + 0.18, "ตัวอย่างสมมติ", ORANGE_L, ORANGE_D, size=10.5, h=0.3)
    tiles = [("Safety", "0", "Green", GREEN, GREEN_L), ("Defect %", "0.8", "Yellow", "B7780A", "FDF3DE"),
             ("Output vs Plan", "92%", "Red", RED, RED_L)]
    tw = (w - 0.5 - 0.24) / 3
    for i, (t, v, s, c, l) in enumerate(tiles):
        xx = x + 0.25 + i * (tw + 0.12)
        rect(sl, xx, y + 0.62, tw, 1.05, fill=l, r=0.1)
        txt(sl, xx + 0.15, y + 0.68, tw - 0.2, 0.28, t, size=11.5, color=SLATE)
        txt(sl, xx + 0.15, y + 0.92, tw - 0.2, 0.45, v, size=22, color=c, bold=True)
        txt(sl, xx + 0.15, y + 1.35, tw - 0.2, 0.26, s, size=11, color=c, font=FSB)
    rect(sl, x + 0.25, y + 1.82, w - 0.5, 0.42, fill="EEF2FA", r=0.08)
    icon(sl, "priority_high", x + 0.35, y + 1.9, 0.26, RED)
    txt(sl, x + 0.7, y + 1.82, w - 1, 0.42, "Top issue: Filler หยุด 45 นาที (Alarm ชุดป้อนฝา)", size=12, color=INK, anchor="m")
    rect(sl, x + 0.25, y + 2.34, w - 0.5, 0.72, fill="EEF2FA", r=0.08)
    for j, (hd, v, c) in enumerate((("Action", "ตรวจชุดป้อนฝา", INK), ("Owner · Due", "Maint · 14:00", INK),
                                     ("Status", "In Progress", BLUE))):
        xx = x + 0.42 + [0, 2.75, 4.5][j]
        txt(sl, xx, y + 2.4, 2.2, 0.3, hd, size=11.5, color=NAVY, font=FSB)
        txt(sl, xx, y + 2.7, 2.2, 0.3, v, size=11.5, color=c, font=FSB if j == 2 else F)
    txt(sl, x + 0.25, y + 3.15, 3, 0.28, "Output by Hour", size=11.5, color=NAVY, font=FSB)
    vals = [0.95, 1.02, 0.94, 0.78, 0.4, 0.85, 1.0, 1.04]
    bx0, by0, bw_, bh_ = x + 0.25, y + 4.72, (w - 0.5) / 8, 1.05
    for i, v in enumerate(vals):
        c = GREEN if v >= 0.92 else (AMBER if v >= 0.7 else RED)
        rect(sl, bx0 + i * bw_ + 0.05, by0 - bh_ * v, bw_ - 0.1, bh_ * v, fill=c, r=0.03)
    line(sl, bx0, by0 - bh_, bx0 + w - 0.5, by0 - bh_, NAVY, 1, dash=True)
    txt(sl, bx0 + w - 1.4, by0 - bh_ - 0.27, 0.9, 0.24, "Target", size=9.5, color=NAVY, font=FSB, align="r")
    rx = x + w + 0.35
    rows = [("compare_arrows", "Target เทียบ Actual ในรอบที่กำหนด", "ไม่ใช่ผลสะสมสิ้นเดือน"),
            ("traffic", "สี G / Y / R ตามเกณฑ์ที่ตกลงกัน", "ทุกคนอ่านสถานะได้ใน 5 วินาที"),
            ("report", "ปัญหาสำคัญ และความเสี่ยงรอบถัดไป", "เลือกไม่เกิน 3 เรื่อง"),
            ("task_alt", "Owner · Due · Action · สถานะปิดงาน", "ทุกเรื่องตามได้ว่าใครทำ เสร็จเมื่อไร")]
    for i, (ic, t, d) in enumerate(rows):
        yy = 1.95 + i * 1.25
        card(sl, rx, yy, MR - rx, 1.1, sh=False)
        icon_badge(sl, ic, rx + 0.22, yy + 0.27, 0.56, GREEN_L, GREEN, round_=False, r=0.12)
        txt(sl, rx + 0.95, yy + 0.18, MR - rx - 1.1, 0.4, t, size=13.5, color=NAVY, font=FSB)
        txt(sl, rx + 0.95, yy + 0.58, MR - rx - 1.1, 0.32, d, size=11.5, color=SLATE)
    notes(sl, "บอร์ดที่ดีตอบได้ใน 5 วินาทีว่าวันนี้ปกติหรือไม่ และใครกำลังแก้อะไร\n"
              "ตัวเลขบนบอร์ดเป็นตัวอย่างสมมติ ใช้อธิบายองค์ประกอบของบอร์ดเท่านั้น")


# ======================================================================= 02 MEETING
K2 = "02 · Purposeful Meeting"


@meta(BLUE, True)
def s21(sl, n, T):
    divider(sl, 2, "Purposeful\nMeeting Structure", "ประชุมเพื่อควบคุมผลการทำงาน ไม่ใช่รายงานข้อมูลอย่างเดียว",
            ["SIM Cadence", "SIM Rhythm", "SIM Board", "Action Management"], "Stabilize Loop · S3",
            "องค์ประกอบที่ 2: การประชุม SIM ต้องจบด้วยการตัดสินใจและ Action ที่ติดตามได้")


@meta(BLUE)
def s22(sl, n, T):
    background(sl)
    header(sl, K2, "Inputs and Outputs of a DMS Meeting", "ข้อมูลเข้าคือข้อเท็จจริง · สิ่งที่ออกคือการตัดสินใจที่ติดตามได้", kc=BLUE)
    ins = [("monitoring", "KPI vs Target"), ("error", "Deviations"), ("visibility", "Risks Ahead"),
           ("pending_actions", "Open Actions")]
    outs = [("gavel", "Clear Decisions"), ("assignment_ind", "Actions with Owner & Due"), ("north", "Escalations")]
    cxm, cym, d = W / 2, 3.95, 2.55
    txt(sl, ML, 1.95, 3, 0.3, "INPUTS", size=12, color=SLATE, font=FSB, spc=2)
    for i, (ic, t) in enumerate(ins):
        y = 2.35 + i * 0.86
        card(sl, ML, y, 3.75, 0.68, sh=False)
        icon(sl, ic, ML + 0.22, y + 0.19, 0.3, BLUE)
        txt(sl, ML + 0.68, y, 3, 0.68, t, size=15, color=NAVY, font=FSB, anchor="m")
        line(sl, ML + 3.75, y + 0.34, cxm - d / 2 + 0.1, cym, "B9CBEA", 1.25)
    circle(sl, cxm, cym, d + 0.5, fill=BLUE, alpha=0.08)
    circle(sl, cxm, cym, d, grad=("3B86F0", "1452B8"), angle=315, sh=True)
    icon_c(sl, "groups", cxm, cym - 0.55, 0.5, WHITE)
    txt(sl, cxm - 1, cym - 0.3, 2, 0.55, "SIM", size=30, color=WHITE, bold=True, align="c", anchor="m")
    txt(sl, cxm - 1, cym + 0.28, 2, 0.32, "Review · Decide", size=13, color="DCE8FF", align="c")
    rx = MR - 3.75
    txt(sl, rx, 2.2, 3, 0.3, "OUTPUTS", size=12, color=SLATE, font=FSB, spc=2)
    for i, (ic, t) in enumerate(outs):
        y = 2.6 + i * 0.92
        rect(sl, rx, y, 3.75, 0.74, fill=NAVY, r=0.1, sh=True)
        icon(sl, ic, rx + 0.22, y + 0.21, 0.32, MINT)
        txt(sl, rx + 0.7, y, 3, 0.74, t, size=15, color=WHITE, font=FSB, anchor="m")
        line(sl, cxm + d / 2 - 0.05, cym, rx, y + 0.37, "B9CBEA", 1.25, arrow=True)
    y = 6.05
    hw = (CW - 0.2) / 2
    rect(sl, ML, y, hw, 0.78, fill=RED_L, r=0.12)
    icon(sl, "close", ML + 0.22, y + 0.25, 0.28, RED)
    txt(sl, ML + 0.62, y, hw - 0.8, 0.78, [[("Report-out Meeting — ", {"font": FSB, "color": NAVY}),
                                            ("เล่าตัวเลขย้อนหลัง จบโดยไม่มีการตัดสินใจ", {})]], size=13, color=INK, anchor="m")
    x2 = ML + hw + 0.2
    rect(sl, x2, y, hw, 0.78, fill=GREEN_L, r=0.12)
    icon(sl, "check", x2 + 0.22, y + 0.25, 0.28, GREEN)
    txt(sl, x2 + 0.62, y, hw - 0.8, 0.78, [[("Purposeful Meeting — ", {"font": FSB, "color": NAVY}),
                                            ("ใช้ข้อมูลควบคุมรอบถัดไป", {})]], size=13, color=INK, anchor="m")
    notes(sl, "ตรวจคุณภาพประชุมด้วยคำถามเดียว: ออกจากห้องแล้วมีการตัดสินใจและ Action ใหม่ที่มีเจ้าของหรือไม่\n"
              "ถ้าไม่มี แปลว่าเป็น Report-out Meeting")


@meta(BLUE)
def s23(sl, n, T):
    background(sl)
    header(sl, K2, "SIM Cadence", "Short Interval Management: จังหวะบริหารจากกะถึงผู้บริหาร", kc=BLUE)
    data = [("SIM 1–2", "Shift & Area", "ควบคุมและส่งมอบงานระหว่างกะ", "BFD3FA", NAVY),
            ("SIM 3", "Section / Supervisor", "ผลและปัญหาของ Section", "7FAAF0", NAVY),
            ("SIM 4", "Plant Daily Review", "ทบทวนรายวันระดับโรงงาน", "3B86F0", WHITE),
            ("SIM 4.5", "Weekly Performance Review", "แนวโน้มและการป้องกันปัญหาซ้ำ", "1A66D9", WHITE),
            ("SIM 6–7", "Executive Weekly / Monthly", "เรื่องที่ต้องใช้อำนาจและทรัพยากร", "0D3E8F", WHITE)]
    cw, gx = 2.27, 0.195
    base = 6.0
    for i, (t, s, d, f, fg) in enumerate(data):
        x = ML + i * (cw + gx)
        hh = 1.75 + i * 0.55
        y = base - hh
        rect(sl, x, y, cw, hh + 0.12, fill=f, r=0.14, sh=(i == 4))
        txt(sl, x + 0.2, y + 0.18, cw - 0.3, 0.42, t, size=20, color=fg, bold=True)
        txt(sl, x + 0.2, y + 0.62, cw - 0.3, 0.5, s, size=12.5, color=fg, font=FSB)
        txt(sl, x + 0.2, y + 1.18, cw - 0.3, 0.6, d, size=11.5, color=fg if fg == WHITE else INK, alpha=0.9 if fg == WHITE else None)
    rect(sl, ML, base + 0.05, CW, 0.05, fill=NAVY)
    line(sl, ML + 1.0, 2.15, ML + 4.6, 2.15, BLUE, 2, arrow=True)
    txt(sl, ML, 1.95, 1.0, 0.4, "Escalate", size=11.5, color=BLUE, font=FSB, anchor="m")
    icon(sl, "near_me", ML, 6.35, 0.3, BLUE)
    txt(sl, ML + 0.42, 6.27, 8, 0.46, "แก้ใกล้จุดเกิดเหตุที่สุดก่อน · ส่งขึ้นเฉพาะเรื่องที่ต้องใช้อำนาจหรือประสานงาน", size=14,
        color=NAVY, font=FSB, anchor="m")
    txt(sl, MR - 3.4, 6.27, 3.4, 0.46, "เวลาจริงยึด SIM Cadence ที่ประกาศใช้", size=11.5, color=SLATE, align="r", anchor="m")
    notes(sl, "SIM เป็นขั้นบันได: เรื่องเริ่มที่ SIM 1–2 และขึ้นไปเฉพาะเมื่อเกินอำนาจหรือต้องประสานหลายหน่วย\n"
              "เวลาและผู้เข้าร่วมของแต่ละ SIM ให้ใช้ตาม SIM Cadence ที่โรงงานประกาศใช้")


@meta(BLUE)
def s24(sl, n, T):
    background(sl)
    header(sl, K2, "SIM Rhythm and Standard Agenda", "ทุก SIM ใช้จังหวะเดียวกัน: ดูย้อน · มองไปข้างหน้า · เลือก · ลงมือ", kc=BLUE)
    data = [("history", "Look Back", "ผลรอบก่อนเทียบเป้า งานค้างเสร็จหรือยัง", "“เมื่อวานเป็นไปตามแผนไหม?”"),
            ("visibility", "Look Forward", "ความเสี่ยงและความพร้อมของรอบถัดไป", "“กะหน้ามีความเสี่ยงอะไร?”"),
            ("low_priority", "Prioritize", "เลือกประเด็นที่สำคัญที่สุด ไม่ใช่ทุกเรื่อง", "“เรื่องไหนสำคัญที่สุด?”"),
            ("bolt", "Act", "วิธีจัดการ ผู้รับผิดชอบ เวลาติดตาม", "“ใคร ทำอะไร เสร็จเมื่อไร?”")]
    cw, gx = 2.9, 0.177
    y, h = 1.95, 2.95
    for i, (ic, t, d, q) in enumerate(data):
        x = ML + i * (cw + gx)
        last = i == 3
        rect(sl, x, y, cw, h, fill=BLUE if last else BLUE_L, r=0.16, sh=last)
        icon(sl, ic, x + 0.25, y + 0.25, 0.4, WHITE if last else BLUE)
        txt(sl, x + 0.25, y + 0.78, cw - 0.4, 0.4, t, size=17, color=WHITE if last else NAVY, font=FSB)
        txt(sl, x + 0.25, y + 1.2, cw - 0.4, 0.7, d, size=12.5, color="DCE8FF" if last else SLATE)
        rect(sl, x + 0.22, y + h - 0.82, cw - 0.44, 0.62, fill=WHITE, alpha=0.18 if last else None, r=0.1,
             text=q, size=12.5, color=WHITE if last else NAVY, font=FSB, anchor="m", margin=0.14)
    txt(sl, ML, 5.12, 4, 0.3, "STANDARD AGENDA", size=12, color=SLATE, font=FSB, spc=2)
    ag = ["ทบทวน Action ค้าง", "ตรวจ KPI · Red / Yellow", "ผลกระทบและการควบคุมที่ทำแล้ว", "Action · Owner · Due · Escalation",
          "ยืนยันเรื่องสำคัญก่อนจบ"]
    cols = ["14275A", "1B3570", "22438A", "2A52A6", BLUE]
    sw = CW / 5
    for i, t in enumerate(ag):
        x = ML + i * sw
        rect(sl, x, 5.48, sw + (0.02 if i < 4 else 0), 1.35, fill=cols[i], r=0.14 if i in (0, 4) else None)
        if i in (0, 4):   # square the inner corners
            rect(sl, x + (sw / 2 if i == 0 else 0), 5.48, sw / 2 + 0.02, 1.35, fill=cols[i])
        txt(sl, x + 0.2, 5.6, 0.6, 0.4, str(i + 1), size=18, color=MINT, bold=True)
        txt(sl, x + 0.2, 6.02, sw - 0.35, 0.72, t, size=12.5, color=WHITE, font=FM)
    notes(sl, "จังหวะ 4 ขั้นใช้ได้ทุกระดับ SIM ส่วน Standard Agenda 5 ข้อเป็นลำดับวาระที่ต้องเหมือนกันทุกวัน\n"
              "ข้อ 1 สำคัญ: เริ่มจาก Action ค้างก่อนเสมอ เพื่อไม่ให้งานหาย")


@meta(BLUE)
def s25(sl, n, T):
    background(sl)
    header(sl, K2, "SIM Board Anatomy", "ห้าโซนที่ควรเห็นบนบอร์ด (ตัวอย่างสมมติ)", kc=BLUE)
    fx, fy, fw, fh = ML, 1.95, CW, 4.9
    rect(sl, fx, fy, fw, fh, fill=NAVY, r=0.18, sh=True)
    pad = 0.14
    cw1 = 3.95
    cw2 = (fw - cw1 - 4 * pad) / 2
    ph = (fh - 3 * pad) / 2

    def panel(x, y, w, h, letter, col, title):
        rect(sl, x, y, w, h, fill=WHITE, r=0.12)
        circle(sl, x + 0.36, y + 0.36, 0.36, fill=col, text=letter, size=12, color=WHITE, font=FSB, align="c",
               anchor="m", margin=0)
        txt(sl, x + 0.65, y + 0.18, w - 0.8, 0.36, title, size=15, color=NAVY, font=FSB, anchor="m")

    def items(x, y, w, rows):
        for i, (c, t) in enumerate(rows):
            yy = y + i * 0.46
            rect(sl, x, yy, w, 0.38, fill="EEF2FA", r=0.08)
            circle(sl, x + 0.18, yy + 0.19, 0.12, fill=c)
            txt(sl, x + 0.36, yy, w - 0.45, 0.38, t, size=12, color=INK, anchor="m")

    ax, ay = fx + pad, fy + pad
    panel(ax, ay, cw1, fh - 2 * pad, "A", BLUE, "KPI vs Target")
    vals = [0.95, 1.0, 0.78, 0.6, 0.98]
    bx, by, bh = ax + 0.25, ay + 2.35, 1.6
    bwd = (cw1 - 0.5) / 5
    for i, v in enumerate(vals):
        c = GREEN if v >= 0.9 else (AMBER if v >= 0.7 else RED)
        rect(sl, bx + i * bwd + 0.05, by - bh * v, bwd - 0.1, bh * v, fill=c, r=0.03)
    line(sl, bx, by - bh * 0.95, bx + cw1 - 0.5, by - bh * 0.95, GREEN_D, 1, dash=True)
    txt(sl, bx, by + 0.05, cw1 - 0.5, 0.28, "Output รายวันเทียบเส้นเป้าหมาย", size=11, color=SLATE)
    items(bx, by + 0.42, cw1 - 0.5, [(GREEN, "Safety · 0 incident"), (AMBER, "Quality · Defect 0.8%"),
                                     (RED, "Delivery · 92% of plan")])
    x2 = ax + cw1 + pad
    x3 = x2 + cw2 + pad
    y2 = ay + ph + pad
    panel(x2, ay, cw2, ph, "B", RED, "Top Abnormalities")
    items(x2 + 0.22, ay + 0.68, cw2 - 0.44, [(RED, "Filler หยุด 45 นาที"), (AMBER, "Defect ซีลสูงกว่าเป้า"),
                                              (RED, "ผลิตต่ำกว่าแผน")])
    panel(x3, ay, cw2, ph, "C", ORANGE, "Risk Next 24 Hours")
    items(x3 + 0.22, ay + 0.68, cw2 - 0.44, [(ORANGE, "เครื่องเดิม เสี่ยงหยุดซ้ำ"), (AMBER, "วัตถุดิบ Lot ใหม่เข้าบ่าย")])
    panel(x2, y2, cw2, ph, "D", GREEN, "Action Tracker")
    cx = x2 + 0.22
    for t, bg, fg in (("Open 3", RED_L, RED_D), ("Doing 2", BLUE_L, BLUE_D), ("Closed 5", GREEN_L, GREEN_D)):
        cx += chip(sl, cx, y2 + 0.68, t, bg, fg, size=11, h=0.32, r=0.06) + 0.08
    items(x2 + 0.22, y2 + 1.15, cw2 - 0.44, [(BLUE, "ตรวจชุดป้อนฝา · Maint · 14:00")])
    panel(x3, y2, cw2, ph, "E", INDIGO, "Escalate to Next SIM")
    items(x3 + 0.22, y2 + 0.68, cw2 - 0.44, [(INDIGO, "อะไหล่สั่งด่วน → SIM 3"), (INDIGO, "สถานะสินค้า → QA / SIM 4")])
    notes(sl, "บอร์ด SIM ต้องมีครบ 5 โซน: KPI, ปัญหาหลัก, ความเสี่ยง 24 ชม., Action และเรื่องที่ส่งต่อ\n"
              "ข้อมูลบนสไลด์เป็นตัวอย่างสมมติ")


@meta(BLUE)
def s26(sl, n, T):
    background(sl)
    header(sl, K2, "Action Management", "ประชุมจบแล้ว งานต้องไม่หาย", kc=BLUE)
    y, h = 1.95, 1.8
    hw = (CW - 0.2) / 2
    rect(sl, ML, y, hw, h, fill=WHITE, line="F2B8AD", lw=1.25, r=0.16)
    icon(sl, "thumb_down", ML + 0.28, y + 0.25, 0.32, RED)
    txt(sl, ML + 0.7, y + 0.2, 3, 0.42, "Weak Action", size=15, color=RED_D, font=FSB, anchor="m")
    txt(sl, ML + 0.28, y + 0.7, hw - 0.5, 0.4, "“ปรับปรุงเครื่องบรรจุ”", size=17, color=NAVY, font=FSB)
    chips(sl, ML + 0.28, y + 1.22, ["ไม่มี Owner", "ไม่มี Due", "ไม่รู้ว่าเสร็จคืออะไร"], RED_L, RED_D, size=11, h=0.34,
          font=F)
    x2 = ML + hw + 0.2
    rect(sl, x2, y, hw, h, fill=WHITE, line="A9DCC9", lw=1.25, r=0.16)
    icon(sl, "thumb_up", x2 + 0.28, y + 0.25, 0.32, GREEN)
    txt(sl, x2 + 0.7, y + 0.2, 3, 0.42, "Strong Action", size=15, color=GREEN_D, font=FSB, anchor="m")
    txt(sl, x2 + 0.28, y + 0.66, hw - 0.5, 0.6, "“ตรวจและแก้สาเหตุการหยุดที่ชุดป้อนฝา พร้อมยืนยันผลการเดินเครื่องตามเกณฑ์ที่ตกลง”",
        size=13.5, color=NAVY, font=FSB)
    chips(sl, x2 + 0.28, y + 1.32, ["Owner: หัวหน้าช่าง", "Due: ระบุวัน-เวลา", "Evidence"], GREEN_L, GREEN_D, size=11,
          h=0.34, font=F)
    txt(sl, ML, 4.05, 4, 0.3, "ACTION LIFECYCLE", size=12, color=SLATE, font=FSB, spc=2)
    st = [("Open", "เปิดงาน", RED_L, RED_D), ("In Progress", "กำลังทำ", BLUE_L, BLUE_D), ("Done", "ทำเสร็จ", "FDF3DE", ORANGE_D),
          ("Verified", "ยืนยันผล", GREEN_L, GREEN_D), ("Closed", "ปิดพร้อมหลักฐาน", GREEN, WHITE)]
    sw = (CW + 0.25 * 4) / 5
    for i, (t, d, f, fg) in enumerate(st):
        x = ML + i * (sw - 0.25)
        s = rect(sl, x, 4.42, sw, 0.95, fill=f, shape=MSO_SHAPE.PENTAGON if i == 0 else MSO_SHAPE.CHEVRON)
        _set_adj(s, adj=28000 if i else 28000)
        txt(sl, x + (0.25 if i == 0 else 0.48), 4.42, sw - 0.7, 0.95,
            [[(t, {"font": FSB, "size": 15})], [(d, {"size": 11.5})]], color=fg, anchor="m")
    rules = [("person_pin", "หนึ่ง Action = หนึ่ง Owner"), ("event_repeat", "ตรวจความคืบหน้าทุกรอบ"),
             ("verified", "Closed = มี Evidence"), ("do_not_disturb_on", "ติดขัด → แสดงเหตุ + ส่งต่อ")]
    rw = (CW - 3 * 0.15) / 4
    for i, (ic, t) in enumerate(rules):
        x = ML + i * (rw + 0.15)
        rect(sl, x, 5.95, rw, 0.85, fill=BLUE_L, r=0.12)
        icon(sl, ic, x + 0.2, 6.22, 0.32, BLUE)
        txt(sl, x + 0.62, 5.95, rw - 0.72, 0.85, t, size=12.5, color=NAVY, font=FSB, anchor="m")
    notes(sl, "Action ที่ดีต้องมี Owner คนเดียว Due ที่ชัด และนิยามว่าเสร็จคืออะไร\n"
              "Done ยังไม่ใช่ Closed — ต้องยืนยันผลและมีหลักฐานก่อนปิด")


# ======================================================================= 03 DEVIATION
K3 = "03 · Deviation & Escalation"


@meta(ORANGE, True)
def s27(sl, n, T):
    divider(sl, 3, "Deviation &\nEscalation", "เห็นความผิดปกติเร็ว ควบคุมผลกระทบ และส่งต่อถูกระดับ",
            ["Deviation", "Containment & Correction", "Reaction Plan", "Escalation", "Risk Next 24h"],
            "Stabilize Loop · S4–S5", "องค์ประกอบที่ 3: ทำให้ความผิดปกติถูกเห็นเร็ว ถูกควบคุม และถูกส่งต่อไปยังคนที่ตัดสินใจได้")


@meta(ORANGE)
def s28(sl, n, T):
    background(sl)
    header(sl, K3, "Deviation: Gap from Standard", "Actual ไม่ตรงกับ Standard / Target / Control Limit", kc=ORANGE_D)
    x, y, w, h = ML, 1.95, 6.3, 4.9
    card(sl, x, y, w, h)
    txt(sl, x + 0.3, y + 0.22, 5, 0.32, "ค่าควบคุมกระบวนการ (ตัวอย่าง)", size=13, color=NAVY, font=FSB)
    px0, px1, up, tg, lo = x + 0.4, x + w - 1.2, y + 1.55, y + 2.55, y + 3.55
    rect(sl, px0, up, px1 - px0, lo - up, fill=GREEN_L)
    line(sl, px0, up, px1, up, GREEN, 1.5)
    line(sl, px0, lo, px1, lo, GREEN, 1.5)
    line(sl, px0, tg, px1, tg, NAVY, 1.25, dash=True)
    for t, yy, c in (("Upper", up, GREEN), ("Target", tg, NAVY), ("Lower", lo, GREEN)):
        txt(sl, px1 + 0.1, yy - 0.15, 0.9, 0.3, t, size=11, color=c, font=FSB, anchor="m")
    vals = [0.05, -0.2, 0.15, -0.3, 0.1, 0.35, -0.15, 0.0, 1.25, 0.1]
    pts = []
    for i, v in enumerate(vals):
        pts.append((px0 + 0.2 + i * (px1 - px0 - 0.4) / (len(vals) - 1), tg - v * (tg - up)))
    for i in range(len(pts) - 1):
        line(sl, *pts[i], *pts[i + 1], NAVY, 2)
    for i, (a, b) in enumerate(pts):
        if vals[i] > 1:
            circle(sl, a, b, 0.3, fill=ORANGE, line=WHITE, lw=2)
            txt(sl, a + 0.2, b - 0.2, 1.3, 0.36, "Deviation", size=13, color=ORANGE_D, font=FSB, anchor="m")
        else:
            circle(sl, a, b, 0.14, fill=NAVY)
    chips(sl, x + 0.3, y + h - 0.6, ["ค่าเครื่องจักร", "ผลคุณภาพ", "KPI", "สภาพหน้างาน"], BG, NAVY, size=11, h=0.34, font=F)
    rx, rw = x + w + 0.3, MR - x - w - 0.3
    rect(sl, rx, y, rw, 1.45, fill=GREEN_L, r=0.14)
    icon(sl, "verified", rx + 0.28, y + 0.25, 0.32, GREEN)
    txt(sl, rx + 0.7, y + 0.2, 3, 0.4, "Fact", size=16, color=GREEN_D, font=FSB, anchor="m")
    txt(sl, rx + 0.28, y + 0.65, rw - 0.5, 0.4, "“เครื่องหยุด 18 นาที จาก Alarm ที่สถานีป้อนฝา”", size=14, color=NAVY, font=FSB)
    txt(sl, rx + 0.28, y + 1.04, rw - 0.5, 0.3, "ตรวจสอบได้", size=11.5, color=SLATE)
    rect(sl, rx, y + 1.6, rw, 1.45, fill="FDF3DE", r=0.14)
    icon(sl, "help", rx + 0.28, y + 1.85, 0.32, ORANGE)
    txt(sl, rx + 0.7, y + 1.8, 3, 0.4, "Assumption", size=16, color=ORANGE_D, font=FSB, anchor="m")
    txt(sl, rx + 0.28, y + 2.25, rw - 0.5, 0.4, "“เกิดจากพนักงานใช้งานไม่ถูกต้อง”", size=14, color=NAVY, font=FSB)
    txt(sl, rx + 0.28, y + 2.64, rw - 0.5, 0.3, "ยังเป็นสมมติฐาน จนกว่าจะมีหลักฐาน", size=11.5, color=SLATE)
    rect(sl, rx, y + 3.25, rw, 1.65, fill=NAVY, r=0.14, sh=True)
    icon(sl, "timer", rx + 0.28, y + 3.5, 0.34, MINT)
    txt(sl, rx + 0.75, y + 3.43, rw - 0.95, 0.45, "พบเร็ว = ควบคุมผลกระทบได้เร็ว", size=15, color=WHITE, font=FSB, anchor="m")
    txt(sl, rx + 0.28, y + 3.98, rw - 0.5, 0.8, "รายงาน Deviation ด้วย Fact ก่อนเสมอ แยก Assumption ไว้ให้ RCA พิสูจน์", size=12.5,
        color="DCE4F7")
    notes(sl, "Deviation คือช่องว่างระหว่างผลจริงกับมาตรฐาน ไม่ใช่ความผิดของคน\n"
              "ฝึกให้ทีมแยก Fact กับ Assumption ตั้งแต่ตอนรายงาน — เป็นพื้นฐานของ RCA ที่ดี")


@meta(ORANGE)
def s29(sl, n, T):
    background(sl)
    header(sl, K3, "Containment and Correction", "ควบคุมความเสี่ยงก่อน แล้วค่อยหาสาเหตุ", kc=ORANGE_D)
    cx = ML
    for i, t in enumerate(["Detect", "Assess Risk", "Follow Reaction Plan", "Record & Escalate"]):
        w = chip(sl, cx, 1.95, t, ORANGE if i == 2 else NAVY, WHITE, size=12.5, h=0.42, pad=0.2)
        cx += w
        if i < 3:
            icon_c(sl, "arrow_forward", cx + 0.22, 2.16, 0.24, "9AA8C7")
            cx += 0.44
    y, h = 2.6, 4.25
    hw = (CW - 0.2) / 2
    for k, (x, l, c, ic, t, d, rows) in enumerate([
        (ML, ORANGE_L, ORANGE, "shield", "Containment", "จำกัดหรือป้องกันผลกระทบไม่ให้ขยายวง",
         [("front_hand", "หยุดกระบวนการที่มีความเสี่ยง", INK), ("inventory_2", "แยกผลิตภัณฑ์ที่อาจได้รับผลกระทบ", INK),
          ("block", "ไม่ส่งชิ้นงานไม่ผ่านเกณฑ์ไปต่อ", INK)]),
        (ML + hw + 0.2, BLUE_L, BLUE, "build", "Correction", "แก้สภาพผิดปกติให้กลับสู่มาตรฐานตามวิธีที่อนุญาต",
         [("tune", "กลับไปใช้ค่าตั้งที่ได้รับอนุญาต", INK), ("build", "เปลี่ยนอุปกรณ์ตามขั้นตอน", INK),
          ("warning", "Correction ≠ สาเหตุถูกกำจัด", RED)])]):
        rect(sl, x, y, hw, h, fill=l, r=0.18)
        icon_badge(sl, ic, x + 0.3, y + 0.3, 0.6, c, round_=False, r=0.12)
        txt(sl, x + 1.08, y + 0.3, 4, 0.6, t, size=20, color=NAVY, font=FSB, anchor="m")
        txt(sl, x + 0.3, y + 1.08, hw - 0.6, 0.4, d, size=13.5, color=INK)
        for j, (ri, rt, rc) in enumerate(rows):
            yy = y + 1.72 + j * 0.78
            rect(sl, x + 0.3, yy, hw - 0.6, 0.64, fill=WHITE, r=0.1)
            icon(sl, ri, x + 0.48, yy + 0.17, 0.3, RED if rc == RED else c)
            txt(sl, x + 0.95, yy, hw - 1.4, 0.64, rt, size=13.5, color=rc, font=FSB if rc == RED else F, anchor="m")
    notes(sl, "Containment ปกป้องลูกค้าและคน Correction ทำให้กระบวนการกลับมาเดิน — ทั้งสองยังไม่ใช่การแก้สาเหตุ\n"
              "ถ้าปัญหาเดิมกลับมา แปลว่าต้องไปต่อที่ RCA")


@meta(ORANGE)
def s30(sl, n, T):
    background(sl)
    header(sl, K3, "Reaction Plan Elements", "แนวทางที่กำหนดไว้ก่อนเกิดเหตุ — ไม่ต้องตัดสินใจใหม่ทุกครั้ง", kc=ORANGE_D)
    x, y, w, h = ML, 1.95, 7.1, 4.9
    card(sl, x, y, w, h)
    rows = [("crisis_alert", "Trigger", "เงื่อนไขที่ถือว่าผิดปกติ", "Seal temp ต่ำกว่าค่าควบคุม"),
            ("pan_tool", "Immediate Action", "หยุด / ควบคุม / แยก / ตรวจ", "หยุดเครื่อง แยกสินค้าช่วงที่ผิดปกติ"),
            ("campaign", "Notify & Response Time", "แจ้งใคร ภายในเวลาเท่าไร", "แจ้งหัวหน้ากะ และ QA ทันที"),
            ("restart_alt", "Restart Criteria", "ใครอนุญาต ด้วยหลักฐานอะไร", "QA ยืนยันผลตรวจซีลก่อนเดินต่อ"),
            ("link", "Linked Standards", "WI · Control Plan · Safety", "WI ตั้งเครื่องซีล · Control Plan")]
    rh = h / len(rows)
    txt(sl, x + 4.6, y - 0.32, 2.4, 0.28, "ตัวอย่างสมมติ", size=10.5, color=ORANGE_D, font=FSB, align="r")
    for i, (ic, t, d, ex) in enumerate(rows):
        yy = y + i * rh
        if i:
            line(sl, x + 0.2, yy, x + w - 0.2, yy, LINE, 1)
        icon(sl, ic, x + 0.3, yy + rh / 2 - 0.16, 0.32, ORANGE)
        txt(sl, x + 0.85, yy, 2.1, rh, t, size=13.5, color=NAVY, font=FSB, anchor="m")
        txt(sl, x + 3.0, yy + 0.14, w - 3.2, 0.38, d, size=12.5, color=INK)
        txt(sl, x + 3.0, yy + 0.5, w - 3.2, 0.34, ex, size=11, color=ORANGE_D)
    rx = x + w + 0.3
    rect(sl, rx, y, MR - rx, h, grad=("A9500A", "E07B12"), angle=300, r=0.18, sh=True)
    icon(sl, "warning", rx + 0.35, y + 1.2, 0.6, WHITE)
    txt(sl, rx + 0.35, y + 1.95, MR - rx - 0.6, 0.55, "Running ≠ Released", size=24, color=WHITE, bold=True)
    txt(sl, rx + 0.35, y + 2.6, MR - rx - 0.65, 1.4,
        "เครื่องกลับมาเดินได้ ไม่ได้แปลว่าเงื่อนไขด้านความปลอดภัยหรือคุณภาพได้รับการยืนยันครบแล้ว", size=14, color=WHITE)
    txt(sl, rx + 0.35, y + 4.05, MR - rx - 0.65, 0.5, "Restart ต้องผ่าน Restart Criteria เสมอ", size=12.5, color=WHITE,
        font=FSB, alpha=0.85)
    notes(sl, "Reaction Plan ที่ดีเขียนไว้ก่อนเกิดเหตุ ทำให้คนหน้างานตัดสินใจได้ทันทีโดยไม่ต้องรอหัวหน้า\n"
              "ย้ำ Running ≠ Released: เดินเครื่องได้ไม่ได้แปลว่าปล่อยสินค้าได้")


@meta(ORANGE)
def s31(sl, n, T):
    background(sl)
    header(sl, K3, "Escalation: Right Issue, Right Level")
    band = [("Right Issue", "เรื่องที่ต้องส่งจริง", "FDF0E1", ORANGE_D), ("Right Level", "ระดับที่มีอำนาจ", "FBDDBE", ORANGE_D),
            ("Right Time", "ก่อนความเสียหายเพิ่ม", "F6C08C", "7A3B04"), ("Right Decision", "ได้การตัดสินใจที่ต้องการ", ORANGE, WHITE)]
    bw = CW / 4
    for i, (t, d, f, fg) in enumerate(band):
        x = ML + i * bw
        rect(sl, x, 1.45, bw + 0.01, 0.82, fill=f)
        txt(sl, x + 0.2, 1.45, bw - 0.3, 0.82, [[(t, {"font": FSB, "size": 15})], [(d, {"size": 12})]], color=fg,
            anchor="m")
    txt(sl, ML, 2.55, 4, 0.3, "ESCALATE WHEN", size=12, color=SLATE, font=FSB, spc=2)
    for i, (ic, c, t) in enumerate([("health_and_safety", RED, "Risk สูงตามเกณฑ์ → ทันที"),
                                    ("trending_down", ORANGE, "Impact กระทบหลายหน่วยงาน"),
                                    ("lock", BLUE, "เกินขอบเขตอำนาจของระดับนั้น")]):
        yy = 2.95 + i * 0.62
        icon(sl, ic, ML, yy + 0.06, 0.32, c)
        txt(sl, ML + 0.48, yy, 3.8, 0.45, t, size=14, color=INK, anchor="m")
    rect(sl, ML, 4.95, 4.4, 0.72, fill=RED_L, r=0.12)
    icon(sl, "close", ML + 0.2, 5.15, 0.3, RED)
    txt(sl, ML + 0.6, 4.95, 3.7, 0.72, "“เครื่องมีปัญหา” — ไม่พอให้ตัดสินใจ", size=13.5, color=RED_D, font=FSB, anchor="m")
    rect(sl, ML, 5.82, 4.4, 1.0, fill=GREEN_L, r=0.12)
    icon(sl, "check", ML + 0.2, 6.17, 0.3, GREEN)
    txt(sl, ML + 0.6, 5.82, 3.7, 1.0, "บอกครบ 4 ช่อง ใน 1 นาที — ผู้รับตัดสินใจได้ทันทีโดยไม่ต้องถามกลับ", size=12.5,
        color=GREEN_D, font=FSB, anchor="m")
    x, y, w, h = ML + 4.65, 2.55, CW - 4.65, 4.27
    rect(sl, x, y, w, h, fill=NAVY, r=0.18, sh=True)
    txt(sl, x + 0.3, y + 0.2, 4, 0.4, "Escalation Message", size=16, color=WHITE, font=FSB, anchor="m")
    chip(sl, x + w - 1.65, y + 0.24, "ตัวอย่างสมมติ", "2A3F78", "FFC98F", size=10.5, h=0.3)
    rows = [("What Happened", "เหตุการณ์จริง ที่ไหน เมื่อไร", "Filler Line A หยุด 45 นาที จาก Alarm ชุดป้อนฝา (กะเช้า)"),
            ("Impact", "ผลกระทบที่ทราบ ณ เวลานั้น", "Output ต่ำกว่าแผน กระทบ Order ส่งรอบบ่าย"),
            ("Done So Far", "การควบคุมที่ทำไปแล้ว", "ใช้ชุดป้อนฝาสำรอง · แยกสินค้าช่วง Alarm รอ QA"),
            ("Need", "การตัดสินใจหรือความช่วยเหลือที่ต้องการ", "อนุมัติสั่งอะไหล่ด่วน และช่างเสริมกะบ่าย")]
    rh = (h - 0.8) / 4
    for i, (k, d, ex) in enumerate(rows):
        yy = y + 0.72 + i * rh
        line(sl, x + 0.3, yy, x + w - 0.3, yy, "34488A", 1)
        txt(sl, x + 0.3, yy + 0.08, 1.75, rh - 0.1, k, size=13, color="FFC98F", font=FSB, anchor="m")
        txt(sl, x + 2.1, yy + 0.1, w - 2.4, 0.32, d, size=12, color="AFC0E8")
        txt(sl, x + 2.1, yy + 0.42, w - 2.4, 0.36, ex, size=12.5, color=WHITE, font=FM)
    notes(sl, "Escalation ที่ดีตอบ 4 ช่อง: เกิดอะไร กระทบอะไร ทำอะไรไปแล้ว และต้องการอะไรจากผู้รับ\n"
              "ฝึกให้ผู้เรียนเขียนข้อความ Escalation จากเหตุการณ์จริงล่าสุดในพื้นที่ของตัวเอง")


@meta(ORANGE)
def s32(sl, n, T):
    background(sl)
    header(sl, K3, "Risk in the Next 24 Hours", "เห็นความเสี่ยงก่อนกลายเป็นปัญหา — จากสัญญาณที่มีหลักฐาน", kc=ORANGE_D)
    tiles = [("health_and_safety", "Safety", RED, RED_L, "งานซ่อมที่ต้อง Lock-out ในกะบ่าย"),
             ("verified", "Quality", INDIGO, INDIGO_L, "วัตถุดิบ Lot ใหม่ ยังไม่มีผลตรวจรับ"),
             ("local_shipping", "Delivery", BLUE, BLUE_L, "Order ด่วนเข้าแผน ไม่มี Buffer"),
             ("precision_manufacturing", "Equipment Readiness", GREEN, GREEN_L, "อะไหล่สำคัญเสื่อมจากผล CIL")]
    tw, th = 2.72, 2.37
    for i, (ic, t, c, l, ex) in enumerate(tiles):
        x = ML + (i % 2) * (tw + 0.16)
        y = 1.95 + (i // 2) * (th + 0.16)
        rect(sl, x, y, tw, th, fill=l, r=0.16)
        icon(sl, ic, x + 0.25, y + 0.28, 0.42, c)
        txt(sl, x + 0.25, y + 0.85, tw - 0.4, 0.62, t, size=16, color=NAVY, font=FSB)
        txt(sl, x + 0.25, y + 1.45, tw - 0.4, 0.28, "สัญญาณตัวอย่าง", size=10.5, color=c, font=FSB)
        txt(sl, x + 0.25, y + 1.72, tw - 0.4, 0.6, ex, size=12, color=INK)
    x, y = ML + 2 * tw + 0.45, 1.95
    w, h = MR - x, 4.9
    card(sl, x, y, w, h)
    txt(sl, x + 0.3, y + 0.25, 3, 0.4, "Risk Card", size=17, color=NAVY, font=FSB, anchor="m")
    chip(sl, x + w - 1.65, y + 0.3, "ตัวอย่างสมมติ", ORANGE_L, ORANGE_D, size=10.5, h=0.3)
    rows = [("Risk", "อะไหล่สำคัญเสื่อม อาจกระทบกะถัดไป"), ("Evidence", "ผลตรวจสภาพจาก CIL กะนี้"),
            ("Impact · When", "เครื่องหยุดระหว่างกะบ่าย"), ("Countermeasure", "เตรียมอะไหล่ · วางแผนเปลี่ยนช่วงเปลี่ยนกะ"),
            ("Owner", "ช่างซ่อมบำรุงประจำไลน์")]
    rh = 0.64
    for i, (k, v) in enumerate(rows):
        yy = y + 0.82 + i * rh
        line(sl, x + 0.3, yy, x + w - 0.3, yy, LINE, 1)
        txt(sl, x + 0.3, yy, 1.9, rh, k, size=13, color=ORANGE_D, font=FSB, anchor="m")
        txt(sl, x + 2.25, yy, w - 2.5, rh, v, size=13, color=INK, anchor="m")
    rect(sl, x + 0.3, y + h - 0.68, w - 0.6, 0.48, fill=ORANGE_L, r=0.1,
         text="ไม่มี Evidence = ยังไม่ใช่ Risk ที่ต้องลงบอร์ด", size=12, color=ORANGE_D, font=FSB, anchor="m", margin=0.15)
    notes(sl, "มองไปข้างหน้า 24 ชม. ใน 4 มิติ: Safety, Quality, Delivery, Equipment\n"
              "Risk ที่จะลงบอร์ดต้องมีหลักฐาน มีผลกระทบและเวลาที่คาด และมีเจ้าของมาตรการ")


# ======================================================================= 04 RCA
K4 = "04 · RCA Management"


@meta(RED, True)
def s33(sl, n, T):
    divider(sl, 4, "RCA Management", "กำจัดสาเหตุของปัญหาสำคัญหรือปัญหาซ้ำ — ไม่ใช่แค่แก้อาการ",
            ["Fix Ladder", "RCA Triggers", "5W2H", "5 Whys & Fishbone", "RCA Flow"], "S5–S6 · Node N",
            "องค์ประกอบที่ 4: เมื่อปัญหาสำคัญหรือเกิดซ้ำ ต้องหาและกำจัดสาเหตุ แล้วอัปเดตมาตรฐาน")


@meta(RED)
def s34(sl, n, T):
    background(sl)
    header(sl, K4, "From Correction to Root Cause Elimination", kc=RED)
    cw, gx = 2.27, 0.195
    x_split = ML + 2 * (cw + gx) - gx / 2
    txt(sl, ML, 1.42, 4, 0.32, "แก้อาการ · This Time", size=13.5, color=ORANGE_D, font=FSB)
    rect(sl, ML, 1.78, x_split - ML - 0.1, 0.05, fill=ORANGE)
    txt(sl, x_split + 0.1, 1.42, 4, 0.32, "แก้สาเหตุ · Never Again", size=13.5, color=RED_D, font=FSB)
    rect(sl, x_split + 0.1, 1.78, MR - x_split - 0.1, 0.05, fill=RED)
    data = [("shield", "Containment", "ป้องกันผลกระทบขยายวง", "FCEDE2", ORANGE, NAVY),
            ("build", "Correction", "ให้สภาพกลับมาปกติในครั้งนี้", "FBE2C6", ORANGE_D, NAVY),
            ("troubleshoot", "RCA", "หาสาเหตุจากหลักฐานจริง", "F5B7A8", RED_D, NAVY),
            ("handyman", "Corrective Action", "แก้สาเหตุเพื่อป้องกันการเกิดซ้ำ", "D9431F", WHITE, WHITE),
            ("verified", "Verification", "ยืนยันว่ามาตรการได้ผลจริง", "9E2513", WHITE, WHITE)]
    base = 6.85
    for i, (ic, t, d, f, icc, fg) in enumerate(data):
        x = ML + i * (cw + gx)
        hh = 2.35 + i * 0.6
        y = base - hh
        rect(sl, x, y, cw, hh, fill=f, r=0.16, sh=(i == 4))
        icon(sl, ic, x + 0.22, y + 0.25, 0.38, icc)
        txt(sl, x + 0.22, y + 0.75, cw - 0.35, 0.4, t, size=15.5, color=fg, font=FSB)
        txt(sl, x + 0.22, y + 1.15, cw - 0.35, 0.75, d, size=12, color=fg if fg == WHITE else SLATE)
        txt(sl, x + 0.22, base - 0.5, 1, 0.35, f"0{i + 1}", size=14, color=fg if fg == WHITE else icc, font=FSB, alpha=0.6)
    notes(sl, "บันได 5 ขั้น: สองขั้นแรกแก้เฉพาะครั้งนี้ สามขั้นหลังป้องกันไม่ให้เกิดอีก\n"
              "หลายทีมหยุดที่ขั้น 2 แล้วปิดงาน — นั่นคือเหตุผลที่ปัญหาเดิมกลับมา")


@meta(RED)
def s35(sl, n, T):
    background(sl)
    header(sl, K4, "When to Open an RCA", "ใช้เกณฑ์ RCA / BDA ตาม WI ที่ประกาศใช้ ไม่ตัดสินจากความรู้สึก", kc=RED)
    data = [("health_and_safety", "High Risk Event", "Safety · Food Safety · Quality", "เช่น พบสิ่งแปลกปลอมในผลิตภัณฑ์"),
            ("repeat", "Recurring Problem", "เกิดซ้ำ หรือมีแนวโน้มกลับมาอีก", "เช่น Alarm ชุดป้อนฝาซ้ำทุกสัปดาห์"),
            ("settings_alert", "Loss / Breakdown", "Downtime หรือ Breakdown ที่เข้าเกณฑ์", "เช่น Breakdown เกินเกณฑ์นาทีใน WI"),
            ("priority_high", "Quick Fix Not Enough", "ประเด็นสำคัญที่แก้เฉพาะหน้าไม่พอ", "เช่น Correction แล้วแต่ยังหลุดเป้า")]
    cw, gx = 2.9, 0.177
    y, h = 1.95, 3.85
    for i, (ic, t, d, ex) in enumerate(data):
        x = ML + i * (cw + gx)
        card(sl, x, y, cw, h)
        icon_badge(sl, ic, x + 0.28, y + 0.3, 0.68, RED, round_=False, r=0.14)
        txt(sl, x + 0.28, y + 1.18, cw - 0.45, 0.65, t, size=16, color=NAVY, font=FSB)
        txt(sl, x + 0.28, y + 1.82, cw - 0.45, 0.7, d, size=12.5, color=SLATE)
        rect(sl, x + 0.2, y + h - 1.08, cw - 0.4, 0.88, fill=RED_L, r=0.1,
             text=ex, size=11.5, color=RED_D, anchor="m", margin=0.14)
    y2 = 6.05
    hw = (CW - 0.2) / 2
    rect(sl, ML, y2, hw, 0.78, fill=RED_L, r=0.12)
    icon(sl, "check_circle", ML + 0.25, y2 + 0.22, 0.34, RED)
    txt(sl, ML + 0.75, y2, hw - 0.9, 0.78, [[("เข้าเกณฑ์", {"font": FSB, "color": NAVY, "size": 14})],
                                             [("เปิด RCA / BDA · ติดตามใน SIM", {"size": 12})]], color=SLATE, anchor="m")
    x2 = ML + hw + 0.2
    rect(sl, x2, y2, hw, 0.78, fill=GREEN_L, r=0.12)
    icon(sl, "sync", x2 + 0.25, y2 + 0.22, 0.34, GREEN)
    txt(sl, x2 + 0.75, y2, hw - 0.9, 0.78, [[("ยังไม่เข้าเกณฑ์", {"font": FSB, "color": NAVY, "size": 14})],
                                             [("ยังต้องแก้และติดตามผ่าน DMS", {"size": 12})]], color=SLATE, anchor="m")
    notes(sl, "เปิด RCA ตามเกณฑ์ใน WI เท่านั้น เพื่อให้ทรัพยากรไปอยู่กับปัญหาที่สำคัญจริง\n"
              "เรื่องที่ไม่เข้าเกณฑ์ไม่ได้หายไป — ยังต้องแก้และติดตามใน DMS ตามปกติ")


@meta(RED)
def s36(sl, n, T):
    background(sl)
    header(sl, K4, "Problem Statement with 5W2H", "ทุกคนต้องวิเคราะห์เหตุการณ์เดียวกัน ด้วยขอบเขตเดียวกัน", kc=RED)
    q = [("What", "ผิดปกติอะไร"), ("Where", "เกิดที่ไหน"), ("When", "เมื่อไร กะไหน"), ("Who / Which", "คนหรือเครื่องจักรใด"),
         ("How", "เกิดขึ้นอย่างไร"), ("How Much", "กระทบเท่าไร")]
    tw, th = 2.42, 0.9
    for i, (t, d) in enumerate(q):
        x = ML + (i % 2) * (tw + 0.12)
        y = 1.95 + (i // 2) * (th + 0.12)
        rect(sl, x, y, tw, th, fill=NAVY, r=0.12,
             text=[[(t, {"font": FSB, "size": 15})], [(d, {"size": 12, "color": "C9D6FF"})]], color=WHITE,
             anchor="m", margin=0.2)
    rect(sl, ML, 5.05, 2 * tw + 0.12, 0.55, fill=RED_L, r=0.1, text="+ Actual เทียบกับ Standard / Target", size=13,
         color=RED_D, font=FSB, anchor="m", margin=0.2)
    rect(sl, ML, 5.75, 2 * tw + 0.12, 1.08, fill=WHITE, line=LINE, r=0.12,
         text=[[("2H ที่ทีมมักลืม: ", {"font": FSB, "color": NAVY}),
                ("How Much ต้องเป็นตัวเลข (ครั้ง · นาที · ชิ้น) ไม่ใช่ “บ่อย” หรือ “เยอะ”", {})]], size=12.5, color=INK,
         anchor="m", margin=0.2)
    x = ML + 2 * tw + 0.45
    w = MR - x
    rect(sl, x, 1.95, w, 1.0, fill=WHITE, line="F2B8AD", lw=1.25, r=0.14)
    icon(sl, "close", x + 0.25, 2.07, 0.26, RED)
    txt(sl, x + 0.6, 2.02, 3, 0.32, "Vague", size=13.5, color=RED_D, font=FSB)
    txt(sl, x + 0.25, 2.4, w - 0.5, 0.4, "“เครื่องบรรจุมีปัญหาบ่อย”", size=16, color=NAVY, font=FSB)
    rect(sl, x, 3.1, w, 3.73, fill=WHITE, line="A9DCC9", lw=1.25, r=0.14, sh=True)
    icon(sl, "check", x + 0.25, 3.23, 0.26, GREEN)
    txt(sl, x + 0.6, 3.18, 3, 0.32, "Specific", size=13.5, color=GREEN_D, font=FSB)
    txt(sl, x + 0.25, 3.58, w - 0.5, 0.75, "“เครื่องบรรจุ Line A หยุดจาก Alarm ชุดป้อนฝา 4 ครั้ง รวม 32 นาที ระหว่างกะเช้า”",
        size=15.5, color=NAVY, font=FSB)
    br = [("Which / Where", "เครื่องบรรจุ Line A"), ("What", "หยุดจาก Alarm ชุดป้อนฝา"), ("How Much", "4 ครั้ง · รวม 32 นาที"),
          ("When", "กะเช้า")]
    for i, (k, v) in enumerate(br):
        yy = 4.52 + i * 0.52
        line(sl, x + 0.25, yy, x + w - 0.25, yy, LINE, 1)
        txt(sl, x + 0.25, yy, 1.9, 0.52, k, size=12.5, color=GREEN_D, font=FSB, anchor="m")
        txt(sl, x + 2.2, yy, w - 2.5, 0.52, v, size=12.5, color=INK, anchor="m")
    notes(sl, "Problem Statement ที่ชัดทำให้ทีมไม่เถียงกันผิดเรื่อง และทำให้ตรวจผลได้หลังแก้\n"
              "ให้ผู้เรียนเขียนประโยค Vague จากพื้นที่ตัวเองใหม่ให้เป็น Specific ด้วย 5W2H")


@meta(RED)
def s37(sl, n, T):
    background(sl)
    header(sl, K4, "5 Whys and Fishbone", "ไล่จากอาการถึงสาเหตุที่จัดการได้ · ทุกปัจจัยเป็นสมมติฐานจนพิสูจน์ด้วยข้อมูล", kc=RED)
    txt(sl, ML, 1.95, 5, 0.3, "5 WHYS · ตัวอย่างสมมติ", size=12, color=SLATE, font=FSB, spc=2)
    whys = [("Why 1", "เครื่องหยุด ← ชุดป้อนฝาติดขัด", "FBE7E3", RED_D, INK),
            ("Why 2", "รางนำฝาเยื้องศูนย์", "F8D5CD", RED_D, INK),
            ("Why 3", "ปรับตั้งหลังเปลี่ยนรุ่นไม่เท่ากัน", "F3B6A8", RED_D, INK),
            ("Root", "ไม่มีค่า Centerline มาตรฐาน", "D9431F", WHITE, WHITE)]
    for i, (k, t, f, kc, fg) in enumerate(whys):
        x = ML + i * 0.22
        y = 2.35 + i * 0.72
        rect(sl, x, y, 5.6 - i * 0.22, 0.6, fill=f, r=0.1)
        txt(sl, x + 0.15, y, 0.8, 0.6, k, size=12, color=kc, font=FSB, anchor="m")
        txt(sl, x + 0.95, y, 4.5, 0.6, t, size=13, color=fg, font=FSB if k == "Root" else F, anchor="m")
    rect(sl, ML, 5.4, 5.6, 0.62, fill=GREEN_L, r=0.1,
         text=[[("Countermeasure: ", {"font": FSB, "color": GREEN_D}), ("กำหนด Centerline + ใส่ใน WI เปลี่ยนรุ่น", {})]],
         size=12.5, color=INK, anchor="m", margin=0.2)
    rect(sl, ML, 6.15, 5.6, 0.68, fill=NAVY, r=0.12)
    icon(sl, "do_not_disturb_on", ML + 0.22, 6.32, 0.32, "FF9C85")
    txt(sl, ML + 0.7, 6.15, 4.8, 0.68, "อย่าหยุดที่ “พนักงานผิดพลาด” — ถามต่อว่าระบบเปิดช่องให้ผิดได้อย่างไร", size=12.5,
        color=WHITE, font=FSB, anchor="m")
    x, y, w, h = ML + 5.9, 1.95, CW - 5.9, 4.88
    card(sl, x, y, w, h)
    txt(sl, x + 0.25, y + 0.18, 4, 0.3, "FISHBONE · 6M", size=12, color=SLATE, font=FSB, spc=2)
    sy = y + 2.5
    hx = x + w - 1.3
    line(sl, x + 0.3, sy, hx, sy, NAVY, 3)
    rect(sl, hx, sy - 0.42, 1.1, 0.84, fill=RED, r=0.1, text=[[("Problem", {"font": FSB, "size": 12.5})],
                                                               [("ฝาติดขัด", {"size": 11})]], color=WHITE, align="c",
         anchor="m", margin=0.04)
    cats = [("Man", "ทักษะปรับตั้งหลังเปลี่ยนรุ่น"), ("Machine", "รางนำฝาสึก / เยื้องศูนย์"), ("Method", "ไม่มีค่า Centerline"),
            ("Material", "ขนาดฝาต่างล็อต"), ("Measure", "ไม่มีจุดตรวจตำแหน่งราง"), ("Environ.", "ฝุ่น / ความชื้นในห้องบรรจุ")]
    span = hx - x - 0.6
    for i, (c, cause) in enumerate(cats):
        top = i < 3
        bx = x + 0.55 + (i % 3) * span / 3 + span / 3 * 0.55
        ex, ey = bx - 0.5, (sy - 1.15 if top else sy + 1.15)
        line(sl, ex, ey, bx, sy, "9AB0D8", 2)
        if top:
            txt(sl, ex - 0.66, ey - 0.86, 1.32, 0.3, c, size=12.5, color=NAVY, font=FSB, align="c")
            txt(sl, ex - 0.66, ey - 0.56, 1.32, 0.52, cause, size=10, color=SLATE, align="c", anchor="b")
        else:
            txt(sl, ex - 0.66, ey + 0.04, 1.32, 0.3, c, size=12.5, color=NAVY, font=FSB, align="c")
            txt(sl, ex - 0.66, ey + 0.32, 1.32, 0.52, cause, size=10, color=SLATE, align="c")
        if top:
            pass
    txt(sl, x + 0.25, y + h - 0.36, w - 0.5, 0.3, "สาเหตุในแต่ละก้างเป็นสมมติฐานตัวอย่าง — ยืนยันด้วยข้อมูลก่อนสรุป", size=11,
        color=SLATE)
    notes(sl, "5 Whys ใช้เมื่อสาเหตุเป็นเส้นตรง Fishbone ใช้เมื่อมีหลายปัจจัยที่ต้องคัดกรอง\n"
              "หยุดถามเมื่อได้สาเหตุที่เราแก้ได้และป้องกันซ้ำได้ เช่น ไม่มีมาตรฐาน — ไม่ใช่โทษคน")


@meta(RED)
def s38(sl, n, T):
    background(sl)
    header(sl, K4, "RCA Flow within DMS", "เชื่อม SIM · BDA · มาตรฐาน — จนกลับเข้าวง Stabilize", kc=RED)
    steps = [("sensors", ORANGE, "Detect", "KPI / หน้างาน"), ("shield", ORANGE, "Contain", "ควบคุมความเสี่ยง"),
             ("rule", RED, "Check Criteria", "RCA / BDA"), ("groups", BLUE, "Track in SIM", "ความคืบหน้า"),
             ("verified", RED_D, "Verify & Close", "ด้วยหลักฐาน"), ("description", GREEN, "Update Standard", "WI · SOP · Control Plan")]
    sw = CW / 6
    yc = 2.65
    for i, (ic, c, t, d) in enumerate(steps):
        cx = ML + sw * i + sw / 2
        circle(sl, cx, yc, 1.0, fill=c, sh=True)
        icon_c(sl, ic, cx, yc, 0.48, WHITE)
        txt(sl, cx - sw / 2, yc + 0.62, sw, 0.36, t, size=14.5, color=NAVY, font=FSB, align="c")
        txt(sl, cx - sw / 2 + 0.05, yc + 0.98, sw - 0.1, 0.55, d, size=12, color=SLATE, align="c")
        if i < 5:
            icon_c(sl, "arrow_forward", cx + sw / 2, yc, 0.26, "9AA8C7")
    tiles = [("person", "Owner", "เจ้าของ RCA ชัดเจน"), ("calendar_today", "Plan & Due", "แผนและกำหนดเสร็จ"),
             ("flag", "Status", "สถานะติดตามได้ใน SIM")]
    tw = (CW - 0.3) / 3
    for i, (ic, t, d) in enumerate(tiles):
        x = ML + i * (tw + 0.15)
        card(sl, x, 4.55, tw, 0.9, sh=False)
        icon(sl, ic, x + 0.25, 4.84, 0.32, RED)
        txt(sl, x + 0.72, 4.55, tw - 0.85, 0.9, [[(t, {"font": FSB, "color": NAVY, "size": 14})], [(d, {"size": 12})]],
            color=SLATE, anchor="m")
    hw = (CW - 0.2) / 2
    rect(sl, ML, 5.65, hw, 1.18, fill=BLUE_L, r=0.12)
    icon(sl, "timer", ML + 0.25, 6.06, 0.36, BLUE)
    txt(sl, ML + 0.8, 5.65, hw - 1, 1.18, "SIM ตรวจความคืบหน้าและปลดอุปสรรค — ไม่วิเคราะห์เชิงลึกในเวลาประชุม", size=13, color=INK,
        anchor="m")
    x2 = ML + hw + 0.2
    rect(sl, x2, 5.65, hw, 1.18, fill=GREEN_L, r=0.12)
    icon(sl, "all_inclusive", x2 + 0.25, 6.06, 0.36, GREEN)
    txt(sl, x2 + 0.8, 5.65, hw - 1, 1.18, "มาตรฐานใหม่ผ่าน Node → กลับเข้าวง Stabilize ที่ S1 และติดตามการเกิดซ้ำ", size=13,
        color=INK, anchor="m")
    notes(sl, "RCA ไม่ได้อยู่นอก DMS: เปิดจากสัญญาณใน DMS ติดตามใน SIM และปิดด้วยมาตรฐานใหม่\n"
              "ห้ามใช้เวลาประชุม SIM วิเคราะห์ RCA เชิงลึก — SIM มีหน้าที่ติดตามและปลดล็อก")


# ======================================================================= 05 PROCESS CONFIRMATION
K5 = "05 · Process Confirmation"


@meta(INDIGO, True)
def s39(sl, n, T):
    divider(sl, 5, "Process Confirmation", "ยืนยันที่หน้างานว่ามาตรฐานเกิดขึ้นจริง ทุกวัน",
            ["4 Confirms", "6 Steps", "Layered PC", "PC vs Gemba Walk"], "Stabilize Loop · S1 · S6",
            "องค์ประกอบที่ 5: หัวหน้าทุกระดับลงไปยืนยันว่ามาตรฐานถูกทำจริง ไม่ใช่ดูจากรายงาน")


@meta(INDIGO)
def s40(sl, n, T):
    background(sl)
    header(sl, K5, "What Process Confirmation Checks", "ตรวจจากสภาพจริง ไม่ใช่ดูรายงานย้อนหลังอย่างเดียว", kc=INDIGO)
    data = [("description", "Confirm Standard", "ขั้นตอนทำตาม SOP / WI ครบหรือไม่", ["ลำดับงาน", "อุปกรณ์ถูกต้อง"]),
            ("tune", "Confirm Control", "ค่าควบคุม CCP / OPRP อยู่ในเกณฑ์หรือไม่", ["CCP", "OPRP", "Safety"]),
            ("emergency_home", "Confirm Reaction", "เมื่อผิดปกติ ตอบสนองตามแผนหรือไม่", ["หยุด", "แจ้ง", "แยก"]),
            ("photo_camera", "Confirm Evidence", "มีสิ่งที่ตรวจสอบได้จริงหรือไม่", ["สังเกตจริง", "ค่าบนเครื่อง", "บันทึก"])]
    cw, gx = 2.9, 0.177
    y, h = 1.95, 4.05
    for i, (ic, t, d, tags) in enumerate(data):
        x = ML + i * (cw + gx)
        rect(sl, x, y, cw, h, fill=INDIGO_L, r=0.16)
        icon_badge(sl, ic, x + 0.28, y + 0.3, 0.72, INDIGO)
        txt(sl, x + 0.28, y + 1.22, 0.5, 0.3, f"0{i + 1}", size=12, color=INDIGO, font=FSB)
        txt(sl, x + 0.28, y + 1.5, cw - 0.45, 0.4, t, size=16, color=NAVY, font=FSB)
        txt(sl, x + 0.28, y + 1.95, cw - 0.45, 0.75, d, size=13, color=SLATE)
        chips(sl, x + 0.28, y + h - 0.95, tags, WHITE, NAVY, size=11, h=0.34, max_x=x + cw - 0.15, row_h=0.42)
    y2 = 6.3
    txt(sl, ML, y2, 1.2, 0.45, "Result:", size=15, color=NAVY, font=FSB, anchor="m")
    cx = ML + 1.15
    for t, bg, fg in (("Pass", GREEN_L, GREEN_D), ("Fail → Reaction Plan ทันที", RED_L, RED_D), ("N/A", BG, SLATE)):
        cx += chip(sl, cx, y2 + 0.02, t, bg, fg, size=13.5, h=0.42, pad=0.2) + 0.12
    txt(sl, cx + 0.3, y2, MR - cx - 0.3, 0.45, "Fail ไม่ใช่การจับผิด แต่เป็นสัญญาณว่ามาตรฐานหรือการฝึกต้องปรับ", size=12,
        color=SLATE, anchor="m", align="r")
    notes(sl, "PC ตรวจ 4 เรื่อง: ทำตามขั้นตอนไหม ค่าควบคุมอยู่ในเกณฑ์ไหม ตอบสนองถูกไหม และมีหลักฐานไหม\n"
              "ผล Fail ต้องนำไปสู่ Reaction Plan ทันที และย้อนดูว่ามาตรฐานหรือการฝึกมีช่องโหว่หรือไม่")


@meta(INDIGO)
def s41(sl, n, T):
    background(sl)
    header(sl, K5, "Process Confirmation in 6 Steps", "ทำเป็นรอบตามแผน · บันทึกและติดตามจนปิด", kc=INDIGO)
    st = [("my_location", "Select Focus", "เลือกจุดเสี่ยงหรือจุดควบคุม", "เช่น จุดซีล · CCP"),
          ("menu_book", "Prepare Standard", "เตรียม WI เกณฑ์ และ Reaction Plan", "WI + เกณฑ์ค่าควบคุม"),
          ("directions_walk", "Go & See", "ดูการทำงานจริงที่จุดงาน", "ไปที่จุดงานจริง"),
          ("photo_camera", "Confirm Evidence", "เทียบผลจริงกับมาตรฐาน", "ค่าบนเครื่อง · บันทึก"),
          ("gavel", "Judge & React", "Pass / Fail / N/A · ตอบสนองเมื่อ Fail", "Fail → หยุด · แจ้ง"),
          ("task_alt", "Record & Follow Up", "บันทึกและติดตามจนปิด", "Owner · Due · ปิดงาน")]
    cols = ["1E2A6E", "27347E", "2F3F95", "3949A8", "4A5BC0", "5B6CD0"]
    sw = CW / 6
    yc = 2.3
    line(sl, ML + sw / 2, yc, MR - sw / 2, yc, "B7BFE6", 3)
    for i, (ic, t, d, ex) in enumerate(st):
        cx = ML + i * sw + sw / 2
        circle(sl, cx, yc, 0.7, fill=cols[i], line=WHITE, lw=3, sh=True)
        icon_c(sl, ic, cx, yc, 0.34, WHITE)
        txt(sl, cx - sw / 2, yc + 0.48, sw, 0.3, f"0{i + 1}", size=12, color=INDIGO, font=FSB, align="c")
        txt(sl, cx - sw / 2 + 0.05, yc + 0.78, sw - 0.1, 0.6, t, size=14, color=NAVY, font=FSB, align="c")
        txt(sl, cx - sw / 2 + 0.1, yc + 1.38, sw - 0.2, 0.7, d, size=11.5, color=SLATE, align="c")
        rect(sl, cx - sw / 2 + 0.06, 4.75, sw - 0.12, 1.15, fill=INDIGO_L, r=0.12)
        txt(sl, cx - sw / 2 + 0.1, 4.85, sw - 0.2, 0.28, "Example", size=10.5, color=SLATE, align="c")
        txt(sl, cx - sw / 2 + 0.12, 5.12, sw - 0.24, 0.7, ex, size=12, color=NAVY, font=FSB, align="c", anchor="m")
    rect(sl, ML, 6.15, CW, 0.66, fill=NAVY, r=0.12)
    icon(sl, "event_repeat", ML + 0.25, 6.3, 0.36, MINT)
    txt(sl, ML + 0.8, 6.15, CW - 1, 0.66, "PC ที่ได้ผล = ทำตามแผนสม่ำเสมอ + Fail ทุกรายการมี Action ที่ปิดด้วยหลักฐาน", size=14,
        color=WHITE, font=FSB, anchor="m")
    notes(sl, "6 ขั้นนี้ใช้ได้ทุกระดับ ต่างกันที่จุดโฟกัส\n"
              "ขั้นที่ 2 มักถูกข้าม: ถ้าไม่ได้เตรียมมาตรฐานไปก่อน จะกลายเป็นการเดินดูทั่วไป ไม่ใช่การยืนยัน")


@meta(INDIGO)
def s42(sl, n, T):
    background(sl)
    header(sl, K5, "Layered Process Confirmation", "แต่ละระดับตรวจคนละมุม ตามหน้าที่ — ไม่ซ้ำซ้อน", kc=INDIGO)
    rows = [("apartment", "Executive", "ประสิทธิผลของระบบ และอุปสรรคสำคัญ", "รายเดือน", "1E2A6E", WHITE),
            ("manage_accounts", "Manager", "การควบคุมพื้นที่ และการติดตามปัญหา", "รายสัปดาห์", "2F3F95", WHITE),
            ("engineering", "Area Leader", "งานจริง มาตรฐาน และความผิดปกติรายวัน", "ทุกวัน / ทุกกะ", INDIGO, WHITE),
            ("verified_user", "Safety / Quality Specialist", "ยืนยันข้อกำหนดเฉพาะด้าน", "ตามแผนความเสี่ยง", INDIGO_L, NAVY)]
    txt(sl, MR - 2.25, 1.9, 2.25, 0.3, "ความถี่ (ข้อเสนอ)", size=11.5, color=INDIGO, font=FSB, align="c")
    for i, (ic, t, d, f_, fill, fg) in enumerate(rows):
        y = 2.3 + i * 1.02
        w = CW - 2.45 - (3 - i) * 0.35 if i < 3 else CW - 2.45
        dashed = i == 3
        rect(sl, ML, y, w, 0.86, fill=fill, r=0.12, line=INDIGO if dashed else None, dash=dashed, lw=1)
        icon(sl, ic, ML + 0.28, y + 0.25, 0.36, WHITE if fg == WHITE else INDIGO)
        txt(sl, ML + 0.95, y, 3.2, 0.86, t, size=15, color=fg, font=FSB, anchor="m")
        txt(sl, ML + 4.25, y, w - 4.4, 0.86, d, size=13, color=fg, anchor="m")
        rect(sl, MR - 2.25, y, 2.25, 0.86, fill=WHITE, line=LINE, r=0.12, text=f_, size=13, color=INDIGO, font=FSB,
             align="c", anchor="m")
    txt(sl, ML, 6.4, CW, 0.42, "ความถี่เป็นข้อเสนอเริ่มต้น — ปรับตามความเสี่ยงของพื้นที่และระบุใน Leader Standard Work", size=11.5,
        color=SLATE, anchor="m")
    notes(sl, "แต่ละระดับมีคำถามต่างกัน: Area Leader ดูงานจริงรายวัน Manager ดูระบบควบคุมของพื้นที่ Executive ดูว่าระบบได้ผลไหม\n"
              "ความถี่ในคอลัมน์ขวาเป็นข้อเสนอเริ่มต้น ให้ยืนยันกับ Leader Standard Work ของแต่ละพื้นที่")


@meta(INDIGO)
def s43(sl, n, T):
    background(sl)
    header(sl, K5, "Process Confirmation vs Gemba Walk", "ใช้คู่กัน แต่เป้าหมายต่างกัน", kc=INDIGO)
    x, y, w, h = ML, 1.95, CW, 4.9
    card(sl, x, y, w, h)
    c0 = 1.95
    cw = (w - c0) / 2
    rect(sl, x, y, c0, h, fill=BG, r=0.14)
    rect(sl, x + c0 - 0.2, y, 0.2, h, fill=BG)
    hh = 0.85
    rect(sl, x + c0, y, cw, hh, fill=INDIGO)
    rect(sl, x + c0 + cw, y, cw, hh, fill=GREEN, r=0.14)
    rect(sl, x + c0 + cw, y + hh / 2, cw, hh / 2, fill=GREEN)
    rect(sl, x + c0 + cw, y, 0.3, hh, fill=GREEN)
    icon(sl, "fact_check", x + c0 + 0.3, y + 0.26, 0.34, WHITE)
    txt(sl, x + c0 + 0.78, y, cw - 1, hh, "Process Confirmation", size=16, color=WHITE, font=FSB, anchor="m")
    icon(sl, "directions_walk", x + c0 + cw + 0.3, y + 0.26, 0.34, WHITE)
    txt(sl, x + c0 + cw + 0.78, y, cw - 1, hh, "Gemba Walk", size=16, color=WHITE, font=FSB, anchor="m")
    rows = [("Purpose", "ยืนยันว่ามาตรฐานถูกทำจริง", "เห็นและเข้าใจกระบวนการจริง"),
            ("Method", "ใช้เกณฑ์และหลักฐาน", "สังเกตการไหลของงาน ความสูญเสีย อุปสรรค"),
            ("Output", "Pass / Fail / N/A + การตอบสนอง", "ข้อค้นพบ และโอกาสปรับปรุง"),
            ("Role in Loop", "รักษามาตรฐาน · Stabilize", "ค้นหาปัญหาที่ยังไม่ปรากฏในรายงาน")]
    rh = (h - hh) / 4
    for i, (k, a, b) in enumerate(rows):
        yy = y + hh + i * rh
        if i:
            line(sl, x, yy, x + w, yy, LINE, 1)
        txt(sl, x + 0.3, yy, c0 - 0.4, rh, k, size=14, color=NAVY, font=FSB, anchor="m")
        txt(sl, x + c0 + 0.3, yy, cw - 0.5, rh, a, size=13.5, color=INK, anchor="m")
        txt(sl, x + c0 + cw + 0.3, yy, cw - 0.5, rh, b, size=13.5, color=INK, anchor="m")
    line(sl, x + c0 + cw, y + hh, x + c0 + cw, y + h, LINE, 1)
    notes(sl, "PC ถามว่า 'ทำตามมาตรฐานไหม' Gemba Walk ถามว่า 'มีอะไรที่เรายังไม่เห็น'\n"
              "ถ้าใช้ Gemba Walk แทน PC จะไม่มีหลักฐานยืนยันมาตรฐาน ถ้าใช้ PC อย่างเดียวจะไม่เห็นปัญหาใหม่")


# ======================================================================= SUMMARY
@meta(NAVY)
def s44(sl, n, T):
    background(sl)
    header(sl, "Summary", "One System, Five Components")
    cx, cy, R = ML + 2.75, 4.35, 1.85
    circle(sl, cx, cy, 2 * R, line="D5DCEE", lw=10)
    circle(sl, cx, cy, 1.7, grad=(NAVY, "2A4590"), angle=315, sh=True)
    icon_c(sl, "all_inclusive", cx, cy - 0.4, 0.36, MINT)
    txt(sl, cx - 0.8, cy - 0.15, 1.6, 0.6, "Stable\nOperation", size=14, color=WHITE, font=FSB, align="c")
    labels = ["KPI Cascade", "Meeting", "Escalation", "RCA", "Confirm"]
    for i in range(5):
        c = COMP[i + 1]
        px, py = polar(cx, cy, R, -90 + i * 72)
        circle(sl, px, py, 1.12, fill=c["c"], line=WHITE, lw=3, sh=True)
        icon_c(sl, c["icon"], px, py - 0.18, 0.32, WHITE)
        txt(sl, px - 0.6, py + 0.04, 1.2, 0.3, labels[i], size=11, color=WHITE, font=FSB, align="c")
    x = ML + 5.95
    w = MR - x
    txt(sl, x, 1.95, 3, 0.3, "EXPECTED OUTCOMES", size=12, color=SLATE, font=FSB, spc=2)
    txt(sl, x + 3.0, 1.95, w - 3.0, 0.3, "MEASURE (ข้อเสนอ)", size=12, color=SLATE, font=FSB, spc=1, align="r")
    rows = [("balance", GREEN, GREEN_L, "กระบวนการผลิตเสถียรขึ้น", "% กะที่ผลลัพธ์อยู่ในมาตรฐาน"),
            ("visibility", BLUE, BLUE_L, "เห็นปัญหาเร็วขึ้น", "เวลาตั้งแต่พบจนตอบสนอง"),
            ("person_check", ORANGE, ORANGE_L, "ทุกการดำเนินการมีเจ้าของชัดเจน", "% Action ปิดตรงเวลา"),
            ("trending_down", RED, RED_L, "ความสูญเสียจากปัญหาเดิมลดลง", "จำนวนปัญหาซ้ำ / เดือน")]
    for i, (ic, c, l, t, m) in enumerate(rows):
        y = 2.4 + i * 0.95
        card(sl, x, y, w, 0.8, sh=False)
        icon_badge(sl, ic, x + 0.18, y + 0.14, 0.52, l, c, round_=False, r=0.1)
        txt(sl, x + 0.88, y, 2.85, 0.8, t, size=13.5, color=NAVY, font=FSB, anchor="m")
        rect(sl, x + w - 2.25, y + 0.17, 2.1, 0.46, fill=l, r=0.08, text=m, size=11.5, color=c, font=FSB, align="c",
             anchor="m", margin=0.04)
    rect(sl, x, 6.25, w, 0.58, fill=NAVY, r=0.1, text="วัดจากผลลัพธ์ ไม่ใช่จำนวนประชุมหรือจำนวนแบบฟอร์ม", size=13.5,
         color=WHITE, font=FSB, anchor="m", margin=0.25)
    notes(sl, "5 องค์ประกอบทำงานเป็นระบบเดียว ขาดตัวใดตัวหนึ่งวงจะไม่หมุน\n"
              "ตัวชี้วัดคอลัมน์ขวาเป็นข้อเสนอสำหรับติดตามความก้าวหน้าของ DMS — ยืนยันนิยามและ Baseline ก่อนใช้จริง")


@meta(NAVY, True)
def s45(sl, n, T):
    rect(sl, 0, 0, W, H, grad=("0E1D52", "0C4D7C"), angle=315)
    for i, a in enumerate((0.05, 0.035, 0.025)):
        b = rect(sl, 6.2 + i * 1.6, -1.5, 0.9, 10.5, fill=WHITE, alpha=a)
        b.rotation = 28
    txt(sl, ML, 0.55, 8, 0.3, "SAPPE INFINITE LOOP", size=12.5, color=MINT, font=FSB, spc=3)
    txt(sl, ML, 0.85, 11, 0.7, "Three Daily Questions", size=34, color=WHITE, bold=True)
    data = [("bar_chart", GREEN, MINT, "STABILIZE", "วันนี้ทำได้ตามมาตรฐานหรือยัง?", "SIM ประจำกะ / วัน", "หน้างาน / พื้นที่"),
            ("ads_click", BLUE, "9FC2FF", "ELEVATE", "จะยกระดับมาตรฐานเรื่องใด ด้วยโครงการอะไร?", "Weekly Review · โครงการ",
             "FI Pillar / ทีมโครงการ"),
            ("hub", "E5533D", "FFB4A3", "NODE", "ปิดงาน → ยืนยันมาตรฐาน → ขยายผล", "ตามเกณฑ์ RCA / BDA", "เจ้าของปัญหา / ทีม RCA")]
    cw, gx = 3.9, 0.165
    y, h = 1.8, 4.6
    for i, (ic, c, lc, lab, q, forum, own) in enumerate(data):
        x = ML + i * (cw + gx)
        rect(sl, x, y, cw, h, fill=WHITE, alpha=0.07, line="FFFFFF", lw=0.5, r=0.18)
        icon_badge(sl, ic, x + 0.32, y + 0.32, 0.72, c)
        txt(sl, x + 0.32, y + 1.25, 3, 0.3, lab, size=12.5, color=lc, font=FSB, spc=2.5)
        txt(sl, x + 0.32, y + 1.6, cw - 0.6, 1.2, q, size=19, color=WHITE, font=FSB)
        line(sl, x + 0.32, y + 3.05, x + cw - 0.32, y + 3.05, "FFFFFF", 0.75, alpha=0.25)
        for j, (k, v) in enumerate((("Forum", forum), ("Owner", own))):
            txt(sl, x + 0.32, y + 3.25 + j * 0.55, cw - 0.6, 0.5, [[(k.upper(), {"size": 10, "color": "9FB2E0",
                                                                                  "font": FSB, "spc": 1.5})],
                                                                    [(v, {"size": 13, "color": WHITE})]])
    rect(sl, ML, 6.72, 0.45, 0.04, fill="E5533D")
    txt(sl, ML + 0.6, 6.58, 5, 0.3, "We Drive with Standard and Commitment", size=13.5, color=WHITE, font=FM)
    notes(sl, "ปิดการอบรมด้วยคำถาม 3 ข้อที่หัวหน้าทุกระดับต้องถามได้ทุกวัน\n"
              "มอบหมาย: ภายใน 1 สัปดาห์ ให้แต่ละพื้นที่ตอบคำถาม Stabilize ใน SIM ของตัวเอง และนำผลมาทบทวนครั้งถัดไป")


SLIDES = [s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35,
          s36, s37, s38, s39, s40, s41, s42, s43, s44, s45]
