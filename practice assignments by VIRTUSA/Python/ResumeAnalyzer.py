import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from tkinter import ttk

# Import the new modules we just created
import nlp_utils

# Try to import matplotlib for the chart
try:
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
except ImportError:
    plt = None

# --- UI ACTIONS ---

def browse_pdf():
    p = filedialog.askopenfilename(filetypes=[("PDF", "*.pdf")])
    if p:
        txt = nlp_utils.get_pdf_text_util(p) # Using logic from nlp_utils
        resume_ent.delete("1.0", tk.END)
        resume_ent.insert(tk.END, txt)

def refresh_chart(m_count, mis_count):
    if not plt: return
    for w in chart_win.winfo_children(): w.destroy()
    
    if (m_count + mis_count) == 0: return

    # Using a professional vertical bar chart
    names = ['Matches', 'Gaps']
    vals = [m_count, mis_count]
    colors = ['#198754', '#f39c12'] # Professional Green and Orange

    fig, ax = plt.subplots(figsize=(4, 2), dpi=100)
    fig.patch.set_facecolor('#ffffff')
    
    bars = ax.bar(names, vals, color=colors, width=0.4)
    ax.set_title("Core Skills Gap Analysis", fontsize=10, fontweight='bold')
    ax.set_ylim(0, max(vals) + 2 if max(vals) > 0 else 5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    for b in bars:
        h = b.get_height()
        ax.text(b.get_x() + b.get_width()/2, h + 0.1, int(h), ha='center', va='bottom', fontsize=9, fontweight='bold')

    canvas = FigureCanvasTkAgg(fig, master=chart_win)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def execute_analysis():
    jd_raw = jd_ent.get("1.0", tk.END).strip()
    res_raw = resume_ent.get("1.0", tk.END).strip()
    
    if not jd_raw or not res_raw:
        messagebox.showwarning("Incomplete", "Provide both JD and Resume text.")
        return

    # Using the logic from our nlp_utils file
    jd_skills = nlp_utils.extract_meaningful_tech_skills(jd_raw)
    res_skills = nlp_utils.extract_meaningful_tech_skills(res_raw)
    
    matches = jd_skills.intersection(res_skills)
    missing = jd_skills.difference(res_skills)
    
    if not jd_skills:
        messagebox.showerror("Error", "No meaningful technical keywords could be found.")
        return

    m_score = (len(matches) / len(jd_skills)) * 100
    
    # Update UI View
    out_panel.config(state=tk.NORMAL)
    out_panel.delete("1.0", tk.END)
    
    out_panel.insert(tk.END, f"Core Knowledge Match: {round(m_score, 2)}%\n", "h_score")
    out_panel.insert(tk.END, "-" * 40 + "\n\n")
    
    out_panel.insert(tk.END, f"✔ Relevant Technical Matches ({len(matches)}):\n", "h_match")
    m_sort = sorted(list(matches))
    i = 0
    while i < len(m_sort):
        out_panel.insert(tk.END, f" • {m_sort[i]}\n")
        i += 1

    out_panel.insert(tk.END, f"\n🚫 Targeted Skills for Improvement ({len(missing)}):\n", "h_miss")
    ms_sort = sorted(list(missing))
    j = 0
    while j < min(len(ms_sort), 14):
        out_panel.insert(tk.END, f" • {ms_sort[j]}\n")
        j += 1
    if len(ms_sort) > 14: out_panel.insert(tk.END, " ... and others")
    
    out_panel.config(state=tk.DISABLED)
    refresh_chart(len(matches), len(missing))

# --- DESIGNED DASHBOARD ---

app = tk.Tk()
app.title("Pro-Grade Resume & Skill Matcher")
app.geometry("900x850")
app.configure(bg="#f1f3f5")

# Header
tk.Label(app, text="Resume Analyzer & Job Matcher", font=("Helvetica", 12, "bold"), bg="#343a40", fg="white", pady=15).pack(fill=tk.X)

# Content
body = tk.Frame(app, bg="#f1f3f5", padx=30, pady=20)
body.pack(fill=tk.BOTH, expand=True)

# Row 1
r1 = tk.Frame(body, bg="#f1f3f5")
r1.pack(fill=tk.X)

# JD
c_l = tk.Frame(r1, bg="#f1f3f5")
c_l.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
tk.Label(c_l, text="Job Description Analytics", font=("Helvetica", 9, "bold"), bg="#f1f3f5", fg="#495057").pack(anchor=tk.W, pady=5)
jd_ent = scrolledtext.ScrolledText(c_l, height=12, font=("Segoe UI", 9), bd=1, relief=tk.SOLID)
jd_ent.pack(fill=tk.BOTH, expand=True)

# Resume
c_r = tk.Frame(r1, bg="#f1f3f5")
c_r.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))
tk.Label(c_r, text="Applicant Profile", font=("Helvetica", 9, "bold"), bg="#f1f3f5", fg="#495057").pack(side=tk.LEFT, pady=5)
tk.Button(c_r, text="📂 Load PDF", font=("Helvetica", 8), command=browse_pdf, bg="#ffffff", relief=tk.GROOVE).pack(side=tk.RIGHT, pady=5)
resume_ent = scrolledtext.ScrolledText(c_r, height=12, font=("Segoe UI", 9), bd=1, relief=tk.SOLID)
resume_ent.pack(fill=tk.BOTH, expand=True)

# Analyze Button
tk.Button(body, text="GENERATE MATCH SCORE", command=execute_analysis, bg="#0d6efd", fg="white", font=("Helvetica", 11, "bold"), pady=10, relief=tk.FLAT).pack(fill=tk.X, pady=20)

# Card Display
card = tk.Frame(body, bg="#ffffff", bd=1, relief=tk.SOLID, padx=25, pady=20)
card.pack(fill=tk.BOTH, expand=True)

card_l = tk.Frame(card, bg="#ffffff")
card_l.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
out_panel = scrolledtext.ScrolledText(card_l, width=45, font=("Segoe UI", 10), state=tk.DISABLED, bg="#ffffff", bd=0)
out_panel.pack(fill=tk.BOTH, expand=True)

out_panel.tag_config("h_score", font=("Helvetica", 16, "bold"), foreground="#0d6efd")
out_panel.tag_config("h_match", font=("Helvetica", 10, "bold"), foreground="#198754")
out_panel.tag_config("h_miss", font=("Helvetica", 10, "bold"), foreground="#f39c12")

card_r = tk.Frame(card, bg="#ffffff")
card_r.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(20, 0))
chart_win = tk.Frame(card_r, bg="#ffffff")
chart_win.pack(fill=tk.BOTH, expand=True)
tk.Label(chart_win, text="Skills Gap Dashboard", font=("Helvetica", 9, "italic"), bg="#ffffff", fg="#adb5bd").pack(pady=60)

if __name__ == "__main__":
    app.mainloop()
