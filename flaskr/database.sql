CREATE TABLE STATUSTYPE(
  id int,
  description varchar(255)
);

CREATE TABLE PROHIBITIONTYPE(
  id int,
  description varchar(255)
);

CREATE TABLE URL(
  id int,
  urlpath varchar(255)
);

CREATE TABLE RESTRICTION(
  id int,
  description varchar(255)
);

Create TABLE REGEXRESTRICTION(
  id int,
  restriction_id int references RESTRICTION(id),
  regex_rule varchar(255)
);

Create TABLE MACHINELEARNINGR(
  id int,
  restriction_id int references RESTRICTION(id),
  model_path varchar(255)
);

Create TABLE IMAGERESTRICTION(
  id int,
  restriction_id int references RESTRICTION(id),
  image_rule varchar(255)
);

Create TABLE URLPROCESSMENT(
  id int,
  url_id int references URL(id),
  status_id int references STATUSTYPE(id),
  date_created DATE
);

CREATE TABLE URLPROHIBITION(
  id int,
  url_id int references URLPROCESSMENT(url_id),
  prohibition_id int references PROHIBITIONTYPE(id),
  date_created DATE
);

CREATE TABLE REASONSPROHIBITION(
  id int,
  url_processment_id int references URLPROCESSMENT(id),
  restriction_id int references RESTRICTION(id),
  date_created DATE,
  URL_ID int references URLPROCESSMENT(url_id)
);
