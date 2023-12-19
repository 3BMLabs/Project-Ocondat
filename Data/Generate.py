import pandas as pd

excel_file_path = 'Steelprofiles.xlsx'

worksheet_name = 'I-shape_parallel_flange'

df = pd.read_excel(excel_file_path, sheet_name=worksheet_name)

fourth_row = df.iloc[3]
print(fourth_row)
value_in_q_column = fourth_row['JSONString']

# print("Value in the 'Q' column of the fourth row:", value_in_q_column)
