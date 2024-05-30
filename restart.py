import os


def delete_files(file_names, folders):
    for folder in folders:
        for file_name in file_names:
            file_path = os.path.join(folder, file_name)
            try:
                os.remove(file_path)
                print(f"File {file_path} Удаление прошло успешно!")
            except FileNotFoundError:
                print(f"File {file_path} Файл не найден")
            except Exception as e:
                print(f" Произошла ошибка при удалении {file_path}: {e}")


if __name__ == "__main__":
    file_names_to_delete = ["0001_initial.py", "0002_initial.py", "db.sqlite3"]
    folders_to_search = [".", "apps/vacancy/migrations", "apps/product/migrations", "apps/production/migrations",
                         "apps/partners/migrations", "apps/news/migrations", "apps/flavor/migrations",
                         "apps/content/migrations", "apps/company_info/migrations", "apps/communication/migrations",
                         "apps/brand_info/migrations", "apps/brand/migrations", "apps/advantages/migrations",
                         "apps/language/migrations"]

    delete_files(file_names_to_delete, folders_to_search)
