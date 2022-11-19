CREATE TABLE Persons (
    username varchar(255),
    usermail varchar(255),
    usercontact varchar(255),
    password varchar(255)
);

CREATE TABLE DONOR2 (
    name varchar(255),
    mobile varchar(255),
    email varchar(255),
    age int,
    gender varchar(10),
    blood varchar(255),
    area varchar(255),
    city varchar(255),
    district varchar(255)
);

CREATE TABLE REQUEST2 (
    drmail varchar(255),
    hospitalname varchar(255),
    recname varchar(255),
    recmobile int,
    recmail varchar(255),
    recage int,
    recgender varchar(10),
    recbloodgroup varchar(255),
    recarea varchar(255),
    reccity varchar(255),
    recdistrict varchar(255)
);
