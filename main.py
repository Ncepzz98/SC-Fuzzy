from grafik import *
from rule import *

print("=========== Proses Fuzification ============= ")

x1 = float(input("Masukkan IPK   = "))
x2 = float(input("Masukkan TOEFL = "))
x3 = float(input("Masukkan TPA   = "))

#========================= Nilai IPK =========================

#================= IPK Low Mid =================

if x1 in ipk_low and x1 in ipk_mid:
    beda_low_mid = set(ipk_low).intersection(ipk_mid)
    b = max(beda_low_mid)
    a = min(beda_low_mid)

    Miu_low = (b-x1)/(b-a)
    Miu_low = round(Miu_low, 2)

    Miu_mid = (x1-a)/(b-a)
    Miu_mid = round(Miu_mid, 2)
    print(Miu_low, Miu_mid)

    a1 = ["low", Miu_low]
    b1 = ["mid", Miu_mid]

#=============== IPK Mid High ====================

elif x1 in ipk_mid and x1 in ipk_high:
    beda_mid_high = set(ipk_mid).intersection(ipk_high)
    b = max(beda_mid_high)
    a = min(beda_mid_high)

    Miu_mid = (b-x1)/(b-a)
    Miu_mid = round(Miu_mid, 2)

    Miu_high = (x1-a)/(b-a)
    Miu_high = round(Miu_high, 2)
    print(Miu_mid, Miu_high)

    a1 = ["mid", Miu_mid]
    b1 = ["high", Miu_high]

#=================== IPK Mid ====================

elif x1 in ipk_mid:

    Miu_mid = 1
    Miu_high = 0

    print(Miu_mid, Miu_high)

    a1 = ["mid", Miu_mid]
    b1 = ["high", Miu_high]

# =================== IPK Low ====================

elif x1 in ipk_low:

    Miu_low = 1
    Miu_mid = 0

    print(Miu_low, Miu_mid)

    a1 = ["low", Miu_low]
    b1 = ["mid", Miu_mid]

# ========================= Nilai TOEFL =========================

# ================= TOEFL Low Mid =================

if x2 in toefl_low and x2 in toefl_mid:
    beda_low_mid = set(toefl_low).intersection(toefl_mid)
    b = max(beda_low_mid)
    a = min(beda_low_mid)

    Miu_low2 = (b - x2) / (b - a)
    Miu_low2 = round(Miu_low2, 2)

    Miu_mid2 = (x2 - a) / (b - a)
    Miu_mid2 = round(Miu_mid2, 2)
    print(Miu_low2, Miu_mid2)

    a2 = ["low", Miu_low2]
    b2 = ["mid", Miu_mid2]

# =============== TOEFL Mid High ====================

elif x2 in toefl_mid and x2 in toefl_high:
    beda_mid_high = set(toefl_mid).intersection(toefl_high)
    b = max(beda_mid_high)
    a = min(beda_mid_high)

    Miu_mid2 = (b - x2) / (b - a)
    Miu_mid2 = round(Miu_mid2, 2)

    Miu_high2 = (x2 - a) / (b - a)
    Miu_high2 = round(Miu_high2, 2)
    print(Miu_mid2, Miu_high2)

    a2 = ["mid", Miu_mid2]
    b2 = ["high", Miu_high2]

# =================== TOEFL High ====================

elif x2 in toefl_high:

    Miu_high2 = 1
    Miu_mid2 = 0

    print(Miu_high2, Miu_mid2)

    a2 = ["high", Miu_high2]
    b2 = ["mid", Miu_mid2]

# =================== TOEFL Mid ====================

elif x2 in toefl_mid:

    Miu_mid2 = 1
    Miu_high2 = 0

    print(Miu_mid2, Miu_high2)

    a2 = ["mid", Miu_mid2]
    b2 = ["high", Miu_high2]

# =================== TOEFL Low ====================

elif x2 in toefl_low:

    Miu_low2 = 1
    Miu_mid2 = 0

    print(Miu_low2, Miu_mid2)

    a2 = ["low", Miu_low2]
    b2 = ["mid", Miu_mid2]

# ========================= Nilai TPA =========================

# ================= TPA Low Mid =================

if x3 in tpa_low and x3 in tpa_mid:
    beda_low_mid = set(tpa_low).intersection(tpa_mid)
    b = max(beda_low_mid)
    a = min(beda_low_mid)

    Miu_low3 = (b - x3) / (b - a)
    Miu_low3 = round(Miu_low3, 2)

    Miu_mid3 = (x3 - a) / (b - a)
    Miu_mid3 = round(Miu_mid3, 2)
    print(Miu_low3, Miu_mid3)

    a3 = ["low", Miu_low3]
    b3 = ["mid", Miu_mid3]

# =============== TPA Mid High ====================

elif x3 in tpa_mid and x3 in tpa_high:
    beda_mid_high = set(tpa_mid).intersection(tpa_high)
    b = max(beda_mid_high)
    a = min(beda_mid_high)

    Miu_mid3 = (b - x3) / (b - a)
    Miu_mid3 = round(Miu_mid3, 2)

    Miu_high3 = (x3 - a) / (b - a)
    Miu_high3 = round(Miu_high3, 2)
    print(Miu_mid3, Miu_high3)

    a3 = ["mid", Miu_mid3]
    b3 = ["high", Miu_high3]

# =================== TPA Mid ====================

elif x3 in tpa_high:

    Miu_high3 = 1
    Miu_mid3 = 0

    print(Miu_high3, Miu_mid3)

    a3 = ["high", Miu_high3]
    b3 = ["mid", Miu_mid3]

# =================== TPA Mid ====================

elif x3 in tpa_mid:

    Miu_mid3 = 1
    Miu_high3 = 0

    print(Miu_mid3, Miu_high3)

    a3 = ["mid", Miu_mid3]
    b3 = ["high", Miu_high3]

# =================== TOEFL Low ====================

elif x3 in tpa_low:

    Miu_low3 = 1
    Miu_mid3 = 0

    print(Miu_low3, Miu_mid3)

    a3 = ["low", Miu_low3]
    b3 = ["mid", Miu_mid3]


#================== Rule in Main =========================

L, G = sending(
    a1[0], a1[1],
    b1[0], b1[1],
    a2[0], a2[1],
    b2[0], b2[1],
    a3[0], a3[1],
    b3[0], b3[1],
)

if G:
    G = max(G)
elif not G:
    G=0

if L:
    L = max(L)
elif not L:
    L=0

print("============ Defuzification ============")

print("Gagal = ", G)
print("Lolos = ", L)

a = 0
b = 100

y1 = ((b-a)*L)+a
y2 = b-((b-a)*G)

print("=========== Cara Sukamoto ================")

print("y1 = ", y1)
print("y2 = ", y2)

s_tar = ((L*y1)+(G*y2))/(L+G)
star = round(s_tar)
print(star)