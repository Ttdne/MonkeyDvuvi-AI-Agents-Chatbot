import pandas as pd

def merge_csv_remove_duplicates(file1, file2, output_file):
    # Đọc hai file CSV với encoding xử lý lỗi
    df1 = pd.read_csv(file1, encoding="utf-8")
    df2 = pd.read_csv(file2, encoding="utf-8")
    
    # Gộp hai bảng
    merged_df = pd.concat([df1, df2], ignore_index=True)
    
    # Loại bỏ bản ghi trùng lặp dựa trên trường 'Address'
    merged_df.drop_duplicates(subset=['Address'], keep='first', inplace=True)
    
    # Ghi vào file mới với UTF-8 encoding
    merged_df.to_csv(output_file, index=False, encoding="utf-8")
    print(f"Merged CSV saved to {output_file}")

# Ví dụ sử dụng
merge_csv_remove_duplicates("file1.csv", "file2.csv", "restaurant.csv")
