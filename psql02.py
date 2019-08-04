import psycopg2


class CMCFC:

    def __init__(self):
        self.conn = psycopg2.connect(host="mcfc01.c4hbjfyzingo.eu-west-2.rds.amazonaws.com", dbname="mcfc01", user="mcfcuser01", password="projecthack01")
        self.cur = self.conn.cursor()


    def go(self,the_table):
        s1 = 'SELECT * from public.' + the_table + ''
        self.cur.execute(s1)
        return self.cur.fetchall()

    def go2(self,the_table, bu, ed, mit):
        s1 = "SELECT "                                 \
             + the_table + ".risk_number, "            \
             + the_table + ".best, "                   \
             + the_table + ".expected, "               \
             + the_table + ".worst, "                  \
             + the_table + ".prob "                   \
             + " from public." + the_table             \
             + " WHERE "                               \
             + the_table + ".business_unit = '" + bu    \
             + "' AND "                                 \
             + the_table + ".extract_date = '" + ed     \
             + "' AND "                                 \
             + the_table + ".risk_mitigation = '" + mit + "'"

        self.cur.execute(s1)
        return self.cur.fetchall()


