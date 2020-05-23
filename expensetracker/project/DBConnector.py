import psycopg2
from datetime import datetime
from psycopg2 import extensions

class PGConnection():
    def __init__(self):
        self.con = psycopg2.connect(
            host="localhost",
            database="expensetracker",
            user="postgres",
            password="hideyuki1994",
            port=5432
        )
        self.cur = self.con.cursor()

    def get_expenses(self):
        get_query = "SELECT name FROM expensetypes"
        try:
            self.cur.execute(get_query)
            self.con.commit()
            rows = self.cur.fetchall()
            expense_list = [expense[0] for expense in rows]
            return expense_list
        except Exception as e:
            print(datetime.now())
            self.get_transaction_status()

    def get_revenues(self):
        get_query = "SELECT name FROM revenuetypes"
        try:
            self.cur.execute(get_query)
            self.con.commit()
            rows = self.cur.fetchall()
            revenue_list = [revenue[0] for revenue in rows]
            return revenue_list
        except Exception as e:
            print(datetime.now())
            self.get_transaction_status()

    def new_expense(self, expense_type):
        add_query = "INSERT INTO expensetypes (name) VALUES (%s)"
        try:
            self.cur.execute(add_query, (expense_type,))
            self.con.commit()
            print("Add query executed successfully:", expense_type)
        except Exception as e:
            print(datetime.now())
            self.get_transaction_status()

    def new_revenue(self, expense_type):
        add_query = "INSERT INTO revenuetypes (name) VALUES (%s)"
        try:
            self.cur.execute(add_query, (expense_type,))
            self.con.commit()
            print("Add query executed successfully:", expense_type)
        except Exception as e:
            print(datetime.now())
            self.get_transaction_status()

    def remove_expense(self, expense_type):
        remove_query = "DELETE FROM expensetypes WHERE name = %s"
        try:
            self.cur.execute(remove_query, (expense_type,))
            self.con.commit()
            print("Delete query executed successfully:", expense_type)
        except Exception as e:
            print(datetime.now())
            self.get_transaction_status()

    def get_transaction_status(self):
        # print the connection status
        print("\nconn.status:", self.con.status)

        # evaluate the status for the PostgreSQL connection
        if self.con.status == extensions.STATUS_READY:
            print("psycopg2 status #1: Connection is ready for a transaction.")

        elif self.con.status == extensions.STATUS_BEGIN:
            print("psycopg2 status #2: An open transaction is in process.")

        elif self.con.status == extensions.STATUS_IN_TRANSACTION:
            print("psycopg2 status #3: An exception has occured.")
            print("Use tpc_commit() or tpc_rollback() to end transaction")

        elif self.con.status == extensions.STATUS_PREPARED:
            print("psycopg2 status #4:A transcation is in the 2nd phase of the process.")
        return self.con.status


def main():
    PGSQL = PGConnection()
    hello = PGSQL.get_revenues()
    print(hello)
    PGSQL.con.commit()
    PGSQL.cur.close()
    # Close the connection
    PGSQL.con.close()


if __name__ == "__main__":
    main()

