# Libraries
import MySQLdb

# Open Database Connection
db = MySQLdb.connect("localhost", "root", "password", "kelas")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute table function
def eksekusi(sql, done, err):
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        if done != " ":
            print done
    except:
        # Rollback in case there is any error
        db.rollback()
        if err != " ":
            print err

# Drop table if it already exist using execute() method.
# cursor.execute("DROP TABLE IF EXISTS tablename")

# # Creating the database
# print "======DATABASE DATA SENSOR DI KELAS======"
# sql = """CREATE TABLE sensordata_holo (
#          nomor int NOT NULL AUTO_INCREMENT,
#          date_n date,
#          time_n time,
#          sensor_id int,
#          temperature double,
#          recommend_temperature text,
#          humidity double,
#          recommend_humidity text,
#          light_intensity int,
#          recommend_light text,
#          sound_intensity int,
#          recommend_sound text,
#          PRIMARY KEY (nomor))"""
# eksekusi(sql, "Tabel Berhasil Dibuat", "Tabel Sudah Ada")

# Creating the database
print "======DATABASE DATA SENSOR DI KELAS======"
sql = """CREATE TABLE `sensors_datum` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `date_n` date NOT NULL, `time_n` time(6) NOT NULL, `mode_belajar` varchar(20) NOT NULL, `sensor_id` integer NOT NULL, `temperature` double precision NOT NULL, `recommend_temperature` longtext NOT NULL, `humidity` double precision NOT NULL, `recommend_humidity` longtext NOT NULL, `light_intensity` integer NOT NULL, `recommend_light` longtext NOT NULL, `sound_intensity` integer NOT NULL, `recommend_sound` longtext NOT NULL)"""
# sql = """CREATE TABLE `sensors_data` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `date_n` date NOT NULL, `time_n` time(6) NOT NULL, `sensor_id` integer NOT NULL, `temperature` double precision NOT NULL, `recommend_temperature` longtext NOT NULL, `humidity` double precision NOT NULL, `recommend_humidity` longtext NOT NULL, `light_intensity` integer NOT NULL, `recommend_light` longtext NOT NULL, `sound_intensity` integer NOT NULL, `recommend_sound` longtext NOT NULL)"""
eksekusi(sql, "Tabel Berhasil Dibuat", "GAGAL! Tabel Sudah Ada")


# disconnect from server
db.close()
