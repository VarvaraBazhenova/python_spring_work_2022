# todo: Написать скрипт создания базы данных(ER-модели) TestSystem
# Скрипт  create_db.py  должен создавать таблицы, индексы, констрейнты в СУБД PostgresSQL
# В задании использовать библиотеку psycopg


# Ссылка на документацию
# https://www.psycopg.org/psycopg3/docs/basic/usage.html
# Для подключения использовать пользователя и базу отличную от postgres

# import psycopg
#
# with psycopg.connect("dbname=postgres user=postgres password=06042022") as conn:
#     with conn.cursor() as cur:
#         cur.execute("""
#             CREATE TABLE "group" (
#                 "id_group" serial PRIMARY KEY,
#                 "name" varchar(10)
#             )
#             """)
#         cur.execute("""
#             CREATE TABLE "student" (
#                 "id_student" serial PRIMARY KEY,
#                 "id_group" integer not null,
#                 "name" varchar(50)
#                 "age" integer
#             )
#             """)
#         cur.execute("""
#             CREATE TABLE "test" (
#                 "id_test" serial PRIMARY KEY,
#                 "id_test_students" integer not null,
#                 "topic" varchar(100),
#                 "results" integer not null,
#                 "dt_test" timestamp,
#                 "lim_20" boolean)
#             """)
#         cur.execute("""
#             CREATE TABLE "test_students" (
#                 "id_student" integer not null,
#                 "id_test" integer not null,
#                 "dt_create" timestamp)
#             """)
#
#         cur.execute("""
#             alter table "student" add constraint "fk_student_id_group"
#             foreign key ("id_group") references "group"("id_group")
#             on delete restrict;
#             """)
#         cur.execute("""
#             alter table "student_test" add constraint "fk_test_student_id_student"
#             foreign key ("id_student") references "student"("id_student")
#             on delete restrict;
#             """)
#         cur.execute("""
#             alter table "student_test" add constraint "fk_test_student_id_test"
#             foreign key ("id_test") references "test"("id_test")
#             on delete restrict;
#             """)
#
#         cur.execute("""
#         CREATE INDEX "idx_student_id_group" ON "student" ("id_group");
#         """)
#         cur.execute("""
#         CREATE INDEX "idx_test_student_id_student" ON "test_student" ("id_student");
#         """)
#         cur.execute("""
#         CREATE INDEX "idx_test_student_id_test" ON "test_student" ("id_test");
#         """)