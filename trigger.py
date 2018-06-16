import io
import sqlite3
import serial



file_path = '/var/www/html/database/sensordata.db'

script = ''' CREATE TRIGGER a
BEFORE INSERT ON sensordata
BEGIN
    SELECT CASE WHEN
        (SELECT COUNT (*) FROM sensordata) >= 3
    THEN
        RAISE(FAIL, "Activated - mytrigger.")
    END;
END;
'''
conn = sqlite3.connect(file_path)
curs=conn.cursor()
curs.execute('''DROP TRIGGER IF EXISTS a''')
curs.executescript(script)
curs.execute('''INSERT INTO sensordata VALUES(datetime('now'),(?))''',('pressed',))
conn.commit()
conn.close()
