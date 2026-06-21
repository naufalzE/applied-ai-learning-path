import numpy as np
def latihan(data,target):
    
    total = data.sum()
    rata_rata = data.mean()
    produktif_mask = (data >= 60)
    produktif = produktif_mask.sum()
    target = (target <= total)
    print(f"""
        
    === STUDY ANALYTICS REPORT ===

    Total Minutes          : {total}
    Average Minutes        : {rata_rata}
    Productive Days Count  : {produktif}
    Productive Days Mask   : {produktif_mask}
    Target Reached         : {target}
    """)
durasi_belajar = np.array([20, 75, 0, 90, 45, 120, 30])
target = int(input("masukan target  : "))
latihan(durasi_belajar,target)
