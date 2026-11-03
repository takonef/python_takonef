import pandas as pd
import matplotlib.pyplot as plt

students_raw = pd.read_excel("students_info.xlsx", sheet_name="logins")
students_raw.columns = [c.strip() for c in students_raw.columns]

empty_rows = students_raw["login"].isna().sum()

students = students_raw.copy()
students["login"] = students["login"].astype(str).str.strip()
students = students[~students["login"].isin(["", "nan", "None"])].copy()
students["group_faculty"] = students["group_faculty"].astype(int)
students["group_out"] = students["group_out"].astype(int)

results = pd.read_html("results_ejudge.html")[0]

merged = students.merge(results, left_on="login", right_on="User", how="inner")
merged["Solved"] = pd.to_numeric(merged["Solved"], errors="coerce").fillna(0).astype(int)

fig, axes = plt.subplots(1, 2, figsize=(16, 5))

avg_fac = merged.groupby("group_faculty")["Solved"].mean().sort_index()
avg_fac.plot(kind="bar", ax=axes[0], color="darkseagreen", edgecolor="gray")
axes[0].set_title("Среднее число решённых задач\nпо факультетским группам")
axes[0].set_xlabel("Факультетская группа")
axes[0].set_ylabel("Среднее число решённых задач")
axes[0].tick_params(axis="x", rotation=0)
for p in axes[0].patches:
    axes[0].annotate(f"{p.get_height():.2f}",
                     (p.get_x() + p.get_width()/2, p.get_height()),
                     ha="center", va="bottom", fontsize=8)

avg_out = merged.groupby("group_out")["Solved"].mean().sort_index()
avg_out.plot(kind="bar", ax=axes[1], color="darkseagreen", edgecolor="gray")
axes[1].set_title("Среднее число решённых задач\nпо группам по информатике")
axes[1].set_xlabel("Группа по информатике")
axes[1].set_ylabel("Среднее число решённых задач")
axes[1].tick_params(axis="x", rotation=0)
for p in axes[1].patches:
    axes[1].annotate(f"{p.get_height():.2f}",
                     (p.get_x() + p.get_width()/2, p.get_height()),
                     ha="center", va="bottom", fontsize=8)

plt.tight_layout()
plt.savefig("progotest.png")
plt.show()

def to_int(x):
    try:
        v = float(x)
        return 0 if pd.isna(v) else int(v)
    except (ValueError, TypeError):
        return 0

merged["G"] = merged["G"].apply(to_int)
merged["H"] = merged["H"].apply(to_int)

selected = merged[(merged["G"] > 10) | (merged["H"] > 10)].copy()

print("Студенты, прошедшие > 1 теста в G или H:")
print(selected[["login", "group_faculty", "group_out", "G", "H"]]
      .to_string(index=False))

print("\nФакультетские группы:", sorted(selected["group_faculty"].unique().tolist()))
print("Группы по информатике:", sorted(selected["group_out"].unique().tolist()))

print("\nнестыковки:")
print(f"- в xlsx есть {empty_rows} пустых строк (без логина)")
xlsx_set = set(students["login"])
ejudge_set = set(results["User"].dropna().astype(str))
print(f"- {len(sorted(ejudge_set - xlsx_set))} логиов есть в ejudge, но нет в xlsx")
print(f"- есть {students['login'].duplicated().sum()} дубликатов логинов в xlsx")