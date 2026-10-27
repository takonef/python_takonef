import csv
import matplotlib.pyplot as plt
from collections import defaultdict

prep_data = defaultdict(lambda: defaultdict(int))
group_data = defaultdict(lambda: defaultdict(int))
all_marks = set()

with open('students.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        prep, group, mark = row[0], row[1], int(row[2])
        prep_data[prep][mark] += 1
        group_data[group][mark] += 1
        all_marks.add(mark)

cmap = plt.get_cmap('RdYlGn') # красивенький градиент 0 = r 0.5 = y 1 = g
sorted_marks = sorted(list(all_marks)) # чтобы оценки шли снизу вверх
def plot_stacked_bar(data_dict, title, x, ax):
    keys = sorted(data_dict.keys())
    bottom_values = [0] * len(keys)

    for mark in sorted_marks:
        counts = [data_dict[k].get(mark, 0) for k in keys]
        color = cmap((mark - 1) / 9)
        
        ax.bar(keys, counts, bottom=bottom_values, label=str(mark), color=color, edgecolor='grey', linewidth=0.5)
        bottom_values = [b + c for b, c in zip(bottom_values, counts)]

    ax.set_title(title)
    ax.set_xlabel(x)
    ax.set_ylabel('Count')
    ax.legend(title='Mark', bbox_to_anchor=(1.01, 1), loc='upper left')

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

plot_stacked_bar(prep_data, 'Marks per prep', 'Prep', ax1)
plot_stacked_bar(group_data, 'Marks per group', 'Group', ax2)
plt.subplots_adjust(hspace=0.3)
plt.savefig('exams.png')
plt.show()