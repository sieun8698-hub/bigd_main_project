
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

heights = [150, 152, 151, 155, 157]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(heights)

for i, h in enumerate(heights):
    ax.annotate(
        f"{h}",
        (i, h),
        textcoords="offset points",
        xytext=(0, 8),
        ha="center"
    )

ax.set_title("키 변화 그래프")
ax.set_ylabel("키 (cm)")
ax.set_xlabel("측정 순서")

fig.savefig("my_first_chart.png")

