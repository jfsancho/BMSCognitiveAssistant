
CREATE DATABASE BMSCognitiveAssistant;

CREATE TABLE Permissions (
    PermissionID INT NOT NULL AUTO_INCREMENT,
    PermissionType CHAR(255) NOT NULL,
    PRIMARY KEY (PermissionID)
);

CREATE TABLE UserTypes (
    UserTypeID INT NOT NULL AUTO_INCREMENT,
    UserType CHAR(100),
    PermissionID INT,
    PRIMARY KEY (UserTypeID),
    FOREIGN KEY (PermissionID) REFERENCES Permissions(PermissionID)
);

CREATE TABLE DeviceTypes (
    DeviceType CHAR(100),
    Protocol CHAR(50) ,
    PRIMARY KEY (DeviceType)
);

CREATE TABLE Devices (
    DeviceID CHAR(100) NOT NULL,
    SubType CHAR(100),
    Description CHAR(100),
    Location CHAR(100),
    DeviceTypeID CHAR(100),
    PRIMARY KEY (DeviceID),
    FOREIGN KEY (DeviceTypeID) REFERENCES DeviceTypes(DeviceType)
);

CREATE TABLE Requests (
    RequestID INT NOT NULL AUTO_INCREMENT,
    Request CHAR(255) NOT NULL,
    Value INT,
    RequestHour TIME,
    RequestDate DATE,
    DeviceID CHAR(100),
    PRIMARY KEY (RequestID),
    FOREIGN KEY (DeviceID) REFERENCES Devices(DeviceID)
);

CREATE TABLE Users (
    UserID CHAR(100) NOT NULL,
    UserName CHAR(100) NOT NULL,
    UserLastname CHAR(100),
    UserTypeID INT,
    Password CHAR(255) NOT NULL,
    PRIMARY KEY (UserID),
    FOREIGN KEY (UserTypeID) REFERENCES UserTypes(UserTypeID)
);

CREATE TABLE UserRequests (
    UserRequestID INT NOT NULL,
    UserID CHAR(100),
    RequestID INT,
    PRIMARY KEY (UserRequestID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (RequestID) REFERENCES Requests(RequestID)
);
