
CREATE TABLE test (
    id           INTEGER PRIMARY KEY AUTOINCREMENT
                         NOT NULL
                         UNIQUE,
    user_id      INTEGER NOT NULL
                         UNIQUE,
    user_name    STRING  NOT NULL,
    user_surname STRING,
    username     STRING
);

CREATE TABLE list_p (
    id           INTEGER PRIMARY KEY AUTOINCREMENT
                         NOT NULL
                         UNIQUE,
    user_id      INTEGER NOT NULL,
    product      STRING  NOT NULL,
    count        REAL    DEFAULT (1),
    status       INTEGER NOT NULL
);

