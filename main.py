# docker run --publish 4200:4200 --publish 5432:5432 crate -Cdiscovery.type=single-node
import time
from crate import client

def main():
    time.sleep(15)
    connection = client.connect("http://"+'crate'+":4200/", username="crate")

    #
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS adib")
    cursor.execute("CREATE TABLE adib (ts TIMESTAMP, val DOUBLE PRECISION, part GENERATED ALWAYS AS date_trunc('month',ts)) PARTITIONED BY(part);")
    cursor.execute("INSERT INTO adib (ts,val) VALUES (1617823229974, 1.23);")
    cursor.execute("INSERT INTO adib (ts,val) VALUES (1620415701974, 2.31);")
    cursor.execute("SHOW TABLES")
    tablas_actuales = cursor.rows
    for tabla in tablas_actuales:
        print(tabla)
    #metemos un sleep porque pycharm a veces ejecuta más rapido de lo que lo hace crateDB y en el select no aparecen todos los datos insertados(puedes comprobarlo comentando el sleep)
    print("Sleeping for 3 seconds...")
    time.sleep(3)

    cursor.execute("SELECT * FROM adib")
    result=cursor.rows
    for row in result:
        print(row)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
