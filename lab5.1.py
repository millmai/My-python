def calculate_average_scores():
    n = int(input("ป้อนจำนวนนักศึกษา: "))
    
    if n <= 0:
        print("จำนวนนักศึกษาต้องมากกว่า 0")
        return
    
    sum_scores = 0  # ตัวแปร sum สำหรับเก็บผลรวมคะแนน เริ่มต้นที่ 0
    
    for i in range(n):
        score = float(input(f"ป้อนคะแนนของนักศึกษาที่ {i+1}: "))
        sum_scores += score  # เพิ่มคะแนนเข้าไปในผลรวม
    
    average_score = sum_scores / n  # คำนวณคะแนนเฉลี่ย
    print(f"คะแนนเฉลี่ยของนักศึกษา {n} คน คือ {average_score:.2f}")

# เรียกใช้ฟังก์ชันเพื่อทดสอบ
calculate_average_scores()