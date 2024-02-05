{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "768eb68b-9228-4a91-af33-75a7944333c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#import the library needed to connect python to the postgres db\n",
    "import psycopg2 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b47a329d-4591-47e3-a1bd-8af1224113aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "# connect to the db, note you can also set the host to local host\n",
    "try:\n",
    "    conn = psycopg2.connect(\"host=127.0.0.1 dbname=postgres user=toluwalopebabington password=Freedom22\")\n",
    "except psycopg2.Error as e:\n",
    "    print (\"Error: Could not make a connection the postgres database\")\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"Successful connection\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58efde73-9eb7-4fc6-8bae-2882b43eea0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# turn autocommit \n",
    "conn.set_session(autocommit=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af721d88-e142-4abf-ba4d-89e90622c528",
   "metadata": {},
   "outputs": [],
   "source": [
    "# create a cusor for running queries against the db\n",
    "try:\n",
    "    cur = conn.cursor()\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"cursor succesfully created\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "888e3fdb-ce33-4fcb-8734-a38bd2618285",
   "metadata": {},
   "outputs": [],
   "source": [
    "# create  the db\n",
    "try:\n",
    "    cur.execute (\"create database myfirstdb\")\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"database succesfully created\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4517f475-0448-4831-a60f-28f1d671e4be",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "try:\n",
    "    cur.close()\n",
    "    conn.close()\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "\n",
    "try:\n",
    "    conn = psycopg2.connect(\"host=127.0.0.1 dbname=myfirstdb user=toluwalopebabington password=Freedom22\")\n",
    "    conn.set_session(autocommit=True)\n",
    "except psycopg2.Error as e:\n",
    "    print (\"Error: Could not make a connection the myfirstdb database\")\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"Successful connection\")\n",
    "\n",
    "try:\n",
    "    cur = conn.cursor()\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"cursor succesfully created\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef553292-1a17-4005-8f26-f2ab9e21d0b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# create table\n",
    "try:\n",
    "    cur.execute (\"create table students (student_id int PRIMARY KEY, Name varchar, age int, gender varchar, subject varchar, marks int);\")\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"table succesfully created\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c95418ea-cebb-476f-aa6e-673d4922b575",
   "metadata": {},
   "outputs": [],
   "source": [
    "# insert into table\n",
    "# create table\n",
    "'''\n",
    "Passing parameters to an SQL statement happens in functions such as\n",
    "cursor.execute() by using %s placeholders in the SQL statement, \n",
    "and passing a sequence of values as the second argument of the function.\n",
    "\n",
    "Named arguments are supported too using %(name)s placeholders in the \n",
    "query and specifying the values into a mapping. Using named arguments\n",
    "allows to specify the values in any order and to repeat the same value\n",
    "in several places in the query. --psycopg2 documentation\n",
    "'''\n",
    "try:\n",
    "    cur.execute (\"insert into students (student_id, name, age, gender, subject, marks) values (%s,%s,%s,%s,%s,%s);\",\n",
    "    (1, 'Edwina', 18, 'Female', 'Kannada', 95))\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"record 1 succesfully added\")\n",
    "\n",
    "try:\n",
    "    cur.execute (\"insert into students (student_id, name, age, gender, subject, marks) values (%(int1)s,%(str2)s,%(int2)s,%(str2)s,%(str3)s,%(int3)s);\",\n",
    "    {'int1':2,'str1':'Austine','int2':15,'str2':'Female','str3':'Gujarati','int3':16})\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"record 2 succesfully added\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ee317c1-42f9-45f0-a999-1f9876493021",
   "metadata": {},
   "outputs": [],
   "source": [
    "# query table\n",
    "try:\n",
    "    cur.execute (\"SELECT * FROM students;\")\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"table succesfully queried\")\n",
    "#cur object is an iterable\n",
    "[r for r in cur]\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b3d4ac8-b17c-48e6-8137-9a8978dafdd2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# query table\n",
    "try:\n",
    "    cur.execute (\"SELECT * FROM students;\")\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"table succesfully queried\")\n",
    "    \n",
    "#show values using fetchone\n",
    "'''\n",
    "Fetch the next row of a query result set, returning a single tuple, \n",
    "or None when no more data is available:\n",
    "'''\n",
    "cur.fetchone()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de2083f0-b11a-4392-9716-a94679427da3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# query table\n",
    "try:\n",
    "    cur.execute (\"SELECT * FROM students;\")\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"table succesfully queried\")\n",
    "    \n",
    "#show values using fetchmany\n",
    "'''\n",
    "Fetch the next set of rows of a query result, returning a list of tuples. \n",
    "An empty list is returned when no more rows are available.\n",
    "'''\n",
    "\n",
    "cur.fetchmany(2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1226f95d-8cee-4de9-a894-ca64c49c0f41",
   "metadata": {},
   "outputs": [],
   "source": [
    "# query table\n",
    "try:\n",
    "    cur.execute (\"SELECT * FROM students;\")\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"table succesfully queried\")\n",
    "    \n",
    "#show values using fetchall\n",
    "'''\n",
    "Fetch all (remaining) rows of a query result, returning them \n",
    "as a list of tuples. An empty list is returned if there is no more record to fetch.\n",
    "'''\n",
    "cur.fetchall()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78bb414b-ce68-4d22-a57c-19f0e570758d",
   "metadata": {},
   "outputs": [],
   "source": [
    "cur.close()\n",
    "conn.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e96c78ac-610c-4d9e-bd4a-09b3bd9f964b",
   "metadata": {},
   "source": [
    "Assignment\n",
    "- Find a dataset minimum 3 tables (DONE)\n",
    "- build a data model (DONE)\n",
    "- write python code to create the table structure and relationships (DONE)\n",
    "- Load the data into the db from the files"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73b35bd9-55f8-4455-b51c-7bc22b5ebcd0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv('/Users/toluwalopebabington/Desktop/new_york_listings_2024.csv')\n",
    "# keep a copy of the file \n",
    "bkp_df = pd.read_csv('/Users/toluwalopebabington/Desktop/new_york_listings_2024.csv')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9485918e-8c35-453c-881e-bef9d6c8631a",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i, rows in df.iterrows():\n",
    "    print(list(rows))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a58e2a47-b146-4dd8-ab97-f427b3e95453",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.rename(columns={'number_of_reviews':'total_review_cnt','number_of_reviews_ltm':'review_cnt_lst12_Mths','calculated_host_listings_count':'listing_count',\n",
    "                  'neighbourhood_group':'neighborhood_group','neighbourhood':'neighborhood'},inplace = True)\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f52d0d87-db64-4655-b849-e77dfc3618d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.head()"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "8dd04eba-3feb-4682-8626-dbc4577c668a",
   "metadata": {},
   "source": [
    "__[NY_Airbnb_Data Model](https://app.diagrams.net/?title=NY_Airbnb_2024.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1SpFIzoI3uCK7L8o9VUvaZClWu_AQfv7j%26export%3Ddownload)__\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ead7b623-7e19-478c-b31b-979ba3656b91",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "#connect to base db first (postgres) then create the new db\n",
    "# create  the db\n",
    "try:\n",
    "    cur.execute (\"create database Airbnb2024NY\") # keep in mind db will be created in lc\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"database succesfully created\")\n",
    "\n",
    "curr.close()\n",
    "conn.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e8d4e3a-1f39-4349-83bd-0af1f6282c6c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# connect to Airbnb2024NY and create cursor\n",
    "\n",
    "try:\n",
    "    conn = psycopg2.connect(\"host=127.0.0.1 dbname=airbnb2024ny user=toluwalopebabington password=Freedom22\")\n",
    "    conn.set_session(autocommit=True)\n",
    "except psycopg2.Error as e:\n",
    "    print (\"Error: Could not make a connection the postgres database\")\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"Successful connection\")\n",
    "\n",
    "# create a cusor for running queries against the db\n",
    "try:\n",
    "    cur = conn.cursor()\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"cursor succesfully created\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e095ec4-4f0a-4a5f-b348-7d7838577d54",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "for practice purposes in the future, after db is created, create the df and use to_sql function to push the data into the db\n",
    "'''\n",
    "\n",
    "try:\n",
    "    cur.execute (\"create table if not exists host (host_id int PRIMARY KEY NOT NULL, host_name varchar(100) NOT NULL, listing_count int);\")\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"host table succesfully created\")\n",
    "\n",
    "try:\n",
    "    cur.execute (\"create table if not exists reviews  (review_id int PRIMARY KEY NOT NULL, total_review_cnt int, last_review date, review_per_month real, review_cnt_lst12_mths int);\")\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"reviews table succesfully created\")\n",
    "\n",
    "\n",
    "try:\n",
    "    cur.execute (\"create table if not exists neighborhood (neighborhood_id int PRIMARY KEY NOT NULL, neighborhood varchar , neighborhood_group varchar );\")\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"neighborhood table succesfully created\")\n",
    "\n",
    "\n",
    "try:\n",
    "    cur.execute (\"create table if not exists listings (listing_id int PRIMARY KEY NOT NULL, room_type varchar, price real , minimum_nights int, availability_365 int, longitude double precision, latitude double precision, license varchar, rating varchar, bedrooms varchar, beds int, baths varchar,listing_name varchar, review_id int NOT NULL, host_id int NOT NULL, neighborhood_id int NOT NULL);\")\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"listings table succesfully created\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f282d780-6f57-4df3-80aa-5306e86b5dae",
   "metadata": {},
   "outputs": [],
   "source": [
    "# add relations\n",
    "try:\n",
    "    cur.execute (\"alter table listings add constraint fk_host foreign key (host_id) references host (host_id), add constraint fk_review foreign key (review_id) references reviews (review_id), add constraint fk_neighborhood foreign key (neighborhood_id) references neighborhood (neighborhood_id);\")\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"relations added\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f015c72-1333-407b-a06f-f340ecd5e783",
   "metadata": {},
   "outputs": [],
   "source": [
    "cur.close()\n",
    "conn.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "741720db-afda-4af7-8146-32ac7fab092f",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a424e65d-d768-42a9-9a70-9b469602dc47",
   "metadata": {},
   "outputs": [],
   "source": [
    "#add review_id column\n",
    "df['review_id'] = df.index +1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "070d7b04-0d60-408c-a32b-ececc934f0c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# create a dataframe for each table\n",
    "host = df[['host_id','host_name','listing_count']].copy()\n",
    "reviews = df[['total_review_cnt','last_review','reviews_per_month','review_cnt_lst12_Mths','review_id']].copy()\n",
    "neighborhood = df[['neighborhood','neighborhood_group']].copy()\n",
    "listing = df[['id','room_type','price','minimum_nights','availability_365','longitude','license','rating','bedrooms','beds','baths','latitude','host_id','review_id','neighborhood']].copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d347c73e-e659-4583-a3a8-084a1c390a13",
   "metadata": {},
   "outputs": [],
   "source": [
    "host.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d77714f-7a38-459b-9b13-992527688d1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# clean up the dataframe host to have only unque values\n",
    "host.drop_duplicates (subset = 'host_id',inplace = True)\n",
    "host['host_id'].is_unique"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f072d2c-4e83-4b38-b067-461f129f1b74",
   "metadata": {},
   "outputs": [],
   "source": [
    "# remove duplicates from neighborhood df \n",
    "neighborhood.drop_duplicates (subset = 'neighborhood',inplace = True)\n",
    "neighborhood['neighborhood'].is_unique\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eab75de0-41a7-4871-a116-ee07affa705f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# add id column to the df\n",
    "neighborhood['neighborhood_id'] = neighborhood.index + 1\n",
    "neighborhood.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e7f175c-73b9-425d-88e5-19e198f815c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''merge the listing and neighborhood dfs to get the neighborhood_id in the listing table then drop unneeded columns\n",
    "rename id to listing_id\n",
    "'''\n",
    "# merge is the closest pandas option to standard sql joins for joining two dfs \n",
    "listing = listing.merge(neighborhood, left_on ='neighborhood',right_on='neighborhood')\n",
    "listing.drop(columns=['neighborhood','neighborhood_group'], inplace = True)\n",
    "listing.rename(columns={'id':'listing_id'},inplace = True)\n",
    "listing.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3b7ef8f-b77c-41d1-893f-2e1fe8e59775",
   "metadata": {},
   "outputs": [],
   "source": [
    "#reconfirm all the dfs look ok using your data model\n",
    "host.head()\n",
    "reviews.head()\n",
    "neighborhood.head()\n",
    "listing.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c805b630-6982-434d-a5af-6ebf28066b4a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# connect to the db using sqlalchemy and load the dfs as tables\n",
    "from sqlalchemy import create_engine\n",
    "\n",
    "try:\n",
    "    conn_string = 'postgresql://toluwalopebabington:Freedom22@127.0.0.1:5432/airbnb2024ny'\n",
    "    db = create_engine(conn_string)\n",
    "    conn = db.connect()\n",
    "except:\n",
    "    print (\"Error: Could not make a connection the postgres database\")\n",
    "else:\n",
    "    print (\"Successful connection\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a16e41c5-e2dd-452d-82dd-2353af5bf916",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''load tables dont forget to remove fks created earlier \n",
    " if exist option being used drops the table if it exists\n",
    "but we can't drop the table because it would create a referential integrity constraint \n",
    "'''\n",
    "try:\n",
    "    host.to_sql('host', conn,index = False, if_exists= 'replace') \n",
    "except psycopg2.Error as e:\n",
    "    print (\"Error: Could not load table host\")\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"host table loaded\")\n",
    "\n",
    "try:\n",
    "    reviews.to_sql('reviews', conn, index = False,if_exists= 'replace') \n",
    "except psycopg2.Error as e:\n",
    "    print (\"Error: Could not load table reviews\")\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"reviews table loaded\")\n",
    "\n",
    "try:\n",
    "    neighborhood.to_sql('neighborhood', conn,index = False, if_exists= 'replace') \n",
    "except psycopg2.Error as e:\n",
    "    print (\"Error: Could not load table neighborhood\")\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"neighborhood table loaded\")\n",
    "\n",
    "try:\n",
    "    listing.to_sql('listings', conn, index = False, if_exists= 'replace') \n",
    "except psycopg2.Error as e:\n",
    "    print (\"Error: Could not load table listings\")\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"listings table loaded\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6e16f48-7742-45d7-831b-3baa0f75020f",
   "metadata": {},
   "outputs": [],
   "source": [
    "conn.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e1890bf9-59d4-4b7a-a097-28194237e83b",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# connect to Airbnb2024NY and create cursor\n",
    "# add keys constraints and relations\n",
    "\n",
    "\n",
    "try:\n",
    "    conn = psycopg2.connect(\"host=127.0.0.1 dbname=airbnb2024ny user=toluwalopebabington password=Freedom22\")\n",
    "    conn.set_session(autocommit=True)\n",
    "except psycopg2.Error as e:\n",
    "    print (\"Error: Could not make a connection the postgres database\")\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"Successful connection\")\n",
    "\n",
    "# create a cusor for running queries against the db\n",
    "try:\n",
    "    cur = conn.cursor()\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"cursor succesfully created\")\n",
    "\n",
    "try:\n",
    "    cur.execute (\"alter table host add primary key (host_id);\")\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"host pk added\")\n",
    "\n",
    "try:\n",
    "    cur.execute (\"alter table reviews add primary key (review_id);\")\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"reviews pk added\")\n",
    "\n",
    "try:\n",
    "    cur.execute (\"alter table listings add primary key (listing_id);\")\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"listings pk added\")\n",
    "\n",
    "try:\n",
    "    cur.execute (\"alter table neighborhood add primary key (neighborhood_id);\")\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"neighborhood pk added\")\n",
    "    \n",
    "try:\n",
    "    cur.execute (\"alter table listings add constraint fk_host foreign key (host_id) references host (host_id), add constraint fk_review foreign key (review_id) references reviews (review_id), add constraint fk_neighborhood foreign key (neighborhood_id) references neighborhood (neighborhood_id);\")\n",
    "except psycopg2.Error as e:\n",
    "    print(e)\n",
    "else:\n",
    "    print (\"relations added\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "edf916bc-b04a-437a-926a-a57fae17c1ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "cur.close()\n",
    "conn.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6bb013e9-c771-4b01-adff-0b2743449501",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
