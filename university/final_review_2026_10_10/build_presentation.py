"""Build the 10 October 2026 VOLLEY final-review presentation.

The cover, heading bands, palette, and slide numbers follow the user-provided
university format PDF. The PDF was a filled example, so its other project's
content is not included here.
"""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FIG = ROOT / "source" / "figures"
OUT = HERE / "VOLLEY_Final_Review_2026-10-10.pptx"
LOGO = HERE / "assets" / "sit-logo.jpg"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]

NAVY = RGBColor(13, 32, 53)
INK = RGBColor(30, 49, 68)
TEAL = RGBColor(0, 150, 160)
PALE = RGBColor(232, 246, 246)
LIGHT = RGBColor(246, 249, 251)
WHITE = RGBColor(255, 255, 255)
MID = RGBColor(99, 118, 132)
RED = RGBColor(185, 65, 65)
AMBER = RGBColor(215, 143, 43)
TEMPLATE_CYAN = RGBColor(78, 172, 194)
TEMPLATE_RED = RGBColor(185, 20, 15)


def box(slide, x, y, w, h, fill=LIGHT, line=None, radius=False):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE,
        Inches(x), Inches(y), Inches(w), Inches(h),
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.fill.background() if line is None else None
    if line is not None:
        shape.line.color.rgb = line
    return shape


def txt(slide, text, x, y, w, h, size=20, bold=False, color=INK,
        align=PP_ALIGN.LEFT, valign=MSO_ANCHOR.TOP, margin=0.015):
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = shape.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(margin)
    tf.margin_top = tf.margin_bottom = Inches(margin)
    tf.vertical_anchor = valign
    p = tf.paragraphs[0]
    p.text = text
    p.alignment = align
    p.font.name = "Aptos"
    p.font.size = Pt(size)
    p.font.bold = bold
    p.font.color.rgb = color
    return shape


def bullets(slide, items, x, y, w, h, size=21, gap=12, color=INK):
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = shape.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = Inches(0.08)
    tf.margin_right = Inches(0.08)
    tf.margin_top = Inches(0.04)
    tf.margin_bottom = 0
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = "•  " + item
        p.font.name = "Aptos"
        p.font.size = Pt(size)
        p.font.color.rgb = color
        p.space_after = Pt(gap)
    return shape


def image_fit(slide, path, x, y, w, h):
    from PIL import Image
    iw, ih = Image.open(path).size
    scale = min(w / iw, h / ih)
    pw, ph = iw * scale, ih * scale
    slide.shapes.add_picture(str(path), Inches(x + (w - pw) / 2),
                             Inches(y + (h - ph) / 2), Inches(pw), Inches(ph))


def footer(slide, source="", label="GEN5 MODEL STUDY"):
    txt(slide, label, 0.44, 7.15, 2.8, 0.22, 8.5, True, MID)
    txt(slide, source, 3.2, 7.15, 8.9, 0.22, 8.5, False, MID)
    txt(slide, str(len(prs.slides)), 12.65, 7.15, 0.35, 0.22, 9, False, MID,
        align=PP_ALIGN.RIGHT)


def base(section, title, source="", label="GEN5 MODEL STUDY"):
    slide = prs.slides.add_slide(BLANK)
    box(slide, 0, 0, 13.333, 7.5, WHITE)
    box(slide, 0, 0, 13.333, 0.78, TEMPLATE_CYAN, NAVY)
    txt(slide, title, 0.44, 0.16, 12.45, 0.52, 25, True, NAVY)
    txt(slide, section.upper(), 0.5, 0.99, 11.8, 0.28, 10, True, TEAL)
    footer(slide, source, label)
    return slide


def card(slide, x, y, w, h, head, body, accent=TEAL, headsize=21, bodysize=17):
    box(slide, x, y, w, h, LIGHT, RGBColor(221, 231, 236), True)
    box(slide, x, y, 0.08, h, accent)
    txt(slide, head, x + 0.23, y + 0.16, w - 0.4, 0.55, headsize, True, NAVY)
    txt(slide, body, x + 0.23, y + 0.82, w - 0.42, h - 1.0, bodysize, False, INK)


def table(slide, headers, rows, widths, x=0.55, y=1.7, row_h=0.67, font=15):
    total = sum(widths)
    cursor = x
    for head, w in zip(headers, widths):
        box(slide, cursor, y, w, 0.55, NAVY)
        txt(slide, head, cursor + 0.08, y + 0.1, w - 0.16, 0.4, 15, True, WHITE)
        cursor += w
    for ri, row in enumerate(rows):
        cursor = x
        yy = y + 0.55 + ri * row_h
        for value, w in zip(row, widths):
            box(slide, cursor, yy, w, row_h, WHITE if ri % 2 else LIGHT,
                RGBColor(225, 232, 237))
            txt(slide, str(value), cursor + 0.08, yy + 0.09, w - 0.16,
                row_h - 0.12, font, False, INK)
            cursor += w
    return total


# 1 Title
s = prs.slides.add_slide(BLANK)
box(s, 0, 0, 13.333, 7.5, WHITE)
txt(s, "Department of Mechanical Engineering", 0.7, 0.22, 11.93, 0.37, 22, True, TEMPLATE_RED, align=PP_ALIGN.CENTER)
txt(s, "B.Tech Project Presentation on", 0.7, 0.66, 11.93, 0.37, 19, True, TEMPLATE_RED, align=PP_ALIGN.CENTER)
txt(s, "VOLLEY: Controlled CubeSat Deployment", 0.7, 1.15, 11.93, 0.52, 29, True, RGBColor(35, 77, 129), align=PP_ALIGN.CENTER)
txt(s, "from a Hosted Orbital Platform", 0.7, 1.72, 11.93, 0.5, 27, True, RGBColor(35, 77, 129), align=PP_ALIGN.CENTER)
txt(s, "Gen5 computational feasibility review", 1.2, 2.19, 10.93, 0.36, 17, True, RGBColor(35, 77, 129), align=PP_ALIGN.CENTER)
image_fit(s, LOGO, 5.77, 2.6, 1.8, 1.5)
txt(s, "Presented By", 2.4, 4.3, 8.5, 0.36, 17, False, RGBColor(35, 77, 129), align=PP_ALIGN.CENTER)
txt(s, "Adityavardhan Mishra  ·  Pratham Chawla", 1.55, 4.67, 10.25, 0.44, 20, True, RGBColor(35, 77, 129), align=PP_ALIGN.CENTER)
txt(s, "PRN 23070125054  ·  PRN 23070125029", 2.1, 5.12, 9.15, 0.34, 15, False, TEMPLATE_RED, align=PP_ALIGN.CENTER)
txt(s, "Guide: Vikas Gulia", 0.8, 5.68, 5.6, 0.42, 18, True, RGBColor(0, 103, 169))
txt(s, "Final review: 10 October 2026", 7.4, 5.68, 5.1, 0.42, 18, True, RGBColor(0, 103, 169), align=PP_ALIGN.RIGHT)
txt(s, "SYMBIOSIS INSTITUTE OF TECHNOLOGY PUNE", 0.6, 6.75, 12.15, 0.45, 23, True, TEMPLATE_RED, align=PP_ALIGN.CENTER)
txt(s, "1", 12.6, 7.14, 0.3, 0.2, 9, False, MID, align=PP_ALIGN.RIGHT)

# 2 Outline
s = base("Outline", "Presentation route", "User-specified final-review outline", "PRESENTATION GUIDE")
items = ["Introduction", "Literature review", "Research gap", "Objectives", "Research methodology",
         "Timeline", "Work progress", "Results", "Conclusion", "Future work", "References"]
for i, item in enumerate(items):
    col, row = (0 if i < 6 else 1), (i if i < 6 else i - 6)
    x = 0.8 + col * 6.1
    y = 1.82 + row * 0.78
    box(s, x, y, 5.65, 0.58, PALE if col == 0 else LIGHT, None, True)
    txt(s, f"{i + 1:02d}  {item}", x + 0.12, y + 0.10, 5.3, 0.4, 19, i in (0, 7, 8), NAVY)

# 3 Introduction
s = base("Introduction", "Which missions might value orbital choice?",
         "NASA 2026 Small Spacecraft SoA; Planet and Spire filings; local market audit")
card(s, 0.65, 1.82, 3.85, 3.48, "Repeat fleets", "Configurable smallsat families and replenishment exist. That context does not establish demand for VOLLEY.")
card(s, 4.75, 1.82, 3.85, 3.48, "Delivery buyer", "A carrier, rideshare integrator or fleet operator might need several distinct release states from one host.")
card(s, 8.85, 1.82, 3.85, 3.48, "Gen5 test", "Compare commanded release with springs, host manoeuvres, transport and onboard propulsion on the same mission.", AMBER)
txt(s, "No customer is confirmed; modeled Gen5 3U mass fails its preset criterion.", 0.8, 5.77, 11.75, 0.62, 21, True, NAVY, align=PP_ALIGN.CENTER)

# 4 Literature
s = base("Literature review", "Existing methods solve different parts of the problem",
         "JAXA; Foster et al. 2018; Feng et al. 2025; Zhao et al. 2022/2025")
table(s, ["Approach", "Strength", "Limit for this thesis"], [
    ("Spring deployer", "Flight heritage; compact; simple", "Limited tailored release speed"),
    ("Spring release / drag", "Relative state or drag can create phasing", "Timing alone, with no relative state change, cannot"),
    ("Orbital transfer vehicle", "Larger orbit changes", "Greater bus, mass and integration burden"),
    ("Electromagnetic research", "Commandable acceleration studied", "Armature, high-g or maturity constraints vary"),
], [2.5, 4.1, 5.65], row_h=0.92, font=17)

# 5 Gap
s = base("Research gap", "A narrower, testable contribution",
         "Thesis manuscript, Related Work and Introduction")
box(s, 0.75, 1.85, 11.8, 1.26, PALE, None, True)
txt(s, "Commanded release for an unmodified CubeSat at moderate acceleration, with the full system counted.",
    1.05, 2.08, 11.2, 0.85, 24, True, NAVY, align=PP_ALIGN.CENTER)
card(s, 0.8, 3.47, 5.72, 2.35, "Contribution examined", "Gen5 reusable-sled linear motor, 3U payload, magazine, pulse power, arrest and orbital utility.", TEAL, 19, 16)
card(s, 6.8, 3.47, 5.72, 2.35, "Boundary", "Electromagnetic CubeSat deployment exists in prior work. Payload qualification and physical performance remain unproved.", AMBER, 19, 16)

# 6 Objectives
s = base("Objectives", "The analytical research objectives have outcomes",
         "Thesis manuscript, BASELINE.md and PROVENANCE.md; presentation synthesis")
table(s, ["Research objective", "Final thesis outcome"], [
    ("Design a commandable 3U system", "Reference CAD and subsystem concepts documented; feed remains open"),
    ("Calculate shot and control performance", "Historical model completed; finite force screen challenges its rating"),
    ("Evaluate orbital utility", "Conditional orbit results; current lifetime not independently closed"),
    ("Count full installed burden", "Mass rollup completed; 3U parity criterion failed"),
    ("Test credibility of key claims", "Numerical cross-checks and limits recorded"),
], [5.05, 7.2], row_h=0.82, font=16)

# 7 Methodology pipeline
s = base("Research methodology", "The analysis chain from mission to decision",
         "Thesis manuscript, Models and Verification; validation register")
steps = ["Mission &\npayload needs", "Architecture\ntrade", "CAD & mass\nmodel", "Shot, power &\norbit models", "Numerical\ncross-checks", "Sensitivity &\nacceptance bands"]
for i, step in enumerate(steps):
    x = 0.55 + i * 2.11
    box(s, x, 2.25, 1.82, 1.62, PALE if i % 2 == 0 else LIGHT, TEAL, True)
    txt(s, step, x + 0.1, 2.59, 1.62, 0.93, 17, True, NAVY, align=PP_ALIGN.CENTER)
    if i < 5:
        txt(s, "→", x + 1.83, 2.75, 0.3, 0.4, 22, True, TEAL, align=PP_ALIGN.CENTER)
box(s, 1.5, 4.64, 10.3, 1.18, LIGHT, None, True)
txt(s, "Models were challenged and revised; hardware performance remains outside this thesis's evidence.",
    1.8, 4.92, 9.7, 0.62, 23, True, NAVY, align=PP_ALIGN.CENTER)

# 8 Methodology checks
s = base("Research methodology", "Numerical checks changed the review baseline",
         "VOLLEY-thesis/appendix/PROVENANCE.md; validation run sheets")
table(s, ["Question", "Method / cross-check", "Evidence limit"], [
    ("Field and thrust", "Analytic field; field-point FEM; finite force screen", "No independent integrated-thrust FEM or measurement"),
    ("Shot and power", "Dynamics; Monte Carlo; ngspice", "Assumed components and interfaces"),
    ("Structure and flow", "CAD; CalculiX; OpenFOAM", "No payload qualification"),
    ("Orbital change", "Orbit model; Cowell / GMAT cases", "Lifetime depends on atmosphere"),
], [2.7, 4.7, 4.85], row_h=0.94, font=16)

# 9 Timeline actual
s = base("Timeline", "Project evolution: documented decisions and analysis",
         "VOLLEY-thesis/appendix/HISTORY.md; thesis README; PLAN-R2")
milestones = [
    ("2023", "Hosted concept", "Free-flyer concept reframed around a host platform"),
    ("Mid-2025*", "LSM direction", "Coilgun study gives way to a linear synchronous motor"),
    ("2025–26*", "CAD generations", "Geometry and mass models mature through Gen5"),
    ("Jul–Sep 2026", "Gen5 evidence", "Cross-checks, defect corrections and thesis record"),
    ("Oct 2026", "Final review", "Gen5 results, failed criterion and thesis record presented"),
]
for i, (date, head, body) in enumerate(milestones):
    y = 1.72 + i * 0.93
    box(s, 0.75, y, 2.0, 0.7, PALE, None, True)
    txt(s, date, 0.88, y + 0.15, 1.75, 0.38, 17, True, TEAL)
    txt(s, head, 3.0, y + 0.06, 2.7, 0.45, 20, True, NAVY)
    txt(s, body, 5.74, y + 0.1, 6.5, 0.45, 17, False, INK)
txt(s, "* Approximate historical milestone; not a documented semester deadline.", 0.9, 6.55, 10.9, 0.3, 11, False, MID)

# 10 Timeline of evidence corrections
s = base("Timeline", "2026 findings changed the review baseline",
         "HISTORY.md; PROVENANCE.md; thesis manuscript, Limitations")
stages = [
    ("Jul", "CAD-derived sled mass replaced an optimistic parametric estimate"),
    ("Aug", "Depth-resolved thrust calculation lowered the historical model speed"),
    ("Aug", "Enclosure buildup exposed the full 3U mass penalty"),
    ("2026", "Independent orbit checks rejected a solar-invariance claim"),
    ("Final", "Results and failures retained in the submitted thesis record"),
]
for i, (tag, body) in enumerate(stages):
    y = 1.76 + i * 0.92
    box(s, 1.0, y, 1.2, 0.67, TEAL, None, True)
    txt(s, tag, 1.11, y + 0.13, 0.98, 0.41, 17, True, WHITE, align=PP_ALIGN.CENTER)
    box(s, 2.42, y, 9.65, 0.67, LIGHT, None, True)
    txt(s, body, 2.65, y + 0.1, 9.18, 0.49, 19, False, INK)

# 11 Work progress
s = base("Work progress", "The current review package is assembled and traceable",
         "Thesis README; BASELINE.md; PROVENANCE.md; validation register")
card(s, 0.7, 1.87, 3.83, 3.88, "Design documented", "Gen5 reference CAD, magazine and release concepts, subsystem models and system mass rollup.", TEAL, 22, 19)
card(s, 4.74, 1.87, 3.83, 3.88, "Analysis delivered", "Shot, control, circuit, structure, thermal, orbit and alternative-case results.", TEAL, 22, 19)
card(s, 8.78, 1.87, 3.83, 3.88, "Evidence delivered", "Manuscript, figures, scripts, numerical checks, provenance and defect register.", TEAL, 22, 19)
txt(s, "Scope: fixed computational study with failed design gates; no physical qualification claim.", 0.85, 6.04, 11.7, 0.48, 18, True, NAVY, align=PP_ALIGN.CENTER)

# 12 Architecture
s = base("Results", "Gen5: fixed reference geometry, feeder fit still open",
         "Thesis manuscript, System Architecture; CAD render", "GEN5 MODEL STUDY")
image_fit(s, ROOT / "cad" / "renders" / "gen5" / "exploded.png", 0.5, 1.7, 7.0, 4.9)
bullets(s, ["1.3 m powered stroke; 1.5 m release station",
            "Reusable 9.45 kg magnet sled",
            "Two cassettes; twelve 3U satellites",
            "FreeCAD STEP assembly: side-fed placement clashes"], 7.7, 2.0, 4.85, 4.3, 19, 17)

# 13 Shot
s = base("Results", "Historical periodic-model shot: challenged by finite geometry",
         "Thesis BASELINE.md; F01_shot.png; P117 energy audit", "GEN5 MODEL PREDICTION")
image_fit(s, FIG / "F01_shot.png", 0.7, 1.85, 11.8, 3.25)
metrics = [("16.0 m/s", "exit speed"), ("10.07 g", "acceleration"),
           ("2.782 kJ", "gross draw"), ("18.8%", "net efficiency")]
for i, (value, label) in enumerate(metrics):
    x = 0.85 + i * 3.12
    box(s, x, 5.28, 2.73, 1.2, PALE, None, True)
    txt(s, value, x + 0.08, 5.4, 2.56, 0.48, 25, True, NAVY, align=PP_ALIGN.CENTER)
    txt(s, label, x + 0.08, 5.92, 2.56, 0.33, 14, False, INK, align=PP_ALIGN.CENTER)
txt(s, "P118 challenges 16.0 m/s; P117 reconciles 124.5 J to assumed model terms.",
    0.85, 6.65, 11.9, 0.28, 13, False, MID)

# 14 Finite force
s = base("Results", "Independent 3-D check confirms ideal finite-force work",
         "P118 analytic; P119 2-D FEM; P121 3-D numerical; P122 gap sensitivity", "COMPUTATIONAL CROSS-CHECK")
image_fit(s, FIG / "gen5_finite_force_sensitivity.png", 0.55, 1.7, 7.65, 4.9)
card(s, 8.45, 1.78, 4.1, 1.95, "1.042 kJ", "Ideal 3-D work: independent surface-charge formulation agrees with P118 under shared inputs.", AMBER, 23, 15)
card(s, 8.45, 3.95, 4.1, 1.95, "−13% work", "Illustrative 12-to-14 mm magnet gap change; not a measured tolerance or motor rating.", RED, 24, 15)
txt(s, "No measured force, selected inverter or demonstrated release speed exists.",
    0.8, 6.64, 11.75, 0.35, 15, True, NAVY, align=PP_ALIGN.CENTER)

# 14 Control
s = base("Results", "Modelled command precision is narrow; it is unmeasured",
         "Thesis BASELINE.md; PROVENANCE.md; F03_mc.png", "GEN5 MODEL PREDICTION")
image_fit(s, FIG / "F03_mc.png", 0.72, 1.73, 7.55, 4.94)
card(s, 8.54, 1.95, 3.95, 2.1, "0.0274 m/s", "3σ exit-velocity dispersion at a 15.8 m/s fleet setpoint.", TEAL, 27, 17)
card(s, 8.54, 4.32, 3.95, 2.0, "Evidence limit", "Monte Carlo under modelled sensing and plant tolerances; no measured dispersion.", AMBER, 21, 16)

# 15 Orbit
s = base("Results", "Historical orbit input has a separate geometry check",
         "P115 Cartesian orbit check; manuscript Astrodynamic Utility", "GEN5 TWO-BODY CHECK")
image_fit(s, FIG / "rated_orbit_crosscheck.png", 0.62, 1.8, 7.65, 4.67)
card(s, 8.52, 1.94, 3.96, 1.95, "+28.8008 km", "Immediate two-body axis rise for an assumed historical 16.029 m/s input.", TEAL, 25, 16)
card(s, 8.52, 4.1, 3.96, 1.95, "1.60× open", "Lifetime remains atmosphere-dependent and lacks an independent rerun for this input.", AMBER, 22, 16)
txt(s, "Persistent phasing requires a relative state change; this result concerns orbital energy.", 0.8, 6.62, 11.75, 0.27, 13, True, NAVY)

# 16 Mass
s = base("Results", "Gen5 fails its 3U mass comparison",
         "Thesis manuscript, Payload Class and Mass-per-Satellite; A46 enclosure result", "GEN5 MODEL STUDY")
box(s, 0.85, 1.72, 11.75, 1.02, LIGHT, RGBColor(221, 231, 236), True)
txt(s, "Modeled dry mass, 12 slots", 1.1, 1.99, 7.4, 0.43, 20, True, NAVY)
txt(s, "126.6 kg", 9.65, 1.99, 2.6, 0.43, 21, True, NAVY, align=PP_ALIGN.RIGHT)
txt(s, "Gen5 per 3U", 0.9, 3.0, 3.2, 0.45, 21, True, NAVY)
box(s, 4.25, 3.03, 6.9, 0.48, TEAL)
txt(s, "10.55 kg", 11.25, 3.02, 1.15, 0.42, 20, True, NAVY, align=PP_ALIGN.RIGHT)
txt(s, "Spring comparator", 0.9, 4.0, 3.2, 0.45, 21, True, NAVY)
box(s, 4.25, 4.03, 3.92, 0.48, MID)
txt(s, "~6 kg", 11.25, 4.02, 1.15, 0.42, 20, True, NAVY, align=PP_ALIGN.RIGHT)
box(s, 0.85, 5.35, 11.75, 0.95, RGBColor(255, 240, 235), None, True)
txt(s, "1.76× heavier per 3U payload; the preset 15% parity band fails.", 1.1, 5.6, 11.25, 0.48, 23, True, RED, align=PP_ALIGN.CENTER)

# 17 Limitations
s = base("Results", "The current side-fed assembly fails a geometric fit check",
         "FreeCAD Gen5 Review.FCStd; P116 assembly packaging report", "CAD INTERFERENCE • OPEN")
image_fit(s, FIG / "gen5_packaging_section.png", 0.64, 1.78, 6.35, 4.92)
card(s, 7.22, 1.92, 5.15, 1.85, "11 mm short", "537 mm of track and cassette width inside 526 mm of usable enclosure width.", RED, 25, 15)
card(s, 7.22, 4.02, 5.15, 1.85, "32,915 mm³", "Exact track/cassette clash on each side; CadQuery and FreeCAD agree.", AMBER, 23, 15)
txt(s, "Reference placement only: a new feeder or enclosure would need a new configuration and rerun.", 0.88, 6.59, 11.55, 0.3, 14, True, NAVY, align=PP_ALIGN.CENTER)

# Unselected R1 geometry
s = base("Results", "R1 clears a scripted path; the feeder is not designed",
         "FreeCAD R1 document and STEP; exact-solid route ledger", "UNSELECTED GEOMETRY")
image_fit(s, ROOT / "figures" / "gen5_feeder_candidate_r1.png", 0.55, 1.75, 7.4, 4.9)
card(s, 8.15, 1.88, 4.37, 1.94, "12 / 12", "Scripted 3U envelope routes and conservative fixed-part swept boxes clear.", TEAL, 25, 15)
card(s, 8.15, 4.03, 4.37, 1.94, "570 mm", "Wider enclosure; lift actuator, retention, tolerance and new mass budget open.", AMBER, 25, 15)
txt(s, "Separate R1 candidate; no change to evaluated Gen5 shot, mass or host-fit claims.",
    0.8, 6.62, 11.8, 0.35, 15, True, NAVY, align=PP_ALIGN.CENTER)

# 18 Demo
s = base("Results", "Computational demonstration: from force to mission decision",
         "P118–P120 finite-force/assumed bank; matched-mission reference", "SIMULATION DEMONSTRATION")
box(s, 0.62, 1.78, 5.72, 4.25, LIGHT, None, True)
box(s, 6.97, 1.78, 5.72, 4.25, LIGHT, None, True)
txt(s, "1. Finite-force geometry screen", 0.84, 1.94, 5.26, 0.47, 19, True, NAVY)
txt(s, "2. Matched mission screen", 7.18, 1.94, 5.21, 0.47, 19, True, NAVY)
image_fit(s, FIG / "gen5_finite_force_fem2d.png", 0.78, 2.5, 5.42, 3.2)
image_fit(s, FIG / "matched_mission_reference.png", 7.14, 2.5, 5.4, 3.2)
txt(s, "→", 6.39, 3.65, 0.5, 0.55, 28, True, TEAL, align=PP_ALIGN.CENTER)
txt(s, "P119 checks force; P120 reruns bank assumptions; no twelve-shot mission case closes.",
    0.86, 6.25, 11.62, 0.62, 17, True, NAVY, align=PP_ALIGN.CENTER)

# Matched mission reference
s = base("Results", "Matched reference mission finds no twelve-shot closure",
         "Common-input spring/Gen5 study; 100 N host, 450 km, 12 × 4 kg payloads", "BOUNDED MISSION SCREEN")
image_fit(s, FIG / "matched_mission_reference.png", 0.55, 1.7, 7.65, 4.9)
card(s, 8.42, 1.83, 4.1, 1.94, "2.69 vs 0.83 kg", "Ideal one-event host propellant: spring versus Gen5's ideal finite-force upper screen.", TEAL, 21, 15)
card(s, 8.42, 4.0, 4.1, 1.94, "4 / 1 / 1", "Accepted twelve-shot prefixes: spring, finite Gen5, historical Gen5.", RED, 24, 15)
txt(s, "Assumed host and devices; optimizer result is not an infeasibility proof or product advantage.",
    0.8, 6.61, 11.8, 0.35, 14, True, NAVY, align=PP_ALIGN.CENTER)

# 19 Conclusion
s = base("Conclusion", "This Gen5 configuration does not pass selection",
         "Thesis manuscript, Conclusion; BASELINE.md; PROVENANCE.md")
bullets(s, ["Historical model reports 16.0 m/s; a finite force screen challenges that performance claim.",
            "The modeled system is 76% heavier per 3U customer and the evaluated side-fed CAD clashes.",
            "R1 geometry clears a scripted path, but has no lift or launch retention design.",
            "No matched twelve-shot reference closes; Gen5 is a documented negative design study."],
        0.95, 1.9, 11.65, 4.8, 22, 21)

# 20 Future Gen6
s = base("Future work", "Gen6 reopens the mechanism and installed-system trade",
         "CURRENT PLAN AND STATUS — PLAN-R2, 29 Sep 2026", "GEN6 PLAN • NOT ACHIEVED")
box(s, 0.8, 1.8, 11.7, 1.17, PALE, None, True)
txt(s, "One shared path • sequential feed • commanded release for each CubeSat", 1.0, 2.1, 11.35, 0.55, 22, True, NAVY, align=PP_ALIGN.CENTER)
bullets(s, ["Investigate approximately 1–2 m/s through 1 km/s across mission cases.",
            "Compare electromagnetic, stored-energy, gas/fluid, hybrid, BOLLEY and conventional options.",
            "Count feeder, retention, arrest, control, energy, thermal, host loads and shared faults."],
        1.15, 3.3, 11.0, 2.45, 21, 19)
txt(s, "1 km/s is a research target, not demonstrated speed or payload/provider compatibility.",
    0.92, 6.28, 11.55, 0.52, 17, True, RED, align=PP_ALIGN.CENTER)

# 21 Future test
s = base("Future work", "Next milestone: one reviewable first-test configuration",
         "PLAN-R2 N0–N5 and agreed near-term end goal", "GEN6 PLAN • NOT ACHIEVED")
steps = [("Freeze", "Named mission, payload and host surrogate"),
    ("Decide", "Fair mechanism and installed-burden trade"),
         ("Measure", "Field, contact, release, arrest, loads and cycle behavior"),
    ("Review", "Drawings, BOM, procedures, uncertainty and review decision")]
for i, (head, body) in enumerate(steps):
    y = 1.8 + i * 1.15
    box(s, 0.83, y, 2.2, 0.84, TEAL if i < 3 else AMBER, None, True)
    txt(s, head, 1.03, y + 0.18, 1.83, 0.48, 20, True, WHITE, align=PP_ALIGN.CENTER)
    box(s, 3.24, y, 9.0, 0.84, LIGHT, None, True)
    txt(s, body, 3.55, y + 0.18, 8.43, 0.5, 20, False, INK)

# 22 References
s = base("References", "Core literature and standards (1/2)",
         "Bibliography from VOLLEY-thesis/source/paper.tex", "SOURCE LIST")
refs = [
    "[1] JAXA, JEM Payload Accommodation Handbook, Vol. 8: Small Satellite Deployment ICD.",
    "[2] Cal Poly, CubeSat Design Specification, Rev. 14, 2020.",
    "[3] C. Foster et al., ‘Constellation phasing with differential drag on Planet Labs satellites,’ J. Spacecraft Rockets 55(2), 2018.",
    "[4] H. Feng et al., ‘Design and reachable domain analysis of on-orbit electromagnetic launcher for CubeSats,’ Int. J. Aerospace Eng., 2025.",
    "[5] Y. Zhao et al., ‘Design and analysis of a new deployer for the in-orbit release of multiple stacked CubeSats,’ Remote Sensing 14(17), 4205, 2022.",
]
bullets(s, refs, 0.76, 1.73, 11.9, 5.03, 17, 18)

# 23 References
s = base("References", "Methods and project records (2/2)",
         "Bibliography from VOLLEY-thesis/source/paper.tex; project records", "SOURCE LIST")
refs = [
    "[6] Y. Zhao et al., ‘Simulation analysis and experimental verification of the transport characteristics of a high-volume CubeSat storage device,’ Aerospace 12(6), 466, 2025.",
    "[7] K. Halbach, ‘Design of permanent multipole magnets with oriented rare earth cobalt material,’ Nucl. Instrum. Methods 169, 1980.",
    "[8] NASA, General Environmental Verification Standard (GEVS), GSFC-STD-7000A, 2013.",
    "[9] D. A. Vallado, Fundamentals of Astrodynamics and Applications, 4th ed., 2013.",
    "[10] A. Mishra, VOLLEY-thesis: manuscript, baseline, provenance and validation records, repo head b30ffdc, 28 Sep 2026.",
    "[11] VOLLEY/BOLLEY, Current Plan and Status — PLAN-R2, controlled working baseline, 29 Sep 2026 (project plan).",
]
bullets(s, refs, 0.76, 1.68, 11.9, 5.13, 16, 16)

OUT.parent.mkdir(parents=True, exist_ok=True)
prs.save(OUT)
print(f"Wrote {OUT} ({len(prs.slides)} slides)")
