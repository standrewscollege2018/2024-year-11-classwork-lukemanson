BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "student_normal" (
	"student_normalID"	INTEGER,
	"firstName"	TEXT,
	"lastName"	TEXT,
	"tutorGroupID"	TEXT,
	"cityID"	TEXT,
	"yearGroup"	INTEGER,
	PRIMARY KEY("student_normalID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "city" (
	"cityID"	INTEGER,
	"cityName"	TEXT,
	PRIMARY KEY("cityID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "tutorGroup" (
	"tutorGroupID"	INTEGER,
	"tutorCode"	TEXT,
	PRIMARY KEY("tutorGroupID" AUTOINCREMENT)
);
INSERT INTO "student_normal" VALUES (1,'John','Doe','1','1',10);
INSERT INTO "student_normal" VALUES (2,'Jane','Smith','2','2',11);
INSERT INTO "student_normal" VALUES (3,'Michael','Johnson','3','3',10);
INSERT INTO "student_normal" VALUES (4,'Emily','Williams','4','4',12);
INSERT INTO "student_normal" VALUES (5,'Alice','Brown','1','2',10);
INSERT INTO "student_normal" VALUES (6,'Robert','Taylor','2','1',11);
INSERT INTO "student_normal" VALUES (7,'Emma','Wilson','3','3',12);
INSERT INTO "student_normal" VALUES (8,'James','Anderson','4','4',10);
INSERT INTO "student_normal" VALUES (9,'Olivia','Martinez','1','1',11);
INSERT INTO "student_normal" VALUES (10,'William','Thomas','2','2',12);
INSERT INTO "student_normal" VALUES (11,'Sophia','Garcia','3','3',10);
INSERT INTO "student_normal" VALUES (12,'Alexander','Lopez','4','4',11);
INSERT INTO "student_normal" VALUES (13,'Isabella','Hernandez','1','1',10);
INSERT INTO "student_normal" VALUES (14,'Daniel','King','2','2',11);
INSERT INTO "student_normal" VALUES (15,'Ella','Scott','3','3',12);
INSERT INTO "student_normal" VALUES (16,'Mason','Lee','4','4',10);
INSERT INTO "student_normal" VALUES (17,'Ava','Walker','1','1',11);
INSERT INTO "student_normal" VALUES (18,'Liam','Perez','2','2',12);
INSERT INTO "student_normal" VALUES (19,'Charlotte','Roberts','3','3',10);
INSERT INTO "student_normal" VALUES (20,'Noah','Turner','4','4',11);
INSERT INTO "student_normal" VALUES (21,'Amelia','Phillips','1','1',10);
INSERT INTO "student_normal" VALUES (22,'Ethan','Campbell','2','2',11);
INSERT INTO "student_normal" VALUES (23,'Chloe','Evans','3','3',12);
INSERT INTO "student_normal" VALUES (24,'Mia','Edwards','4','4',10);
INSERT INTO "student_normal" VALUES (25,'Luna','Hill','1','1',11);
INSERT INTO "student_normal" VALUES (26,'Logan','Wright','2','2',12);
INSERT INTO "student_normal" VALUES (27,'Harper','Mitchell','3','3',10);
INSERT INTO "student_normal" VALUES (28,'Lily','Robinson','4','4',11);
INSERT INTO "student_normal" VALUES (29,'Aiden','Clark','1','1',10);
INSERT INTO "student_normal" VALUES (30,'Zoe','Lewis','2','2',11);
INSERT INTO "student_normal" VALUES (31,'Lucas','Green','3','3',12);
INSERT INTO "student_normal" VALUES (32,'Penelope','White','4','4',10);
INSERT INTO "student_normal" VALUES (33,'Elijah','Hall','1','1',11);
INSERT INTO "student_normal" VALUES (34,'Riley','Baker','2','2',12);
INSERT INTO "student_normal" VALUES (35,'Ellie','Adams','3','3',10);
INSERT INTO "student_normal" VALUES (36,'Benjamin','Carter','4','4',11);
INSERT INTO "student_normal" VALUES (37,'Aria','Morris','1','1',10);
INSERT INTO "student_normal" VALUES (38,'Jackson','Turner','2','2',11);
INSERT INTO "student_normal" VALUES (39,'Scarlett','Harris','3','3',12);
INSERT INTO "student_normal" VALUES (40,'Mateo','Hughes','4','4',10);
INSERT INTO "student_normal" VALUES (41,'Grace','Ross','1','1',11);
INSERT INTO "student_normal" VALUES (42,'Ian','Wood','2','2',12);
INSERT INTO "student_normal" VALUES (43,'Eva','Nelson','3','3',10);
INSERT INTO "student_normal" VALUES (44,'Leo','Bennett','4','4',11);
INSERT INTO "student_normal" VALUES (45,'Hazel','Morales','1','1',10);
INSERT INTO "student_normal" VALUES (46,'Luke','Foster','2','2',11);
INSERT INTO "student_normal" VALUES (47,'Nova','Gray','3','3',12);
INSERT INTO "student_normal" VALUES (48,'Anthony','Sullivan','4','4',10);
INSERT INTO "student_normal" VALUES (49,'Nora','Butler','1','1',11);
INSERT INTO "student_normal" VALUES (50,'Miles','Simmons','2','2',12);
INSERT INTO "student_normal" VALUES (51,'Stella','Fisher','3','3',10);
INSERT INTO "student_normal" VALUES (52,'Nathan','Russell','4','4',11);
INSERT INTO "student_normal" VALUES (53,'Violet','Parker','1','1',10);
INSERT INTO "student_normal" VALUES (54,'Aaron','Stewart','2','2',11);
INSERT INTO "student_normal" VALUES (55,'Aurora','Long','3','3',12);
INSERT INTO "student_normal" VALUES (56,'Hudson','Barnes','4','4',10);
INSERT INTO "student_normal" VALUES (57,'Piper','Reed','1','1',11);
INSERT INTO "student_normal" VALUES (58,'Roman','Sanders','2','2',12);
INSERT INTO "student_normal" VALUES (59,'Clara','Campbell','3','3',10);
INSERT INTO "student_normal" VALUES (60,'Christian','Bennett','4','4',11);
INSERT INTO "student_normal" VALUES (61,'Audrey','Diaz','1','1',10);
INSERT INTO "student_normal" VALUES (62,'Owen','Richardson','2','2',11);
INSERT INTO "student_normal" VALUES (63,'Elliot','Kim','3','3',12);
INSERT INTO "student_normal" VALUES (64,'Maya','Hughes','4','4',10);
INSERT INTO "student_normal" VALUES (65,'Santiago','Gomez','1','1',11);
INSERT INTO "student_normal" VALUES (66,'Ruby','Alexander','2','2',12);
INSERT INTO "student_normal" VALUES (67,'Eleanor','Myers','3','3',10);
INSERT INTO "student_normal" VALUES (68,'Lincoln','Nguyen','4','4',11);
INSERT INTO "student_normal" VALUES (69,'Hannah','Ward','1','1',10);
INSERT INTO "student_normal" VALUES (70,'Gabriel','Rossi','2','2',11);
INSERT INTO "student_normal" VALUES (71,'Madeline','Ferguson','3','3',12);
INSERT INTO "student_normal" VALUES (72,'Grayson','Kennedy','4','4',10);
INSERT INTO "student_normal" VALUES (73,'Aubrey','Murray','1','1',11);
INSERT INTO "student_normal" VALUES (74,'Maverick','Rivera','2','2',12);
INSERT INTO "student_normal" VALUES (75,'Ivy','Hamilton','3','3',10);
INSERT INTO "student_normal" VALUES (76,'Christopher','Wells','4','4',11);
INSERT INTO "student_normal" VALUES (77,'Delilah','Owens','1','1',10);
INSERT INTO "student_normal" VALUES (78,'Emmett','Morgan','2','2',11);
INSERT INTO "student_normal" VALUES (79,'David','White','1','1',10);
INSERT INTO "student_normal" VALUES (80,'Sophie','Jones','2','2',11);
INSERT INTO "student_normal" VALUES (81,'Christopher','Brown','3','3',10);
INSERT INTO "student_normal" VALUES (82,'Anna','Taylor','4','4',12);
INSERT INTO "student_normal" VALUES (83,'Matthew','Evans','1','1',10);
INSERT INTO "student_normal" VALUES (84,'Rebecca','Garcia','2','2',11);
INSERT INTO "student_normal" VALUES (85,'Andrew','Martinez','3','3',10);
INSERT INTO "student_normal" VALUES (86,'Julia','Rodriguez','4','4',12);
INSERT INTO "student_normal" VALUES (87,'Ryan','Hernandez','1','1',10);
INSERT INTO "student_normal" VALUES (88,'Lauren','Lopez','2','2',11);
INSERT INTO "student_normal" VALUES (89,'Nicholas','Hill','3','3',10);
INSERT INTO "student_normal" VALUES (90,'Samantha','Gonzalez','4','4',12);
INSERT INTO "student_normal" VALUES (91,'Brandon','Perez','1','1',10);
INSERT INTO "student_normal" VALUES (92,'Victoria','Sanchez','2','2',11);
INSERT INTO "student_normal" VALUES (93,'Gabriel','Ramirez','3','3',10);
INSERT INTO "student_normal" VALUES (94,'Stephanie','Torres','4','4',12);
INSERT INTO "student_normal" VALUES (95,'Eric','Flores','1','1',10);
INSERT INTO "student_normal" VALUES (96,'Nicole','Diaz','2','2',11);
INSERT INTO "student_normal" VALUES (97,'Joshua','Rivera','3','3',10);
INSERT INTO "student_normal" VALUES (98,'Kelly','Gomez','4','4',12);
INSERT INTO "student_normal" VALUES (99,'Tyler','Ortiz','1','1',10);
INSERT INTO "student_normal" VALUES (100,'Michelle','Vasquez','2','2',11);
INSERT INTO "student_normal" VALUES (101,'Austin','Jimenez','3','3',10);
INSERT INTO "student_normal" VALUES (102,'Maria','Castillo','4','4',12);
INSERT INTO "student_normal" VALUES (103,'Justin','Ruiz','1','1',10);
INSERT INTO "student_normal" VALUES (104,'Kayla','Chavez','2','2',11);
INSERT INTO "student_normal" VALUES (105,'Kevin','Mercado','3','3',10);
INSERT INTO "student_normal" VALUES (106,'Laura','Valdez','4','4',12);
INSERT INTO "student_normal" VALUES (107,'Kyle','Reyes','1','1',10);
INSERT INTO "student_normal" VALUES (108,'Kimberly','Fernandez','2','2',11);
INSERT INTO "student_normal" VALUES (109,'Steven','Gutierrez','3','3',10);
INSERT INTO "student_normal" VALUES (110,'Hannah','Perez','4','4',12);
INSERT INTO "student_normal" VALUES (111,'Caleb','Torres','1','1',10);
INSERT INTO "student_normal" VALUES (112,'Allison','Castro','2','2',11);
INSERT INTO "student_normal" VALUES (113,'Evan','Herrera','3','3',10);
INSERT INTO "student_normal" VALUES (114,'Natalie','Alvarez','4','4',12);
INSERT INTO "student_normal" VALUES (115,'Jacob','Mendoza','1','1',10);
INSERT INTO "student_normal" VALUES (116,'Madison','Vargas','2','2',11);
INSERT INTO "student_normal" VALUES (117,'Zachary','Guerrero','3','3',10);
INSERT INTO "student_normal" VALUES (118,'Angela','Contreras','4','4',12);
INSERT INTO "student_normal" VALUES (119,'Jasmine','Soto','1','1',10);
INSERT INTO "student_normal" VALUES (120,'Marcus','Luna','2','2',11);
INSERT INTO "student_normal" VALUES (121,'Dylan','Arias','3','3',10);
INSERT INTO "student_normal" VALUES (122,'Vanessa','Mendez','4','4',12);
INSERT INTO "student_normal" VALUES (123,'Derek','Hernandez','1','1',10);
INSERT INTO "student_normal" VALUES (124,'Paige','Guzman','2','2',11);
INSERT INTO "student_normal" VALUES (125,'Jeremy','Velez','3','3',10);
INSERT INTO "student_normal" VALUES (126,'April','Salazar','4','4',12);
INSERT INTO "city" VALUES (1,'Auckland');
INSERT INTO "city" VALUES (2,'Wellington');
INSERT INTO "city" VALUES (3,'Christchurch');
INSERT INTO "city" VALUES (4,'Hamilton');
INSERT INTO "tutorGroup" VALUES (1,'PAD');
INSERT INTO "tutorGroup" VALUES (2,'JLU');
INSERT INTO "tutorGroup" VALUES (3,'JLE');
INSERT INTO "tutorGroup" VALUES (4,'BEV');
COMMIT;
