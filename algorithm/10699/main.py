from datetime import datetime, timedelta

# 입력된 날짜와 시간 문자열
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 입력된 날짜와 시간을 datetime 객체로 변환 (시간대는 UTC+0)
dt = datetime.strptime(now,"%Y-%m-%d %H:%M:%S")

# KST로 시간대 변경 (UTC+9)
kst_offset = timedelta(hours=9)  # KST의 시간 차이
kst_dt = dt + kst_offset

output_date = kst_dt.strftime('%Y-%m-%d')
print(output_date)