CREATE SCHEMA inventory;
CREATE SCHEMA accounting;

CREATE TABLE inventory.stores (
    ID          SERIAL PRIMARY KEY,
    NAME        TEXT NOT NULL,
    MAXSTORE    NUMERIC
);
CREATE TABLE inventory.itemtypes (
    ID          SERIAL PRIMARY KEY,
    NAME        TEXT NOT NULL,
    PRICE       NUMERIC NOT NULL
);
CREATE TABLE inventory.items (
    ID          SERIAL PRIMARY KEY,
    STOREID     INT NOT NULL REFERENCES inventory.stores,
    ITEMTYPEID  INT NOT NULL REFERENCES inventory.itemtypes,
    QUANTITY    INTEGER NOT NULL
);
CREATE TABLE accounting.accounts (
    ID          SERIAL PRIMARY KEY,
    NAME        TEXT NOT NULL,
    BUDGET      NUMERIC NOT NULL
);
CREATE TABLE accounting.transactions (
    ID          SERIAL PRIMARY KEY,
    ACCOUNTID   INT NOT NULL REFERENCES accounting.accounts,
    AMOUNT      NUMERIC NOT NULL
);