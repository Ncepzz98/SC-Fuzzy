def sending(
            a1, skor_a1,
            b1, skor_b1,
            a2, skor_a2,
            b2, skor_b2,
            a3, skor_a3,
            b3, skor_b3
):
    h_lolos = []
    h_gagal = []

#============== Rule A1 A2 A3 ======================================================================
    if a1 is "low" and a2 is "low" and a3 is "low":
         n = min(skor_a1,skor_a2,skor_a3)
         h_gagal.append(n)

    elif a1 is "low" and a2 is "low" and a3 is "mid":
         n = min(skor_a1,skor_a2,skor_a3)
         h_gagal.append(n)

    elif a1 is "low" and a2 is "low" and a3 is "high":
         n = min(skor_a1,skor_a2,skor_a3)
         h_gagal.append(n)

    elif a1 is "low" and a2 is "mid" and a3 is "low":
         n = min(skor_a1,skor_a2,skor_a3)
         h_gagal.append(n)

    elif a1 is "low" and a2 is "mid" and a3 is "mid":
         n = min(skor_a1,skor_a2,skor_a3)
         h_gagal.append(n)

    elif a1 is "low" and a2 is "mid" and a3 is "high":
         n = min(skor_a1, skor_a2, skor_a3)
         h_gagal.append(n)

    elif a1 is "low" and a2 is "high" and a3 is "low":
        n = min(skor_a1, skor_a2, skor_a3)
        h_gagal.append(n)

    elif a1 is "low" and a2 is "high" and a3 is "mid":
        n = min(skor_a1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif a1 is "low" and a2 is "high" and a3 is "high":
        n = min(skor_a1, skor_a2, skor_a3)
        h_lolos.append(n)

    #===================================================

    elif a1 is "mid" and a2 is "low" and a3 is "low":
        n = min(skor_a1, skor_a2, skor_a3)
        h_gagal.append(n)

    elif a1 is "mid" and a2 is "low" and a3 is "mid":
        n = min(skor_a1, skor_a2, skor_a3)
        h_gagal.append(n)

    elif a1 is "mid" and a2 is "low" and a3 is "high":
        n = min(skor_a1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif a1 is "mid" and a2 is "mid" and a3 is "low":
        n = min(skor_a1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif a1 is "mid" and a2 is "mid" and a3 is "mid":
        n = min(skor_a1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif a1 is "mid" and a2 is "mid" and a3 is "high":
        n = min(skor_a1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif a1 is "mid" and a2 is "high" and a3 is "low":
        n = min(skor_a1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif a1 is "mid" and a2 is "high" and a3 is "mid":
        n = min(skor_a1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif a1 is "mid" and a2 is "high" and a3 is "high":
        n = min(skor_a1, skor_a2, skor_a3)
        h_lolos.append(n)

    #===========================================================

    elif a1 is "high" and a2 is "low" and a3 is "low":
        n = min(skor_a1, skor_a2, skor_a3)
        h_gagal.append(n)

    elif a1 is "high" and a2 is "low" and a3 is "mid":
        n = min(skor_a1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif a1 is "high" and a2 is "low" and a3 is "high":
        n = min(skor_a1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif a1 is "high" and a2 is "mid" and a3 is "low":
        n = min(skor_a1, skor_a2, skor_a3)
        h_gagal.append(n)

    elif a1 is "high" and a2 is "mid" and a3 is "mid":
        n = min(skor_a1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif a1 is "high" and a2 is "mid" and a3 is "high":
        n = min(skor_a1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif a1 is "high" and a2 is "high" and a3 is "low":
        n = min(skor_a1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif a1 is "high" and a2 is "high" and a3 is "mid":
        n = min(skor_a1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif a1 is "high" and a2 is "high" and a3 is "high":
        n = min(skor_a1, skor_a2, skor_a3)
        h_lolos.append(n)


# ============== Rule A1 A2 B3 ===============================================================
    if a1 is "low" and a2 is "low" and b3 is "low":
        n = min(skor_a1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif a1 is "low" and a2 is "low" and b3 is "mid":
        n = min(skor_a1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif a1 is "low" and a2 is "low" and b3 is "high":
        n = min(skor_a1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif a1 is "low" and a2 is "mid" and b3 is "low":
        n = min(skor_a1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif a1 is "low" and a2 is "mid" and b3 is "mid":
        n = min(skor_a1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif a1 is "low" and a2 is "mid" and b3 is "high":
        n = min(skor_a1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif a1 is "low" and a2 is "high" and b3 is "low":
        n = min(skor_a1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif a1 is "low" and a2 is "high" and b3 is "mid":
        n = min(skor_a1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif a1 is "low" and a2 is "high" and b3 is "high":
        n = min(skor_a1, skor_a2, skor_b3)
        h_lolos.append(n)

    # ===================================================

    elif a1 is "mid" and a2 is "low" and b3 is "low":
        n = min(skor_a1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif a1 is "mid" and a2 is "low" and b3 is "mid":
        n = min(skor_a1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif a1 is "mid" and a2 is "low" and b3 is "high":
        n = min(skor_a1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif a1 is "mid" and a2 is "mid" and b3 is "low":
        n = min(skor_a1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif a1 is "mid" and a2 is "mid" and b3 is "mid":
        n = min(skor_a1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif a1 is "mid" and a2 is "mid" and b3 is "high":
        n = min(skor_a1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif a1 is "mid" and a2 is "high" and b3 is "low":
        n = min(skor_a1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif a1 is "mid" and a2 is "high" and b3 is "mid":
        n = min(skor_a1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif a1 is "mid" and a2 is "high" and b3 is "high":
        n = min(skor_a1, skor_a2, skor_b3)
        h_lolos.append(n)

    # ===========================================================

    elif a1 is "high" and a2 is "low" and b3 is "low":
        n = min(skor_a1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif a1 is "high" and a2 is "low" and b3 is "mid":
        n = min(skor_a1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif a1 is "high" and a2 is "low" and b3 is "high":
        n = min(skor_a1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif a1 is "high" and a2 is "mid" and b3 is "low":
        n = min(skor_a1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif a1 is "high" and a2 is "mid" and b3 is "mid":
        n = min(skor_a1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif a1 is "high" and a2 is "mid" and b3 is "high":
        n = min(skor_a1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif a1 is "high" and a2 is "high" and b3 is "low":
        n = min(skor_a1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif a1 is "high" and a2 is "high" and b3 is "mid":
        n = min(skor_a1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif a1 is "high" and a2 is "high" and b3 is "high":
        n = min(skor_a1, skor_a2, skor_b3)
        h_lolos.append(n)


# ============== Rule A1 B2 A3 ===============================================================
    if a1 is "low" and b2 is "low" and a3 is "low":
        n = min(skor_a1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif a1 is "low" and b2 is "low" and a3 is "mid":
        n = min(skor_a1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif a1 is "low" and b2 is "low" and a3 is "high":
        n = min(skor_a1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif a1 is "low" and b2 is "mid" and a3 is "low":
        n = min(skor_a1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif a1 is "low" and b2 is "mid" and a3 is "mid":
        n = min(skor_a1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif a1 is "low" and b2 is "mid" and a3 is "high":
        n = min(skor_a1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif a1 is "low" and b2 is "high" and a3 is "low":
        n = min(skor_a1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif a1 is "low" and b2 is "high" and a3 is "mid":
        n = min(skor_a1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif a1 is "low" and b2 is "high" and a3 is "high":
        n = min(skor_a1, skor_b2, skor_a3)
        h_lolos.append(n)

    # ===================================================

    elif a1 is "mid" and b2 is "low" and a3 is "low":
        n = min(skor_a1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif a1 is "mid" and b2 is "low" and a3 is "mid":
        n = min(skor_a1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif a1 is "mid" and b2 is "low" and a3 is "high":
        n = min(skor_a1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif a1 is "mid" and b2 is "mid" and a3 is "low":
        n = min(skor_a1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif a1 is "mid" and b2 is "mid" and a3 is "mid":
        n = min(skor_a1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif a1 is "mid" and b2 is "mid" and a3 is "high":
        n = min(skor_a1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif a1 is "mid" and b2 is "high" and a3 is "low":
        n = min(skor_a1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif a1 is "mid" and b2 is "high" and a3 is "mid":
        n = min(skor_a1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif a1 is "mid" and b2 is "high" and a3 is "high":
        n = min(skor_a1, skor_b2, skor_a3)
        h_lolos.append(n)

    # ===========================================================

    elif a1 is "high" and b2 is "low" and a3 is "low":
        n = min(skor_a1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif a1 is "high" and b2 is "low" and a3 is "mid":
        n = min(skor_a1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif a1 is "high" and b2 is "low" and a3 is "high":
        n = min(skor_a1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif a1 is "high" and b2 is "mid" and a3 is "low":
        n = min(skor_a1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif a1 is "high" and b2 is "mid" and a3 is "mid":
        n = min(skor_a1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif a1 is "high" and b2 is "mid" and a3 is "high":
        n = min(skor_a1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif a1 is "high" and b2 is "high" and a3 is "low":
        n = min(skor_a1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif a1 is "high" and b2 is "high" and a3 is "mid":
        n = min(skor_a1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif a1 is "high" and b2 is "high" and a3 is "high":
        n = min(skor_a1, skor_b2, skor_a3)
        h_lolos.append(n)

# ============== Rule A1 B2 B3 ===============================================================
    if a1 is "low" and b2 is "low" and b3 is "low":
        n = min(skor_a1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif a1 is "low" and b2 is "low" and b3 is "mid":
        n = min(skor_a1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif a1 is "low" and b2 is "low" and b3 is "high":
        n = min(skor_a1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif a1 is "low" and b2 is "mid" and b3 is "low":
        n = min(skor_a1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif a1 is "low" and b2 is "mid" and b3 is "mid":
        n = min(skor_a1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif a1 is "low" and b2 is "mid" and b3 is "high":
        n = min(skor_a1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif a1 is "low" and b2 is "high" and b3 is "low":
        n = min(skor_a1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif a1 is "low" and b2 is "high" and b3 is "mid":
        n = min(skor_a1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif a1 is "low" and b2 is "high" and b3 is "high":
        n = min(skor_a1, skor_b2, skor_b3)
        h_lolos.append(n)

    # ===================================================

    elif a1 is "mid" and b2 is "low" and b3 is "low":
        n = min(skor_a1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif a1 is "mid" and b2 is "low" and b3 is "mid":
        n = min(skor_a1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif a1 is "mid" and b2 is "low" and b3 is "high":
        n = min(skor_a1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif a1 is "mid" and b2 is "mid" and b3 is "low":
        n = min(skor_a1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif a1 is "mid" and b2 is "mid" and b3 is "mid":
        n = min(skor_a1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif a1 is "mid" and b2 is "mid" and b3 is "high":
        n = min(skor_a1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif a1 is "mid" and b2 is "high" and b3 is "low":
        n = min(skor_a1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif a1 is "mid" and b2 is "high" and b3 is "mid":
        n = min(skor_a1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif a1 is "mid" and b2 is "high" and b3 is "high":
        n = min(skor_a1, skor_b2, skor_b3)
        h_lolos.append(n)

    # ===========================================================

    elif a1 is "high" and b2 is "low" and b3 is "low":
        n = min(skor_a1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif a1 is "high" and b2 is "low" and b3 is "mid":
        n = min(skor_a1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif a1 is "high" and b2 is "low" and b3 is "high":
        n = min(skor_a1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif a1 is "high" and b2 is "mid" and b3 is "low":
        n = min(skor_a1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif a1 is "high" and b2 is "mid" and b3 is "mid":
        n = min(skor_a1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif a1 is "high" and b2 is "mid" and b3 is "high":
        n = min(skor_a1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif a1 is "high" and b2 is "high" and b3 is "low":
        n = min(skor_a1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif a1 is "high" and b2 is "high" and b3 is "mid":
        n = min(skor_a1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif a1 is "high" and b2 is "high" and b3 is "high":
        n = min(skor_a1, skor_b2, skor_b3)
        h_lolos.append(n)

# ============== Rule B1 A2 A3 ===============================================================
    if b1 is "low" and a2 is "low" and a3 is "low":
        n = min(skor_b1, skor_a2, skor_a3)
        h_gagal.append(n)

    elif b1 is "low" and a2 is "low" and a3 is "mid":
        n = min(skor_b1, skor_a2, skor_a3)
        h_gagal.append(n)

    elif b1 is "low" and a2 is "low" and a3 is "high":
        n = min(skor_b1, skor_a2, skor_a3)
        h_gagal.append(n)

    elif b1 is "low" and a2 is "mid" and a3 is "low":
        n = min(skor_b1, skor_a2, skor_a3)
        h_gagal.append(n)

    elif b1 is "low" and a2 is "mid" and a3 is "mid":
        n = min(skor_b1, skor_a2, skor_a3)
        h_gagal.append(n)

    elif b1 is "low" and a2 is "mid" and a3 is "high":
        n = min(skor_b1, skor_a2, skor_a3)
        h_gagal.append(n)

    elif b1 is "low" and a2 is "high" and a3 is "low":
        n = min(skor_b1, skor_a2, skor_a3)
        h_gagal.append(n)

    elif b1 is "low" and a2 is "high" and a3 is "mid":
        n = min(skor_b1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif b1 is "low" and a2 is "high" and a3 is "high":
        n = min(skor_b1, skor_a2, skor_a3)
        h_lolos.append(n)

    # ===================================================

    elif b1 is "mid" and a2 is "low" and a3 is "low":
        n = min(skor_b1, skor_a2, skor_a3)
        h_gagal.append(n)

    elif b1 is "mid" and a2 is "low" and a3 is "mid":
        n = min(skor_b1, skor_a2, skor_a3)
        h_gagal.append(n)

    elif b1 is "mid" and a2 is "low" and a3 is "high":
        n = min(skor_b1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif b1 is "mid" and a2 is "mid" and a3 is "low":
        n = min(skor_b1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif b1 is "mid" and a2 is "mid" and a3 is "mid":
        n = min(skor_b1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif b1 is "mid" and a2 is "mid" and a3 is "high":
        n = min(skor_b1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif b1 is "mid" and a2 is "high" and a3 is "low":
        n = min(skor_b1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif b1 is "mid" and a2 is "high" and a3 is "mid":
        n = min(skor_b1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif b1 is "mid" and a2 is "high" and a3 is "high":
        n = min(skor_b1, skor_a2, skor_a3)
        h_lolos.append(n)

    # ===========================================================

    elif b1 is "high" and a2 is "low" and a3 is "low":
        n = min(skor_b1, skor_a2, skor_a3)
        h_gagal.append(n)

    elif b1 is "high" and a2 is "low" and a3 is "mid":
        n = min(skor_b1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif b1 is "high" and a2 is "low" and a3 is "high":
        n = min(skor_b1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif b1 is "high" and a2 is "mid" and a3 is "low":
        n = min(skor_b1, skor_a2, skor_a3)
        h_gagal.append(n)

    elif b1 is "high" and a2 is "mid" and a3 is "mid":
        n = min(skor_b1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif b1 is "high" and a2 is "mid" and a3 is "high":
        n = min(skor_b1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif b1 is "high" and a2 is "high" and a3 is "low":
        n = min(skor_b1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif b1 is "high" and a2 is "high" and a3 is "mid":
        n = min(skor_b1, skor_a2, skor_a3)
        h_lolos.append(n)

    elif b1 is "high" and a2 is "high" and a3 is "high":
        n = min(skor_b1, skor_a2, skor_a3)
        h_lolos.append(n)

# ============== Rule B1 A2 B3 ===============================================================
    if b1 is "low" and a2 is "low" and b3 is "low":
        n = min(skor_b1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif b1 is "low" and a2 is "low" and b3 is "mid":
        n = min(skor_b1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif b1 is "low" and a2 is "low" and b3 is "high":
        n = min(skor_b1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif b1 is "low" and a2 is "mid" and b3 is "low":
        n = min(skor_b1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif b1 is "low" and a2 is "mid" and b3 is "mid":
        n = min(skor_b1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif b1 is "low" and a2 is "mid" and b3 is "high":
        n = min(skor_b1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif b1 is "low" and a2 is "high" and b3 is "low":
        n = min(skor_b1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif b1 is "low" and a2 is "high" and b3 is "mid":
        n = min(skor_b1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif b1 is "low" and a2 is "high" and b3 is "high":
        n = min(skor_b1, skor_a2, skor_b3)
        h_lolos.append(n)

    # ===================================================

    elif b1 is "mid" and a2 is "low" and b3 is "low":
        n = min(skor_b1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif b1 is "mid" and a2 is "low" and b3 is "mid":
        n = min(skor_b1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif b1 is "mid" and a2 is "low" and b3 is "high":
        n = min(skor_b1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif b1 is "mid" and a2 is "mid" and b3 is "low":
        n = min(skor_b1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif b1 is "mid" and a2 is "mid" and b3 is "mid":
        n = min(skor_b1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif b1 is "mid" and a2 is "mid" and b3 is "high":
        n = min(skor_b1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif b1 is "mid" and a2 is "high" and b3 is "low":
        n = min(skor_b1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif b1 is "mid" and a2 is "high" and b3 is "mid":
        n = min(skor_b1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif b1 is "mid" and a2 is "high" and b3 is "high":
        n = min(skor_b1, skor_a2, skor_b3)
        h_lolos.append(n)

    # ===========================================================

    elif b1 is "high" and a2 is "low" and b3 is "low":
        n = min(skor_b1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif b1 is "high" and a2 is "low" and b3 is "mid":
        n = min(skor_b1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif b1 is "high" and a2 is "low" and b3 is "high":
        n = min(skor_b1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif b1 is "high" and a2 is "mid" and b3 is "low":
        n = min(skor_b1, skor_a2, skor_b3)
        h_gagal.append(n)

    elif b1 is "high" and a2 is "mid" and b3 is "mid":
        n = min(skor_b1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif b1 is "high" and a2 is "mid" and b3 is "high":
        n = min(skor_b1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif b1 is "high" and a2 is "high" and b3 is "low":
        n = min(skor_b1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif b1 is "high" and a2 is "high" and b3 is "mid":
        n = min(skor_b1, skor_a2, skor_b3)
        h_lolos.append(n)

    elif b1 is "high" and a2 is "high" and b3 is "high":
        n = min(skor_b1, skor_a2, skor_b3)
        h_lolos.append(n)

# ============== Rule B1 B2 A3 ===============================================================
    if b1 is "low" and b2 is "low" and a3 is "low":
        n = min(skor_b1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif b1 is "low" and b2 is "low" and a3 is "mid":
        n = min(skor_b1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif b1 is "low" and b2 is "low" and a3 is "high":
        n = min(skor_b1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif b1 is "low" and b2 is "mid" and a3 is "low":
        n = min(skor_b1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif b1 is "low" and b2 is "mid" and a3 is "mid":
        n = min(skor_b1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif b1 is "low" and b2 is "mid" and a3 is "high":
        n = min(skor_b1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif b1 is "low" and b2 is "high" and a3 is "low":
        n = min(skor_b1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif b1 is "low" and b2 is "high" and a3 is "mid":
        n = min(skor_b1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif b1 is "low" and b2 is "high" and a3 is "high":
        n = min(skor_b1, skor_b2, skor_a3)
        h_lolos.append(n)

    # ===================================================

    elif b1 is "mid" and b2 is "low" and a3 is "low":
        n = min(skor_b1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif b1 is "mid" and b2 is "low" and a3 is "mid":
        n = min(skor_b1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif b1 is "mid" and b2 is "low" and a3 is "high":
        n = min(skor_b1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif b1 is "mid" and b2 is "mid" and a3 is "low":
        n = min(skor_b1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif b1 is "mid" and b2 is "mid" and a3 is "mid":
        n = min(skor_b1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif b1 is "mid" and b2 is "mid" and a3 is "high":
        n = min(skor_b1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif b1 is "mid" and b2 is "high" and a3 is "low":
        n = min(skor_b1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif b1 is "mid" and b2 is "high" and a3 is "mid":
        n = min(skor_b1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif b1 is "mid" and b2 is "high" and a3 is "high":
        n = min(skor_b1, skor_b2, skor_a3)
        h_lolos.append(n)

    # ===========================================================

    elif b1 is "high" and b2 is "low" and a3 is "low":
        n = min(skor_b1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif b1 is "high" and b2 is "low" and a3 is "mid":
        n = min(skor_b1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif b1 is "high" and b2 is "low" and a3 is "high":
        n = min(skor_b1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif b1 is "high" and b2 is "mid" and a3 is "low":
        n = min(skor_b1, skor_b2, skor_a3)
        h_gagal.append(n)

    elif b1 is "high" and b2 is "mid" and a3 is "mid":
        n = min(skor_b1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif b1 is "high" and b2 is "mid" and a3 is "high":
        n = min(skor_b1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif b1 is "high" and b2 is "high" and a3 is "low":
        n = min(skor_b1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif b1 is "high" and b2 is "high" and a3 is "mid":
        n = min(skor_b1, skor_b2, skor_a3)
        h_lolos.append(n)

    elif b1 is "high" and b2 is "high" and a3 is "high":
        n = min(skor_b1, skor_b2, skor_a3)
        h_lolos.append(n)

# ============== Rule B1 B2 B3 ===============================================================
    if b1 is "low" and b2 is "low" and b3 is "low":
        n = min(skor_b1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif b1 is "low" and b2 is "low" and b3 is "mid":
        n = min(skor_b1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif b1 is "low" and b2 is "low" and b3 is "high":
        n = min(skor_b1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif b1 is "low" and b2 is "mid" and b3 is "low":
        n = min(skor_b1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif b1 is "low" and b2 is "mid" and b3 is "mid":
        n = min(skor_b1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif b1 is "low" and b2 is "mid" and b3 is "high":
        n = min(skor_b1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif b1 is "low" and b2 is "high" and b3 is "low":
        n = min(skor_b1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif b1 is "low" and b2 is "high" and b3 is "mid":
        n = min(skor_b1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif b1 is "low" and b2 is "high" and b3 is "high":
        n = min(skor_b1, skor_b2, skor_b3)
        h_lolos.append(n)

    # ===================================================

    elif b1 is "mid" and b2 is "low" and b3 is "low":
        n = min(skor_b1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif b1 is "mid" and b2 is "low" and b3 is "mid":
        n = min(skor_b1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif b1 is "mid" and b2 is "low" and b3 is "high":
        n = min(skor_b1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif b1 is "mid" and b2 is "mid" and b3 is "low":
        n = min(skor_b1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif b1 is "mid" and b2 is "mid" and b3 is "mid":
        n = min(skor_b1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif b1 is "mid" and b2 is "mid" and b3 is "high":
        n = min(skor_b1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif b1 is "mid" and b2 is "high" and b3 is "low":
        n = min(skor_b1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif b1 is "mid" and b2 is "high" and b3 is "mid":
        n = min(skor_b1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif b1 is "mid" and b2 is "high" and b3 is "high":
        n = min(skor_b1, skor_b2, skor_b3)
        h_lolos.append(n)

    # ===========================================================

    elif b1 is "high" and b2 is "low" and b3 is "low":
        n = min(skor_b1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif b1 is "high" and b2 is "low" and b3 is "mid":
        n = min(skor_b1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif b1 is "high" and b2 is "low" and b3 is "high":
        n = min(skor_b1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif b1 is "high" and b2 is "mid" and b3 is "low":
        n = min(skor_b1, skor_b2, skor_b3)
        h_gagal.append(n)

    elif b1 is "high" and b2 is "mid" and b3 is "mid":
        n = min(skor_b1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif b1 is "high" and b2 is "mid" and b3 is "high":
        n = min(skor_b1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif b1 is "high" and b2 is "high" and b3 is "low":
        n = min(skor_b1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif b1 is "high" and b2 is "high" and b3 is "mid":
        n = min(skor_b1, skor_b2, skor_b3)
        h_lolos.append(n)

    elif b1 is "high" and b2 is "high" and b3 is "high":
        n = min(skor_b1, skor_b2, skor_b3)
        h_lolos.append(n)

    return h_lolos, h_gagal

