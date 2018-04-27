CREATE TABLE IF NOT EXISTS AnimeEntries (
    Id INT,
    Title TEXT,
    Picture TEXT,
    Episodes INT,
    Type TEXT,
    PRIMARY KEY (Id)
);

CREATE TABLE IF NOT EXISTS AnimeRelations (
    Id INT NOT NULL,
    IdRelation INT NOT NULL,
    PRIMARY KEY (Id, IdRelation),
    FOREIGN KEY (Id) REFERENCES Entries (Id),
    FOREIGN KEY (IdRelation) REFERENCES AnimeEntries (Id)
);

CREATE TABLE IF NOT EXISTS Users (
    UserId TEXT,
    GoogleUserId TEXT NOT NULL,
    DateCreated INT NOT NULL,
    PRIMARY KEY (UserId)
);

CREATE TABLE IF NOT EXISTS UserEpisodeNotes (
    UserId TEXT,
    EpisodeNumber INT NOT NULL,
    AnimeId INT NOT NULL,
    Note TEXT NOT NULL,
    DateCreated INT NOT NULL,
    PRIMARY KEY (UserId, EpisodeNumber, AnimeId),
    FOREIGN KEY (UserId) REFERENCES Users(UserId)
);

CREATE TABLE IF NOT EXISTS UserWaifus (
    UserId TEXT,
    WaifuId INT NOT NULL,
    AnimeId INT NOT NULL,
    WaifuName TEXT NOT NULL,
    ImageURL TEXT,
    DateCreated INT NOT NULL,
    PRIMARY KEY (UserId, WaifuId),
    FOREIGN KEY (UserId) REFERENCES Users(UserId)
);