"""Cover, agenda and Part 00 (DMS Introduction) — slides 1-14."""
from dms_lib import *  # noqa: F401,F403

K0 = "Part 00 · Introduction"


def s01_cover(sl, n, T):
    rect(sl, 0, 0, W, H, grad=("0E1D52", "0C4D7C"), angle=315)
    # subtle diagonal light bands
    for i, a in enumerate((0.05, 0.035, 0.025)):
        b = rect(sl, 6.2 + i * 1.6, -1.5, 0.9, 10.5, fill=WHITE, alpha=a)
        b.rotation = 28
    txt(sl, ML, 1.35, 7, 0.3, "SAPPE FACTORY  ·  DMS TRAINING", size=12.5, color=MINT, font=FSB, spc=3)
    txt(sl, ML, 1.7, 6.8, 2.45, "Daily\nManagement\nSystem", size=54, color=WHITE, bold=True, ls=0.92)
    txt(sl, ML, 4.3, 6.6, 0.45, "DMS Introduction & 5 Components", size=21, color="C9D6FF", font=FM)
    txt(sl, ML, 4.8, 6.9, 0.7, "บริหารงานประจำวันให้ควบคุมได้ ตั้งแต่เป้าหมายโรงงานจนถึงหน้างานจริง",
        size=15, color="E4EAF7")
    rect(sl, ML, 5.83, 0.45, 0.04, fill="E5533D")
    txt(sl, ML + 0.6, 5.7, 5, 0.3, "We Drive with Standard and Commitment", size=13.5, color=WHITE, font=FM)

    x, y0, w, h, g = 7.75, 1.55, 4.93, 0.74, 0.14
    descs = ["เป้าหมายที่เชื่อมกันทุกระดับ", "ประชุมเพื่อตัดสินใจ ไม่ใช่รายงาน", "เห็นเร็ว ควบคุมได้ ส่งต่อถูกระดับ",
             "กำจัดสาเหตุ ไม่ให้เกิดซ้ำ", "ยืนยันมาตรฐานที่หน้างานจริง"]
    for i in range(5):
        c = COMP[i + 1]
        y = y0 + i * (h + g)
        rect(sl, x, y, w, h, fill=WHITE, alpha=0.08, line="FFFFFF", lw=0.5, r=0.12)
        icon_badge(sl, c["icon"], x + 0.16, y + 0.13, 0.48, c["c"], round_=False, r=0.1)
        txt(sl, x + 0.8, y + 0.1, 0.5, 0.3, f"{i + 1:02d}", size=12, color="9FB2E0", font=FSB)
        txt(sl, x + 1.2, y + 0.07, 3.6, 0.32, c["name"], size=15, color=WHITE, font=FSB)
        txt(sl, x + 1.2, y + 0.39, 3.6, 0.28, descs[i], size=11, color="B9C6E6")
    notes(sl, "เปิดการอบรม: DMS คือระบบบริหารงานประจำวันของ Sappe ประกอบด้วย 5 องค์ประกอบ\n"
              "ตั้งความคาดหวัง: จบการอบรมแล้วทุกคนต้องอธิบายได้ว่า DMS ทำงานอย่างไรในพื้นที่ของตัวเอง")


def s02_agenda(sl, n, T):
    background(sl)
    header(sl, "Agenda", "Training Roadmap", "ภาพรวมเนื้อหา 6 ส่วน · ใช้เวลาอบรมตามลำดับซ้ายไปขวา")
    items = [
        (None, "all_inclusive", "PART 00", "DMS Introduction",
         "DMS คืออะไร · วงจรการทำงาน · มาตรฐาน · SAPPE Infinite Loop", "Slides 03–14"),
        (1, None, "COMPONENT 01", None, "ถ่ายทอดเป้าหมายจากโรงงานสู่หน้างาน", "Slides 15–20"),
        (2, None, "COMPONENT 02", None, "SIM Cadence และการประชุมที่จบด้วยการตัดสินใจ", "Slides 21–26"),
        (3, None, "COMPONENT 03", None, "เห็นความผิดปกติเร็ว ควบคุม และส่งต่อถูกระดับ", "Slides 27–32"),
        (4, None, "COMPONENT 04", None, "กำจัดสาเหตุของปัญหาสำคัญและปัญหาซ้ำ", "Slides 33–38"),
        (5, None, "COMPONENT 05", None, "ยืนยันว่ามาตรฐานเกิดขึ้นจริงที่หน้างาน", "Slides 39–43"),
    ]
    cw, ch, gx, gy = 3.9, 2.38, 0.165, 0.2
    for i, (k, ic, lab, title, desc, rng) in enumerate(items):
        x = ML + (i % 3) * (cw + gx)
        y = 1.95 + (i // 3) * (ch + gy)
        if k is None:
            fill, fg, sub, accent, tc = NAVY, WHITE, "C9D6FF", MINT, WHITE
        else:
            c = COMP[k]
            fill, fg, sub, accent, tc = c["l"], NAVY, SLATE, c["c"], c["d"]
            ic, title = c["icon"], c["name"]
        rect(sl, x, y, cw, ch, fill=fill, r=0.16, sh=(k is None))
        icon(sl, ic, x + 0.28, y + 0.26, 0.42, accent)
        txt(sl, x + 0.28, y + 0.8, 3.3, 0.26, lab, size=11, color=tc if k else "AFC0E8", font=FSB, spc=1)
        txt(sl, x + 0.28, y + 1.06, 3.4, 0.38, title, size=17, color=fg, font=FSB)
        txt(sl, x + 0.28, y + 1.45, 3.4, 0.55, desc, size=12, color=sub)
        txt(sl, x + 0.28, y + ch - 0.42, 3.0, 0.26, rng, size=10, color=accent if k is None else tc,
            font=FSB)
    notes(sl, "เนื้อหาแบ่งเป็น Part 00 (หลักการ) และ 5 องค์ประกอบ แต่ละองค์ประกอบมีสีประจำ ใช้สีเดียวกันตลอดเอกสาร\n"
              "ปิดท้ายด้วย Summary และคำถามประจำวัน 3 ข้อ (Slides 44–45)")


def s03_why(sl, n, T):
    background(sl)
    header(sl, K0, "Why a Factory Needs DMS", "เป้าหมายของโรงงานไม่เท่ากับผลลัพธ์ที่เกิดขึ้นจริงเสมอไป")
    x, y, w, h = ML, 1.95, 6.0, 4.9
    card(sl, x, y, w, h)
    txt(sl, x + 0.35, y + 0.28, 5.3, 0.34, "Cost of Late Detection", size=16, color=NAVY, font=FSB)
    txt(sl, x + 0.35, y + 0.64, 5.3, 0.3, "จำนวนกะที่ปัญหาเดินต่อเนื่องก่อนถูกพบ (โรงงาน 3 กะ / วัน)",
        size=11.5, color=SLATE)
    rows = [("ภายในกะ", 1, GREEN), ("สิ้นวัน", 3, AMBER), ("สิ้นสัปดาห์", 21, ORANGE), ("สิ้นเดือน", 90, RED)]
    bx, bw_max = x + 1.55, 3.55
    for i, (lab, v, col) in enumerate(rows):
        yy = y + 1.25 + i * 0.72
        txt(sl, x + 0.35, yy, 1.2, 0.42, lab, size=13, color=INK, font=FSB, anchor="m")
        bw = max(0.18, bw_max * v / 90)
        rect(sl, bx, yy + 0.06, bw_max, 0.3, fill=BG, r=0.08)
        rect(sl, bx, yy + 0.06, bw, 0.3, fill=col, r=0.08)
        lx = bx + bw + 0.1 if bw < 2.6 else bx + bw - 0.75
        txt(sl, lx, yy, 0.7, 0.42, f"{v} กะ", size=13, color=col if bw < 2.6 else WHITE, font=FSB, anchor="m",
            align="l" if bw < 2.6 else "r")
    rect(sl, x + 0.35, y + 4.15, w - 0.7, 0.5, fill=RED_L, r=0.1,
         text=[[("×90  ", {"font": FSB, "color": RED, "size": 15}),
                ("พบช้า 1 เดือน = ปัญหาเดียวกันสะสมนาน 90 กะ ก่อนมีใครแก้", {"size": 12})]],
         color=INK, anchor="m", margin=0.14)

    rx = 7.0
    items = [("track_changes", BLUE, BLUE_L, "Target ≠ Actual",
              "เครื่องหยุด วัตถุดิบผิดปกติ หรืองานส่งต่อระหว่างกะไม่ครบ ทำให้ผลจริงหลุดเป้า"),
             ("schedule", ORANGE, ORANGE_L, "Late Detection",
              "ปัญหาเล็กสะสมเป็นของเสีย ชั่วโมงผลิตที่สูญหาย และความเสี่ยงคุณภาพ"),
             ("replay", RED, RED_L, "Firefighting Only", "แก้เฉพาะหน้าอย่างเดียว ปัญหาเดิมจึงกลับมาซ้ำ")]
    for i, (ic, c, l, t, d) in enumerate(items):
        yy = 1.95 + i * 1.12
        icon_badge(sl, ic, rx, yy + 0.04, 0.56, l, c, round_=False, r=0.12)
        txt(sl, rx + 0.75, yy, 4.9, 0.34, t, size=15, color=NAVY, font=FSB)
        txt(sl, rx + 0.75, yy + 0.35, 4.9, 0.65, d, size=12.5, color=SLATE)
    rect(sl, rx, 5.6, MR - rx, 1.25, fill=NAVY, r=0.14, sh=True)
    icon(sl, "visibility", rx + 0.3, 5.98, 0.48, MINT)
    txt(sl, rx + 0.98, 5.72, 4.55, 1.0, "DMS ทำให้เห็นช่องว่างระหว่างเป้าหมายกับผลจริงทุกวัน — ก่อนที่ความสูญเสียจะสะสม",
        size=15, color=WHITE, font=FSB, anchor="m")
    notes(sl, "ชี้ให้เห็นว่าปัญหาไม่ได้แพงเพราะตัวมันเอง แต่แพงเพราะพบช้า\n"
              "ตัวเลข 1/3/21/90 กะ คือระยะเวลาที่ปัญหาเดินต่อหากเราดูผลแค่สิ้นกะ สิ้นวัน สิ้นสัปดาห์ หรือสิ้นเดือน")


def s04_pillars(sl, n, T):
    background(sl)
    header(sl, K0, "Core Pillars of DMS", "สามสิ่งที่ทำให้เครื่องมือทั้ง 5 องค์ประกอบทำงานได้จริง")
    data = [
        (GREEN, GREEN_L, "forum", "PILLAR 1", "Information Flow", "สื่อสารความผิดปกติให้เร็วที่สุด ไม่รอสิ้นกะหรือสิ้นวัน",
         ["แจ้งทันทีเมื่อพบสิ่งผิดปกติ", "ใช้ข้อเท็จจริง ไม่ใช่ความรู้สึก", "ส่งต่อข้อมูลครบระหว่างกะ"], "Early · Fact-based · Visible"),
        (BLUE, BLUE_L, "groups", "PILLAR 2", "Responsibility at Each Level", "ความเป็นเจ้าของและความรับผิดชอบชัดเจนตามบทบาท",
         ["รู้ว่าเรื่องใดตัดสินใจเองได้", "รู้ว่าเรื่องใดต้องส่งต่อ", "ทุก Action มีเจ้าของ"], "Clear Owner · Clear Decision Right"),
        (RED, RED_L, "alarm", "PILLAR 3", "Behaviour · Drum Beat", "เดินตามจังหวะกลอง ทำเป็นกิจวัตร ตรงเวลา และสม่ำเสมอ",
         ["ประชุมตรงเวลา ตามวาระมาตรฐาน", "ติดตามงานค้างทุกรอบ", "ทำซ้ำจนเป็นนิสัยของทีม"], "Same Rhythm · Every Shift"),
    ]
    cw, gx = 3.9, 0.165
    for i, (c, l, ic, lab, t, d, pts, tag) in enumerate(data):
        x, y, h = ML + i * (cw + gx), 1.95, 4.9
        card(sl, x, y, cw, h)
        rect(sl, x, y, cw, 0.07, fill=c)
        icon_badge(sl, ic, x + 0.32, y + 0.35, 0.78, c, sh=True)
        txt(sl, x + 0.32, y + 1.3, 3.2, 0.28, lab, size=11.5, color=c, font=FSB, spc=2)
        txt(sl, x + 0.32, y + 1.58, 3.3, 0.42, t, size=16.5, color=NAVY, font=FSB)
        txt(sl, x + 0.32, y + 2.03, 3.3, 0.62, d, size=12.5, color=SLATE)
        for j, p in enumerate(pts):
            yy = y + 2.78 + j * 0.4
            icon(sl, "check_circle", x + 0.32, yy + 0.04, 0.24, c)
            txt(sl, x + 0.66, yy, 3.0, 0.32, p, size=12.5, color=INK)
        rect(sl, x + 0.32, y + h - 0.68, cw - 0.64, 0.44, fill=l, r=0.08, text=tag, size=11.5, color=c,
             font=FSB, anchor="m", margin=0.14)
    notes(sl, "เครื่องมือทั้ง 5 จะใช้ไม่ได้ถ้าขาด 3 เสาหลักนี้: ข้อมูลไหลเร็ว คนรู้บทบาท และทำสม่ำเสมอเป็นจังหวะ\n"
              "ถามผู้เรียน: ในพื้นที่ของเรา เสาไหนอ่อนที่สุดตอนนี้?")


def s05_traffic(sl, n, T):
    background(sl)
    header(sl, K0, "DMS as a Traffic System", "มีจุดหมายอย่างเดียวไม่พอ ต้องมีกฎ สัญญาณ ข้อมูล และระบบแจ้งเหตุด้วย")
    data = [("flag", "Destination", "Target & KPI", "จุดหมายที่ทุกระดับต้องไปให้ถึง"),
            ("menu_book", "Traffic Rules", "Standard Work", "วิธีทำงานที่ถูกต้องและเหมือนกันทุกกะ"),
            ("traffic", "Traffic Lights", "Green / Yellow / Red", "สถานะปกติและผิดปกติที่เห็นได้ทันที"),
            ("videocam", "Cameras & Data", "Actual Tracking", "ติดตามผลจริงตามรอบเวลา"),
            ("construction", "Incident & Road Repair", "Escalation & RCA", "แจ้งเหตุทันเวลา และแก้ที่สาเหตุเมื่อเกิดซ้ำ")]
    cw, gx = 2.27, 0.195
    for i, (ic, a, t, d) in enumerate(data):
        x, y, h = ML + i * (cw + gx), 1.95, 3.85
        card(sl, x, y, cw, h)
        icon_badge(sl, ic, x + 0.25, y + 0.3, 0.72, NAVY)
        txt(sl, x + 0.25, y + 1.18, cw - 0.4, 0.32, a, size=11.5, color=SLATE, font=FM)
        icon(sl, "south", x + 0.25, y + 1.52, 0.26, "9AA8C7")
        txt(sl, x + 0.25, y + 1.88, cw - 0.4, 0.7, t, size=16, color=GREEN, font=FSB)
        txt(sl, x + 0.25, y + 2.62, cw - 0.4, 0.9, d, size=12, color=SLATE)
    y = 6.0
    rect(sl, ML, y, CW, 0.82, fill=NAVY, r=0.14, sh=True)
    txt(sl, ML + 0.25, y, 1.0, 0.82, "DMS =", size=17, color=WHITE, font=FSB, anchor="m")
    parts = [("groups", "คน"), ("rule", "มาตรฐาน"), ("database", "ข้อมูล"), ("gavel", "การตัดสินใจ")]
    px, pw = ML + 1.35, 2.42
    for i, (ic, t) in enumerate(parts):
        xx = px + i * (pw + 0.28)
        rect(sl, xx, y + 0.16, pw, 0.5, fill="22397A", r=0.08)
        icon(sl, ic, xx + 0.6, y + 0.27, 0.28, MINT)
        txt(sl, xx + 0.98, y + 0.16, 1.4, 0.5, t, size=14, color=WHITE, font=FSB, anchor="m")
        if i < 3:
            txt(sl, xx + pw, y + 0.16, 0.28, 0.5, "+", size=16, color=MINT, font=FSB, align="c", anchor="m")
    notes(sl, "อุปมาระบบจราจร: เป้าหมายคือจุดหมาย มาตรฐานคือกฎจราจร สี G/Y/R คือไฟจราจร\n"
              "ข้อมูลจริงคือกล้อง และ Escalation/RCA คือระบบแจ้งเหตุและซ่อมถนน — ขาดอย่างใดอย่างหนึ่งรถก็ติด")


def s06_isnot(sl, n, T):
    background(sl)
    header(sl, K0, "What DMS Is — and Is Not", "แยกให้ชัดตั้งแต่ต้น เพื่อไม่ให้ DMS กลายเป็นงานเอกสาร")
    y, h, w = 1.95, 4.2, 5.95
    rect(sl, ML, y, w, h, grad=("0B7A5D", "11906F"), angle=315, r=0.18, sh=True)
    icon(sl, "check_circle", ML + 0.4, y + 0.38, 0.46, WHITE)
    txt(sl, ML + 1.0, y + 0.34, 4, 0.52, "DMS Is", size=22, color=WHITE, font=FSB, anchor="m")
    is_ = ["ระบบควบคุมและปรับปรุงงานประจำวันจากข้อเท็จจริง",
           "มาตรฐาน → ติดตาม → พบความผิดปกติ → ตอบสนอง → ติดตามจนปิด",
           "ทุกเรื่องมีเจ้าของ มีกำหนดเวลา และมีหลักฐานการปิด",
           "แก้ที่สาเหตุ แล้วอัปเดตมาตรฐานให้ทุกกะทำเหมือนกัน"]
    for i, t in enumerate(is_):
        yy = y + 1.15 + i * 0.72
        icon(sl, "check", ML + 0.42, yy + 0.04, 0.26, MINT)
        txt(sl, ML + 0.85, yy, 4.8, 0.66, t, size=13.5, color=WHITE)
    x2 = ML + w + 0.22
    rect(sl, x2, y, w, h, fill=RED_L, r=0.18)
    icon(sl, "cancel", x2 + 0.4, y + 0.38, 0.46, RED)
    txt(sl, x2 + 1.0, y + 0.34, 4, 0.52, "DMS Is Not", size=22, color=RED_D, font=FSB, anchor="m")
    nots = ["การประชุมเพื่อรายงานผลย้อนหลัง", "การทำ Dashboard หรือบอร์ดให้ดูดี",
            "การตรวจเอกสารให้ครบขั้นตอน หรือเพิ่มจำนวนประชุม", "การตรวจเพื่อหาคนผิด"]
    for i, t in enumerate(nots):
        yy = y + 1.15 + i * 0.72
        icon(sl, "close", x2 + 0.42, yy + 0.04, 0.26, RED)
        txt(sl, x2 + 0.85, yy, 4.8, 0.66, t, size=13.5, color=INK)
    yy = 6.35
    txt(sl, ML, yy, 1.4, 0.4, "Success =", size=15, color=NAVY, font=FSB, anchor="m")
    cx = ML + 1.4
    for t, bg, fg in (("รักษามาตรฐาน", GREEN_L, GREEN_D), ("ตอบสนองต่อปัญหา", BLUE_L, BLUE_D),
                      ("ลดการเกิดซ้ำ", ORANGE_L, ORANGE_D)):
        cx += chip(sl, cx, yy + 0.02, t, bg, fg, size=12.5, h=0.38, pad=0.18) + 0.12
    notes(sl, "เน้นฝั่งขวา: ถ้าทีมเริ่มใช้ DMS เป็นการรายงานหรือหาคนผิด ระบบจะตาย\n"
              "ความสำเร็จวัดจาก 3 อย่าง: รักษามาตรฐานได้ ตอบสนองทันเวลา และปัญหาเดิมไม่กลับมา")


def s07_cycle(sl, n, T):
    background(sl)
    header(sl, K0, "The DMS Control Cycle", "วงจรต่อเนื่องที่หมุนทุกกะ จนการแก้ไขกลายเป็นวิธีทำงานปกติ")
    data = [("rule", GREEN, "Set Standard & Target", "กำหนดวิธีทำงาน ค่าควบคุม และเป้าหมาย", "SOP · WI · Target"),
            ("monitoring", "0F7C80", "Run & Track", "ทำงานตามมาตรฐาน บันทึกผลจริงตามรอบ", "Record · KPI"),
            ("error", ORANGE, "Detect Deviation", "เห็นความเบี่ยงเบนจากมาตรฐานทันเวลา", "Red / Yellow"),
            ("shield", RED, "Contain & Escalate", "ควบคุมผลกระทบ ส่งต่อเมื่อเกินอำนาจ", "Contain · Escalate"),
            ("published_with_changes", BLUE, "Fix & Standardize", "แก้สาเหตุ ปรับมาตรฐาน ตรวจผลต่อเนื่อง", "New Standard")]
    cw, gx = 2.12, 0.35
    y, h = 1.95, 3.3
    for i, (ic, c, t, d, tag) in enumerate(data):
        x = ML + i * (cw + gx)
        card(sl, x, y, cw, h)
        rect(sl, x, y, cw, 0.07, fill=c)
        icon_badge(sl, ic, x + 0.22, y + 0.3, 0.66, c)
        txt(sl, x + 0.22, y + 0.03 + 1.05, 0.5, 0.3, f"0{i + 1}", size=11, color=c, font=FSB)
        txt(sl, x + 0.22, y + 1.32, cw - 0.35, 0.62, t, size=15, color=NAVY, font=FSB)
        txt(sl, x + 0.22, y + 1.95, cw - 0.35, 0.75, d, size=12, color=SLATE)
        chip(sl, x + 0.22, y + h - 0.5, tag, BG, NAVY, size=10.5, h=0.32)
        if i < 4:
            icon_c(sl, "arrow_forward", x + cw + gx / 2, y + h / 2, 0.26, "9AA8C7")
    # return loop
    x1 = ML + cw / 2
    x2 = ML + 4 * (cw + gx) + cw / 2
    yb = y + h + 0.45
    line(sl, x2, y + h + 0.05, x2, yb, "9AA8C7", 1.5, dash=True)
    line(sl, x2, yb, x1, yb, "9AA8C7", 1.5, dash=True)
    line(sl, x1, yb, x1, y + h + 0.08, "9AA8C7", 1.5, dash=True, arrow=True)
    rect(sl, 3.9, yb - 0.24, 5.55, 0.48, fill=WHITE, line=LINE, r=0.24,
         text=[[("มาตรฐานใหม่กลับเป็นจุดเริ่มต้นของรอบถัดไป", {})]], size=13, color=NAVY, font=FSB, align="c",
         anchor="m")
    icon(sl, "autorenew", 4.08, yb - 0.14, 0.28, GREEN)
    # cadence strip
    y3 = 6.25
    rect(sl, ML, y3, CW, 0.6, fill=BG, r=0.1)
    txt(sl, ML + 0.25, y3, 2.2, 0.6, "รอบการหมุน", size=12.5, color=NAVY, font=FSB, anchor="m")
    for i, t in enumerate(["ทุกกะ: Run · Detect · Contain", "ทุกวัน: ทบทวน KPI และ Action ใน SIM",
                           "เมื่อเข้าเกณฑ์: RCA → New Standard"]):
        txt(sl, ML + 2.1 + i * 3.4, y3, 3.3, 0.6, t, size=12, color=SLATE, anchor="m")
    notes(sl, "อธิบายทีละขั้น และย้ำว่าขั้นสุดท้ายไม่ใช่ 'แก้เสร็จ' แต่คือ 'มาตรฐานใหม่' ที่ทุกกะใช้\n"
              "ถ้าไม่ปิดวงด้วยมาตรฐานใหม่ ปัญหาเดิมจะกลับมาในกะถัดไป")


def s08_standards(sl, n, T):
    background(sl)
    header(sl, K0, "Standards: The Foundation of DMS", "ถ้าไม่ชัดว่าอะไรคือ “ปกติ” ก็จะไม่เห็นว่าอะไรคือ “ผิดปกติ”")
    data = [(NAVY, "HOW", "description", "SOP / WI / Standard Work", "วิธีปฏิบัติที่ถูกต้องและเหมือนกันทุกคน ทุกกะ",
             ["Step", "Key Point", "Photo"]),
            (GREEN, "WHAT", "tune", "Control Point", "ค่าหรือเงื่อนไขที่ต้องควบคุม เช่น อุณหภูมิ ความดัน ความสมบูรณ์ของซีล",
             ["Temp", "Pressure", "Seal"]),
            (ORANGE, "IF ABNORMAL", "emergency_home", "Reaction Plan",
             "สิ่งที่ต้องทำเมื่อผลตรวจไม่ผ่าน: หยุด แจ้ง แยก หรือเพิ่มการตรวจ", ["Stop", "Notify", "Segregate"]),
            (INDIGO, "LEADERS", "badge", "Leader Standard Work", "กิจกรรมบริหารประจำ: ทบทวน KPI ติดตามงานค้าง ลงตรวจหน้างาน",
             ["KPI Review", "Gemba", "Confirm"])]
    cw, gx = 2.9, 0.177
    y, h = 1.95, 3.95
    for i, (c, lab, ic, t, d, tags) in enumerate(data):
        x = ML + i * (cw + gx)
        card(sl, x, y, cw, h)
        rect(sl, x, y, cw, 0.66, fill=c, r=0.14)
        rect(sl, x, y + 0.4, cw, 0.26, fill=c)
        txt(sl, x + 0.22, y, 2.1, 0.66, lab, size=12.5, color=WHITE, font=FSB, spc=2, anchor="m")
        icon(sl, ic, x + cw - 0.55, y + 0.17, 0.32, WHITE)
        txt(sl, x + 0.22, y + 0.85, cw - 0.4, 0.42, t, size=15.5, color=NAVY, font=FSB)
        txt(sl, x + 0.22, y + 1.3, cw - 0.4, 1.2, d, size=12.5, color=SLATE)
        chips(sl, x + 0.22, y + h - 0.88, tags, BG, NAVY, size=10.5, h=0.32, max_x=x + cw - 0.15)
    y2 = 6.1
    rect(sl, ML, y2, CW, 0.75, fill=NAVY, r=0.14, sh=True)
    txt(sl, ML + 0.3, y2, 2.2, 0.75, "Good Standard", size=16, color=WHITE, font=FSB, anchor="m")
    for i, (ic, t) in enumerate([("visibility", "มองเห็นได้"), ("front_hand", "ทำได้จริง"),
                                 ("straighten", "วัดได้ชัด"), ("verified", "ตรวจยืนยันได้")]):
        xx = ML + 2.7 + i * 2.35
        icon(sl, ic, xx, y2 + 0.23, 0.3, MINT)
        txt(sl, xx + 0.4, y2, 1.9, 0.75, t, size=14, color=WHITE, font=FSB, anchor="m")
    notes(sl, "มาตรฐานมี 4 ชั้น: วิธีทำ (HOW) ค่าที่ต้องคุม (WHAT) สิ่งที่ทำเมื่อผิดปกติ (Reaction Plan) และงานประจำของหัวหน้า\n"
              "มาตรฐานที่ดีต้องผ่าน 4 เกณฑ์ด้านล่าง ถ้าตรวจยืนยันไม่ได้ ก็ทำ Process Confirmation ไม่ได้")


def s09_loop(sl, n, T):
    background(sl)
    header(sl, K0, "SAPPE Infinite Loop")
    cx = ML + CW - 2 * 2.05
    chip(sl, 8.4, 0.82, "Stabilize · S1–S6", GREEN, WHITE, size=12, h=0.4, pad=0.18, r=0.1)
    chip(sl, 10.45, 0.82, "Elevate · E1–E6", BLUE, WHITE, size=12, h=0.4, pad=0.18, r=0.1)
    r, cy = 1.5, 3.86
    lcx, rcx = W / 2 - r, W / 2 + r
    # soft fills
    circle(sl, lcx, cy, 2 * r - 0.3, fill=GREEN_L)
    circle(sl, rcx, cy, 2 * r - 0.3, fill=BLUE_L)
    circle(sl, lcx, cy, 2 * r, line=GREEN, lw=19)
    arc(sl, rcx, cy, r, 180, 0, BLUE, 19)
    arc(sl, rcx, cy, r, 0, 180, "EA6A1F", 19)
    # direction arrows
    for th in (90, 180, 270):
        ax, ay = polar(lcx, cy, r, th)
        t = rect(sl, ax - 0.09, ay - 0.08, 0.18, 0.16, fill=WHITE, shape=MSO_SHAPE.ISOSCELES_TRIANGLE)
        t.rotation = th + 180
    for th in (90, 0, 270):
        ax, ay = polar(rcx, cy, r, th)
        t = rect(sl, ax - 0.09, ay - 0.08, 0.18, 0.16, fill=WHITE, shape=MSO_SHAPE.ISOSCELES_TRIANGLE)
        t.rotation = th
    txt(sl, lcx - 1.0, cy - 0.6, 2.0, 0.48, "Stabilize", size=24, color=GREEN, bold=True, align="c")
    txt(sl, lcx - 1.0, cy - 0.12, 2.0, 0.34, "รักษามาตรฐาน", size=14, color=GREEN_D, font=FSB, align="c")
    txt(sl, lcx - 1.0, cy + 0.24, 2.0, 0.3, "S1–S6 · ทุกกะ / ทุกวัน", size=11, color=SLATE, align="c")
    txt(sl, rcx - 1.0, cy - 0.6, 2.0, 0.48, "Elevate", size=24, color=BLUE, bold=True, align="c")
    txt(sl, rcx - 1.0, cy - 0.12, 2.0, 0.34, "ยกระดับมาตรฐาน", size=14, color=BLUE_D, font=FSB, align="c")
    txt(sl, rcx - 1.0, cy + 0.24, 2.0, 0.3, "E1–E6 · ทำเป็นโครงการ", size=11, color=SLATE, align="c")
    # node N
    circle(sl, W / 2, cy, 1.15, fill="F7D9D2", alpha=0.7)
    circle(sl, W / 2, cy, 0.86, grad=("E5533D", "B32A17"), angle=315, line=WHITE, lw=3, sh=True,
           text="N", size=28, color=WHITE, bold=True, align="c", anchor="m")
    S = [(55, "S1", "Confirm Basic Condition", "ยืนยันสภาพพื้นฐาน"),
         (125, "S2", "Deploy KPI & Ownership", "วาง KPI และผู้รับผิดชอบ"),
         (163, "S3", "Run Daily Performance Dialogue", "เวทีทบทวนประจำกะ / วัน"),
         (197, "S4", "Read Real-Time Variation", "อ่านความผันผวนจริง"),
         (235, "S5", "Eliminate Bad Days", "กำจัดวันหลุดเป้า"),
         (305, "S6", "Update & Confirm Standard", "อัปเดต / ยืนยันมาตรฐาน")]
    E = [(125, "E1", "Align to Loss Tree", "เชื่อม Loss Tree / นโยบาย", BLUE),
         (55, "E2", "Identify & Screen", "ค้นหาและคัดกรองโอกาส", "EA6A1F"),
         (17, "E3", "Define Project & Charter", "นิยามโครงการ / Charter", "EA6A1F"),
         (343, "E4", "Prioritize by Value & Class", "จัดลำดับตามมูลค่า A/B/C", "EA6A1F"),
         (305, "E5", "Select Method & Plan", "เลือกวิธีและวางแผน", BLUE),
         (235, "E6", "Manage Pipeline", "บริหารพอร์ตโครงการ", BLUE)]

    def node(ccx, th, code, en, th_, col, tcol):
        nx, ny = polar(ccx, cy, r, th)
        circle(sl, nx, ny, 0.56, fill=col, line=WHITE, lw=2.5, sh=True, text=code, size=13, color=WHITE,
               font=FSB, align="c", anchor="m", margin=0)
        dx = math.cos(math.radians(th))
        dy = math.sin(math.radians(th))
        lw_ = 1.7 if abs(dy) > 0.75 else 2.25
        if abs(dy) > 0.75:          # top / bottom labels, pushed away from the centre node
            shift = 0.3 if nx > W / 2 else -0.3
            lx, ly, al = nx - lw_ / 2 + shift, (ny + 0.34 if dy > 0 else ny - 0.98), "c"
        elif dx < 0:                # left side
            lx, ly, al = nx - 0.36 - lw_, ny - 0.3, "r"
        else:
            lx, ly, al = nx + 0.36, ny - 0.3, "l"
        txt(sl, lx, ly, lw_, 0.62, [[(en, {"font": FSB, "color": tcol, "size": 11})],
                                    [(th_, {"size": 10, "color": SLATE})]], align=al, anchor="b" if dy < -0.75 else "t")

    for th, code, en, th_ in S:
        node(lcx, th, code, en, th_, GREEN, GREEN_D)
    for th, code, en, th_, col in E:
        node(rcx, th, code, en, th_, col, BLUE_D if col == BLUE else ORANGE_D)
    # bottom legend
    y, h = 6.18, 0.72
    w3 = CW / 3
    for i, (ic, c, l, t, d) in enumerate([("bar_chart", GREEN, GREEN_L, "Stabilize", "วันนี้ทำได้ตามมาตรฐานหรือยัง?"),
                                          ("hub", RED, RED_L, "Node · Standard & Replication",
                                           "B1: S6 → N → E1  ·  B2: E6 → N → S1"),
                                          ("ads_click", BLUE, BLUE_L, "Elevate", "ยกระดับมาตรฐานเรื่องใด ด้วยโครงการใด?")]):
        x = ML + i * w3
        rect(sl, x, y, w3, h, fill=l, r=0.12 if i != 1 else None)
        icon_badge(sl, ic, x + 0.2, y + 0.17, 0.44, c)
        txt(sl, x + 0.78, y + 0.08, w3 - 0.9, 0.3, t, size=12.5, color=c if i else GREEN_D, font=FSB)
        txt(sl, x + 0.78, y + 0.38, w3 - 0.9, 0.36, d, size=11.5, color=INK)
    notes(sl, "วงซ้าย Stabilize คือ DMS ประจำวัน (S1–S6) วงขวา Elevate คือการยกระดับด้วยโครงการ (E1–E6)\n"
              "Node N คือจุดส่งต่อ: B1 ปัญหาที่วงซ้ายแก้ไม่ได้ส่งไปเป็นโครงการ, B2 มาตรฐานใหม่จากโครงการกลับมาที่ S1")


def s10_modes(sl, n, T):
    background(sl)
    header(sl, K0, "Three Modes of Work in the Loop", "ทั้งสามเชื่อมกัน แต่ใช้วิธีและจังหวะเวลาต่างกัน")
    data = [(GREEN, GREEN_L, "Stabilize · S1–S6", "calendar_month", "Daily Management", "ควบคุมสภาพปกติ แก้ความผิดปกติประจำวัน",
             "CIL ไม่ครบ → ทำให้ครบก่อนเริ่มกะ", "ทุกกะ / ทุกวัน", "หน้างาน / พื้นที่"),
            (RED, RED_L, "Node · N", "hub", "Structured Problem Solving",
             "จัดการปัญหาสำคัญหรือปัญหาซ้ำด้วย RCA / BDA แล้วยืนยันเป็นมาตรฐาน", "เครื่องหยุดอาการเดิมซ้ำ → เปิด RCA",
             "ตามเกณฑ์ที่กำหนด", "เจ้าของปัญหา / ทีม RCA"),
            (BLUE, BLUE_L, "Elevate · E1–E6", "rocket_launch", "Improvement Project", "เปลี่ยนความสามารถของกระบวนการอย่างมีนัยสำคัญ",
             "ลด Changeover Loss ทั้งไลน์ → FI Project", "เป็นโครงการ", "FI Pillar / ทีมโครงการ")]
    cw, gx = 3.62, 0.57
    y, h = 1.95, 4.35
    for i, (c, l, tag, ic, t, d, ex, cad, own) in enumerate(data):
        x = ML + i * (cw + gx)
        rect(sl, x, y, cw, h, fill=l, r=0.18)
        chip(sl, x + 0.28, y + 0.28, tag, c, WHITE, size=11, h=0.34, pad=0.14)
        icon(sl, ic, x + cw - 0.65, y + 0.26, 0.38, c)
        txt(sl, x + 0.28, y + 0.8, cw - 0.4, 0.42, t, size=16.5, color=NAVY, font=FSB)
        txt(sl, x + 0.28, y + 1.25, cw - 0.5, 0.9, d, size=12.5, color=SLATE)
        rect(sl, x + 0.28, y + 2.2, cw - 0.56, 0.95, fill=WHITE, r=0.1,
             text=[[("Example", {"font": FSB, "size": 11, "color": SLATE})], [(ex, {"size": 12.5})]],
             color=INK, margin=0.14, anchor="m")
        for j, (k, v) in enumerate((("Cadence", cad), ("Owner", own))):
            txt(sl, x + 0.28, y + 3.42 + j * 0.38, cw - 0.4, 0.34, [[(k + ":  ", {"font": FSB, "color": NAVY}),
                                                                       (v, {"color": INK})]], size=12.5)
        if i < 2:
            ax = x + cw + gx / 2
            icon_c(sl, "arrow_forward" if i == 0 else "sync_alt", ax, y + h / 2 - 0.12, 0.34, c if i == 0 else BLUE)
            txt(sl, ax - 0.3, y + h / 2 + 0.1, 0.6, 0.3, "B1" if i == 0 else "B2", size=12, color=GREEN if i == 0 else BLUE,
                font=FSB, align="c")
    y2 = 6.45
    icon(sl, "keyboard_return", ML, y2 + 0.04, 0.32, RED)
    txt(sl, ML + 0.45, y2, 11.5, 0.4, "มาตรฐานใหม่จาก RCA หรือโครงการ กลับมาที่ S1 ผ่าน B2 Handover — DMS ติดตามต่อ",
        size=14, color=NAVY, font=FSB, anchor="m")
    notes(sl, "ใช้ตัวอย่างแยกให้เห็นว่าเรื่องไหนจบใน DMS ประจำวัน เรื่องไหนต้องเปิด RCA และเรื่องไหนต้องเป็นโครงการ\n"
              "ความผิดพลาดที่พบบ่อย: เอาปัญหาระดับโครงการมาแก้ในประชุม SIM ทุกวันจนประชุมยืดเยื้อ")


def s11_components(sl, n, T):
    background(sl)
    header(sl, K0, "The 5 Components of DMS", "ระบบเดียว ห้าองค์ประกอบ — ทุกองค์ประกอบตอบคำถามสำคัญหนึ่งข้อ")
    y0 = 1.9
    roof = rect(sl, ML, y0, CW, 0.55, fill=NAVY, r=0.1,
                text="Stable Operation  ·  ผลลัพธ์คงที่ทุกวัน", size=15, color=WHITE, font=FSB, align="c", anchor="m")
    qs = ["เป้าหมายของเรา\nคืออะไร?", "วันนี้ต้องตัดสินใจ\nเรื่องอะไร?", "อะไรผิดไปจาก\nมาตรฐาน?", "ทำไมปัญหาจึง\nเกิดซ้ำ?",
          "มาตรฐานถูกทำ\nจริงหรือไม่?"]
    ds = ["เป้าหมายที่เชื่อมกันทุกระดับ", "ประชุมตามหน้าที่และช่วงเวลา", "เห็นปัญหาและส่งต่อทันเวลา", "กำจัดสาเหตุของปัญหาสำคัญหรือปัญหาซ้ำ",
          "ยืนยันว่ามาตรฐานเกิดขึ้นจริงที่หน้างาน"]
    cw, gx = 2.27, 0.195
    y, h = y0 + 0.68, 3.6
    for i in range(5):
        c = COMP[i + 1]
        x = ML + i * (cw + gx)
        rect(sl, x, y, cw, h, grad=(c["c"], c["d"]), angle=270, r=0.14, sh=True)
        icon(sl, c["icon"], x + 0.22, y + 0.25, 0.44, WHITE)
        txt(sl, x + 0.22, y + 0.82, 1, 0.3, f"0{i + 1}", size=12, color=WHITE, font=FSB, alpha=0.75)
        txt(sl, x + 0.22, y + 1.08, cw - 0.35, 0.65, c["name"], size=15.5, color=WHITE, font=FSB)
        txt(sl, x + 0.22, y + 1.75, cw - 0.35, 0.7, ds[i], size=12, color=WHITE, alpha=0.9)
        rect(sl, x + 0.18, y + h - 0.95, cw - 0.36, 0.78, fill=WHITE, alpha=0.16, r=0.1)
        icon(sl, "help", x + 0.3, y + h - 0.82, 0.22, WHITE)
        txt(sl, x + 0.6, y + h - 0.9, cw - 0.8, 0.7, qs[i], size=12, color=WHITE, font=FSB, anchor="m")
    rect(sl, ML, y + h + 0.13, CW, 0.55, fill="DEE4F2", r=0.1,
         text="Foundation  ·  SOP / WI  ·  Control Point  ·  Reaction Plan  ·  Leader Standard Work", size=13.5,
         color=NAVY, font=FSB, align="c", anchor="m")
    notes(sl, "ภาพบ้าน: หลังคาคือผลลัพธ์คงที่ เสา 5 ต้นคือองค์ประกอบ ฐานคือมาตรฐาน\n"
              "ให้ผู้เรียนจำคำถามประจำแต่ละองค์ประกอบ — เป็นคำถามที่หัวหน้าต้องถามได้ทุกวัน")


def s12_on_loop(sl, n, T):
    background(sl)
    header(sl, "Part 00 · Stabilize Loop", "5 Components on the Stabilize Loop",
           "DMS คือเครื่องยนต์ที่หมุนวง S1–S6 ทุกกะ ทุกวัน", kc=GREEN)
    data = [("S1", "Confirm Basic Condition & Standard", "ยืนยันสภาพพื้นฐานและมาตรฐาน", [5]),
            ("S2", "Deploy KPI Cascade & Ownership", "วาง KPI และผู้รับผิดชอบ", [1]),
            ("S3", "Run Daily Performance Dialogue", "เวทีทบทวนประจำกะ / วัน", [2]),
            ("S4", "Read Real-Time Variation", "อ่านความผันผวนจริง", [3]),
            ("S5", "Eliminate Bad Days", "กำจัดวันหลุดเป้า", [3, 4]),
            ("S6", "Update & Confirm Standard", "อัปเดตและยืนยันมาตรฐาน → ส่งต่อ Node", [4, 5])]
    short = {1: "01 KPI Cascade", 2: "02 Purposeful Meeting (SIM)", 3: "03 Deviation & Escalation",
             4: "04 RCA", 5: "05 Process Confirmation"}
    cw, ch, gx, gy = 3.9, 1.95, 0.165, 0.18
    for i, (code, t, d, cs) in enumerate(data):
        x = ML + (i % 3) * (cw + gx)
        y = 1.95 + (i // 3) * (ch + gy)
        card(sl, x, y, cw, ch)
        circle(sl, x + 0.55, y + 0.55, 0.66, fill=WHITE, line=GREEN, lw=2.5, text=code, size=14, color=GREEN,
               font=FSB, align="c", anchor="m", margin=0)
        txt(sl, x + 1.02, y + 0.25, cw - 1.15, 0.62, t, size=14, color=NAVY, font=FSB, anchor="m")
        txt(sl, x + 0.25, y + 0.98, cw - 0.4, 0.35, d, size=12.5, color=SLATE)
        cx = x + 0.25
        for k in cs:
            cx += chip(sl, cx, y + ch - 0.48, short[k], COMP[k]["l"], COMP[k]["d"], size=10.5, h=0.32) + 0.08
    # coverage matrix strip
    y = 6.2
    rect(sl, ML, y, CW, 0.65, fill=BG, r=0.1)
    txt(sl, ML + 0.22, y, 1.9, 0.65, "Coverage", size=12.5, color=NAVY, font=FSB, anchor="m")
    cov = [(1, "S2"), (2, "S3"), (3, "S4 · S5"), (4, "S5 · S6"), (5, "S1 · S6")]
    for i, (k, s) in enumerate(cov):
        xx = ML + 1.55 + i * 2.12
        circle(sl, xx + 0.12, y + 0.325, 0.2, fill=COMP[k]["c"])
        txt(sl, xx + 0.3, y, 1.8, 0.65, [[(f"0{k} ", {"font": FSB, "color": COMP[k]["d"]}), ("→ " + s, {})]],
            size=12, color=INK, anchor="m")
    notes(sl, "แต่ละขั้นของวง Stabilize ใช้องค์ประกอบใดเป็นเครื่องมือหลัก\n"
              "ถ้าองค์ประกอบใดหายไป วงจะหยุดหมุนที่ขั้นนั้น — ใช้เป็น checklist วินิจฉัยพื้นที่ได้")


def s13_e2e(sl, n, T):
    background(sl)
    header(sl, K0, "End-to-End Example: Seal Defect", "กรณีสมมติ: ซีลซองไม่สมบูรณ์สูงกว่าเป้าหมายในสายบรรจุ")
    data = [(GREEN, "sensors", "1 · Signal", "KPI Cascade", "KPI ระดับไลน์แสดง Defect ซีลสูงกว่าเป้า", "KPI ขึ้นสีแดง"),
            (ORANGE, "emergency_home", "2 · Respond", "Deviation & Escalation",
             "ทำตาม Reaction Plan ควบคุมผลิตภัณฑ์ แจ้ง และยกระดับตามเกณฑ์", "สินค้าถูกควบคุม · แจ้งแล้ว"),
            (BLUE, "groups", "3 · Review", "Purposeful Meeting", "SIM ติดตามผลกระทบ สถานะการควบคุม และผู้รับผิดชอบ",
             "มี Owner + Due"),
            (RED, "troubleshoot", "4 · Solve", "RCA Management", "เกิดซ้ำหรือเข้าเกณฑ์ → วิเคราะห์สาเหตุ กำหนดมาตรการถาวร",
             "Root Cause + มาตรการถาวร"),
            (INDIGO, "fact_check", "5 · Sustain", "Process Confirmation", "หัวหน้างานยืนยันมาตรฐานใหม่ที่หน้างาน",
             "PC ผ่าน · ไม่เกิดซ้ำ")]
    cw, gx = 2.27, 0.195
    y = 1.95
    line(sl, ML + 0.4, y + 0.62, MR - 0.4, y + 0.62, LINE, 2)
    for i, (c, ic, t, comp, d, out) in enumerate(data):
        x = ML + i * (cw + gx)
        rect(sl, x, y, cw, 0.07, fill=c, r=0.03)
        icon_badge(sl, ic, x + cw / 2 - 0.36, y + 0.26, 0.72, c, round_=False, r=0.14, sh=True)
        txt(sl, x, y + 1.12, cw, 0.4, t, size=17, color=NAVY, font=FSB, align="c")
        txt(sl, x, y + 1.5, cw, 0.3, comp, size=12, color=c, font=FSB, align="c")
        txt(sl, x + 0.1, y + 1.88, cw - 0.2, 1.3, d, size=12.5, color=SLATE, align="c")
        card(sl, x, 4.95, cw, 1.22, fill=WHITE)
        rect(sl, x, 4.95, cw, 0.36, fill=c, alpha=0.12, r=0.14)
        txt(sl, x, 4.95, cw, 0.36, "OUTPUT", size=10, color=c, font=FSB, align="c", anchor="m", spc=2)
        txt(sl, x + 0.12, 5.35, cw - 0.24, 0.76, out, size=13, color=NAVY, font=FSB, align="c", anchor="m")
        if i < 4:
            icon_c(sl, "chevron_right", x + cw + gx / 2, 5.56, 0.26, "9AA8C7")
    txt(sl, ML, 6.42, CW, 0.32, "ตัวอย่างสมมติเพื่อการอบรม — ลำดับการทำงานของ 5 องค์ประกอบต่อปัญหาเดียว", size=11,
        color=MUTED, align="c", anchor="m")
    notes(sl, "เล่าเป็นเรื่องเดียวตั้งแต่ KPI แดงจนถึงมาตรฐานใหม่ถูกยืนยัน\n"
              "ถามผู้เรียน: ในเหตุการณ์จริงล่าสุดของพื้นที่ เราหยุดอยู่ที่ขั้นไหน?")


def s14_cycles(sl, n, T):
    background(sl)
    header(sl, K0, "DMS Improvement Cycles")
    rect(sl, 8.95, 0.78, 3.73, 0.5, fill=NAVY, r=0.25,
         text=[[("Target Condition:  ", {"color": WHITE, "font": FSB}), ("No Deviation", {"color": "FF9C85", "font": FSB})]],
         size=13.5, align="c", anchor="m")
    cx, bw = 6.67, 3.3
    bx = cx - bw / 2
    # lane headers
    rect(sl, 0.85, 1.6, 3.15, 0.55, fill=RED, r=0.08,
         text=[[("Reactive Improvement Cycle", {"font": FSB, "size": 12.5})], [("ตอบสนองเมื่อพบ Deviation", {"size": 10.5})]],
         color=WHITE, anchor="m", margin=0.14)
    rect(sl, 9.35, 1.6, 3.15, 0.55, fill=GREEN, r=0.08,
         text=[[("Active Improvement Cycle", {"font": FSB, "size": 12.5})], [("ป้องกันก่อนปัญหาเกิด", {"size": 10.5})]],
         color=WHITE, anchor="m", margin=0.14)

    def box(x, y, w, h, t, s, fill, fg, line_=None, sub=SLATE):
        return rect(sl, x, y, w, h, fill=fill, line=line_, lw=1.25, r=0.08,
                    text=[[(t, {"font": FSB, "size": 12.5, "color": fg})], [(s, {"size": 10.5, "color": sub})]],
                    align="c", anchor="m", margin=0.06)

    box(bx - 0.25, 1.48, bw + 0.5, 0.72, "Specifications", "People Safety · Food Safety · Compliance · Product Specs", NAVY, WHITE,
        sub="C9D6FF")
    box(bx, 2.42, bw, 0.55, "Standards & Monitoring Plan", "WI · OPL · Visuals", BLUE, WHITE, sub="DCE8FF")
    box(bx, 3.22, bw, 0.55, "Shop Floor Sticks to Standard", "ทำงานตาม WI · OPL · Visuals", BLUE_L, NAVY, BLUE)
    box(bx, 4.02, bw, 0.55, "Deviation Observed", "Safety · Quality · Process", ORANGE_L, NAVY, ORANGE)
    d = rect(sl, cx - 1.05, 4.8, 2.1, 0.92, fill=WHITE, line=ORANGE, lw=1.5, shape=MSO_SHAPE.DIAMOND,
             text="Action defined\nin Standard?", size=11, color=NAVY, font=FSB, align="c", anchor="m", margin=0)
    for y1, y2 in ((2.2, 2.42), (2.97, 3.22), (3.77, 4.02), (4.57, 4.8)):
        line(sl, cx, y1, cx, y2, NAVY, 1.5, arrow=True)
    # yes branch
    ca_x, nc_x, yb = 4.3, 6.75, 6.08
    box(ca_x, yb, 2.3, 0.62, "Take Corrective Action", "Continue Operation", GREEN_L, NAVY, GREEN)
    box(nc_x, yb, 2.3, 0.62, "NC / RCA", "ตามกระบวนการที่ตกลงไว้", ORANGE_L, NAVY, ORANGE)
    line(sl, cx, 5.72, cx, 5.88, GREEN, 1.5)
    line(sl, ca_x + 1.15, 5.88, nc_x + 1.15, 5.88, GREEN, 1.5)
    line(sl, ca_x + 1.15, 5.88, ca_x + 1.15, yb, GREEN, 1.5, arrow=True)
    line(sl, nc_x + 1.15, 5.88, nc_x + 1.15, yb, GREEN, 1.5, arrow=True)
    txt(sl, cx + 0.08, 5.66, 0.6, 0.24, "Yes", size=11, color=GREEN, font=FSB)
    # reactive lane
    box(0.85, 3.22, 3.15, 0.62, "Escalation Management", "ส่งต่อถูกระดับ ทันเวลา", RED_L, NAVY, RED, sub=RED_D)
    rect(sl, 0.85, 4.12, 3.15, 1.3, fill=RED_L, line=RED, lw=1.25, r=0.08,
         text=[[("RCA Management", {"font": FSB, "size": 12.5, "color": NAVY})],
               [("•  If Safety incident", {"size": 10.5})], [("•  If Product block", {"size": 10.5})],
               [("•  If Repetitive / Big breakdown", {"size": 10.5})]], color=RED_D, anchor="m", margin=0.14)
    line(sl, 2.42, 3.84, 2.42, 4.12, RED, 1.5, arrow=True)
    poly(sl, [(cx - 1.05, 5.26), (4.3, 5.26), (4.3, 3.53), (4.0, 3.53)], RED, 1.5)
    txt(sl, 4.4, 5.0, 0.5, 0.24, "No", size=11, color=RED, font=FSB)
    poly(sl, [(0.85, 4.77), (0.62, 4.77), (0.62, 2.69), (bx, 2.69)], RED, 1.5)
    poly(sl, [(nc_x + 1.15, yb + 0.62), (nc_x + 1.15, 6.88), (2.42, 6.88), (2.42, 5.42)], RED, 1.5)
    # active lane
    box(9.35, 3.18, 3.15, 0.62, "Process Confirmation", "Gemba Walk management system", GREEN_L, NAVY, GREEN, sub=GREEN_D)
    box(9.35, 4.05, 3.15, 0.62, "Coaching · Training", "Process Improvement", GREEN_L, NAVY, GREEN, sub=GREEN_D)
    line(sl, bx + bw, 3.49, 9.35, 3.49, GREEN, 1.5, arrow=True)
    line(sl, 10.92, 3.8, 10.92, 4.05, GREEN, 1.5, arrow=True)
    poly(sl, [(12.5, 4.36), (12.72, 4.36), (12.72, 2.69), (bx + bw, 2.69)], GREEN, 1.5)
    rect(sl, 9.35, 5.05, 3.15, 1.3, grad=(NAVY, "203A86"), angle=315, r=0.12, sh=True,
         text=[[("Supported by SIM 0–6", {"font": FSB, "size": 13})],
               [("KPI Matrix ชัด · มีเจ้าของทุกประชุม · วาระชัด · มีกลไกติดตาม", {"size": 11, "color": "C9D6FF"})]],
         color=WHITE, anchor="m", margin=0.18)
    notes(sl, "อ่านจากกลาง: Specification → มาตรฐาน → หน้างานทำตาม → เมื่อพบ Deviation ถามว่ามาตรฐานกำหนดวิธีรับมือไว้หรือไม่\n"
              "ไม่มี → วงแดง (Reactive): Escalate และ RCA แล้วอัปเดตมาตรฐาน · วงเขียว (Active): PC และ Coaching ป้องกันก่อนเกิด")


SLIDES = [s01_cover, s02_agenda, s03_why, s04_pillars, s05_traffic, s06_isnot, s07_cycle, s08_standards,
          s09_loop, s10_modes, s11_components, s12_on_loop, s13_e2e, s14_cycles]
