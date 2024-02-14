
/* Create dimension tables*/

CREATE TABLE IF NOT EXISTS dimcustomer
(
    customer_key serial NOT NULL ,
    customer_id smallint NOT NULL,
    first_name character varying(45) NOT NULL,
    last_name character varying(45)  NOT NULL,
    email character varying(50), 
    address character varying(50)  NOT NULL,
    district character varying(20) NOT NULL,
    city character varying(50)  NOT NULL,
    country character varying(50) NOT NULL,
    postal_code character varying(10) NOT NULL,
	address2 character varying(50),
    phone character varying(20) NOT NULL,
    active smallint NOT NULL,
    create_date timestamp NOT NULL,
    end_date date NOT NULL,
    start_date date NOT NULL
);


CREATE TABLE IF NOT EXISTS dimdate
(
    date_key integer NOT NULL PRIMARY KEY,
    date date NOT NULL,
    year smallint NOT NULL,
    month smallint NOT NULL,
    week smallint NOT NULL,
    day smallint NOT NULL,
    is_weekend boolean,
    quarter integer NOT NULL
);

CREATE TABLE IF NOT EXISTS public.dimmovie
(
    movie_key serial NOT NULL PRIMARY KEY,
    film_id smallint NOT NULL,
    title character varying NOT NULL,
    description text ,
    release_year year,
    language character varying(20)NOT NULL,
    original_language character varying(20),
    rental_duration smallint NOT NULL,
    length smallint NOT NULL,
    rating character varying(5) NOT NULL,
    special_features character varying(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS dimstore
(
    store_key serial NOT NULL PRIMARY KEY,
    store_id smallint NOT NULL,
    address character varying(50) NOT NULL,
    address2 character varying(50),
    district character varying(20) NOT NULL,
    city character varying(50) NOT NULL,
    country character varying(50) NOT NULL,
    postal_code character varying(10),
    manager_first_name character varying(45) NOT NULL,
    manager_last_name character varying(45) NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL
);

---create fact tables
CREATE TABLE IF NOT EXISTS factsales
(
    sales_key serial NOT NULL PRIMARY KEY,
    date_key integer  REFERENCES dimdate (date_key),
    store_key integer REFERENCES dimstore (store_key),
    customer_key integer REFERENCES dimcustomer (customer_key),
    movie_key integer  REFERENCES dimmovie (movie_key),
    sales_amount numeric NOT NULL
);

---Populate all dimension tables and fact table

INSERT INTO dimdate(date_key, date, year, month, week, day, is_weekend,quarter)
SELECT DISTINCT (to_char(payment_date,'yyyymmdd')::integer) as date_key,
date(payment_date) as date, 
EXTRACT (year FROM payment_date) as year, 
EXTRACT (month FROM payment_date) as month, 
EXTRACT (week FROM payment_date) as week, 
EXTRACT (day FROM payment_date) as day,X
CASE WHEN EXTRACT (DOW FROM payment_date) >= 6 THEN true
WHEN EXTRACT (DOW FROM payment_date) < 6 THEN false
ELSE null END,
EXTRACT (quarter FROM payment_date) as quarter
FROM payment;

-------
INSERT INTO dimcustomer(customer_key, customer_id, first_name, last_name, email, address,
district, city, country, postal_code, address2, phone, active, create_date,start_date,end_date)
SELECT c.customer_id,c.customer_id,c.first_name,c.last_name,c.email,a.address,a.district,cy.city,
ct.country,a.postal_code,a.address2,a.phone,c.active,c.create_date,current_date,current_date

FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city cy ON a.city_id = cy.city_id
JOIN country ct ON cy.country_id = ct.country_id;

--------
INSERT INTO dimmovie(movie_key, film_id, title, description, release_year, language, original_language,
rental_duration, length, rating, special_features)
SELECT f.film_id,f.film_id,f.title,f.description,f.release_year,l.name as language,l.name as original_language,
f.rental_duration,f.length,f.rating,f.special_features

FROM film f
JOIN language l on f.language_id = l.language_id;

-----

INSERT INTO dimstore(store_key, store_id, address, address2, district, city, country, postal_code,
manager_first_name, manager_last_name, start_date, end_date)
SELECT s.store_id,s.store_id,a.address,a.address2,a.district,cy.city,ct.country,a.postal_code,
st.first_name as manager_first_name,st.last_name as manager_last_name ,current_date,current_date

FROM store s 
JOIN address a on s.address_id = a.address_id
JOIN city cy ON a.city_id = cy.city_id
JOIN country ct ON cy.country_id = ct.country_id
JOIN staff st on st.staff_id = s.manager_staff_id;
---------

INSERT INTO factsales( date_key, store_key, customer_key, movie_key, sales_amount)

SELECT (to_char(p.payment_date,'yyyymmdd')::integer),i.store_id, p.customer_id,i.film_id,
p.amount
FROM payment p 
JOIN rental r on r.rental_id = p.rental_id
JOIN inventory i on i.inventory_id = r.inventory_id;


