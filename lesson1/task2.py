total_seconds = int(input("Пожалуйста, введите время в секундах"))
hours = total_seconds // 3600
minutes = total_seconds % 3600 // 60
seconds = total_seconds % 3600 % 60
print(f"hh {hours:02d} mm {minutes:02d} ss {seconds:02d}")


