-- pracownicy.sql
DROP TABLE IF EXISTS pracownicy;
DROP TABLE IF EXISTS place;
DROP TABLE IF EXISTS kontakty;
DROP TABLE IF EXISTS stanowiska;

CREATE TABLE pracownicy (
    imie TEXT(30),
    nazwisko TEXT(30),
    kod INTEGER,
    miasto_z TEXT(30),
    ulica TEXT(30),
    data_u DATE,
    miasto_u TEXT(30)
);

CREATE TABLE place(
    id_p INTEGER,
    id_s INTEGER,
    placa DECIMAL,
    data_z DATA,
    FOREIGN KEY (id_p) REFERENCES kontakty(id_pracownika)
    FOREIGN KEY (id_s) REFERENCES stanowiska(id_stanowiska)
);

CREATE TABLE kontakty(
    id_pracownika INTEGER PRIMARY KEY,
    typ_k BOOLEAN,
    kontakt TEXT (12),
    uwagi TEXT (30)
);

CREATE TABLE stanowiska(
    id_stanowiska INTEGER PRIMARY KEY AUTOINCREMENT,
    stanowisko TEXT(30)
);
