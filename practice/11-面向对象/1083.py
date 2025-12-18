# 题目描述
# 实现一个图书馆管理系统，包含图书类、借阅记录类和图书馆管理类，要求实现图书管理、借阅、归还、查询等功能。
# 类定义要求
# 1.Book类：
#     属性：isbn (ISBN号), title (书名), author (作者), is_borrowed (是否被借出)
#     方法：
#
#     __init__(self, isbn, title, author)
#     __str__(self): 返回图书信息字符串
#
# 2.BorrowRecord 类：
#     属性：record_id (记录ID), book_isbn (图书ISBN), borrower_id (借阅者ID), borrow_date (借阅日期), return_date (归还日期，初始为None)
#     方法：
#
#     __init__(self, record_id, book_isbn, borrower_id, borrow_date)
#     mark_returned(self, return_date): 标记为已归还
#
# 3.Library 类：
#     属性：
#
#     books (字典): ISBN到Book对象的映射
#     borrow_records (字典): record_id到BorrowRecord对象的映射
#     next_record_id (整数): 下一个可用的记录ID，初始化为1
#
#     方法：
#
#     add_book(self, isbn, title, author): 添加图书
#     remove_book(self, isbn): 移除图书
#     borrow_book(self, isbn, borrower_id, borrow_date): 借阅图书
#     return_book(self, isbn, borrower_id, return_date): 归还图书
#     search_books(self, keyword): 搜索图书
#     list_available_books(self): 列出可借图书
#     list_borrowed_books(self): 列出已借出图书
#     get_borrow_history(self, borrower_id): 获取借阅历史
#
# 程序如下：
#
# class Book:
#     """图书类"""
#     def __init__(self, isbn, title, author):
#         self.isbn = isbn
#         self.title = title
#         self.author = author
#         self.is_borrowed = False
#         self.current_borrower = None  # 当前借阅者ID
#     def __str__(self):
#         status = "Borrowed by " + self.current_borrower if self.is_borrowed else "Available"
#         return f'{self.isbn} "{self.title}" by {self.author} - {status}'
# class BorrowRecord:
#     """借阅记录类"""
#
# class Library:
#     """图书馆管理类"""
#     def __init__(self):
#         self.books = {}  # ISBN -> Book对象
#         self.borrow_records = {}  # record_id -> BorrowRecord对象
#         self.next_record_id = 1
#         # 存储每个借阅者的借阅记录ID列表
#         self.borrower_records = {}  # borrower_id -> [record_ids]
#
# class LibraryManagementSystem:
#     """图书馆管理系统主类"""
#     def __init__(self):
#         self.library = Library()
#     def process_command(self, command):
#         """处理命令"""
#         parts = command.strip().split()
#         if not parts:
#             return ""
#         cmd = parts[0]
#         try:
#             if cmd == "ADD_BOOK":
#                 if len(parts) < 4:
#                     return "Error: ADD_BOOK command requires at least 3 arguments"
#                 isbn = parts[1]
#                 # 处理带引号的标题
#                 title_parts = []
#                 i = 2
#                 while i < len(parts) and parts[2].startswith('"') and not parts[i].endswith('"'):
#                     i += 1
#                 title = ' '.join(parts[2:i+1]).strip('"')
#                 author = ' '.join(parts[i+1:]) if len(parts) > i else "Unknown"
#                 success, message = self.library.add_book(isbn, title, author)
#                 return message
#
#             elif cmd == "REMOVE_BOOK":
#                 if len(parts) != 2:
#                     return "Error: REMOVE_BOOK command requires 1 argument"
#
#                 isbn = parts[1]
#                 success, message = self.library.remove_book(isbn)
#                 return message
#             elif cmd == "BORROW":
#                 if len(parts) != 4:
#                     return "Error: BORROW command requires 3 arguments"
#                 isbn = parts[1]
#                 borrower_id = parts[2]
#                 borrow_date = parts[3]
#                 success, message = self.library.borrow_book(isbn, borrower_id, borrow_date)
#                 return message
#             elif cmd == "RETURN":
#                 if len(parts) != 4:
#                     return "Error: RETURN command requires 3 arguments"
#                 isbn = parts[1]
#                 borrower_id = parts[2]
#                 return_date = parts[3]
#                 success, message = self.library.return_book(isbn, borrower_id, return_date)
#                 return message
#
#             elif cmd == "SEARCH":
#                 if len(parts) < 2:
#                     return "Error: SEARCH command requires at least 1 argument"
#                 keyword = ' '.join(parts[1:])
#                 results = self.library.search_books(keyword)
#                 return '\n'.join(results) if results else "No books found"
#
#             elif cmd == "LIST_AVAILABLE":
#                 results = self.library.list_available_books()
#                 return '\n'.join(results) if results else "No available books"
#             elif cmd == "LIST_BORROWED":
#                 results = self.library.list_borrowed_books()
#                 return '\n'.join(results) if results else "No borrowed books"
#             elif cmd == "HISTORY":
#                 if len(parts) != 2:
#                     return "Error: HISTORY command requires 1 argument"
#
#                 borrower_id = parts[1]
#                 history = self.library.get_borrow_history(borrower_id)
#                 return '\n'.join(history) if history else "No borrow history"
#             elif cmd == "EXIT":
#                 return "EXIT"
#             else:
#                 return f"Error: Unknown command {cmd}"
#         except Exception as e:
#             return f"Error: {str(e)}"
# def main():
#     """主函数"""
#     system = LibraryManagementSystem()
#     while True:
#         try:
#             line = input().strip()
#             if not line:
#                 continue
#             result = system.process_command(line)
#             if result == "EXIT":
#                 break
#             if result:  # 只输出非空结果
#                 print(result)
#         except EOFError:
#             break
# if __name__ == "__main__":
#     main()
class Book:
    """图书类"""

    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.current_borrower = None  # 当前借阅者ID

    def __str__(self):
        # 根据上下文决定输出格式
        # 在search和list_available中显示简单状态，在list_borrowed中显示详细状态
        if self.is_borrowed:
            # 这里返回简单状态，详细状态在Library类中处理
            status = "Borrowed"
        else:
            status = "Available"
        return f'{self.isbn} "{self.title}" by {self.author} - {status}'


class BorrowRecord:
    """借阅记录类"""

    def __init__(self, record_id, book_isbn, borrower_id, borrow_date):
        self.record_id = record_id
        self.book_isbn = book_isbn
        self.borrower_id = borrower_id
        self.borrow_date = borrow_date
        self.return_date = None

    def mark_returned(self, return_date):
        """标记为已归还"""
        self.return_date = return_date

    def __str__(self):
        return_date_str = self.return_date if self.return_date else "None"
        return f"{self.record_id}: {self.book_isbn} borrowed on {self.borrow_date} returned on {return_date_str}"


class Library:
    """图书馆管理类"""

    def __init__(self):
        self.books = {}  # ISBN -> Book对象
        self.borrow_records = {}  # record_id -> BorrowRecord对象
        self.next_record_id = 1
        # 存储每个借阅者的借阅记录ID列表
        self.borrower_records = {}  # borrower_id -> [record_ids]

    def add_book(self, isbn, title, author):
        """添加图书"""
        if isbn in self.books:
            return False, f"Error: Book {isbn} already exists"
        self.books[isbn] = Book(isbn, title, author)
        return True, f"Book {isbn} added"

    def remove_book(self, isbn):
        """移除图书"""
        if isbn not in self.books:
            return False, f"Error: Book {isbn} not found"

        book = self.books[isbn]
        if book.is_borrowed:
            return False, f"Error: Book {isbn} is borrowed"

        del self.books[isbn]
        return True, f"Book {isbn} removed"

    def borrow_book(self, isbn, borrower_id, borrow_date):
        """借阅图书"""
        if isbn not in self.books:
            return False, f"Error: Book {isbn} not found"

        book = self.books[isbn]
        if book.is_borrowed:
            return False, f"Error: Book {isbn} is already borrowed"

        # 更新图书状态
        book.is_borrowed = True
        book.current_borrower = borrower_id

        # 创建借阅记录
        record_id = self.next_record_id
        self.next_record_id += 1
        record = BorrowRecord(record_id, isbn, borrower_id, borrow_date)
        self.borrow_records[record_id] = record

        # 更新借阅者记录
        if borrower_id not in self.borrower_records:
            self.borrower_records[borrower_id] = []
        self.borrower_records[borrower_id].append(record_id)

        return True, f"Book {isbn} borrowed by {borrower_id}"

    def return_book(self, isbn, borrower_id, return_date):
        """归还图书"""
        if isbn not in self.books:
            return False, f"Error: Book {isbn} not found"

        book = self.books[isbn]
        if not book.is_borrowed:
            return False, f"Error: Book {isbn} is not borrowed"

        # 检查借阅者ID是否匹配
        if book.current_borrower != borrower_id:
            return False, f"Error: Book {isbn} is not borrowed by {borrower_id}"

        # 更新图书状态
        book.is_borrowed = False
        book.current_borrower = None

        # 找到未归还的记录并标记为已归还
        for record_id, record in self.borrow_records.items():
            if record.book_isbn == isbn and record.borrower_id == borrower_id and record.return_date is None:
                record.mark_returned(return_date)
                break

        return True, f"Book {isbn} returned by {borrower_id}"

    def search_books(self, keyword):
        """搜索图书"""
        results = []
        for book in self.books.values():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                # 搜索时显示简单状态
                if book.is_borrowed:
                    status = "Borrowed"
                else:
                    status = "Available"
                results.append(f'{book.isbn} "{book.title}" by {book.author} - {status}')
        return results

    def list_available_books(self):
        """列出可借图书"""
        results = []
        for book in self.books.values():
            if not book.is_borrowed:
                results.append(str(book))
        return results

    def list_borrowed_books(self):
        """列出已借出图书"""
        results = []
        for book in self.books.values():
            if book.is_borrowed:
                # 已借出图书显示借阅者ID
                results.append(f'{book.isbn} "{book.title}" by {book.author} - Borrowed by {book.current_borrower}')
        return results

    def get_borrow_history(self, borrower_id):
        """获取借阅历史"""
        if borrower_id not in self.borrower_records:
            return []

        history = []
        for record_id in self.borrower_records[borrower_id]:
            record = self.borrow_records[record_id]
            history.append(str(record))
        return history


class LibraryManagementSystem:
    """图书馆管理系统主类"""

    def __init__(self):
        self.library = Library()

    def process_command(self, command):
        """处理命令"""
        parts = command.strip().split()
        if not parts:
            return ""
        cmd = parts[0]
        try:
            if cmd == "ADD_BOOK":
                if len(parts) < 4:
                    return "Error: ADD_BOOK command requires at least 3 arguments"
                isbn = parts[1]
                # 处理带引号的标题
                if parts[2].startswith('"'):
                    i = 2
                    while i < len(parts) and not parts[i].endswith('"'):
                        i += 1
                    title = ' '.join(parts[2:i + 1]).strip('"')
                    author = ' '.join(parts[i + 1:]) if i + 1 < len(parts) else "Unknown"
                else:
                    title = parts[2]
                    author = ' '.join(parts[3:]) if len(parts) > 3 else "Unknown"
                success, message = self.library.add_book(isbn, title, author)
                return message

            elif cmd == "REMOVE_BOOK":
                if len(parts) != 2:
                    return "Error: REMOVE_BOOK command requires 1 argument"
                isbn = parts[1]
                success, message = self.library.remove_book(isbn)
                return message

            elif cmd == "BORROW":
                if len(parts) != 4:
                    return "Error: BORROW command requires 3 arguments"
                isbn = parts[1]
                borrower_id = parts[2]
                borrow_date = parts[3]
                success, message = self.library.borrow_book(isbn, borrower_id, borrow_date)
                return message

            elif cmd == "RETURN":
                if len(parts) != 4:
                    return "Error: RETURN command requires 3 arguments"
                isbn = parts[1]
                borrower_id = parts[2]
                return_date = parts[3]
                success, message = self.library.return_book(isbn, borrower_id, return_date)
                return message

            elif cmd == "SEARCH":
                if len(parts) < 2:
                    return "Error: SEARCH command requires at least 1 argument"
                keyword = ' '.join(parts[1:])
                results = self.library.search_books(keyword)
                return '\n'.join(results) if results else "No books found"

            elif cmd == "LIST_AVAILABLE":
                results = self.library.list_available_books()
                return '\n'.join(results) if results else "No available books"

            elif cmd == "LIST_BORROWED":
                results = self.library.list_borrowed_books()
                return '\n'.join(results) if results else "No borrowed books"

            elif cmd == "HISTORY":
                if len(parts) != 2:
                    return "Error: HISTORY command requires 1 argument"
                borrower_id = parts[1]
                history = self.library.get_borrow_history(borrower_id)
                return '\n'.join(history) if history else "No borrow history"

            elif cmd == "EXIT":
                return "EXIT"
            else:
                return f"Error: Unknown command {cmd}"
        except Exception as e:
            return f"Error: {str(e)}"


def main():
    """主函数"""
    system = LibraryManagementSystem()
    while True:
        try:
            line = input().strip()
            if not line:
                continue
            result = system.process_command(line)
            if result == "EXIT":
                break
            if result:  # 只输出非空结果
                print(result)
        except EOFError:
            break


if __name__ == "__main__":
    main()