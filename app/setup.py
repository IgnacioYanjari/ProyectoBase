from config import *
import psycopg2
conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))

cur = conn.cursor()

# sql = """ DROP SCHEMA public CASCADE;
# CREATE SCHEMA public;
# """

# cur.execute(sql)

sql = """
CREATE TABLE negocios( id serial PRIMARY KEY , dueno_id integer , calle varchar, nombre varchar , comuna varchar, ciudad varchar, region varchar, telefono integer);
CREATE TABLE stocks(Negocio_id integer , producto_id bigint , stock_producto integer , proveedor_id integer , precio integer );
CREATE TABLE duenos(id serial PRIMARY KEY , nombre varchar , telefono integer , email varchar );
CREATE TABLE proveedores(id serial PRIMARY KEY , telefono integer ,comuna varchar,ciudad varchar ,region varchar ,calle varchar ,precio integer,nombre varchar);
CREATE TABLE productos(id bigserial PRIMARY KEY , nombre varchar , detalle varchar);
CREATE TABLE ventas(num_venta serial PRIMARY KEY , negocio_id integer, fecha timestamp);
CREATE TABLE ventas_detalle(num_venta integer, producto_id bigint , monto integer , cantidad integer);
"""

#queda con 255 el varchar
cur.execute(sql)
conn.commit()
cur.close()
conn.close()
