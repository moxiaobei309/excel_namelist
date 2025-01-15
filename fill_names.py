import openpyxl
import os

def fill_names_to_excel():
    """
    将 name.txt 文件中的人名填充到 data.xlsx 的 Sheet1 工作表中
    从 A1 单元格开始按列向下填充
    """
    try:
        # 检查 name.txt 文件是否存在
        if not os.path.exists('name.txt'):
            print("错误：name.txt 文件不存在")
            return

        # 读取 name.txt 文件并处理
        names = []
        with open('name.txt', 'r', encoding='utf-8') as file:
            for line in file:
                # 去除空白字符并按空格分割
                line = line.strip()
                if line:
                    # 将每行的多个名字分开
                    names.extend(name for name in line.split() if name)

        # 如果没有读取到任何姓名
        if not names:
            print("警告：name.txt 文件中没有找到有效的姓名")
            return

        # 创建新的 Excel 工作簿
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = 'Sheet1'

        # 从 A1 单元格开始填充姓名
        for index, name in enumerate(names, start=1):
            sheet[f'A{index}'] = name

        # 保存 Excel 文件
        workbook.save('data.xlsx')
        print(f"成功：已将 {len(names)} 个姓名写入 data.xlsx")

    except PermissionError:
        print("错误：无法写入文件，请检查文件是否被其他程序打开")
    except Exception as e:
        print(f"发生未知错误：{str(e)}")

if __name__ == '__main__':
    fill_names_to_excel()
